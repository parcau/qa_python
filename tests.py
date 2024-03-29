import pytest
from main import BooksCollector


class TestBooksCollector:

    # 1. Проверяем добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Проверяем установку жанра для книги
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Оно', 'Ужасы']
        ]
    )
    def test_set_book_genre_existing_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # 3. Проверка получения жанра книги по названию
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Маска', 'Комедии']
        ]
    )
    def test_get_book_genre_by_name_existing_name(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # 4. Проверка вывода списка книг с определённым жанром
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Бременские музыканты', 'Мультфильмы']
        ]
    )
    def test_get_books_with_specific_genre_add_book_set_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre)

    # 5. Проверяем получения словара books_genre
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Свистит фляга', 'Комедии']
        ]
    )
    def test_get_books_genre_get_dict(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre()

    # 6 Проверка возврата книг подходящих детям
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Фантастика'],
            ['Бременские музыканты', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children_return_book_for_children(self, name, genre, collector):
        books_for_children = [name]
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == books_for_children

    # 7. Проверка добавляения книги в Избранное

    def test_add_book_in_favorites_already_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 8. Проверяем удаление книги из Избранного

    def test_delete_book_from_favorites_absent_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert len(collector.get_list_of_favorites_books()) == 0


    # 9.  Проверка получения списка Избранных книг
    @pytest.mark.parametrize(
        'name',
        [
            'Гордость и предубеждение и зомби',
            'Маска'
        ]
    )
    def test_get_list_of_favorites_books(self, name, collector):
        sample_books = name
        expected_result = sample_books
        collector.favorites = sample_books
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == expected_result
