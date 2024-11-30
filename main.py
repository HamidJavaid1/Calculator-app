from flet import *

class Calculator(Container):
    def __init__(self):
        super().__init__()
        self.alignment = alignment.center
        self.mainapp = Column(spacing=10, horizontal_alignment="center")
        self.width = 320
        self.padding = 10
        self.bgcolor = '#333333'
        self.content = self.mainapp
   
        self.textdisplay = TextField(bgcolor="#444444", border_width=0 , read_only=True, color="white" , text_size=25,)
        self.mainapp.controls.append(self.textdisplay)
        
        buttons = [
            ["9" , "8" ,"7", "+"],
            ["6" , "5" , "4","-"],
            ["3","2","1","*"],
            ["0",".","C","/"]
        ]

        for button in buttons:
            self.btnrow = Row(spacing=20, alignment="center")
            for btn in button:
                self.btn = ElevatedButton(text=btn, bgcolor="#444444", color="#ffffff" , width=50, height=50,on_click=lambda e, n=btn: self.handleclick(n))
                self.btnrow.controls.append(self.btn)
            self.mainapp.controls.append(self.btnrow)
        
        equalbtn = Button(text="=" ,width=50 , height=50 , color="white" , bgcolor="blue")
        equalbtn.on_click = self.calculate
        self.mainapp.controls.append(equalbtn)

    def handleclick(self,number):
        if number == "C":
            self.textdisplay.value = None
        else:
            if self.textdisplay.value == "Error":
               self.textdisplay.value = number
            else:
             self.textdisplay.value +=  number
        self.textdisplay.update()

    def calculate(self,e):
     try:
      self.textdisplay.value = str(eval(self.textdisplay.value))
     except SyntaxError:
        self.textdisplay.value = "Error"
     self.textdisplay.update()

def main(page:Page):
    page.title = "Calculator app"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.appbar = AppBar(
            leading=Icon(icons.CALCULATE_OUTLINED),
            leading_width=40,
            title=Text("My First in Python with flet, Flutter"),
            center_title=True,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                IconButton(icons.WB_SUNNY_OUTLINED),
                IconButton(icons.FILTER_3),
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Item 1"),
                        PopupMenuItem(),  # divider
                        PopupMenuItem(
                            text="Checked item", checked=False, 
                        ),
                    ]
                ),
            ],
        )
    page.add(Calculator())

app(target=main)