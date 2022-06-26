![datum](docs/datum.jpg "Reference Point")

# datum

An automated data pipeline to create pre-trained detection models for transfer learning utilizing the OpenImages dataset.


### Core Components

- Data aggregation by [FiftyOne](https://github.com/voxel51/fiftyone)
- Training with [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- Deployment through [Cog](https://github.com/replicate/cog) 

### Prereqs

- Docker
- NVIDIA GPU (if training)

## Installation

Install script pulls and builds Fiftyone and YOLOv5 images.

```bash
utils/Install.sh
```

## Dataset creation

- Change line 10 of [datum/__main__.py](datum/__main__.py) to the classes you want
- Modify dataset.yaml file in /data folder
```yaml
# Original
train: ./images/train/
val: ./images/val/
# Correct
train: /data/images/train/
val: /data/images/val/
```

## Training

Use Ultralytics' [Docker image](https://hub.docker.com/r/ultralytics/yolov5) to train on dataset.

- Spin up container
```bash
utils/Train.sh
```
- Run [training sequence](https://docs.ultralytics.com/tutorials/train-custom-datasets/) inside container
```bash
python train.py --img 640 --batch 16 --epochs 100 --data /data/dataset.yaml --weights yolov5s.pt
```

### To-do

- Make class selection more user friendly
- Use Docker volumes for dataset
- Automate dataset.yaml formatting
- Create full compose stack
