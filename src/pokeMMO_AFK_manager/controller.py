from ImgProcessingModel import ImgProcessingModel
from ScreenCaptureModel import ScreenCaptureModel
from config import get_template_path, get_public_path


class AppController:
    def __init__(self, view):
        self.view = view
        self.scmodel = ScreenCaptureModel()
        self.cv2model = ImgProcessingModel()
        
        self.view.btn_accion.configure(command=self.ejecutar_matching)
        
    def ejecutar_matching(self):
        screenshot = self.scmodel.capturar()
        rutaTemplate = get_template_path("held_item.png")
        rutaImg = get_public_path("pokemmo.png")
        self.cv2model.find_template_from_img(rutaImg, rutaTemplate)
        #rutaTemplate = get_template_path("template_ejemplo.png")
        #self.cv2model.find_template(screenshot, rutaTemplate)