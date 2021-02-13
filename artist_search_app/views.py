from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    # original query incluing any leading/trailing whitespace and uppercase letters
    query = request.POST['query']
    # copy of query with leading/trailing whitespace removed and all letters to lowercase 
    # which we can use to compare against artists on the artist list
    query_copy = query.lower().strip()
    
    # filename and path of the artist list, can simply be changed here
    artist_list_file_path = "./artist_search_app/static/artist_list.txt"
    # attempt to open the band list file
    try:
        artist_list = open(artist_list_file_path)
    # if it fails it means the file is missing and show this error message
    except:
        return HttpResponse(f"Error: Failed to load '{artist_list_file_path}' as the file appears to be missing")
    
    # to store a perfect match if there is one
    perfect_match = None
    # to store matches starting with query but not perfect matches
    artists_starting_with_query = []
    # all results containing the query substring will populate into this list
    all_results = []
    
    # for each line in the artist list file do the following
    for line in artist_list:
        # make a copy of line for comparison and strip its whitespace and put in lowercase
        line_copy = line.strip().lower()
        # check to see if we have a perfect match, and if so store it
        if line_copy == query_copy:
            perfect_match = line
            print("perfect match found")
        # if not perfect match, see if the artist name starts with the query and if so store it
        elif line_copy.startswith(query_copy):
            artists_starting_with_query.append(line)
        # otherwise, if the artist name has the query anywhere in it, store it in all results
        elif query_copy in line_copy:
            all_results.append(line)
    # push artists with names starting with query to the front of all results
    for artist in artists_starting_with_query:
        all_results.insert(0, artist)
    # if we have a perfect match put that at the top of results
    if perfect_match != None:
        all_results.insert(0, perfect_match)
    
    # store all results, the original query, and the count in contect 
    context = {
        'results': all_results, 
        'query': query, 
        'count': len(all_results)}
    # pass context to template and render
    return render(request, "index.html", context)