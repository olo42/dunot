from zettelkasten.zettel import Zettel

# Date tests
def test_get_date():
    z = Zettel('any_url')
    z.date_time = '1.4.2022 13:00'
    
    assert z.get_date() == '1.4.2022'

def test_get_no_date():
    z = Zettel('any_url')
    z.date_time = None
    
    assert z.get_date() == None

# Time tests
def test_get_time():
    z = Zettel('any_url')
    z.date_time = '1.4.2022 13:00'
    
    assert z.get_time() == '13:00'

def test_get_no_time_if_none_is_given():
    z = Zettel('any_url')
    z.date_time = None
    
    assert z.get_time() == None

def test_get_no_time_if_no_time_is_given():
    z = Zettel('any_url')
    z.date_time = '1.4.2022'
    
    assert z.get_time() == None