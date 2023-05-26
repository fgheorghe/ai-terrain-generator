from diffusers import DiffusionPipeline
from diffusers import StableDiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("../train/terrain/model/")
# Comment the line above and uncomment the line below to use the huggingface pretrained model:
# pipeline = DiffusionPipeline.from_pretrained("fgheorghe/terrain-generator")
pipeline = pipeline.to("cuda")

image = pipeline().images[0]
image.save("output.png")

