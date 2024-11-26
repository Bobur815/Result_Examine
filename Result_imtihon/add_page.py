from moduls import *

class AddWindow(QWidget):
    def __init__(self,main_window):
        super().__init__()
        
        self.setWindowTitle("Add page")
        self.setFixedSize(700,500)

        self.main_window = main_window

        self.setFont(QFont("Times",14))

        main_layout = QVBoxLayout()

        self.info = QMessageBox(self)

        self.title = QLineEdit()
        self.description = QLineEdit()
        self.deadline = QLineEdit()
        self.time = QLineEdit()
        self.assigned_to = QLineEdit()

        self.title.setPlaceholderText("task title...")
        self.description.setPlaceholderText("task description...")
        self.deadline.setPlaceholderText("deadline (YYYY-MM-DD)")
        self.time.setPlaceholderText("time (HH:MM)")
        self.assigned_to.setPlaceholderText("assigned to (name)")

        self.add_task = QPushButton("Add task",self)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.description)
        main_layout.addWidget(self.deadline)
        main_layout.addWidget(self.time)
        main_layout.addWidget(self.assigned_to)
        main_layout.addWidget(self.add_task)

        self.setLayout(main_layout)

        self.add_task.clicked.connect(self.save_data)

    def save_data (self):

        title = self.title.text()
        description = self.description.text()
        deadline = self.deadline.text()
        time = self.time.text()
        assgined_to = self.assigned_to.text()

        if not self.check_title(title) or not self.check_description(description) or not self.check_deadline(deadline) or not self.check_time(deadline,time) or not self.check_assigned_to(assgined_to):
            return


        conn = get_cursor()

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute("""INSERT INTO tasks (title,description,deadline,time,assigned_to) 
                           VALUES (%s,%s,%s,%s,%s);""",(title,description,deadline,time,assgined_to))
            conn.commit()
            self.info.information(self,"Muvafaqiyatli","Ma'lumotlar muvaffaqiyatli saqlandi")
            self.main_window.load_data()

        self.close()

    def check_title(self,title):
        if not title:
            self.info.warning(self,"InsertionError","Title bo'sh bo'lishi mumkin emas")
            return False
        if len(title)>255:
            self.info.warning(self,"InsertionError","Title satri juda uzun")
            return False
        
        return True
    
    def check_description(self,description):
        
        if len(description)>500:
            self.info.warning(self,"InsertionError","Description satri juda uzun")
            return False
        return True
        
    def check_time(self,date,time):
        ls_date = date.split('-')

        year = int(ls_date[0])
        month = int(ls_date[1])
        day = int(ls_date[2])

        ls = time.split(':')
        
        hour = int(ls[0])
        minute = int(ls[1])

        try:
            vaqt = datetime(year,month,day,hour,minute)
        except Error as er:
            self.info.warning(self,f"{er}","Vaqt noto'g'ri formatda")
            return False
        
        if vaqt<datetime.now():
            self.info.warning(self,"Date error","Sana faqat kelajakdagi kunlarni qabul qiladi")
            return False
        
        return True
    
    def check_assigned_to(self,name:str):

        if not name:
            self.info.warning(self,"Insertion error","Assigned to maydoni bo'sh bo'lmasligi kerak")
            return False
        
        if len(name)>255:
            self.info.warning(self,"InsertionError","Ism juda uzun")
            return False
        
        for let in name:
            if let.isdigit():
                self.info.warning(self,"InsertionError","Ismda raqamlar bo'lmasligi kerak")
                return False

        return True

        


        


    def check_deadline(self,deadline):
        ls = deadline.split('-')

        year = int(ls[0])
        month = int(ls[1])
        day = int(ls[2])

        try:
            date = datetime(year=year,month=month,day=day)
             
        except Error as er:
            self.info.warning(self,f"{er}","Sana noto'g'ri formatda")
            return False
        
        if date<datetime.now():
            self.info.warning(self,"Date error","Sana faqat kelajakdagi kunlarni qabul qiladi")
            return False
        
        return True
        