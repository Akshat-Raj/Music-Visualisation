from multiprocessing import Process
from visualize import req_plot,playing_audio


if __name__=="__main__":
    p1 = Process(target=playing_audio, args=())
    p1.start()
    p2 = Process(target=req_plot, args=())
    p2.start()
    p1.join()
    p2.join()
