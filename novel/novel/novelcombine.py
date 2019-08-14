
import os
if __name__ == "__main__":

    print("start...")
    path = "G:/novel/"

    for p,d,fs in os.walk(path):
       # print(p)
        # 创建书籍
        for f in fs:
            print(os.path.join(p,f).split("\\")[-1])
        with open("G:/小说/"+p.split("/")[2]+".txt",mode="a",encoding="utf-8") as book:
            try:
                for f in fs:
                    with open(os.path.join(p,f),mode="r",encoding="utf-8") as tm:
                        book.writelines(os.path.join(p,f).split("\\")[-1].replace(".txt", "")+"\n")
                        book.write(tm.read())
                    print(f+" ok")
            except:
                print("nopop!!")
                        


        # for f in fs:
        #     try:
        #         if not os.path.exists(path+os.path.join(p,f).split("/")[2].split("\\")[0]+".txt"):
        #                 with open(path+ os.path.join(p,f).split("/")[2].split("\\")[0] +".txt",mode='a+',encoding="utf-8") as tf:
        #                      with open(os.path.join(p,f),mode='r',encoding="utf-8") as t1:
        #                         tf.write(t1.read())               
        #         print(f+"写入ok！！！")
        #     except:
        #         print("nooo")