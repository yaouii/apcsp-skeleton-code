from queue import Queue
import wikipediaapi
import time

user_agent = "MsOrret'sWikipediaGame/1.0 (orret.deborah@pusd.us)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")


def fetch_links(page):
    links_list = []
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
        
    return links_list

def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()
  
    visited = set()  # To keep track of visited pages
    queue = Queue()  # For BFS traversal
    parent = {}  # To track the parent page for each page in the path

    queue.put(start_page.title)
    visited.add(start_page.title)

    while not queue.empty():
        current_page_title = queue.get()
        if current_page_title == target_page.title:
            break

        # Fetch links from the current page using the Wikipedia API
        current_page = wiki_wiki.page(current_page_title)
        links = fetch_links(current_page)

        for link in links:
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link] = current_page_title

    # Reconstruct the path from target_page to start_page
    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]
    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("This algorithm took", end_time-start_time, "seconds to run!")
  
    return path

# Example usage:
start_page = wiki_wiki.page('Python_(programming_language)')
target_page = wiki_wiki.page('Compiler')
path = wikipedia_game_solver(start_page, target_page)
print("Shortest path:", path)

