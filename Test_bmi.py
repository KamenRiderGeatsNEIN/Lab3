import Lab2.bmi as bmi

def test_bmi_normal_weight():
    test=0
    input_height= 1.75
    input_weight=65

    result=bmi.calculate_bmi(input_height,input_weight)
    assert (result==test)



def test_bmi_over_weight():
    test=1
    input_height= 1.75
    input_weight=80

    result=bmi.calculate_bmi(input_height,input_weight)
    assert (result==test)

def test_bmi_under_weight():
    test=-1
    input_height= 1.75
    input_weight=50

    result=bmi.calculate_bmi(input_height,input_weight)
    assert (result==test)