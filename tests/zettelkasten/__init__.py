from zettelkasten.zettel import Zettel

def test_get_date():
    z = Zettel('some_url')
    z.date = '1.4.2022 12:00'

    assert z.get_date() == '1.4.2022'
