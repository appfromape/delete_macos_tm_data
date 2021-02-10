import os

datas = []

if len(os.popen("tmutil listlocalsnapshotdates").read().split("\n")) == 2:
    print("Your system is clean!")

else:

    data = os.popen("tmutil listlocalsnapshotdates").read().split("\n")

    for d in data:
        datas.append(d)

    del datas[0]
    del datas[-1]

    for n in range(len(datas)):
        os.system(f'tmutil deletelocalsnapshots { datas[n] }')