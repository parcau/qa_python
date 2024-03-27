import pytest
from main import BooksCollector


class TestBooksCollector:

    # 1. Проверяем добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Проверяем установку жанра для книги
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Оно', 'Ужасы'],
            ['Чип и Дейл', 'Мультфильмы']

        ]
    )
    def test_set_book_genre_existing_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert genre in collector.books_genre.values()

    # 3. Проверка получения жанра книги по названию
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Звонок', 'Ужасы'],
            ['Маска', 'Комедии']

        ]
    )
    def test_get_book_genre_by_name_existing_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # 4. Проверка вывода списка книг с определённым жанром
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Бременские музыканты', 'Мультфильмы']

        ]
    )
    def test_get_books_with_specific_genre_add_book_set_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre)

    # 5. Проверяем получения словара books_genre
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Бременские музыканты', 'Мультфильмы'],
            ['Свистит фляга', 'Комедии']

        ]
    )
    def test_get_books_genre_get_dict(self, name, genre):
        books_genre = {name: genre}
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == books_genre

    # 6 Проверка возврата книг подходящих детям
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Фантастика'],
            ['Маска', 'Комедии'],
            ['Бременские музыканты', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children_return_book_for_children(self, name, genre):
        books_for_children = [name]
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == books_for_children

    # 7. Проверка добавляения книги в Избранное
    @pytest.fixture(scope="function")
    def verif_name(self):
        verif_name = 'Гордость и предубеждение и зомби'
        return verif_name

    def test_add_book_in_favorites_already_in_favorites(self, verif_name):
        collector = BooksCollector()
        collector.add_new_book(verif_name)
        collector.add_book_in_favorites(verif_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    # 8. Проверяем удаление книги из Избранного

    def test_delete_book_from_favorites_absent_in_favorites(self, verif_name):
        collector = BooksCollector()
        collector.add_new_book(verif_name)
        collector.add_book_in_favorites(verif_name)
        collector.delete_book_from_favorites(verif_name)
        assert len(collector.get_list_of_favorites_books()) == 0


    # 9.  Проверка получения списка Избранных книг
    @pytest.mark.parametrize(
        'name',
        [
            'Гордость и предубеждение и зомби',
            'Маска',
            'Бременские музыканты'
        ]
    )
    def test_get_list_of_favorites_books(self, name):
        sample_books = name
        expected_result = sample_books
        collector = BooksCollector()
        collector.favorites = sample_books
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == expected_result
