An experimental unconditional AI terrain generator.

Dataset based on: https://www.usgs.gov/programs/national-geospatial-program/national-map

# Install dependencies

Download to train/terrain/: https://raw.githubusercontent.com/huggingface/diffusers/main/examples/unconditional_image_generation/train_unconditional.py

Optionally comment this line in the file above: check_min_version("0.17.0.dev0")

Issue the following:

```bash
python -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt 
```

# Prepare dataset

```bash
make dataset
```

# Train

```bash 
make learn
```

# Generate

```bash
make output
```