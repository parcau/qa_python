import pytest


class TestBooksCollector:

    # 1. Проверяем добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Проверка установки жанра и его получения по названию книги
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Маска', 'Комедии']
        ]
    )
    def test_set_and_get_book_genre_by_name_existing_name(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # 3. Проверка вывода списка книг с определённым жанром
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
        assert collector.get_books_with_specific_genre(genre) == [name]

    # 4. Проверяем получение словаря books_genre
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
        assert collector.get_books_genre() == {name: genre}

    # 5. Проверка возврата книг подходящих детям
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

    # 6. Проверка добавляения и получения списка Избранных

    def test_add_book_and_get_list_in_favorites_already_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 7. Проверяем удаление книги из Избранного

    def test_delete_book_from_favorites_absent_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert len(collector.get_list_of_favorites_books()) == 0
