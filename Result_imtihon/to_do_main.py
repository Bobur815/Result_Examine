from moduls import * 

class MainWindow (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To Do list")
        self.setFixedSize(1000,600)
        self.setFont(QFont("Times",12))

        self.info = QMessageBox(self)

        self.add_btn = QPushButton("Add task",self)
        self.del_btn = QPushButton("Delete",self)
        self.update_btn = QPushButton("Update",self)


        main_layout = QVBoxLayout()
        vert_layout = QHBoxLayout()

        vert_layout.addWidget(self.add_btn)
        vert_layout.addWidget(self.del_btn)
        vert_layout.addWidget(self.update_btn)

        self.table_widget = QTableWidget(self)
        self.table_widget.setSelectionBehavior(True)

        main_layout.addLayout(vert_layout)
        main_layout.addWidget(self.table_widget)

        self.setLayout(main_layout)
        self.load_data()

        self.del_btn.clicked.connect(self.delete_item)
        self.add_btn.clicked.connect(self.add_page)
        self.update_btn.clicked.connect(self.update_page)

    def update_page(self):
        from update import UpdateWindow
        target = self.table_widget.selectedItems()

        if not target:
            return self.info.information(self,"Selection error","Item not selected")
        
        self.update_oyna = UpdateWindow(self,target)

        self.update_oyna.show()

    def add_page(self):
        from add_page import AddWindow

        self.add_oyna = AddWindow(self)
        self.add_oyna.show()

    def load_data(self):
        self.table_widget.clear()

        conn = get_cursor()

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks;")
            tasks = cursor.fetchall()
            conn.commit()

            self.table_widget.setRowCount(len(tasks))
            self.table_widget.setColumnCount(7)
            self.table_widget.setHorizontalHeaderLabels(["Id","Title","Description","Deadline","Time","Completed","Assigned to"])
            self.table_widget.horizontalHeader().setStretchLastSection(True)

            self.table_widget.setColumnWidth(0,10)
            self.table_widget.setColumnWidth(1,100)
            self.table_widget.setColumnWidth(2,300)
            self.table_widget.setColumnWidth(3,130)
            self.table_widget.setColumnWidth(4,90)
            self.table_widget.setColumnWidth(5,120)

            for row, data in enumerate(tasks):
                for column, item in enumerate(data):
                    self.table_widget.setItem(row,column,QTableWidgetItem(str(item)))
        

    def delete_item(self):
        selected_row = self.table_widget.selectedItems()
        if not selected_row:
            return self.info.information(self,"Selection error","Item not selected")

        task_id = selected_row[0].text()

        
        
        conn = get_cursor()

        conn.autocommit = True

        
        with conn.cursor() as cursor:
             cursor.execute("DELETE FROM tasks WHERE id = %s;",(task_id,))
             conn.commit()

             self.load_data()

             self.info.information(self,"Deletion","Item deleted")
        
        




if __name__ == "__main__":

    app = QApplication([])

    oyna = MainWindow()
    oyna.show()

    sys.exit(app.exec_())