import os
from dotenv import load_dotenv
from openai import OpenAI


## VARIAVEIS DE AMBIENTE
load_dotenv()
LLM_MODEL = os.getenv('LLM_MODEL') ## MODELO DA LLM
PROMPT_LLM = os.getenv('PROMPT_LLM') ## PROMPT DA LLM


client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

def completion(response): ## função para falar com a inteligência Artificial
       try:
            result = client.chat.completions.create(
               model=f"{LLM_MODEL}",
               messages=[{"role":"system", "content": f"{PROMPT_LLM}"},
               {"role": "user","content":f"{response}"}],
               temperature=0,
               max_tokens=1000
             )
            return result
       except Exception as e:
             print(f'Erro:{e}')
             return None