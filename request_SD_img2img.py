import requests


class ControlnetRequest:
    def __init__(self, b64img, prompt, neg_prompt, url="http://localhost:7860"):
        self.url = url + "/controlnet/img2img"
        self.body = {
            "init_images": [b64img],
            "enabled": True,
            "resize_mode": 1,
            "prompt": prompt,
            "denoising_strength": 0.75,
            "negative_prompt": neg_prompt,
            "seed": 500,
            "subseed": 10,
            "subseed_strength": 1,
            "batch_size": 1,
            "n_iter": 20,
            "steps": 50,
            "cfg_scale": 7,
            "width": 512,
            "height": 512,
            "restore_faces": True,
            "eta": 0,
            "sampler_index": "Euler a",
            "controlnet_model": 'control_canny-fp16 [e3fe7712]',
            "controlnet_guidance": 1.0,
            "processor_res": 512,
            "controlnet_guessmode": False,
        }

    def send_request(self):

        r = requests.post(self.url, json=self.body)
        return r.json()
