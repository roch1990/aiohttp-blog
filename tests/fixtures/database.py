import datetime
import psycopg2

categories = [
    {
        'route': 'music',
        'title': 'Music',
        'image': 'static/images/music.png'
    },
    {
        'route': 'cartoons',
        'title': 'Cartoons',
        'image': 'static/images/cartoon.png'
    },
    {
        'route': 'sport',
        'title': 'Sport',
        'image': 'static/images/sport.png'
    }
]

entities = [
    {
        'creation_date': datetime.datetime.now(),
        'title': 'Sector gaza',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                'sed do eiusmod tempor incididunt ut labore et dolore magna '
                'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                'Duis aute irure dolor in reprehenderit in voluptate velit '
                'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint '
                'occaecat cupidatat non proident, sunt in culpa qui officia '
                'deserunt mollit anim id est laborum',
        'rating': 93,
        'voters_count': 100,
        'category': 'music'
    },
    {
        'creation_date': datetime.datetime.now(),
        'title': 'Ruki vverh',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                'sed do eiusmod tempor incididunt ut labore et dolore magna '
                'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                'Duis aute irure dolor in reprehenderit in voluptate velit '
                'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint '
                'occaecat cupidatat non proident, sunt in culpa qui officia '
                'deserunt mollit anim id est laborum',
        'rating': 32,
        'voters_count': 32,
        'category': 'music'
    },
    {
        'creation_date': datetime.datetime.now(),
        'title': 'Nu pogodi',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                'sed do eiusmod tempor incididunt ut labore et dolore magna '
                'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                'Duis aute irure dolor in reprehenderit in voluptate velit '
                'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint '
                'occaecat cupidatat non proident, sunt in culpa qui officia '
                'deserunt mollit anim id est laborum',
        'rating': 5,
        'voters_count': 10,
        'category': 'cartoons'
    },
    {
        'creation_date': datetime.datetime.now(),
        'title': 'Footbal',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                'sed do eiusmod tempor incididunt ut labore et dolore magna '
                'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                'Duis aute irure dolor in reprehenderit in voluptate velit '
                'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint '
                'occaecat cupidatat non proident, sunt in culpa qui officia '
                'deserunt mollit anim id est laborum',
        'rating': 15,
        'voters_count': 20,
        'category': 'sport'
    },
]


def insert_categories(cursor: psycopg2.extensions.cursor):
    for item in categories:
        sql_expr = f"INSERT INTO categories (route, title, image) " \
            f"VALUES (\'{item.get('route')}\', \'{item.get('title')}\', \'{item.get('image')}\')"

        cursor.execute(sql_expr)


def insert_entities(cursor: psycopg2.extensions.cursor):
    for item in entities:
        sql_expr = f"INSERT INTO entities (" \
            f"creation_date, " \
            f"title, " \
            f"text, " \
            f"rating, " \
            f"voters_count, " \
            f"category_id" \
        f") " \
        f"VALUES (" \
            f"\'{item.get('creation_date')}\', " \
            f"\'{item.get('title')}\', " \
            f"\'{item.get('text')}\', " \
            f"\'{item.get('rating')}\', " \
            f"\'{item.get('voters_count')}\'," \
            f"(SELECT id FROM categories WHERE route=\'{item.get('category')}\')" \
        f")"
        cursor.execute(sql_expr)


if __name__ == "__main__":
    try:
        connection = psycopg2.connect(
            user="test",
            password="test",
            host="127.0.0.1",
            port="5432",
            database="test"
        )

        cursor = connection.cursor()

        insert_categories(cursor)
        insert_entities(cursor)

        cursor.close()
        connection.commit()
        connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, psycopg2.Error) as error :
        print("Error while connecting to PostgreSQL", error)
