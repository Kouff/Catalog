# Django Catalog

## Preparation for running
Clone a project and move to it:

    $ git clone https://github.com/Kouff/Catalog.git
    $ cd Catalog

Create a [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)
and [activate](https://virtualenv.pypa.io/en/latest/user_guide.html#activators) it and install a requirements:

    $ pip install -r requirements.txt

Create the file `.env` with virtual environments (see in `.env.example`):

    SECRET_KEY={secret}
    DEBUG={true|false}
    DB_NAME={name}
    DB_USER={user}
    DB_PASSWORD={password}
    DB_HOST={host}
    DB_PORT={port}

Migrate:

    $ python manage.py migrate

## Loading of a test data

    $ python manage.py loaddata fixtures/catalog.json

## Running of the project

    $ python manage.py runserver

## Urls

- ### catalogs/

Response `catalogs/`:
```json
{
    "count": 33,
    "next": "catalogs/?limit=10&offset=20",
    "previous": "catalogs/?limit=10",
    "results": [
        {
            "id": 11,
            "name": "Laptops"
        },
        {
            "id": 12,
            "name": "PC"
        },
        ...
    ]
}
```

- ### catalogs/\<int:catalog_id>/products/

Response `catalogs/1/products/`:
```json
{
    "count": 111,
    "next": "catalogs/1/products/?limit=10&offset=20",
    "previous": "catalogs/1/products/?limit=10",
    "results": [
        {
            "id": 11,
            "name": "Samsung Odyssey G5A 27",
            "description": "A high-quality model from the new series of Samsung Odyssey gaming monitors.",
            "price": 14000.0
        },
        {
            "id": 12,
            "name": "Samsung Odyssey G7 32",
            "description": "High-quality gaming monitor with a 31.5-inch WQHD/2K resolution.",
            "price": 19000.0
        },
        ...
    ],
    "params": [
        {
            "name": "Brightness",
            "values": [
                {
                    "value": "250",
                    "count": 33
                },
                {
                    "value": "300",
                    "count": 74
                },
                ...
            ]
        },
        {
            "name": "Diagonal",
            "values": [
                {
                    "value": "24",
                    "count": 57
                },
                {
                    "value": "25",
                    "count": 7
                },
                ...
            ]
        },
        ...
    ]
}
```
- ### products/\<int:pk>/

Response `products/1/`:
```json
{
    "id": 1,
    "name": "MSI Optix G241",
    "description": "A monitor designed to win hot gaming battles with a 23.8-inch screen.",
    "price": 7800.0,
    "images": [
        {
            "file": "media/products/msi_optix_g241(1).png",
            "title": "in front"
        },
        {
            "file": "media/products/msi_optix_g241(2).png",
            "title": "in front 2"
        },
        ...
    ],
    "params": [
        {
            "name": "Brightness",
            "value": "250"
        },
        {
            "name": "Diagonal",
            "value": "24"
        },
        ...
    ]
}
```
