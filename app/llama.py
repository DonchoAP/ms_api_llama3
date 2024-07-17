from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class Llama3:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/llama-3-7b")
        self.model = AutoModelForCausalLM.from_pretrained("facebook/llama-3-7b")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def generate_response(self, prompt, max_length=100):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        
        output = self.model.generate(
            input_ids, 
            max_length=max_length, 
            num_return_sequences=1, 
            no_repeat_ngram_size=2, 
            top_k=50, 
            top_p=0.95, 
            temperature=0.7
        )
        
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

llama = Llama3()