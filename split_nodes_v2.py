import nuke
from PySide2 import QtWidgets

class ChannelListWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Channel List")
        self.setGeometry(100, 100, 300, 200)

        # Crear el layout
        self.layout = QtWidgets.QVBoxLayout()

        # Lista de canales
        self.list_widget = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_widget)

        # Botón para crear nodos Shuffle
        self.button_ok = QtWidgets.QPushButton("Create Shuffles")
        self.button_ok.clicked.connect(self.create_shuffles)
        self.layout.addWidget(self.button_ok)

        self.setLayout(self.layout)
        # Iniciar la lista desde el principio
        self.populate_channels()

    def populate_channels(self):
        self.list_widget.clear()

        selected_nodes = nuke.selectedNodes()
        # Posible error de no seleccionar un nodo
        if not selected_nodes:
            self.list_widget.addItem("No nodes selected.")
            return
        # Quedarme con el nombre general del nodo
        node = selected_nodes[0]
        channels = node.channels()
        base_channels = {ch.split(".")[0] for ch in channels}

        # Añadir la lista al widget y habilitar selección múltiple
        self.list_widget.addItems(sorted(base_channels))
        self.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

    # Crear nodos Shuffle
    def create_shuffles(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            nuke.message("No channels selected.")
            return

        # Recorrer los canales seleccionados
        selected_channels = [item.text() for item in selected_items]
        selected_nodes = nuke.selectedNodes()
        if not selected_nodes:
            nuke.message("No nodes selected.")
            return

        # Crear nodos Shuffle
        for source_node in selected_nodes:
            for channel in selected_channels:
                shuffle_node = nuke.createNode("Shuffle")
                shuffle_node.setInput(0, source_node)
                shuffle_node['in'].setValue(channel)
                shuffle_node['label'].setValue(f"Shuffle for {channel}")

        nuke.message("Shuffles created for selected channels.")


