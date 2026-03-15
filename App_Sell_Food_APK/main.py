
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.popup import Popup


menu = {
    "Bánh mì": {"small": 3000,"large":3000, "img": "images/banhmi.png"},
    "Hủ tiếu": {"small": 25000, "large": 30000, "img": "images/hutieu.png"},
    "Bún riêu": {"small": 25000, "large": 30000, "img": "images/bunrieu.png"},
    "Cháo": {"small": 20000, "large": 23000, "img": "images/chao.png"}
}


class Divider(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1,1,1,0.6)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update,size=self.update)

    def update(self,*args):

        self.rect.pos=self.pos
        self.rect.size=self.size


class POSApp(App):

    def build(self):

        self.order={}
        self.total=0

        root=BoxLayout(orientation="horizontal")

        # ===== BACKGROUND =====
        with root.canvas.before:
            self.bg=Rectangle(
                source="images/background.jpg",
                pos=root.pos,
                size=root.size
            )

        root.bind(size=self.update_bg,pos=self.update_bg)

        # ===== MENU =====
        left=BoxLayout(
            orientation="vertical",
            size_hint_x=0.6,
            padding=10
        )

        title=Label(
            text="MENU",
            size_hint_y=0.1,
            color=(1,1,0,1),
            font_size = 32,
            bold = True
        )

        left.add_widget(title)

        scroll=ScrollView()

        grid=GridLayout(
            cols=3,
            spacing=10,
            size_hint_y=None
        )

        grid.bind(minimum_height=grid.setter("height"))

        for item in menu:

            box=BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=180
            )

            img_btn=Button(
                background_normal=menu[item]["img"],
                background_down=menu[item]["img"]
            )

            img_btn.bind(on_press=lambda x,i=item:self.choose_size(i))

            name=Label(text=item,size_hint_y=0.3)

            box.add_widget(img_btn)
            box.add_widget(name)

            grid.add_widget(box)

        scroll.add_widget(grid)

        left.add_widget(scroll)

        # ===== DIVIDER =====
        divider=Divider(size_hint_x=0.01)

        # ===== BILL =====
        right=BoxLayout(
            orientation="vertical",
            size_hint_x=0.39,
            padding=10,
            spacing=10
        )

        bill_title=Label(
            text="HÓA ĐƠN",
            size_hint_y=0.1,
            color=(0,1,0,1),
            font_size = 32,
            bold = True
        )

        self.bill_label=Label(
            text="Chưa có món",
            halign="left",
            valign="top"
        )

        self.note_input=TextInput(
            hint_text="Ghi chú đơn hàng...",
            size_hint_y=0.15
        )

        self.money_input=TextInput(
            hint_text="Tiền khách đưa",
            multiline=False,
            size_hint_y=0.1
        )

        self.total_label=Label(
            text="Tổng tiền: 0đ",
            size_hint_y=0.1,
            color=(1,0,0,1),
            font_size = 28,
            bold = True
        )

        pay_btn=Button(
            text="YÊU CẦU THANH TOÁN",
            size_hint_y=0.15
        )

        pay_btn.bind(on_press=self.pay)

        right.add_widget(bill_title)
        right.add_widget(self.bill_label)
        right.add_widget(self.note_input)
        right.add_widget(self.money_input)
        right.add_widget(self.total_label)
        right.add_widget(pay_btn)

        root.add_widget(left)
        root.add_widget(divider)
        root.add_widget(right)

        return root


    # ===== BACKGROUND =====
    def update_bg(self,*args):

        self.bg.pos=self.root.pos
        self.bg.size=self.root.size


    # ===== SIZE POPUP =====
    def choose_size(self,item):

        layout=BoxLayout()

        btn_small=Button(text="Nhỏ")
        btn_large=Button(text="Lớn")

        layout.add_widget(btn_small)
        layout.add_widget(btn_large)

        popup=Popup(
            title="Chọn size",
            content=layout,
            size_hint=(0.5,0.3)
        )

        btn_small.bind(on_press=lambda x:self.add_item(item,"small"))
        btn_large.bind(on_press=lambda x:self.add_item(item,"large"))

        btn_small.bind(on_press=popup.dismiss)
        btn_large.bind(on_press=popup.dismiss)

        popup.open()


    # ===== ADD ITEM =====
    def add_item(self,item,size):

        key=f"{item}_{size}"

        self.order[key]=self.order.get(key,0)+1

        self.update_bill()


    # ===== UPDATE BILL =====
    def update_bill(self):

        text=""
        total=0

        for key,qty in self.order.items():

            item,size=key.split("_")

            price=menu[item][size]

            size_name="Nhỏ" if size=="small" else "Lớn"

            total+=price*qty

            text+=f"{item} ({size_name}) x{qty}   {price*qty}đ\n"

        if text=="":
            text="Chưa có món"

        self.total=total

        self.bill_label.text=text
        self.total_label.text=f"Tổng tiền: {total}đ"


    # ===== PAYMENT =====
    def pay(self,instance):

        try:
            money=int(self.money_input.text)
        except:
            money=0

        change=money-self.total

        note=self.note_input.text

        print("===== HÓA ĐƠN =====")
        print(self.bill_label.text)
        print("Ghi chú:",note)
        print("Tiền khách:",money)
        print("Tiền thừa:",change)

        self.total_label.text=f"Tổng: {self.total}đ | Tiền thừa: {change}đ"

        self.order={}
        self.bill_label.text="Chưa có món"
        self.note_input.text=""
        self.money_input.text=""
        self.total=0


POSApp().run()
