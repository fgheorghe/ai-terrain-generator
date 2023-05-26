An experimental unconditional terrain generating model.

Dataset: https://github.com/fgheorghe/terrain-generator-dataset

Requires: https://huggingface.co/docs/diffusers/training/unconditional_training

And: https://raw.githubusercontent.com/huggingface/diffusers/main/examples/unconditional_image_generation/train_unconditional.py

Optionally comment this line in the file above: check_min_version("0.17.0.dev0")

# Usage

```bash 
python -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
mkdir -p model && \
sh train.sh
```