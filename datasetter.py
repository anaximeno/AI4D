"""
Module used for downloading images used to train, test, and validate models.
"""

import sys
import argparse

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
        image_download(search_text=keyword, n_images=imgs_per_class, image_dir=output_dir, engine=engine)

    if 'stats' not in kwargs or kwargs['stats'] is True:
        print(f' => Download finished, find the downloaded files at {output_dir!r}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('datasetter')

    parser.add_argument('--out_dir', type=str, required=False,
                        help="determine the output dir for the downloaded images (Default: '%s')" % DATASET_PATH,
                        default=DATASET_PATH)
    parser.add_argument('-n', type=int, required=False,
                        help="number of images to search (Default: '%s')" % DEFAULT_NUMBER_OF_IMAGES_PER_CLASS,
                        default=DEFAULT_NUMBER_OF_IMAGES_PER_CLASS)
    parser.add_argument('--engine', required=False, type=str,
                        help="search engine to be used (Default: '%s') [Supported: 'google','bing', 'baidu', 'flickr']" % DEFAULT_SEARCH_ENGINE,
                        default=DEFAULT_SEARCH_ENGINE)
    parser.add_argument('--species', help="a list of the scientific names of pest and plagues to search (Default: %s)" % MAIN_SPECIES,
                        required=False, nargs='*', default=MAIN_SPECIES)

    args = parser.parse_args()
    download_images(args.species, imgs_per_class=args.n, output_dir=args.out_dir, engine=args.engine)
