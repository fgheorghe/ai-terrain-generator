An experimental unconditional terrain generating dataset.

Dataset based on: https://www.usgs.gov/programs/national-geospatial-program/national-map

# Usage

```bash
python -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
python download-images.py && \
cd images && \
mogrify -verbose -resize 256x256! -format jpg *.jpg
```