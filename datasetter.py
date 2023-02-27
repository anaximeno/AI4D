"""
Module used for downloading images used to train, test, and validate models.
"""

import sys
import argparse
import pandas as pd

sys.path.append('./helpers')
from ai_utils import image_download
from constants import *


def download_images(keywords: list[str], imgs_per_class: int, output_dir: str, engine: str = 'bing', **kwargs) -> None:
    """Manages the process of downloading images"""

    if 'stats' not in kwargs or kwargs['stats'] is True:
        print(' => Searching for (search engine is {})\n{}'.format(engine, '\n'.join('\t-> ' + key for key in keywords)))
        print(' => Maximum images per class is %i' % imgs_per_class)
        print(' => Output directory is "%s"\n' % output_dir)

    for keyword in keywords:
        image_download(search_text=keyword, n_images=imgs_per_class, image_dir=output_dir, engine='baidu')

    if 'stats' not in kwargs or kwargs['stats'] is True:
        print(f' => Download finished, find the downloaded files at {output_dir!r}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('datasetter')

    parser.add_argument('--out-dir', '--out_dir', type=str, required=False,
                        help='Determine the output dir for the downloaded images', default=DATASET_PATH)
    parser.add_argument('-n', type=int, required=False,
                        help='Number of images to search', default=DEFAULT_NUMBER_OF_IMAGES_PER_CLASS)
    parser.add_argument('--engine', required=False, type=str, help='Search engine', default='bing')

    args = parser.parse_args()

    download_images(MAIN_SPECIES[0:2], imgs_per_class=args.n, output_dir=args.out_dir, engine=args.engine)