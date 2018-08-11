from DiabeticPredict import function
import argparse


default_model = "Data/model.csv"
default_test_data = "Data/test_dataset.csv"
default_output = "predicted_result.csv"

parser = argparse.ArgumentParser()
parser.add_argument("-model", "-m", help="model filename (csv format) or default", default=default_model)
parser.add_argument("-test", "-t", help="test filename (csv format) or default", default=default_test_data)
parser.add_argument("-output", "-o", help="output filename (csv format) or default", default=default_output)

args = parser.parse_args()

model = args.model
test = args.test
output = args.output

result_df = function.predict_diabetic(model, test)
function.save_result(result_df, output)

