#!/usr/bin/python3
import fiftyone as fo
import fiftyone.zoo as foz
import argparse

parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "--classes", type=list, default=["Box"], help=("List of classes to download")
)
parser.add_argument(
    "--num_samples", type=int, default=1000, help="Number of samples to download."
)
parser.add_argument(
    "--download_folder",
    type=str,
    default="/fiftyone/",
    help="Folder where to download the images.",
)
parser.add_argument(
    "--export_dir",
    type=str,
    default="/data/",
    help="Folder where to download the images.",
)

args = parser.parse_args()

splits = ["train", "validation", "test"]

dataset = foz.load_zoo_dataset(
    "open-images-v6",
    splits=splits,
    max_samples=args.num_samples,
    seed=0,
    label_types=["detections"],
    classes=args.classes,
    shuffle=True,
)

for split in ["train", "val"]:
    # Export images and ground truth labels to disk
    dataset.export(
        export_dir=args.export_dir,
        dataset_type=fo.types.YOLOv5Dataset,
        label_field="detections",
        classes=args.classes,
        split=split,
    )

if __name__ == "__main__":
    session = fo.launch_app(dataset)
    session.wait()
