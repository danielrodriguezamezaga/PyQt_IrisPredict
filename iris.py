# Exercise of: Daniel Rodriguez Amezaga
from PyQt5.QtWidgets import *
import pickle
import sys

# Import model already trained with jupyter NoteBook
model = pickle.load(open('savemodel.sav', 'rb'))

def predict():
    print("Sepal Length: ", float(sepal_length_edit.text()))
    print("Sepal Width: ", float(sepal_width_edit.text()))
    print("Petal Length: ", float(petal_length_edit.text()))
    print("Petal Width: ", float(petal_width_edit.text()))
    result = model.predict([[float(sepal_length_edit.text()), 
                             float(sepal_width_edit.text()), 
                             float(petal_length_edit.text()), 
                             float(petal_width_edit.text())]])[0]
    print(result)
    
def funcion_salir():
    ventana.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = QMainWindow()
    ventana.setGeometry(800, 100, 500, 500)

    ventana.setWindowTitle("Iris - Prediction")
    label_1 = QLabel(ventana)
    label_1.setText("Complete the fields to predict the flower")
    label_1.adjustSize()
    label_1.move(100, 20)

    sepal_length = QLabel(ventana)
    sepal_length.setText("Sepal Length: ")
    sepal_length.adjustSize()
    sepal_length.move(100, 100)
    
    sepal_width = QLabel(ventana)
    sepal_width.setText("Sepal Width: ")
    sepal_width.adjustSize()
    sepal_width.move(100, 150)
    
    petal_length = QLabel(ventana)
    petal_length.setText("Petal Length: ")
    petal_length.adjustSize()
    petal_length.move(100, 200)
    
    petal_width = QLabel(ventana)
    petal_width.setText("Petal Width: ")
    petal_width.adjustSize()
    petal_width.move(100, 250)
    
    boton_1 = QPushButton(ventana)
    boton_1.setText("Predict with CMD")
    boton_1.clicked.connect(predict)
    boton_1.adjustSize()
    boton_1.move(150, 300)

    boton_2 = QPushButton(ventana)
    boton_2.setText("Exit")
    boton_2.clicked.connect(funcion_salir)
    boton_2.move(390, 450)

    sepal_length_edit = QLineEdit(ventana)
    sepal_length_edit.move(200, 100)
    
    sepal_width_edit = QLineEdit(ventana)
    sepal_width_edit.move(200, 150)
    
    petal_length_edit = QLineEdit(ventana)
    petal_length_edit.move(200, 200)
    
    petal_width_edit = QLineEdit(ventana)
    petal_width_edit.move(200, 250)
    
    estilos = """QPushButton {
        background-color: grey;
        color: black;
        border-width: 2px;
        border-style: solid;
        border-radius: 5;
        padding: 2px;
    }
    """
    
    QApplication.instance().setStyleSheet(estilos)

    ventana.show()
    sys.exit(app.exec_())
