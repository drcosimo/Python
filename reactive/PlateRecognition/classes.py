import asyncio
from enum import Enum
import string
import sys
import reactivex

accepted_plates = ["QW123WQ","SA222SD"]
accepted_tags = ["a123-ab33-c564","aaaa-1111-bbbb"]
auth_key = "abcdef"

class deviceType(Enum):
    FRONT_CAM = 1
    REAR_CAM = 2
    RFID = 3

class evt:
    value:string
    type:deviceType

    def __init__(self,value,deviceType) -> None:
        self.value = value
        self.type = deviceType

# class observer that subscribes to the observable and analyzes the plates
class transit_analyzer(reactivex.Observer):
    # gate connection method, called when a plate/tag is accepted
    async def openGate(self):
        try:
            r,w = await asyncio.open_connection("127.0.0.1",12000)
            w.write(auth_key.encode("utf-8"))
            await w.drain()
            response = await r.read(1024)
            print(response.decode(encoding="utf-8"))

            w.close()
            await w.wait_closed()
        except Exception as e:
            print(e.with_traceback(sys.exc_info()[2]))
            
    def on_next(self,e:evt):
        # TO DO : checks if the evt value appears in the db
        print(f"got {e.value} from {e.type}")
        if e.type == deviceType.RFID.value:
            # check in tags
            if e.value in accepted_tags:
                # open gate in a cuncurrent task
                asyncio.create_task(self.openGate())
            else:
                print("plate not recognized")
        elif e.type == deviceType.FRONT_CAM.value or e.type == deviceType.REAR_CAM.value:
            # check in plates
            if e.value in accepted_plates:
                # open gate in a cuncurrent task
                asyncio.create_task(self.openGate())
            else:
                print("plate not recognized")

    def on_error(self,e:Exception):
        print(e.with_traceback(sys.exc_info()[2]))

    def on_completed(self):
        print("completed")
    
    

# wraps the handleClient method to encapsulate the queue and deviceType references
class clientHandler:
    queue:asyncio.Queue
    devType:deviceType

    def __init__(self,q:asyncio.Queue,d:deviceType):
        self.queue = q
        self.devType = d

    async def handleClient(self,reader:asyncio.StreamReader,writer:asyncio.StreamWriter):
        print(f"connected with {self.devType}")
        try:
            while True:
                # handle gracefully client disconnection
                if reader.at_eof():
                    break
                # wait for the value
                value = await reader.read(1024)
                # wrap in an event
                event = evt(value.decode(),self.devType)
                # enqueue event
                await self.queue.put(event)
                self.queue.task_done()
        except Exception as e:
            print(e.with_traceback(sys.exc_info()[2]))

        # closing connection
        writer.close()
        await writer.wait_closed()