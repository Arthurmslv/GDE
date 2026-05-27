from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class TaskUI(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Nova Tarefa"
        )

        self.resize(
            400,
            350
        )

        layout = QVBoxLayout()

        self.titulo = QLineEdit()

        self.titulo.setPlaceholderText(
            "Título da tarefa"
        )

        self.disciplina = QLineEdit()

        self.disciplina.setPlaceholderText(
            "Disciplina"
        )

        self.prioridade = QComboBox()

        self.prioridade.addItems([
            "Baixa",
            "Média",
            "Alta"
        ])

        self.data = QDateEdit()

        self.data.setCalendarPopup(
            True
        )

        self.data.setDate(
            QDate.currentDate()
        )

        self.descricao = QTextEdit()

        self.descricao.setPlaceholderText(
            "Descrição..."
        )

        self.salvar = QPushButton(
            "Salvar"
        )

        layout.addWidget(
            QLabel("Título")
        )

        layout.addWidget(
            self.titulo
        )

        layout.addWidget(
            QLabel("Disciplina")
        )

        layout.addWidget(
            self.disciplina
        )

        layout.addWidget(
            QLabel("Prioridade")
        )

        layout.addWidget(
            self.prioridade
        )

        layout.addWidget(
            QLabel("Data")
        )

        layout.addWidget(
            self.data
        )

        layout.addWidget(
            QLabel("Descrição")
        )

        layout.addWidget(
            self.descricao
        )

        layout.addWidget(
            self.salvar
        )

        self.setLayout(
            layout
        )