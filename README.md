# KINGDOM
Created rest api and a simple webpage using json from this [country api.](https://restcountries.eu/rest/v2/all)
## Requirement
Python 3.6+


## Installation
- Install the dependency using 
`pip install -r requirements.txt`
- Rename **.env.example** file that is situated in **kingdom/** folder to **.env**
- Change `SECRET_KEY` , `DB_NAME` in the **.env** file.
- Make Migrations `python manage.py migrate`
- Run this command to insert data `python manage.py runscript insert_all_data`, **THIS COMMAND WILL TAKE MORE THAN 6MINS TO FINISH. DO NOT STOP THE COMMAND MIDDLE OF THE OPERATION**
- If previous command was successful, Create a Super Admin `python manage.py createsuperuser`
- Run the application `python manage.py runserver` . This will run the server at http://127.0.0.1:8000/.

## How to use

### Frontend
When you hit the server url `(http://127.0.0.1:8000/)` in the browser, this will redirect you to the `login` page. You can login through superuser that you have created earlier. You can also register a new superuser in `registration` page.

### Consuming API

Send curl request with basic authentication.

```
curl --request GET -u username:password 'http://127.0.0.1:8000/api/v1/countries/'
```
> Insert **Super Admin's username and password** in the `username` and `password` field when requesting through `curl`.

### API Endpoints

#### Here `{pk}` is Particular Countries Primary Key.

### 1. List of all countries
```
Path : /api/v1/countries/
Http Method: GET
Authorization: Basic Auth

Response: [
    {
        "id": 1,
        "languages": [
            {
                "id": 1,
                "name": "Pashto"
            },
        ],
        "neighbours": [
            {
                "id": 49,
                "name": "China",
                "alpha3code": "CHN"
            },

        ],
        "name": "Afghanistan",
        "alpha2code": "AF",
        "capital": "Kabul",
        "population": "27657145",
        "timezone": "['UTC+04:30']",
        "flag": "https://restcountries.eu/data/afg.svg"
    },
    ...
]
````

### 2. Details of a specific country
```
Path : /api/v1/countries/{pk}/
Http Method: GET
Authorization: Basic Auth

Response: {
    "id": 1,
    "languages": [
        {
            "id": 1,
            "name": "Pashto"
        },
    ],
    "neighbours": [
        {
            "id": 233,
            "name": "Turkmenistan",
            "alpha3code": "TKM"
        },
        {
            "id": 242,
            "name": "Uzbekistan",
            "alpha3code": "UZB"
        }
    ],
    "name": "Afghanistan",
    "alpha2code": "AF",
    "capital": "Kabul",
    "population": "27657145",
    "timezone": "['UTC+04:30']",
    "flag": "https://restcountries.eu/data/afg.svg"
}
````

### 3. Create a new country
```
Path : /api/v1/countries/
Http Method: POST
Authorization: Basic Auth
Media Type: application/json
Content: {
            "name": "test",
            "alpha2code": "tst",
            "capital": "testing",
            "population": "123",
            "timezone": "['UTC+04:30']",
            "flag": "test.com",
            "languages": [
                1
            ],
            "neighbours": [
                2
            ]
        }

Response: {
            "id": 254,
            "name": "test",
            "alpha2code": "tst",
            "capital": "testing",
            "population": "123",
            "timezone": "['UTC+04:30']",
            "flag": "test.com",
            "languages": [
                1
            ],
            "neighbours": [
                2
            ]
        }
````
> Here you can send `languages` as empty array. But you have to send atleast one value in `neighbours` array. Also `languages` and `neighbours` array's only accept primary key values.

### 4. Update an existing country
```
Path : /api/v1/countries/{pk}/
Http Method: PATCH/PUT
Authorization: Basic Auth
Media Type: application/json
Content: {
            "name": "test",
            "alpha2code": "tst",
            "capital": "testing",
            "population": "123",
            "timezone": "['UTC+04:30']",
            "flag": "test.com",
            "languages": [
                1, 2
            ],
            "neighbours": [
                2, 4
            ]
        }

Response: {
            "id": 254,
            "name": "test",
            "alpha2code": "tst",
            "capital": "testing",
            "population": "123",
            "timezone": "['UTC+04:30']",
            "flag": "test.com",
            "languages": [
                1, 2
            ],
            "neighbours": [
                2,
                4
            ]
        }
````
> Here you can send `languages` as empty array. But you have to send atleast one value in `neighbours` array. Also `languages` and `neighbours` array's only accept primary key values.

### 5. Delete an existing country
```
Path : /api/v1/countries/{pk}/
Http Method: DELETE
Authorization: Basic Auth

````

### 6. List of neighbouring countries of a specific country
```
Path : /api/v1/countries/{pk}/neighbours/
Http Method: GET
Authorization: Basic Auth

Response: [
    {
        "id": 49,
        "name": "China",
        "alpha3code": "CHN"
    },
    {
        "id": 108,
        "name": "Iran (Islamic Republic of)",
        "alpha3code": "IRN"
    },
]
````

### 7. List of countries that speak the same language based on a specific language. `language` parameter is case sensitive.
```
Path : /api/v1/countries/?language=Example
Http Method: GET
Authorization: Basic Auth

Response: [
    {
        "id": 19,
        "languages": [
            {
                "id": 19,
                "name": "Bengali"
            }
        ],
        "neighbours": [
            {
                "id": 105,
                "name": "India",
                "alpha3code": "IND"
            },
            {
                "id": 154,
                "name": "Myanmar",
                "alpha3code": "MMR"
            }
        ],
        "name": "Bangladesh",
        "alpha2code": "BD",
        "capital": "Dhaka",
        "population": "161006790",
        "timezone": "['UTC+06:00']",
        "flag": "https://restcountries.eu/data/bgd.svg"
    }
]
````

### 8. Searching a country by its name (should be able to search partial name)
```
Path : /api/v1/countries/?search=example
Http Method: GET
Authorization: Basic Auth

Response: [
    {
        "id": 3,
        "languages": [
            {
                "id": 5,
                "name": "Albanian"
            }
        ],
        "neighbours": [
            {
                "id": 88,
                "name": "Greece",
                "alpha3code": "GRC"
            },
            {
                "id": 133,
                "name": "Macedonia (the former Yugoslav Republic of)",
                "alpha3code": "MKD"
            },
            {
                "id": 150,
                "name": "Montenegro",
                "alpha3code": "MNE"
            },
            {
                "id": 183,
                "name": "Republic of Kosovo",
                "alpha3code": "KOS"
            }
        ],
        "name": "Albania",
        "alpha2code": "AL",
        "capital": "Tirana",
        "population": "2886026",
        "timezone": "['UTC+01:00']",
        "flag": "https://restcountries.eu/data/alb.svg"
    },
    {
        "id": 217,
        "languages": [
            {
                "id": 29,
                "name": "Norwegian"
            }
        ],
        "neighbours": [],
        "name": "Svalbard and Jan Mayen",
        "alpha2code": "SJ",
        "capital": "Longyearbyen",
        "population": "2562",
        "timezone": "['UTC+01:00']",
        "flag": "https://restcountries.eu/data/sjm.svg"
    }
]
````
