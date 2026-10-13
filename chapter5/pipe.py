from multiprocessing.connection import Connection, Pipe
from threading import Thread, current_thread


class Writer(Thread):
    def __init__(
            self,
            conn: Connection
        ):
        super().__init__()
        self.conn = conn
        self.name = "Writer"

    def run(self) -> None:
        print(f"{current_thread().name}: Sending rubber duck...")
        self.conn.send("rubber duck")

class Reader(Thread):
    def __init__(
            self,
            conn: Connection
        ):
        super().__init__()
        self.conn = conn
        self.name = "Reader"

    def run(self) -> None:
        print(f"{current_thread().name}: Reading...")
        msg = self.conn.recv()
        print(f"{current_thread().name}: Received: {msg}")

def main() -> None:
    reader_conn, writer_conn = Pipe()

    reader = Reader(reader_conn)
    writer = Writer(writer_conn)

    threads = [
        reader,
        writer
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
