from movies import Movies

def display_menu():
    print("Menu:")
    print("1. List all movie names")
    print("2. Search movies by name")
    print("3. Search movies by cast")
    print("q. Quit")

if __name__ == "__main__":
    movies = Movies('./movies.txt')

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            movie_names = movies.get_movie_names()
            print("All Movie Names:")
            for name in movie_names:
                print(name)
        elif choice == '2':
            keyword = input("Enter a word to search by name: ")
            search_result = movies.search_movies_by_name(keyword)
            print("Search Result:")
            for result in search_result:
                print(result)
        elif choice == '3':
            keyword = input("Enter a word to search by cast: ")
            search_result = movies.search_movies_by_cast(keyword)
            print("Search Result:")
            for result in search_result:
                print(result)
        elif choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
