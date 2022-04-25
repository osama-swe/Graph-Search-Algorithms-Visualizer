# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import main as main
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 706)
        MainWindow.setWhatsThis("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 303, 201, 30))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.run())
        self.pushButton.setGeometry(QtCore.QRect(740, 610, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.dfsButton = QtWidgets.QRadioButton(self.centralwidget)
        self.dfsButton.setGeometry(QtCore.QRect(10, 10, 95, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dfsButton.setFont(font)
        self.dfsButton.setObjectName("dfsButton")
        self.algoType = QtWidgets.QButtonGroup(MainWindow)
        self.algoType.setObjectName("algoType")
        self.algoType.addButton(self.dfsButton)
        self.bfsButton = QtWidgets.QRadioButton(self.centralwidget)
        self.bfsButton.setGeometry(QtCore.QRect(10, 50, 95, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bfsButton.setFont(font)
        self.bfsButton.setObjectName("bfsButton")
        self.algoType.addButton(self.bfsButton)
        self.depth_limitedButton = QtWidgets.QRadioButton(self.centralwidget)
        self.depth_limitedButton.setGeometry(QtCore.QRect(10, 90, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.depth_limitedButton.setFont(font)
        self.depth_limitedButton.setObjectName("depth_limitedButton")
        self.algoType.addButton(self.depth_limitedButton)
        self.iterative_deepingButton = QtWidgets.QRadioButton(self.centralwidget)
        self.iterative_deepingButton.setGeometry(QtCore.QRect(10, 130, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.iterative_deepingButton.setFont(font)
        self.iterative_deepingButton.setObjectName("iterative_deepingButton")
        self.algoType.addButton(self.iterative_deepingButton)
        self.uniform_costButton = QtWidgets.QRadioButton(self.centralwidget)
        self.uniform_costButton.setGeometry(QtCore.QRect(10, 170, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.uniform_costButton.setFont(font)
        self.uniform_costButton.setObjectName("uniform_costButton")
        self.algoType.addButton(self.uniform_costButton)
        self.greedyButton = QtWidgets.QRadioButton(self.centralwidget)
        self.greedyButton.setGeometry(QtCore.QRect(10, 210, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.greedyButton.setFont(font)
        self.greedyButton.setObjectName("greedyButton")
        self.algoType.addButton(self.greedyButton)
        self.a_starButton = QtWidgets.QRadioButton(self.centralwidget)
        self.a_starButton.setGeometry(QtCore.QRect(10, 250, 95, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.a_starButton.setFont(font)
        self.a_starButton.setObjectName("a_starButton")
        self.algoType.addButton(self.a_starButton)
        self.depth_limit_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.depth_limit_lineEdit.setGeometry(QtCore.QRect(179, 93, 113, 30))
        self.depth_limit_lineEdit.setObjectName("depth_limit_lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 352, 113, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 55, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 304, 131, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 300, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 350, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(480, 355, 131, 231))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Search Visualizer"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "enter goals separated by a space"))
        self.label.setText(_translate("MainWindow", "Goal(s)"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.dfsButton.setText(_translate("MainWindow", "DFS"))
        self.bfsButton.setText(_translate("MainWindow", "BFS"))
        self.depth_limitedButton.setText(_translate("MainWindow", "Depth Limited"))
        self.iterative_deepingButton.setText(_translate("MainWindow", "Iterative Deepening"))
        self.uniform_costButton.setText(_translate("MainWindow", "Uniform Cost"))
        self.greedyButton.setText(_translate("MainWindow", "Greedy"))
        self.a_starButton.setText(_translate("MainWindow", "A*"))
        self.depth_limit_lineEdit.setPlaceholderText(_translate("MainWindow", "enter depth limit"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "enter start node"))
        self.label_2.setText(_translate("MainWindow", "Start"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "enter nodes number"))
        self.label_3.setText(_translate("MainWindow", "Number of Nodes"))
        self.label_4.setText(_translate("MainWindow", "Edges"))
        self.textEdit.setPlaceholderText(
            _translate("MainWindow", "edge connecting nodes 1 and 2 is represented by:            1 2"))

    def run(self):

        goals = self.lineEdit.text().split()
        start = int(self.lineEdit_2.text())
        number_of_nodes = int(self.lineEdit_3.text())
        edges = self.textEdit.toPlainText().split('\n')
        formatted_edges = []
        for i in range(len(edges)):
            tuple = (int(edges[i][0]), int(edges[i][2]))
            formatted_edges.append(tuple)
        G = nx.Graph()
        G.add_nodes_from(range(1, number_of_nodes + 1))
        G.add_edges_from(formatted_edges)
        plt.figure("Graph")
        color_map = []
        for i in range(1, number_of_nodes + 1):
            if i == start:
                color_map.append('gold')
            elif str(i) in goals:
                color_map.append('lightgreen')
            else:
                color_map.append('lightgray')
        nx.draw_networkx(G, node_color=color_map, pos=graphviz_layout(G), arrows=False, with_labels=True)
        plt.show()

        if self.dfsButton.isChecked():
            main.dfs(start, goals, G)

        if self.bfsButton.isChecked():
            main.bfs(start, goals, G)

        if self.depth_limitedButton.isChecked():
            depthlimit = int(self.depth_limit_lineEdit.text())
            if depthlimit < 0:
                print("Invalid depth limit")
            else:
                main.depth_limited(start, goals, G, depthlimit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
