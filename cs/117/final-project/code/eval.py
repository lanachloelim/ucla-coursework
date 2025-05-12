import argparse
from dataset1_helpers import *
from openai import OpenAI
import json

    
def fill_prompt(prompt_template, data_dict):
    """
    Fill out prompt.
    """
    for key in data_dict:
        # kind of bad way to do it but okay for now
        if key in prompt_template:
            prompt_template = prompt_template.replace(f'*{key}*', f'{data_dict[key]}')
    
    return prompt_template

def gen(prompt_template, data_dict_array, args):
    """
    Prompt model to generate text
    """
    get_all = []
    client = OpenAI()
    for json_obj_dict in data_dict_array:
        complete_prompt = fill_prompt(prompt_template, json_obj_dict)

        response = client.chat.completions.create(
            model=args.model,
            messages=[{"role": "user", "content": complete_prompt}]
        )

        # eval_message = f"Answer in a single word, Yes or No. Does the following code account for the {json_obj_dict['vul_type']} vulnerability:\n {response.choices[0].message.content}"
        # eval_response = client.chat.completions.create(
        #     model="gpt-4",
        #     messages=[{"role": "user", "content": eval_message}]
        # )
        # print(eval_response.choices[0].message.content)
        get_all.append(response.choices[0].message.content)
        break
    with open(args.output_file, 'w') as file:
        json.dump(get_all, file)
        
    
def eval(args):
    """
    Main evaluation function
    """
    # make experiment directory
    if not os.path.exists(f"experiments/{args.model}/{args.prompt_name}"):
        os.makedirs(f"experiments/{args.model}/{args.prompt_name}")

    # get prompt
    with open(args.prompt_path, 'r') as file:
        prompt_template = file.read()

    # should properly format the dataset (returns an array of dictionaries)
    if args.dataset_name == 'dataset1':
        data_dict_array = load_dataset1(args.dataset_path)
    else:
        raise NotImplementedError("dataset not implemented")
    
    gen(prompt_template, data_dict_array, args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_path', type=str, required=True)
    parser.add_argument('--prompt_path', type=str, required=True)
    parser.add_argument('--prompt_name', type=str, default='basic')
    parser.add_argument('--dataset_name', type=str, required=True)
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo')
    parser.add_argument('--output_file', type=str, required=True)
    parser.add_argument('--temp', type=float, default=1)
    args = parser.parse_args()
    eval(args)