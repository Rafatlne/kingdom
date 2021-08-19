import requests
from countries.models import Country, Language, Neighbour


def run():
    url = "https://restcountries.eu/rest/v2/all"
    response = requests.request("GET", url).json()
    bulk_insert_language_neighbour(response)
    insert_into_country_through_table(response)


def bulk_insert_language_neighbour(response):
    language_set = set()
    language_object_list = []
    neighbour_object_list = []

    for single_list in response:
        # insert unique languages
        for language in single_list['languages']:
            if language['name'] not in language_set:
                language_set.add(language['name'])
                language_object_list.append(
                    Language(
                        name=language['name']
                    )
                )

        neighbour_object_list.append(
            Neighbour(
                name=single_list['name'],
                alpha3code=single_list['alpha3Code']
            )
        )

    lang_obj = Language.objects.bulk_create(language_object_list)
    Neighbour.objects.bulk_create(neighbour_object_list)


def insert_into_country_through_table(response):
    language_all_objects = list(Language.objects.all())
    neighbour_all_objects = list(Neighbour.objects.all())

    language_all_objects = {
        language.name: language for language in language_all_objects
    }

    neighbour_all_objects = {
        neighbour.alpha3code: neighbour for neighbour in neighbour_all_objects
    }

    for single_list in response:
        country = Country(
            alpha2code=single_list['alpha2Code'],
            name=single_list['name'],
            capital=single_list['capital'],
            population=single_list['population'],
            timezone=single_list['timezones'],
            flag=single_list['flag'],
        )

        country.save()

        for language in single_list['languages']:
            # language_obj = Language.objects.filter(
            #     name=language['name']).first()
            # country.languages.add(language_obj)
            country.languages.add(language_all_objects[language['name']])

        for border in single_list['borders']:
            # neighbour_obj = Neighbour.objects.filter(alpha3code=border).first()
            # country.neighbours.add(neighbour_obj)
            country.neighbours.add(neighbour_all_objects[border])
