import multiprocessing

def out_put(k):
    print(k)
    print("This is outside the multi")
    
# out_put()

if __name__=="__main__":
    t = multiprocessing.Process(target=out_put, args=(50, ))
    t.start()
    t.join()
    print("Done processing!!!")