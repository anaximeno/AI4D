"""
Module used for downloading images used to train, test, and validate models.
"""

import sys
import argparse
import pandas as pd

sys.path.append('./helpers')
from ai_utils import image_download


DATASET_PATH = './data/dataset'
PESTS_CSV_METADATA_PATH = './data/pestes e pragas - cabo verde.csv'
DEFAULT_NUMBER_OF_IMAGES_PER_CLASS = 1000


def download_images(keyworks: list[str], imgs_per_class: int, output_dir: str) -> None:
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser('datasetter')

    parser.add_argument('--out-dir', '--out_dir', type=str, required=False,
                        help='Determine the output dir for the downloaded images', default=DATASET_PATH)
    parser.add_argument('-n', type=int, required=False,
                        help='Number of images to search', default=DEFAULT_NUMBER_OF_IMAGES_PER_CLASS)

    args = parser.parse_args()

    dataframe = pd.read_csv(PESTS_CSV_METADATA_PATH)
