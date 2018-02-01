#
# OtterTune - upload_data.py
#
# Copyright (c) 2017-18, Carnegie Mellon University Database Group
#
'''
Created on Nov 30, 2017

@author: dvanaken
'''

import argparse
import glob
import logging
import os
import sys
import requests

# Logging
LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)


def upload(basedir, upload_code, upload_url):
    for wkld_dir in sorted(glob.glob(os.path.join(basedir, '*'))):
        LOG.info('Uploading sample for workload %s...', wkld_dir)
        sample_idx = 0
        while True:
            samples = glob.glob(os.path.join(wkld_dir, 'sample-{}__*').format(sample_idx))
            if len(samples) == 0:
                break
            assert len(samples) == 4
            basename = samples[0].split('__')[0]
            params = {
                'summary': open(basename + '__summary.json', 'rb'),
                'knobs': open(basename + '__knobs.json', 'rb'),
                'metrics_before':open(basename + '__metrics_start.json', 'rb'),
                'metrics_after':open(basename + '__metrics_end.json', 'rb'),
            }

            response = requests.post(upload_url+"/new_result/",
                                    files=params,
                                    data={'upload_code':  upload_code})
            LOG.info("Response: %s\n", urllib2.urlopen(request).read())
            sample_idx += 1


def main():
    parser = argparse.ArgumentParser(description="Upload generated data to the website")
    parser.add_argument('datadir', type=str, nargs=1,
                        help='Directory containing the generated data')
    parser.add_argument('upload_code', type=str, nargs=1,
                        help='The website\'s upload code')
    parser.add_argument('--upload_url', type=str, nargs=1,
                        help='The website\'s URL')    
    args = parser.parse_args()    
    url = "http://0.0.0.0:8000" if not args.upload_url else args.upload_url
    upload(args.datadir, args.upload_code, args.upload_url)

if __name__ == "__main__":
    main()
