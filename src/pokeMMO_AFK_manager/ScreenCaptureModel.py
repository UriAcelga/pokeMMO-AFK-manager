from mss import mss
class ScreenCaptureModel:
    def __init__(self):
        self.sct = mss()
        
    def capturar(self, region=None):
        """
        Captura la pantalla.
        
        Args:
            region: Región de la pantalla donde sacar la captura {'top': int, 'left': int, 'width': int, 'height': int}
            
        Returns:
            Screenshot: Objeto mss.Screenshot: Arreglo de bytes con los píxeles sin procesar de la captura.
        """
        return self.sct.grab(region if region else self.sct.monitors[1])