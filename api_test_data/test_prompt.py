import requests
# from fastapi import FastAPI

# app = FastAPI()



txt2img_styles_res = requests.get('https://photolab-ai.com/media/giff/ai/txt2img_styles/txt2img_styles.json')
styles_dict = txt2img_styles_res.json()

# app.txt2img_styles = styles_dict


style_id = 1
prompt = ""

global_style_dict = next((d for d in styles_dict if d.get("id") == 1), None)
if style_id != 1:
        style_dict = next((d for d in styles_dict if d.get("id") == style_id), None)
        if style_dict:
            prompt = style_dict['prompt'].format(prompt=prompt)
    prompt += global_style_dict['prompt']
    # negative_prompt += global_style_dict['negative_prompt']
print(prompt)