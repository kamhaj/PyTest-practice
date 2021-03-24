''' pytest fixture '''
from StudentDB import StudentDB
import pytest


@pytest.fixture(scope='module')
def db():
    print('\n~~~~~~~~~~~~ setup ~~~~~~~~~~~~~')
    db_fixture = StudentDB()
    db_fixture.connect('database_mock.json')
    yield db_fixture
    print('\n~~~~~~~~~~ tierdown ~~~~~~~~~~~')
    db_fixture.close()

def test_miley_data(db):
    miley_data = db.get_data("Miley")
    assert miley_data['id'] == 2
    assert miley_data['name'] == 'Miley'  
    assert miley_data['grade'] == 'failed'
    
    
def test_george_data(db):
    george_data = db.get_data("George")
    assert george_data['id'] == 3
    assert george_data['name'] == 'George'  
    assert george_data['grade'] == 'passed'


def test_ben_data(db):
    george_data = db.get_data("Ben")
    assert george_data['id'] == 1
    assert george_data['name'] == 'Ben'  
    assert george_data['grade'] == 'passed'
    
    
def test_jack_data(db):
    jack_data = db.get_data("Jack")
    assert jack_data['id'] == 5
    assert jack_data['name'] == 'Jack'  
    assert jack_data['grade'] == 'passed'
    
    
'''  setup and tear down methods  '''
# from StudentDB import StudentDB
# import pytest

# db = None

# ## pytest will run it before test cases
# def setup_module(module):
    # print('\n~~~~~~~~~~~~ setup ~~~~~~~~~~~~~')
    # global db
    # db = StudentDB()
    # db.connect('database_mock.json')
 
# ## pytest will run it after test cases   
# def teardown_module(module):
    # print('\n~~~~~~~~~~ tierdown ~~~~~~~~~~~')
    # db.close()

 
# def test_miley_data():
    # miley_data = db.get_data("Miley")
    # assert miley_data['id'] == 2
    # assert miley_data['name'] == 'Miley'  
    # assert miley_data['grade'] == 'failed'
    
    
# def test_george_data():
    # george_data = db.get_data("George")
    # assert george_data['id'] == 3
    # assert george_data['name'] == 'George'  
    # assert george_data['grade'] == 'passed'
        

