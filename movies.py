class Movies:
    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            movie_name = None
            movie_cast = None

            for row_idx, line in enumerate(file):
                if row_idx % 3 == 0:
                    movie_name = line.rstrip()
                elif row_idx % 3 == 1:
                    movie_cast = line.rstrip().split(',')
                elif row_idx % 3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    movie_name = None
                    movie_cast = None

            if movie_name and movie_cast:
                # Add the last movie to the list
                self._movies.append(
                    {
                        'name': movie_name,
                        'cast': movie_cast
                    }
                )

    def get_movie_names(self):
        return [movie['name'] for movie in self._movies]

    def search_movies_by_name(self, keyword):
        return [movie['name'] for movie in self._movies if keyword.lower() in movie['name'].lower()]

    def search_movies_by_cast(self, keyword):
        result = []
        for movie in self._movies:
            if any(keyword.lower() in cast.lower() for cast in movie['cast']):
                result.append(movie['name'])
        return result

    def get_all_movies(self):
        return self._movies
