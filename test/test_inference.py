import sys
sys.path.append('./') 
from utilities.utils import run_inference


#Test the output of prediction: is it in the right format(probabilities)
def test_inference_neg(inference_data_neg):
    prediction = run_inference(inference_data_neg)

    assert 0 <= round(prediction[1],3) <= 1.0


def test_inference_pos(inference_data_pos):
    prediction = run_inference(inference_data_pos)

    assert 0 <= round(prediction[1],3) <= 1.0