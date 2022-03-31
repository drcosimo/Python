import asyncio
import reactivex

from classes import deviceType,transit_analyzer,clientHandler

# the wrapper of the on_subscription function
def wrapper(queue:asyncio.Queue):
    # the on_subscription function gets the data from the queue 
    # and passes it to the on_next method of the observer 
    def on_subscription(observer:transit_analyzer,scheduler):
        # async function that asynchronously gets data from the queue
        async def getData():
            try:
                while True:
                    # wait for an event
                    event = await queue.get()
                    # hands the event to the observer
                    observer.on_next(event)
            except Exception as e:
                # error handling
                observer.on_error(e)
                
        # create task for running the async function
        asyncio.create_task(getData())
    # return the observable
    return reactivex.create(on_subscription)

async def tcp_connection(d:deviceType,q:asyncio.Queue):
    # create clientHandler object
    ctx = clientHandler(q,d)
    # open connection
    # i am client
    if(d == 3):
        # open connection
        reader,writer = await asyncio.open_connection("127.0.0.1",10000 + d)
        # function that read data from the device and enqueues it
        await ctx.handleClient(reader,writer)
    # i am server
    else:
        # start server, the client_callback is encapsulated in a class to carry the queue and device type
        server = await asyncio.start_server(ctx.handleClient,"127.0.0.1", 10000 + d)
        await server.serve_forever()



async def main():
    # define one queue for each device
    queue = asyncio.Queue()
    # create tasks for tcp connections
    [asyncio.create_task(tcp_connection(i+1,queue)) for i in range(3)]
    # create observable that gets data from queue
    obs= wrapper(queue)
    # define the subscriber
    trans_anal = transit_analyzer()
    # subscribe to the observable
    obs.subscribe(trans_anal)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(main())
    loop.run_forever()