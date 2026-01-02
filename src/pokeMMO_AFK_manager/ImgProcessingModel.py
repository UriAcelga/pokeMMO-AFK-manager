import numpy as np
import cv2
from config import get_public_path


class ImgProcessingModel:
    def __init__(self):
        self.methods = [cv2.TM_CCOEFF_NORMED,
                        cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]

    def find_template(self, screenshot, template_path, threshold=0.8):
        """
        Busca una imagen de plantilla dentro de una imagen de escena usando coincidencia de patrones.

        Args:
            screenshot: Objeto Screenshot sin procesar.
            template_path: Ruta al archivo de imagen que servirá como plantilla (template).
            threshold: Nivel de confianza mínimo para considerar un acierto (0.0 a 1.0). 
                            Por defecto es 0.8.

        Returns:
            Optional[Tuple[int, int]]: Coordenadas (x, y) del centro del mejor acierto encontrado.
                                    Retorna None si no se supera el umbral de confianza o si no se encuentra la plantilla especificada.
        """
        img_np = np.array(screenshot)
        img_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)
        #cv2.imwrite(get_public_path('screenshot.png'), img_rgb)
        
        template = cv2.imread(template_path)
        w, h = template.shape[:2][::-1]
        
        img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
        template_hsv = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)

        
        for i, method in enumerate(self.methods, start=1):
            result = cv2.matchTemplate(img_hsv, template_hsv, method)

            # dibujar resultado para visualización
            matching_points = []
            if method == cv2.TM_SQDIFF_NORMED:
                loc = np.where(result <= 0.05)
            elif method == cv2.TM_CCORR_NORMED:
                loc = np.where(result >= 0.98)
            else:
                loc = np.where(result >= threshold)
            for pt in zip(*loc[::-1]):
                matching_points.append(pt)
                cv2.rectangle(
                    img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            res_path = get_public_path('res' + str(i) + '.png')
            cv2.imwrite(res_path, img_rgb)
            print(matching_points)
        

    def find_template_from_img(self, img_path, template_path, threshold=0.8):
        img_rgb = cv2.imread(img_path)
        # se obtiene la imagen en rgb para dibujar los rectángulos de
        # los matches, para más eficiencia, ahorrar el paso intermedio
        template = cv2.imread(template_path)
        w, h = template.shape[:2][::-1]

        img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
        template_hsv = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)

        # cv2.imwrite(get_public_path("imgGris.png"), img_hsv)
        # cv2.imwrite(get_public_path("templateGris.png"), template_hsv)

        for i, method in enumerate(self.methods, start=1):
            result = cv2.matchTemplate(img_hsv, template_hsv, method)

            # dibujar resultado para visualización
            matching_points = []
            if method == cv2.TM_SQDIFF_NORMED:
                loc = np.where(result <= 0.05)
            elif method == cv2.TM_CCORR_NORMED:
                loc = np.where(result >= 0.98)
            else:
                loc = np.where(result >= threshold)
            for pt in zip(*loc[::-1]):
                matching_points.append(pt)
                cv2.rectangle(
                    img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            res_path = get_public_path('res' + str(i) + '.png')
            cv2.imwrite(res_path, img_rgb)
            print(matching_points)
