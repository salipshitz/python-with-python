from PIL import ImageTk
from WCK import Widget

class ImageView(Widget):
        ui_option_width = 512
        ui_option_height = 512
        
        def __init__(self, master **options):
                self.photo = self.image = None
                self.ui_init(master, options)
                
        def ui_handle_config(self):
                return {
                        int(self.ui_option_width),
                        int(self.ui_option_height)

                }
        
        def ui_handle_repair(self, draw, x0, y0, x1, y1):
                if self.photo is None:
                        return
                if self.image is None:
                        self.image = self.ui_image(str(self.photo))
                draw.paste(self.image)
        
        def set_image(self, image):
                self.photo = ImageTk.PhotoImage(image)
                self.image = None
                self.ui_damage()
