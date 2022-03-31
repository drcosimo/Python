import asyncio
import random as rd

tags = ["a123-ab33-c564","aaaa-1111-bbbb","3333-dddd-2222"]


async def handleClient(reader:asyncio.StreamReader, writer: asyncio.StreamWriter):
    try:
        while True:
            # wait random time
            await asyncio.sleep(rd.randint(0,10))
            # send random data
            data = tags[rd.randint(0,len(tags)-1)].encode("utf-8")
            # try to write through the buffer
            writer.write(data)
            # wait for appropriate moment to write
            await writer.drain()
    except KeyboardInterrupt:
        # handle closing of connection
        writer.write_eof()
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        print("connection closed")
    except ConnectionResetError:
       print("client disconnected")

async def main():
    # create server
    server = await asyncio.start_server(handleClient,"127.0.0.1",10003)
    # serve indefinetely
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())