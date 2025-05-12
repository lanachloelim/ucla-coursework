import argparse
from dataset1_helpers import *
from openai import OpenAI
import numpy as np

from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score

def gen(data_dict_array):
    """
    Prompt model to generate text
    """
    client = OpenAI()
    predicted = []
    true = []

    for json_obj_dict in data_dict_array:
        eval_message = f"Answer in a single word, Yes or No. I will present two functions. Tell me if the {json_obj_dict['vul_type']} type vulnerabilitiy is fixed from the first to second. {json_obj_dict['func_src_before']}\n"
        eval_message2 = f"Answer in a single word, Yes or No. Is the following function have {json_obj_dict['vul_type']} type vulnerabilities:\n {json_obj_dict['func_src_after']}"
        
        eval_response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": eval_message}]
        )

        eval_response2 = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": eval_message2}]
        )
        print(eval_response.choices[0].message.content) # should be no
        predicted.append(eval_response.choices[0].message.content == 'Yes')
        print(eval_response2.choices[0].message.content) # should be yes
        predicted.append(eval_response2.choices[0].message.content == 'Yes')
        true.append(1)
        true.append(0)
    
    predicted = np.array(predicted).astype(int)
    true = np.array(true).astype(int)

    print(accuracy_score(true, predicted))
    print(roc_auc_score(true, predicted))
    print(precision_score(true, predicted))
    print(recall_score(true, predicted))

        
    
def eval(args):
    """
    Main evaluation function
    """

    # should properly format the dataset (returns an array of dictionaries)
    if args.dataset_name == 'dataset1':
        data_dict_array = load_dataset1(args.dataset_path)
    else:
        raise NotImplementedError("dataset not implemented")
    
    gen(data_dict_array)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_path', type=str, required=True)
    parser.add_argument('--dataset_name', type=str, required=True)
    parser.add_argument('--temp', type=float, default=1)
    args = parser.parse_args()
    eval(args)