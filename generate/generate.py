from diffusers import DiffusionPipeline
from diffusers import StableDiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("../train/terrain/model/")
pipeline = pipeline.to("cuda")

image = pipeline().images[0]
image.save("output.png")