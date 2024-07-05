from queue import Queue

queue = Queue()

class Ticket():
    def __init__(self, name:str, text:str):
        self.__name = name
        self.__text = text
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def text(self) -> str:
        return self.__text
    
    def solve(self):
        print(f"Заявка {self.__name} оброблена")

def generate_request():
    name = input("Введіть ім'я заявки: ")
    text = input("Введіть текст заявки: ")
    ticket = Ticket(name, text)
    queue.put(ticket)

def process_request():
    if not queue.empty():
        ticket = queue.get()
        ticket.solve()
    else:
        print("Немає невиконаних заявок")

def main():
    while True:
        generate_request()
        process_request()

main()
