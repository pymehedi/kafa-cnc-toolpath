import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QMessageBox, QGraphicsView, QGraphicsScene, QToolBar
from PyQt6.QtGui import QAction, QIcon, QPixmap, QPainter, QColor, QKeySequence, QPen, QBrush, QFont
from PyQt6.QtCore import Qt, QPointF

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CNC Toolpath Designer")
        self.setGeometry(100, 100, 800, 600)
        # Set dummy company logo
        pixmap = QPixmap(32, 32)
        pixmap.fill(QColor("black"))
        painter = QPainter(pixmap)
        painter.setPen(QColor("black"))
        painter.drawText(10, 20, "CNC")
        painter.end()
        self.setWindowIcon(QIcon(pixmap))

        # Create menubar
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")
        new_action = QAction("New", self)
        new_action.setShortcut(QKeySequence.StandardKey.New)
        new_action.triggered.connect(lambda: print("New action triggered"))
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.triggered.connect(lambda: print("Open action triggered"))
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.setShortcut(QKeySequence.StandardKey.Save)
        save_action.triggered.connect(lambda: print("Save action triggered"))
        file_menu.addAction(save_action)

        save_as_action = QAction("Save As", self)
        save_as_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        save_as_action.triggered.connect(lambda: print("Save As action triggered"))
        file_menu.addAction(save_as_action)

        export_dxf_action = QAction("Export to DXF", self)
        export_dxf_action.setShortcut(QKeySequence("Ctrl+E"))
        export_dxf_action.triggered.connect(lambda: print("Export to DXF action triggered"))
        file_menu.addAction(export_dxf_action)

        file_menu.addSeparator()

        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        copy_action = QAction("Copy", self)
        copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        copy_action.triggered.connect(lambda: print("Copy action triggered"))
        edit_menu.addAction(copy_action)

        paste_action = QAction("Paste", self)
        paste_action.setShortcut(QKeySequence.StandardKey.Paste)
        paste_action.triggered.connect(lambda: print("Paste action triggered"))
        edit_menu.addAction(paste_action)

        undo_action = QAction("Undo", self)
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        undo_action.triggered.connect(lambda: print("Undo action triggered"))
        edit_menu.addAction(undo_action)

        redo_action = QAction("Redo", self)
        redo_action.setShortcut(QKeySequence.StandardKey.Redo)
        redo_action.triggered.connect(lambda: print("Redo action triggered"))
        edit_menu.addAction(redo_action)

        delete_action = QAction("Delete", self)
        delete_action.setShortcut(QKeySequence.StandardKey.Delete)
        delete_action.triggered.connect(lambda: print("Delete action triggered"))
        edit_menu.addAction(delete_action)

        select_all_action = QAction("Select All", self)
        select_all_action.setShortcut(QKeySequence.StandardKey.SelectAll)
        select_all_action.triggered.connect(lambda: print("Select All action triggered"))
        edit_menu.addAction(select_all_action)

        # Draw menu
        draw_menu = menubar.addMenu("Draw")
        line_action = QAction("Line", self)
        line_action.setShortcut(QKeySequence("Ctrl+L"))
        line_action.triggered.connect(lambda: print("Line action triggered"))
        draw_menu.addAction(line_action)

        arc_action = QAction("Arc", self)
        arc_action.setShortcut(QKeySequence("Ctrl+R"))
        arc_action.triggered.connect(lambda: print("Arc action triggered"))
        draw_menu.addAction(arc_action)

        spline_action = QAction("Spline", self)
        spline_action.setShortcut(QKeySequence("Ctrl+P"))
        spline_action.triggered.connect(lambda: print("Spline action triggered"))
        draw_menu.addAction(spline_action)

        circle_action = QAction("Circle", self)
        circle_action.setShortcut(QKeySequence("Ctrl+I"))
        circle_action.triggered.connect(lambda: print("Circle action triggered"))
        draw_menu.addAction(circle_action)

        rectangle_action = QAction("Rectangle", self)
        rectangle_action.setShortcut(QKeySequence("Ctrl+Shift+T"))
        rectangle_action.triggered.connect(lambda: print("Rectangle action triggered"))
        draw_menu.addAction(rectangle_action)

        polyline_action = QAction("Polyline", self)
        polyline_action.setShortcut(QKeySequence("Ctrl+Shift+Y"))
        polyline_action.triggered.connect(lambda: print("Polyline action triggered"))
        draw_menu.addAction(polyline_action)

        # Edit Curves menu
        edit_curves_menu = menubar.addMenu("Edit Curves")
        trim_action = QAction("Trim", self)
        trim_action.setShortcut(QKeySequence("Ctrl+T"))
        trim_action.triggered.connect(lambda: print("Trim action triggered"))
        edit_curves_menu.addAction(trim_action)

        join_action = QAction("Join", self)
        join_action.setShortcut(QKeySequence("Ctrl+J"))
        join_action.triggered.connect(lambda: print("Join action triggered"))
        edit_curves_menu.addAction(join_action)

        # Transform menu
        transform_menu = menubar.addMenu("Transform")
        scale_action = QAction("Scale", self)
        scale_action.setShortcut(QKeySequence("Ctrl+Alt+S"))
        scale_action.triggered.connect(lambda: print("Scale action triggered"))
        transform_menu.addAction(scale_action)

        move_action = QAction("Move", self)
        move_action.setShortcut(QKeySequence("Ctrl+M"))
        move_action.triggered.connect(lambda: print("Move action triggered"))
        transform_menu.addAction(move_action)

        rotate_action = QAction("Rotate", self)
        rotate_action.setShortcut(QKeySequence("Ctrl+Shift+R"))
        rotate_action.triggered.connect(lambda: print("Rotate action triggered"))
        transform_menu.addAction(rotate_action)

        mirror_action = QAction("Mirror", self)
        mirror_action.setShortcut(QKeySequence("Ctrl+Shift+M"))
        mirror_action.triggered.connect(lambda: print("Mirror action triggered"))
        transform_menu.addAction(mirror_action)

        move_to_ucs_origin_action = QAction("Move to UCS-Origin", self)
        move_to_ucs_origin_action.setShortcut(QKeySequence("Ctrl+Shift+O"))
        move_to_ucs_origin_action.triggered.connect(lambda: print("Move to UCS-Origin action triggered"))
        transform_menu.addAction(move_to_ucs_origin_action)

        # Help menu
        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.setShortcut(QKeySequence.StandardKey.HelpContents)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        # Create separate toolbars for each menu
        # File toolbar
        file_toolbar = self.addToolBar("File")
        file_toolbar.addAction(new_action)
        file_toolbar.addAction(open_action)
        file_toolbar.addAction(save_action)
        file_toolbar.addAction(save_as_action)
        file_toolbar.addAction(export_dxf_action)
        file_toolbar.addSeparator()
        file_toolbar.addAction(exit_action)

        # Edit toolbar
        edit_toolbar = self.addToolBar("Edit")
        edit_toolbar.addAction(copy_action)
        edit_toolbar.addAction(paste_action)
        edit_toolbar.addAction(undo_action)
        edit_toolbar.addAction(redo_action)
        edit_toolbar.addAction(delete_action)
        edit_toolbar.addAction(select_all_action)

        # Draw toolbar
        draw_toolbar = self.addToolBar("Draw")
        draw_toolbar.addAction(line_action)
        draw_toolbar.addAction(arc_action)
        draw_toolbar.addAction(spline_action)
        draw_toolbar.addAction(circle_action)
        draw_toolbar.addAction(rectangle_action)
        draw_toolbar.addAction(polyline_action)

        # Edit Curves toolbar
        edit_curves_toolbar = self.addToolBar("Edit Curves")
        edit_curves_toolbar.addAction(trim_action)
        edit_curves_toolbar.addAction(join_action)

        # Transform toolbar
        transform_toolbar = self.addToolBar("Transform")
        transform_toolbar.addAction(scale_action)
        transform_toolbar.addAction(move_action)
        transform_toolbar.addAction(rotate_action)
        transform_toolbar.addAction(mirror_action)
        transform_toolbar.addAction(move_to_ucs_origin_action)

        # Set up the graphics view
        self.scene = QGraphicsScene(self)
        self.view = GraphicsView(self.scene)
        self.setCentralWidget(self.view)

        # Draw the 2D plane
        self.draw_plane()

    def draw_plane(self):
        # Clear the scene
        self.scene.clear()

        # Set scene rect to a large area, say -1000 to 1000 mm
        self.scene.setSceneRect(-10000, -10000, 20000, 20000)

        # Pen for axes
        axis_pen = QPen(QColor("gray"),1)
        

        # Draw main axes
        self.scene.addLine(-1000, 0, 1000, 0, axis_pen)  # X axis
        self.scene.addLine(0, -1000, 0, 1000, axis_pen)  # Y axis





    def show_about(self):
        QMessageBox.about(self, "About CNC Toolpath Designer", "Company: CNC CAD\nVersion: 1.0\nThis is a dummy description for the CNC Toolpath Designer application.")


class GraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def wheelEvent(self, event):
        zoom_in_factor = 1.15
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor

        self.scale(zoom_factor, zoom_factor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
