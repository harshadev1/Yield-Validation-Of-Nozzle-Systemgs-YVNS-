from YVNS import convert_hour
from YVNS import static_elevation
from YVNS import flow_nozzles
from YVNS import end_result


def test_convert_hour():
    assert convert_hour(0.25) == 900
    assert convert_hour(2) == 7200


def test_static_elevation():
    assert static_elevation(10) == 3.686241145449588
    assert static_elevation(5) == 1.843120572724794


def test_flow_nozzles():
    assert flow_nozzles(4) == 200
    assert flow_nozzles(16) == 400

def test_end_result():
    assert end_result(1) == 100
    assert end_result(9) == 300
