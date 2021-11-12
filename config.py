﻿class DefaultConfigs(object):
    
    # 复制文件的后缀名
    last = ['pptx', '.ppt', '.doc', 'docx', '.pdf', '.txt']
    """ last = [
    'pptx', 'html', '.ppt', '.vbs', '.mp4', '.caj', '.xml', '.m4a', '.wav', '.avi',
    '.WAV', '.AVI', '.MP4', '.exe', '.mp3', '.MP3', '.bat', '.png', '.PNG', '.gif',
    '.GIF', 'jpeg', 'JPEG', '.jpg', '.JPG', '.doc', 'docx', '.pdf', 'xlsx'] """
    
    # 目标位置
    path = ['F:\\', 'G:\\']
    
    # 复制位置
    save = 'D:\\EdData\\'
    
    # 是否需要文件夹
    fold = False
    
    # 复制前延时或定时复制
    de_t = {
        "Chinese":   [(1, 10, 10, 0), (2, 13, 30, 0), (3, 14, 20, 0), (4,  8, 20, 0), (5, 11,  0, 0)],
        "Biology":   [(1, 13, 30, 0), (3,  9, 10, 0)],
        "Chemistry": [(1, 15, 10, 0), (3, 16, 10, 0)]
    }
    '''
    {
        'Mathematics': [(1,  8, 20, 0), (2,  9, 10, 0), (3, 11,  0, 0), (3, 11, 50, 0), (4, 14, 20, 0), (5, 13, 30, 0)],
        'Chinese':     [(1, 10, 10, 0), (2, 13, 30, 0), (3, 14, 20, 0), (4,  8, 20, 0), (5, 11,  0, 0)],
        'English':     [(1, 11,  0, 0), (2, 14, 20, 0), (3,  8, 20, 0), (4, 13, 30, 0), (5, 10, 10, 0)],
        'Physics':     [(1, 16, 10, 0), (3, 13, 30, 0), (4, 10, 10, 0)],
        'Chemistry':   [(1, 15, 20, 0), (3, 16, 10, 0), (5, 11, 50, 0)],
        'Politics':    [(1, 14, 20, 0), (4, 11, 50, 0)],
        'History':     [(2, 10, 10, 0), (4,  9, 10, 0)],
        'Geography':   [(2,  8, 20, 0), (5,  8, 20, 0)],
        'Biology':     [(1, 13, 30, 0), (2,  9, 10, 0)]
    }
    '''

config = DefaultConfigs()