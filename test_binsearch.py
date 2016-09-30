from pytest import raises
from binsearch import binary_search
import numpy as np

def test_mymath():
    input = list(range(10))
    assert binary_search(input,5) == 5
    assert binary_search(input,4.5) == -1
    assert binary_search([5],5) == 0
    assert binary_search(input, 5, 1,3) == -1
    assert binary_search(input, 2, 1,3) == 2
    assert binary_search(input, 2, 3, 1) == -1
    assert binary_search(input, 2, 2, 2) == 2
    assert binary_search(input, 5, 2, 2) == -1    
def test_infinite_data():    
    assert binary_search([1,2,np.inf], 2) == 1
    assert binary_search([1,2,np.inf], np.inf) == 2
def test_array_type():
    with raises(TypeError):
        binary_search(5,5)
def test_missing_data():#The time complexity is O(n), so I add one warning in the doc    
    with raises(ValueError):
        binary_search([1,2,3,4,np.nan],2)  
def test_zero_elements():
    with raises(ValueError):
        binary_search([],2)  
def test_non_int_elements():
    with raises(TypeError):
        binary_search(['a',2,3],2)
def test_sorted():#The time complexity is O(n), so I add one warning in the doc
    with raises(TypeError):
        binary_search([4,2,3],2)         
def test_needle_toolarge():
    with raises(ValueError):
        binary_search([1,2,3,4],5) 
def test_needle_toosmall():
    with raises(ValueError):
        binary_search([1,2,3,4],-2)  
def test_missing_and_str():#An integration of two errors together    
    with raises(TypeError):
        binary_search([1,2,3,4,"a",np.nan],2)          
def test_missing_and_str_large_needle():#An integration of three errors together    
    with raises(TypeError):
        binary_search([1,2,3,4,"a",np.nan],5)                  