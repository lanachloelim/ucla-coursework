import os

all_cwes = ["022", "078", "079", "089", "125", "190", "416", "476", "787"]
prompts = ["zero_shot", "zero_shot_cot", "zero_shot_with_vul"]
dataset = "dataset1"
model = "gpt-3.5-turbo"
for prompt in prompts:
    for cwe in all_cwes:
        run_string = f"python3 eval.py --dataset_path data/dataset1/val/cwe-{cwe}.jsonl --prompt_path prompts/{dataset}/{prompt}.txt --dataset_name {dataset}  --output_file experiments/{model}/{prompt}/cwe-{cwe} --prompt_name {prompt}"
        os.system(run_string)