from bank import value
def test_bank0():
  assert value("hello,world")==0
  assert value("Hello,world")==0
def test_bank20():
  assert value("hell,hitler")==20
  assert value("HELL,HITLER")==20
def test_bank100():
  assert value(",00293wjieja")==100


