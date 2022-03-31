import asyncio


key = "abcdef"

async def handleClient(reader:asyncio.StreamReader,writer:asyncio.StreamWriter):
    data = await reader.read(1024)
    value = data.decode(encoding="utf-8")
    if key == value:
        writer.write("authentication succeded, gate is opening".encode("utf-8"))
        await writer.drain() 
        # when the auth client writes, it means i have to open the gate
        print("signal received, gate is opening...")
    else:
        writer.write("authentication failed".encode("utf-8"))
        await writer.drain()
        print("auth failed")
    # closing connection
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handleClient,"127.0.0.1",12000)
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())