import asyncio
import reactivex


# the on_subscription function assigns to the observer the values that
# will compose the observable.
# the function defines how these values are emitted from the Observable to the observers
def on_subscription(observer,scheduler):
    # the async function that generates the events
    async def genValues():
        try:
            for i in range(100):
                await asyncio.sleep(1)
                # we pass the values we want to emit to the on_next method of the observer
                observer.on_next(i)
            observer.on_completed()
        except Exception :
            observer.on_error(Exception)
    # create and run task based on coroutine genValues, in this way the on_subscription method executes async code
    asyncio.run(genValues())

if __name__ == "__main__":
    # the on_subscription method defines how the events are emitted to the subscriber.
    # The emission logic is encapsulated in an Observable that will emit the events specified in the creation method
    # when an observer subscribes to it
    obs = reactivex.create(on_subscription)
    # the on_next method then will do something with the emitted values based on 
    # how we define the behaviour of on_next
    obs.subscribe(on_next=lambda i : print("value:{0}".format(i)), on_completed=lambda : print("completed"), on_error= lambda e : print("error:{0}".format(e)))

