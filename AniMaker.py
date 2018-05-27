from moviepy.editor import VideoClip
import numpy as np
from PIL import Image
import argparse
import os
'''
TODO
可跳过序号
'''
def make_frame(f,rfps,fps,time):
    print(f,rfps,fps,time)
    def func(t):
#        print('t=%s fps=%s time=%s l=%s'%(t,fps,time,len(os.listdir(f))))
        print(os.listdir(f)[int(t/time*len(os.listdir(f)))])
        return np.array(Image.open(f+"\\"+os.listdir(f)[int(t/time*len(os.listdir(f)))]))
    return func

def main():
    parser = argparse.ArgumentParser(prog='AniMaker',description='动画短片制作器by lzy2002 site:lzy2002.com')
    parser.add_argument('-i','--inputs',help='输入文件所在目录',required=True)
    parser.add_argument('-o','--output',help='输出文件',default='movie.mp4')
    parser.add_argument('-f','--fps',help='帧频fps',default=24)
    parser.add_argument('-rf','--recordfps',help='录制帧频fps',default=60)
    parser.add_argument('-t','--time',help='时长s',default=5)
    args = parser.parse_args()
    animation = VideoClip(make_frame(args.inputs,float(args.recordfps),int(args.fps),float(args.time)), duration=float(args.time))
    animation.write_videofile(args.output, fps=int(args.fps))

if __name__ == '__main__':
    main()

