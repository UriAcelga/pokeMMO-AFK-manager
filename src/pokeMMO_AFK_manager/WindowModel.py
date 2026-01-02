import pyautogui
import ctypes


class WindowModel:
    def __init__(self):
        self.windowList = pyautogui.getAllWindows()

        self._SW_RESTORE = 9 #Constante mágica

    def print_window_list(self):
        print(
            f"--- Se encontraron {len(self.windowList)} ventanas activas ---")

        for window in self.windowList:
            # Filtramos windows vacías (procesos de fondo sin interfaz)
            if window.title:
                print(f"Title: [{window.title}]")

    def enfocar_ventana(self, windowTitle):
        #FindWindowW para encontrar la ventana
        #ShowWindow para activar la ventana si está minimizada
        #SetForegroundWindow enfoca la ventana
        #SW_RESTORE - Constante mágica para restaurar ventana

        dllHandler = ctypes.windll.user32 #user32 tiene las funciones de manipulación

        windowId = dllHandler.FindWindowW(None, windowTitle)
        
        if not windowId:
            raise ValueError(f"Ventana con nombre [{windowTitle}] no encontrada.")
        
        dllHandler.ShowWindow(windowId, self._SW_RESTORE)
        dllHandler.SetForegroundWindow(windowId)
        rect_arr = (ctypes.c_long * 4)() #Estructura necesaria para pasar como referencia
        #0 - left / 1 - top / 2 - right / 3 - bottom
        res = dllHandler.GetWindowRect(windowId, ctypes.byref(rect_arr)) #recibe una referencia a RECT y retorna el diccionario de coordenadas de ventana
        if res == 0:
            raise ValueError(f"No se encontraron coordenadas para la ventana [{windowTitle}].")
        return {"left": rect_arr[0],
                "top": rect_arr[1],
                "width": rect_arr[2] - rect_arr[0],
                "height": rect_arr[3] - rect_arr[1]}

    
            
