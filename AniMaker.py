from moviepy.editor import VideoClip
import numpy as np
from PIL import Image
import argparse

def make_frame(inputs):
    def func(t):
        return np.array(Image.open(inputs+"\\"+str(int(t*60))+".jpg"))
    return func

def main():
    parser = argparse.ArgumentParser(prog='AniMaker',description='动画短片制作器by lzy2002 site:lzy2002.com')
    parser.add_argument('-i','--inputs',help='输入文件所在目录',required=True)
    parser.add_argument('-o','--output',help='输出文件',default='movie.mp4')
    parser.add_argument('-f','--fps',help='帧频fps',default=24)
    parser.add_argument('-t','--time',help='时长s',default=5)
    args = parser.parse_args()
    animation = VideoClip(make_frame(args.inputs), duration=args.time)
    animation.write_videofile(args.output, fps=args.fps)

if __name__ == '__main__':
    main()

