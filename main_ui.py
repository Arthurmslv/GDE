from PyQt5.QtWidgets import *

class MainUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Gestor de Estudos"
        )

        self.resize(
            850,
            500
        )

        central = QWidget()

        self.setCentralWidget(
            central
        )

        layout = QVBoxLayout()

        topLayout = QHBoxLayout()

        self.btnNova = QPushButton(
            "Nova Tarefa"
        )

        self.btnEditar = QPushButton(
            "Editar"
        )

        self.btnExcluir = QPushButton(
            "Excluir"
        )

        self.btnConcluir = QPushButton(
            "Concluir"
        )

        self.buscar = QLineEdit()

        self.buscar.setPlaceholderText(
            "Buscar tarefa..."
        )

        topLayout.addWidget(
            self.btnNova
        )

        topLayout.addWidget(
            self.btnEditar
        )

        topLayout.addWidget(
            self.btnExcluir
        )

        topLayout.addWidget(
            self.btnConcluir
        )

        topLayout.addStretch()

        topLayout.addWidget(
            self.buscar
        )

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(
            5
        )

        self.tabela.setHorizontalHeaderLabels([
            "Título",
            "Disciplina",
            "Data",
            "Prioridade",
            "Status"
        ])

        self.tabela.horizontalHeader().setStretchLastSection(
            True
        )

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.tabela.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.tabela.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.tabela.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        bottomLayout = QHBoxLayout()

        self.lblTotal = QLabel(
            "Total: 0"
        )

        self.lblPendentes = QLabel(
            "Pendentes: 0"
        )

        self.lblConcluidas = QLabel(
            "Concluídas: 0"
        )

        bottomLayout.addWidget(
            self.lblTotal
        )

        bottomLayout.addSpacing(
            30
        )

        bottomLayout.addWidget(
            self.lblPendentes
        )

        bottomLayout.addSpacing(
            30
        )

        bottomLayout.addWidget(
            self.lblConcluidas
        )

        layout.addLayout(
            topLayout
        )

        layout.addWidget(
            self.tabela
        )

        layout.addLayout(
            bottomLayout
        )

        central.setLayout(
            layout
        )