# -*- coding: UTF-8 -*-

import time, datetime
import copy, os
from config import config

# 设置默认值
last  = ['pptx', '.ppt', '.doc', 'docx', '.pdf', '.txt']
pathx = ['F:\\', 'G:\\']
savex = 'D:\\EdData\\'
fold  = False
de_t  = 600

# 从config.py中导入设置
try: pathx = config.path
except: pass
try: last  = config.last
except: pass
try: savex = config.save
except: pass
try: fold  = config.fold
except: pass
try: de_t  = config.de_t
except: pass

global ddtp, if_conti
ddt   = 0
ddtp  = ""
ddtt  = 0

if_conti = True

def Traceback(s):
    print(s)
    logger = open('./console.log', 'a')
    logger.write(s + "\n")
    logger.close()

def Traceback_WARNING(t, s):
    if t[0] == "e":
        if t[1] == "w":
            if t[2] == "f":
                Traceback("WARNING from function " + s + " :")
        elif t[1] == "i":
            Traceback("  INFO: " + s)
    elif t[0] == "c":
        if t[1] == "w":
            if t[2] == "f":
                Traceback("来自函数 " + s + " 的警告:")
        elif t[1] == "i":
            Traceback("  信息: " + s)
    elif t[0] == "b":
        Traceback("    " + s)
    else:
        Traceback(s)

def calc_delta_t(tup):
    dans = 0
    try:
        dweek   = tup[0] - datetime.datetime.today().isoweekday()
        dhour   = tup[1] - datetime.datetime.today().hour
        dminute = tup[2] - datetime.datetime.today().minute
        dsecond = tup[3] - datetime.datetime.today().second
        dans = ((dweek * 24 + dhour) * 60 + dminute) * 60 + dsecond
        if dans < 0:
            dans += 7 * 24 * 60 * 60
    except:   # 参数错误
        dans = 7 * 24 * 60 * 60
    return dans

def calc_delta_t_everyd(tup):
    dans = 0
    try:
        dhour   = tup[0] - datetime.datetime.today().hour
        dminute = tup[1] - datetime.datetime.today().minute
        dsecond = tup[2] - datetime.datetime.today().second
        dans = (dhour * 60 + dminute) * 60 + dsecond
        if dans < 0:
            dans += 24 * 60 * 60
        if dans >= 24 * 60 * 60:
            dans -= 24 * 60 * 60
    except:   # 参数错误
        dans = 24 * 60 * 60
    return dans

def calc_delay_str(s):
    try:
        tupx = (int(s[0] + s[1]), int(s[3] + s[4]), int(s[6] + s[7]))
    except:
        Traceback_WARNING("ewff", "calc_delay_str():")
        Traceback_WARNING("b",    "String index out of range with string: \"" + str(s) + "\"")
        Traceback_WARNING("ei",   "This string format is not allowed")
        Traceback_WARNING("cwff", "calc_delay_str():")
        Traceback_WARNING("b",    "字符串长度过短，字符串数据为: \"" + str(s) + "\"")
        Traceback_WARNING("ci",   "该格式的字符串是无法识别的")
        return 24 * 60 * 60
    return calc_delta_t_everyd(tupx)

def Traceback_WARNING_tuple(tup, t, s):
    if t == 'e':
        Traceback_WARNING("ewff", "calc_delay_tuple():")
        Traceback_WARNING("b",    "Unsupported PARAMETER TYPE in a tuple with data: " + str(tup))
        Traceback_WARNING("ei",   s)
    elif t == 'c':
        Traceback_WARNING("cwff", "calc_delay_tuple():")
        Traceback_WARNING("b",    "元组中含有不支持格式的数据，元组数据为: " + str(tup))
        Traceback_WARNING("ci",   s)

def calc_delay_tuple(tup):
    if len(tup) == 1:
        if type(tup[0]) == int:
            return tup[0]
        elif type(tup[0]) == str:
            return calc_delay_str(tup[0])
        else:
            Traceback_WARNING_tuple(tup, "e", "if len(tuple) == 1, then the only parameter's type should be int or str")
            Traceback_WARNING_tuple(tup, "c", "当元组元素数量为1时，元素应为 int 类型 或 str 类型")
            return 24 * 60 * 60
    elif len(tup) == 2:
        if type(tup[1]) == str:
            s = tup[1]
            return calc_delta_t(calc_delay_str(s))
        else:
            Traceback_WARNING_tuple(tup, "e", "if len(tuple) == 2, then the first parameter's type should be int\nand the second one should be str")
            Traceback_WARNING_tuple(tup, "c", "当元组元素数量为2时，第一项元素应为 int 类型，第二项元素应为 str 类型")
            return 24 * 60 * 60
    elif len(tup) == 3:
        return calc_delta_t_everyd(tup)
    elif len(tup) == 4:
        return calc_delta_t(tup)
    else:
        Traceback_WARNING_tuple(tup, "c", "元组参数不能少于1个多于4个")
        return 24 * 60 * 60

def calc_delay_list(lis):
    tans = []
    mint = 7 * 24 * 60 * 60
    if len(lis) == 1:
        return calc_delay_str(lis[0])
    else:
        for l in lis:
            dt = calc_delay_tuple(l)
            if dt < mint:
                mint = dt
        return mint

def calc_delay_dict(dic):
    tans = []
    mint = 7 * 24 * 60 * 60
    for k, v in list(dic.items()):
        if type(v) == tuple:
            dt = calc_delta_t(v)
            if dt < mint:
                mint = dt
                tans = [k, dt]
        elif type(v) == list:
            for l in v:
                dt = calc_delay_tuple(l)
                if dt < mint:
                    mint = dt
                    tans = [k + "\\", dt]
    return tans

def calc_delay(obj):
    global ddtp
    if type(obj) == int:
        return ["", obj]
    elif type(obj) == str:
        return ["", calc_delay_str(obj)]
    elif type(obj) == tuple:
        return ["", calc_delay_tuple(obj)]
    elif type(obj) == list:
        return ["", calc_delay_list(obj)]
    elif type(obj) == dict:
        return calc_delay_dict(obj)

global other, fail, altogether
other = []
fail = 0
altogether = 0

def dect_root(dirs, root):
    for r in root:
        if dirs[-len(r):] == r:
            return True
    return False

def copy_file(dir_path, root, save_path):
    global other, fail, altogether
    dir_list = []
    dir_st = []
    try:
        os.makedirs(save_path)
    except OSError as e:
        pass
    try:
        for dirs in os.listdir(dir_path):
            if dect_root(dirs, root):
                print(dirs)
                result = os.system('copy "' + str(dir_path) + str(dirs) + '" "' + str(save_path) + '" /Y')
                os.system("cls")
                fail = fail + int(result)
                altogether += 1
            elif not('.' in dirs) and dirs[:1] != '.':
                dir_list.append(str(dir_path) + str(dirs) + '\\')
                dir_st.append(str(dirs) + '\\')
            else:
                other.append(str(dirs))
    except:
        pass
    return dir_list, dir_st

while if_conti:
    
    ddt  = calc_delay(de_t)
    save = savex + ddt[0]
    time.sleep(ddt[1])

    for path in pathx:
        try:
            ret, rl = copy_file(path, last, save)
            while ret != []:
                n_ret = []
                n_rl = []
                for ret_dir, ret_name in zip(ret, rl):
                    if fold:
                        o_ret, o_rl = copy_file(ret_dir, last, save + ret_name)
                    else:
                        o_ret, o_rl = copy_file(ret_dir, last, save)
                    for t, l in zip(o_ret, o_rl):
                        n_ret.append(t)
                        n_rl.append(l)
                ret = n_ret
                rl = n_rl
                print(n_ret,n_rl)
        except:
            pass

    logger = open('./console.log', 'a')
    logger.write('\nfail:' + str(fail) + ', success:' + str(int(altogether) - int(fail)) + '\n')
    times = 0

    for k in other:
        logger.write(str(k) + ',')
        if  times == 10:
            logger.write('\n')
            times = 0
        times += 1
    logger.close()

    if type(de_t) == int:
        if_conti = False

    # 伪装cmd
    os.system("cls")
    print("Microsoft Windows [版本 10.0.17763.2114]\n(c) 2018 Microsoft Corporation。保留所有权利。")
