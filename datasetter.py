"""
Module used for downloading images used to train, test, and validate models.
"""

import sys
import argparse
import pandas as pd

sys.path.append('./helpers')
from ai_utilities import image_download


DATASET_PATH = './data/dataset'
PESTS_CSV_METADATA_PATH = './data/pestes e pragas - cabo verde.csv'


def download_images(keyworks: list[str], output_dir: str) -> None:
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser('datasetter')
    parser.add_argument('--out-dir', '--out_dir', type=str, required=False,
                        help='Determine the output dir for the downloaded images', default=DATASET_PATH)

    args = parser.parse_args()

    dataframe = pd.read_csv(PESTS_CSV_METADATA_PATH)
