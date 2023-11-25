from urllib import request


remote_url='https://www.kaggle.com/datasets/ibriiee/video-games-sales-dataset-2022-updated-extra-feat/download?datasetVersionNumber=1'
local_file='Video_Games.csv/'
request.urlretrieve(remote_url, local_file)