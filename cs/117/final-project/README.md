# UCLA COM SCI 117: Final Project

## LLM Driven Security Vulnerability Repair

<img width="748" alt="Screenshot 2025-05-11 at 5 51 37 PM" src="https://github.com/user-attachments/assets/ee183b18-7f17-4918-a136-19e68e588347" />

### Summary

This project explores the use of Large Language Models (LLMs), specifically OpenAI's GPT-3.5-turbo, to automatically repair security vulnerabilities in code. By leveraging prompt engineering rather than fine-tuning, we aim to guide out-of-the-box LLMs to fix code vulnerabilities across multiple datasets. Our best prompt achieved over a 50% repair rate. We also introduce a semi-automatic evaluation system combining LLMs and human review for robust assessment of repairs.

**Key Contributions:**
- Evaluated prompt engineering strategies for vulnerability repair with LLMs.
- Developed a zero-shot vulnerability evaluation framework combining automatic and human evaluation.
- Achieved a >50% repair rate using Few Shot Chain-of-Thought prompts.
- Conducted ablation studies on false positives, adversarial attacks, and line-level repair.

---

### Resources

**Datasets:**
- **SVEN**: 9 CWE types from the MITRE Top 25, each sample is a function with a known vulnerability.
- **Big-Vul**: C/C++ vulnerabilities from the CVE database, 91 vulnerability types, 3,754 vulnerabilities from 348 open-source GitHub projects.
- **Vul4J**: Real-world Java vulnerabilities, each with a human patch and test cases for reproducibility.

**Model: Salesforce CodeT5 by Hugging Face** ([link](https://huggingface.co/Salesforce/codet5-small))
- Used as a base for the semi-automatic evaluation tool. The decoder was replaced with a binary classification head to automatically assess whether code repairs were successful.

---

### Acknowledgements
Group project by Lana Lim, Vinay Shukla, Brian Felipe Brito, and Steven Pan. Assistance from Prof. Yuan Tian and TA Ying Li.
