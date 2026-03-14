from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.graphics import Rectangle

menu = {
    "Bánh mì": {"Giá": 3000, "img": "images/banhmi.png"},
    "Hủ tiếu": {"Giá": 30000, "img": "images/hutieu.png"},
    "Bún riêu": {"Giá": 30000, "img": "images/bunrieu.png"},
    "Cháo": {"Giá": 20000, "img": "images/chao.png"}
}


class OrderApp(App):

    def build(self):

        self.order = {}
        self.total = 0
        self.history = []

        root = BoxLayout(orientation="horizontal")

        # ===== BACKGROUND =====
        with root.canvas.before:
            self.bg = Rectangle(
                source="images/background.jpg",
                pos=root.pos,
                size=root.size
            )

        root.bind(size=self.update_bg, pos=self.update_bg)

        # ===== MENU =====
        menu_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        menu_layout.bind(minimum_height=menu_layout.setter("height"))

        for item in menu:

            box = BoxLayout(size_hint_y=None, height=90)

            img = Image(
                source=menu[item]["img"],
                size_hint_x=0.3
            )

            label = Label(
                text=item,
                color=(1, 1, 0, 1)
            )

            btn_add = Button(text="+", size_hint_x=0.2)
            btn_remove = Button(text="-", size_hint_x=0.2)

            btn_add.bind(on_press=lambda x, i=item: self.add_item(i))
            btn_remove.bind(on_press=lambda x, i=item: self.remove_item(i))

            box.add_widget(img)
            box.add_widget(label)
            box.add_widget(btn_add)
            box.add_widget(btn_remove)

            menu_layout.add_widget(box)

        scroll = ScrollView(size_hint_x=0.4)
        scroll.add_widget(menu_layout)

        # ===== BILL =====
        bill_layout = BoxLayout(
            orientation="vertical",
            size_hint_x=0.3
        )

        self.bill_label = Label(
            text="Chưa có món",
            color=(1, 1, 1, 1)
        )

        self.money_input = TextInput(
            hint_text="Tiền khách đưa",
            size_hint_y=None,
            height=40,
            multiline=False
        )

        pay_btn = Button(
            text="Thanh toán",
            size_hint_y=None,
            height=80
        )

        pay_btn.bind(on_press=self.calculate)

        self.result_label = Label(
            text="Tổng: 0",
            color=(1, 0, 0, 1)
        )

        bill_layout.add_widget(self.bill_label)
        bill_layout.add_widget(self.money_input)
        bill_layout.add_widget(pay_btn)
        bill_layout.add_widget(self.result_label)

        # ===== HISTORY =====
        history_layout = BoxLayout(
            orientation="vertical",
            size_hint_x=0.3
        )

        history_title = Label(
            text="Lịch sử đơn",
            color=(0, 1, 0, 1)
        )

        self.history_label = Label(
            text="Chưa có đơn",
            halign="left"
        )

        history_layout.add_widget(history_title)
        history_layout.add_widget(self.history_label)

        root.add_widget(scroll)
        root.add_widget(bill_layout)
        root.add_widget(history_layout)

        return root

    def update_bg(self, *args):
        self.bg.pos = self.root.pos
        self.bg.size = self.root.size

    def add_item(self, item):

        self.order[item] = self.order.get(item, 0) + 1
        self.update_bill()

    def remove_item(self, item):

        if item in self.order:

            self.order[item] -= 1

            if self.order[item] <= 0:
                del self.order[item]

        self.update_bill()

    def update_bill(self):

        text = ""
        total = 0

        for item, qty in self.order.items():

            price = menu[item]["Giá"]

            total += price * qty

            text += f"{item} x{qty} = {price*qty}đ\n"

        self.total = total

        if text == "":
            text = "Chưa có món"

        self.bill_label.text = text

    def calculate(self, instance):

        try:
            customer = int(self.money_input.text)
        except:
            customer = 0

        change = customer - self.total

        self.result_label.text = f"Tổng: {self.total}đ\nTiền thừa: {change}đ"

        # ===== LƯU LỊCH SỬ =====
        order_text = ""

        for item, qty in self.order.items():
            order_text += f"{item} x{qty} | Đã thanh toán\n"

        if order_text != "":
            self.history.append(order_text)

        self.history_label.text = "\n".join(self.history)

        # Reset hóa đơn
        self.order = {}
        self.bill_label.text = "Chưa có món"
        self.money_input.text = ""
        self.total = 0


OrderApp().run()
