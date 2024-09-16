import nuke
from PySide2 import QtWidgets

class ChannelListWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Channel List")
        self.setGeometry(100, 100, 300, 200)

        # Create the layout
        self.layout = QtWidgets.QVBoxLayout()

        # channels list
        self.list_widget = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_widget)

        #  Button to create Shuffle nodes
        self.button_ok = QtWidgets.QPushButton("Create Shuffles")
        self.button_ok.clicked.connect(self.create_shuffles)
        self.layout.addWidget(self.button_ok)

        self.setLayout(self.layout)
        # Start the list from the beginning
        self.populate_channels()

    def populate_channels(self):
        self.list_widget.clear()

        selected_nodes = nuke.selectedNodes()
        # Possible error of not selecting a node
        if not selected_nodes:
            self.list_widget.addItem("No nodes selected.")
            return
        # Keep the general name of the node
        node = selected_nodes[0]
        channels = node.channels()
        base_channels = {ch.split(".")[0] for ch in channels}

        # Add list to widget and enable multiple selection
        self.list_widget.addItems(sorted(base_channels))
        self.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

    # Create Shuffle nodes
    def create_shuffles(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            nuke.message("No channels selected.")
            return

        # Scroll through the selected channels
        selected_channels = [item.text() for item in selected_items]
        selected_nodes = nuke.selectedNodes()
        if not selected_nodes:
            nuke.message("No nodes selected.")
            return

        # Create Shuffle nodes
        for source_node in selected_nodes:
            for channel in selected_channels:
                shuffle_node = nuke.createNode("Shuffle")
                shuffle_node.setInput(0, source_node)
                shuffle_node['in'].setValue(channel)
                shuffle_node['label'].setValue(f"Shuffle for {channel}")

        nuke.message("Shuffles created for selected channels.")



