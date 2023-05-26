dataset:
	cd datasets/terrain/ && \
	python download-images.py && \
	cd images && \
	mogrify -verbose -resize 256x256! -format jpg *.jpg && \
	cd ../../
learn:
	cd train/terrain/ && \
	mkdir -p model && \
	sh train.sh
output:
	cd generate/ && python generate.py
all: dataset learn output