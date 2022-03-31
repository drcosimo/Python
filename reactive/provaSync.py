import reactivex


def on_subscribe(observer,scheduler):
    for i in range(100):
        observer.on_next(i)


obs = reactivex.create(on_subscribe)
obs.subscribe(on_next=lambda i : print("values:{0}".format(i)))