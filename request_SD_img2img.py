import requests


class ControlnetRequest:
    def __init__(self, b64img, prompt, neg_prompt, url="http://localhost:7860"):
        self.url = url + "/controlnet/img2img"
        self.body = {
            "init_images": [b64img],
            "resize_mode": 0,
            "denoising_strength": 0.75,
            "inpainting_fill": 0,
            "inpaint_full_res": True,
            "inpaint_full_res_padding": 0,
            "prompt": prompt,
            "negative_prompt": neg_prompt,
            "styles": [""],
            "seed": -1,
            "subseed": -1,
            "subseed_strength": 0,
            "seed_resize_from_h": -1,
            "seed_resize_from_w": -1,
            "sampler_name": "",
            "batch_size": 1,
            "n_iter": 1,
            "steps": 75,
            "cfg_scale": 6,
            "width": 512,
            "height": 512,
            "restore_faces": False,
            "tiling": False,
            "do_not_save_samples": False,
            "do_not_save_grid": False,
            "eta": 0,
            "s_churn": 0,
            "s_tmax": 0,
            "s_tmin": 0,
            "s_noise": 0,
            "override_settings": {},
            "override_settings_restore_afterwards": True,
            "script_args": [],
            "sampler_index": "DPM++ 2S a Karras",
            "include_init_images": False,
            "script_name": "",
            "send_images": True,
            "save_images": False,
            "alwayson_scripts": {},
            "controlnet_units": [
                {
                    "input_image": "",
                    "mask": "",
                    "module": "depth_midas",
                    "model": "control_depth-fp16 [400750f6]",
                    "weight": 1,
                    "resize_mode": "Crop and Resize",
                    "lowvram": False,
                    "processor_res": 512,
                    "threshold_a": 64,
                    "threshold_b": 64,
                    "guidance": 1,
                    "guidance_start": 0,
                    "guidance_end": 1,
                    "guessmode": True,
                    "pixel_perfect": False
                }
            ]
        }

    def send_request(self):
        r = requests.post(self.url, json=self.body)
        return r.json()
