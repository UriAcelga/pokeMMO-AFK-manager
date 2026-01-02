from ImgProcessingModel import ImgProcessingModel
from ScreenCaptureModel import ScreenCaptureModel
from WindowModel import WindowModel
from config import get_template_path, get_public_path


class AppController:
    def __init__(self, view):
        self.view = view
        self.scmodel = ScreenCaptureModel()
        self.cv2model = ImgProcessingModel()
        self.windowmodel = WindowModel()

        self.targetWindow = "PokeMMO"
        self.coords = None #Coordenadas de la ventana del juego
        
        self.view.btn_accion.configure(command=self.ejecutar_matching)
        self.view.btn_window.configure(command=self.activar_ventana)

        
    def ejecutar_matching(self):
        screenshot = self.scmodel.capturar(self.coords)
        rutaTemplate = get_template_path("held_item.png")
        self.cv2model.find_template(screenshot, rutaTemplate)

    def activar_ventana(self):
        """
        Activa y pone foco en la ventana. Se registran las coordenadas de la misma.
        
        Returns:
            {"left": x, "top": y, "width": a, "height": b}
        """
        self.windowmodel.print_window_list()
        try:
            self.coords = self.windowmodel.enfocar_ventana(self.targetWindow)
        except ValueError:
            self.view.window_not_found_popup(self.targetWindow)