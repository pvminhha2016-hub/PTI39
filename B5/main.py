class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

class HomeworkList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_finished(self):
        self.__finished = True

        for item in self.items:
            if item.completed == False:
                print(item.name)
                self.__finished = False

        if self.__finished:
            print("All finished")


homework_list = HomeworkList()

homework_list.add_item(Homework("Lập trình App Producer", 3, False))
homework_list.add_item(Homework("Làm văn", 2, True))
homework_list.add_item(Homework("Lập trình Gamemaker", 1, False))

homework_list.all_finished()