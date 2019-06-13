from song_guess import lower_answer

def test_lower_answer():
    
    """
    Tests functionality of lower_answer function,
    to make player inputs lowercase
    """
    
    test = lower_answer("HELLO")
    
    assert test == "hello"
    
    print ("Passed lower_answer")
    
# Runs test
test_lower_answer()
