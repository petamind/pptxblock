"""Ok this is for slicing video"""
import os
import threading
import time

class SliceVideo(threading.Thread):
    """
    Slice the video to images
    """

    def __init__(self, threadID, video_id, video_url, thumbs_html):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.video_id = video_id
        self.video_url = video_url
        self.thumbs_html = thumbs_html

    def run(self):
        # print "Starting " + self.name
        # new_path = 'E:/vids/new_days.txt'
        # new_days = open(new_path, 'w')

        # title = 'Video Test writing\n'
        # new_days.write(title)
        #print(title)
        # new_days.close()
        download_cmd = ('youtube-dl {1} -o /vids/{0}/{0}.mp4').format(self.video_id, self.video_url)
        os.system(download_cmd)
        
        slice_cmd = ('scenedetect -i /vids/{0}/{0}.mp4 -co /vids/{0}/{0}.csv -d content -si -df 4').format(self.video_id)
        os.system(slice_cmd)
        #read cvs
        fline = open(('/vids/{0}/{0}').format(self.video_id)).readline().rstrip()
        times = fline.split(",")
        #process to html div 
        self.thumbs_html += fline



# def print_time(thread_name, counter, delay):
#     "OK docstring"
#     threadName = ""
#     return
