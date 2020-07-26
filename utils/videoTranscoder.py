import configparser
import os

from transcoded.job import TranscodingJob
from transcoded.__main__ import parse_profiles

def transcodeVideo(inputFile, outputFile):
    config = configparser.ConfigParser()
    config.read('utils/tcon.ini')
    profiles = parse_profiles(config)
    print(profiles)

    for profile in parse_profiles(config):
        job = TranscodingJob()

        job.sources.append(os.path.abspath('testVideos/inputs/{}'.format(inputFile)))
        job.destination = os.path.abspath('/testVideos/outputs/{}'.format(outputFile))

        job.profile = profile
        job.user = 'test'

        job.run()
