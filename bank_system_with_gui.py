import customtkinter, random, math, mysql.connector
import pandas as pd
from PIL import Image

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")  
        
class BankUI_CreateAccount(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # APP PROPERTIES #
        self.resizable(0, 0)
        self.geometry("300x360")
        self.after(250, lambda: self.iconbitmap('bank.ico'))
        self.title("Bank System")

        # LOGO IMAGES #
        self.account_icon = customtkinter.CTkImage(light_image = Image.open("icons/account_dark.png"), dark_image = Image.open("icons/account_light.png"), size = (15, 15))
        self.create_icon = customtkinter.CTkImage(light_image = Image.open("icons/create_dark.png"), dark_image = Image.open("icons/create_light.png"), size = (20, 20))
        
        self.title = customtkinter.CTkLabel(self, text = "  Criar Conta", image = self.account_icon, fg_color = "transparent", compound = "left",
                                            text_color = ("gray10", "gray90"), font = customtkinter.CTkFont(size = 15, weight = "bold"))
        self.title.place(x = 95, y = 15)
        
        self.name = customtkinter.CTkEntry(self, width = 200, height = 40, placeholder_text = "Nome", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"))
        self.name.place(x = 50, y = 80)
        
        self.pin = customtkinter.CTkEntry(self, width = 75, height = 40, placeholder_text = "PIN", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"), show = "*")
        self.pin.place(x = 112.5, y = 140)
        
        self.confirm_pin = customtkinter.CTkEntry(self, width = 125, height = 40, placeholder_text = "Confirmar PIN", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"), show = "*")
        self.confirm_pin.place(x = 87.5, y = 200)
        
        self.create = customtkinter.CTkButton(self, text = "Criar Conta", width = 150, height = 50, image = self.create_icon, compound = "left", 
                                               text_color = ("gray10", "gray90"), font = customtkinter.CTkFont(size = 13, weight = "normal"), 
                                               command = self.create_account)
        self.create.place(x = 75, y = 285)
        
    def create_account(self):
        account_name = self.name.get().strip().lower().title()
        account_pin = self.pin.get()
        account_confirm_pin = self.confirm_pin.get()
        
        if account_pin == account_confirm_pin:
            bank.create_account(account_name, account_pin)
        else:
            bankUI.open_notification_window("Os PIN´s não correspondem!")

class BankUI_LoginAccount(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # APP PROPERTIES #
        self.resizable(0, 0)
        self.geometry("300x300")
        self.after(250, lambda: self.iconbitmap('bank.ico'))
        self.title("Bank System")

        # LOGO IMAGES #
        self.account_icon = customtkinter.CTkImage(light_image = Image.open("icons/account_dark.png"), dark_image = Image.open("icons/account_light.png"), size = (15, 15))
        self.login_icon = customtkinter.CTkImage(light_image = Image.open("icons/login_dark.png"), dark_image = Image.open("icons/login_light.png"), size = (20, 20))
        
        self.title = customtkinter.CTkLabel(self, text = "  Entrar", image = self.account_icon, fg_color = "transparent", compound = "left",
                                            text_color = ("gray10", "gray90"), font = customtkinter.CTkFont(size = 15, weight = "bold"))
        self.title.place(x = 112.5, y = 15)
        
        self.name = customtkinter.CTkEntry(self, width = 200, height = 40, placeholder_text = "Nome", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"))
        self.name.place(x = 50, y = 80)
        
        self.pin = customtkinter.CTkEntry(self, width = 75, height = 40, placeholder_text = "PIN", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"), show = "*")
        self.pin.place(x = 112.5, y = 140)
        
        self.login = customtkinter.CTkButton(self, text = "Entrar", width = 150, height = 50, image = self.login_icon, compound = "left", 
                                               text_color = ("gray10", "gray90"), font = customtkinter.CTkFont(size = 13, weight = "normal"),
                                               command = self.login_account)
        self.login.place(x = 75, y = 225)
        
    def login_account(self):
        account_name = self.name.get().strip().lower().title()
        account_pin = self.pin.get()
        
        bank.login_account(account_name, account_pin)
        
class BankUI_EditAccount(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # APP PROPERTIES #
        self.resizable(0, 0)
        self.geometry("300x360")
        self.after(250, lambda: self.iconbitmap('bank.ico'))
        self.title("Bank System")

        # LOGO IMAGES #
        self.account_icon = customtkinter.CTkImage(light_image = Image.open("icons/account_dark.png"), dark_image = Image.open("icons/account_light.png"), size = (15, 15))
        self.edit_icon = customtkinter.CTkImage(light_image = Image.open("icons/edit_dark.png"), dark_image = Image.open("icons/edit_light.png"), size = (20, 20))
        
        self.title = customtkinter.CTkLabel(self, text = "  Editar Conta", image = self.account_icon, fg_color = "transparent", compound = "left",
                                            text_color = ("gray10", "gray90"), font = customtkinter.CTkFont(size = 15, weight = "bold"))
        self.title.place(x = 95, y = 15)
        
        self.name = customtkinter.CTkEntry(self, width = 200, height = 40, placeholder_text = "Nome", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"))
        self.name.place(x = 50, y = 80)
        
        self.pin = customtkinter.CTkEntry(self, width = 75, height = 40, placeholder_text = "PIN", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"), show = "*")
        self.pin.place(x = 112.5, y = 140)
        
        self.confirm_pin = customtkinter.CTkEntry(self, width = 125, height = 40, placeholder_text = "Confirmar PIN", justify = "center", 
                                           font = customtkinter.CTkFont(size = 15, weight = "normal"), show = "*")
        self.confirm_pin.place(x = 87.5, y = 200)
        
        self.edit = customtkinter.CTkButton(self, text = "Editar Conta", width = 150, height = 50, image = self.edit_icon, compound = "left", 
                                               text_color = ("gray10", "gray90"), font = customtkinter.CTkFont(size = 13, weight = "normal"), 
                                               command = self.edit_account)
        self.edit.place(x = 75, y = 285)
        
    def edit_account(self):
        account_name = self.name.get().strip().lower().title()
        account_pin = self.pin.get()
        account_confirm_pin = self.confirm_pin.get()
        
        if account_pin == account_confirm_pin:
            bank.edit_account(account_name, account_pin, bankUI.get_logged_number())
        else:
            bankUI.open_notification_window("Os PIN´s não correspondem!")

class BankUI_Notification(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # APP PROPERTIES #
        self.resizable(0, 0)
        self.geometry("300x75")
        self.after(250, lambda: self.iconbitmap('bank.ico'))
        self.title("Bank System")
        
    def notify(self, notification):
        self.text = customtkinter.CTkLabel(self, text = notification, fg_color = "transparent", anchor = "center", width = 300, height = 75,
                                            text_color = ("gray10", "gray90"), font = customtkinter.CTkFont(size = 15, weight = "bold"))
        self.text.place(x = 0, y = 0)
        
class BankUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # APP VARS #
        self.createaccount_window = None
        self.loginaccount_window = None
        self.editaccount_window = None
        self.notification_window = None
        self.createaccount_state = False
        self.loginaccount_state = False
        self.editaccount_state = False
        self.notification_state = False
        self.last_notify = ""
        self.logged_number = ""
        self.money_on_hand = 0
        
        # APP PROPERTIES #
        self.resizable(0, 0)
        self.geometry("960x540")
        self.iconbitmap("bank.ico")
        self.title("Bank System")

        # LOGO IMAGES #
        self.account_icon = customtkinter.CTkImage(light_image = Image.open("icons/account_dark.png"), dark_image = Image.open("icons/account_light.png"), size = (20, 20))
        self.bank_logo = customtkinter.CTkImage(Image.open("icons/bank.png"), size = (128, 56))
        self.create_icon = customtkinter.CTkImage(light_image = Image.open("icons/create_dark.png"), dark_image = Image.open("icons/create_light.png"), size = (20, 20))
        self.deposit_icon = customtkinter.CTkImage(light_image = Image.open("icons/deposit_dark.png"), dark_image = Image.open("icons/deposit_light.png"), size = (20, 20))
        self.edit_icon = customtkinter.CTkImage(light_image = Image.open("icons/edit_dark.png"), dark_image = Image.open("icons/edit_light.png"), size = (20, 20))
        #self.help_icon = customtkinter.CTkImage(light_image = Image.open("icons/help_dark.png"), dark_image = Image.open("icons/help_light.png"), size = (20, 20))
        self.historic_icon = customtkinter.CTkImage(light_image = Image.open("icons/historic_dark.png"), dark_image = Image.open("icons/historic_light.png"), size = (20, 20))
        self.home_icon = customtkinter.CTkImage(light_image = Image.open("icons/home_dark.png"), dark_image = Image.open("icons/home_light.png"), size = (20, 20))
        self.login_icon = customtkinter.CTkImage(light_image = Image.open("icons/login_dark.png"), dark_image = Image.open("icons/login_light.png"), size = (20, 20))
        self.logout_icon = customtkinter.CTkImage(light_image = Image.open("icons/logout_dark.png"), dark_image = Image.open("icons/logout_light.png"), size = (20, 20))
        self.moneyhand_icon = customtkinter.CTkImage(light_image = Image.open("icons/moneyhand_dark.png"), dark_image = Image.open("icons/moneyhand_light.png"), size = (20, 20))
        #self.money_icon = customtkinter.CTkImage(light_image = Image.open("icons/money_dark.png"), dark_image = Image.open("icons/money_light.png"), size = (20, 20))
        #self.number_icon = customtkinter.CTkImage(light_image = Image.open("icons/number_dark.png"), dark_image = Image.open("icons/number_light.png"), size = (20, 20))
        #self.pin_icon = customtkinter.CTkImage(light_image = Image.open("icons/pin_dark.png"), dark_image = Image.open("icons/pin_light.png"), size = (20, 20))
        self.transfer_icon = customtkinter.CTkImage(light_image = Image.open("icons/transfer_dark.png"), dark_image = Image.open("icons/transfer_light.png"), size = (20, 20))
        self.withdraw_icon = customtkinter.CTkImage(light_image = Image.open("icons/withdraw_dark.png"), dark_image = Image.open("icons/withdraw_light.png"), size = (20, 20))

        # GRID #
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
    
        # NAV FRAME #
        self.nav_frame = customtkinter.CTkFrame(self, corner_radius = 0)
        self.nav_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.nav_frame.grid_rowconfigure(3, weight = 1)
    
        self.nav_frame_logo = customtkinter.CTkLabel(self.nav_frame, text = "", image = self.bank_logo)
        self.nav_frame_logo.grid(row = 0, column = 0, padx = 20, pady = 20)
    
        self.nav_home_frame_button = customtkinter.CTkButton(self.nav_frame, corner_radius = 0, height = 40, border_spacing = 10, 
                                                             text = "Início", fg_color = "transparent", text_color = ("gray10", "gray90"), 
                                                             hover_color = ("gray70", "gray30"), image = self.home_icon, anchor="w", 
                                                             command = self.select_home_frame)
        self.nav_home_frame_button.grid(row = 1, column = 0, sticky = "ew")
        
        self.nav_historic_frame_button = customtkinter.CTkButton(self.nav_frame, corner_radius = 0, height = 40, border_spacing = 10, 
                                                                 text = "Histórico", fg_color = "transparent", 
                                                                 text_color = ("gray10", "gray90"), hover_color = ("gray70", "gray30"), 
                                                                 image = self.historic_icon, anchor = "w", 
                                                                 command = self.select_historic_frame)
        self.nav_historic_frame_button.grid(row = 2, column = 0, sticky = "ew")
  
        self.money_hand = customtkinter.CTkLabel(self.nav_frame, text = f" {self.money_on_hand}€", height = 20, image = self.moneyhand_icon, 
                                                                fg_color = "transparent", compound = "left", text_color = ("gray10", "gray90"), 
                                                                font = customtkinter.CTkFont(size = 15, weight = "normal"))
        self.money_hand.grid(row = 3, column = 0, padx = 20, pady = 65, sticky = "s")
    
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.nav_frame, values=["Escuro", "Claro"], command = self.change_appearance_mode)
        self.appearance_mode_menu.grid(row = 3, column = 0, padx = 20, pady = 20, sticky = "s")
    
        # HOME FRAME #
        self.home_frame = customtkinter.CTkFrame(self, fg_color = "transparent")
    
        self.home_frame_account = customtkinter.CTkFrame(self.home_frame, corner_radius = 20, width = 300, height = 200, 
                                                         fg_color = ("gray75", "gray25"))
        self.home_frame_account.place(x = 30, y = 25)
        
        self.home_frame_account_create = customtkinter.CTkButton(self.home_frame_account, text = "Criar Conta", width = 150, height = 50, 
                                                                 image = self.create_icon, compound = "left", text_color = ("gray10", "gray90"),
                                                                 command = self.open_createaccount_window)
        self.home_frame_account_create.place(x = 75, y = 40)
        self.home_frame_account_login = customtkinter.CTkButton(self.home_frame_account, text = "Entrar", width = 150, height = 50, 
                                                                image = self.login_icon, compound = "left", text_color = ("gray10", "gray90"), 
                                                                font = customtkinter.CTkFont(size = 13, weight = "normal"),
                                                                command = self.open_loginaccount_window)
        self.home_frame_account_login.place(x = 75, y = 110)
        
        self.home_frame_deposit = customtkinter.CTkFrame(self.home_frame, corner_radius = 20, width = 190, height = 200, fg_color= "transparent")
        self.home_frame_deposit.place(x = 350, y = 25)
        self.home_frame_deposit_amount = customtkinter.CTkEntry(self.home_frame_deposit, width = 180, height = 50, placeholder_text = "Quantidade", 
                                                                justify = "center", font = customtkinter.CTkFont(size = 20, weight = "normal"))
        self.home_frame_deposit_amount.place(x = 5, y = 35)
        self.home_frame_deposit_confirm = customtkinter.CTkButton(self.home_frame_deposit, text = "Depositar", width = 130, height = 50, 
                                                                  image = self.deposit_icon, compound = "left", text_color = ("gray10", "gray90"), 
                                                                  font = customtkinter.CTkFont(size = 13, weight = "normal"), command = self.account_deposit_trigger)
        self.home_frame_deposit_confirm.place(x = 30, y = 120)
        
        self.home_frame_separator = customtkinter.CTkLabel(self.home_frame, corner_radius = 2.5, text = "", width = 2.5, height = 200, 
                                                           fg_color= ("gray75", "gray25"))
        self.home_frame_separator.place(x = 552.5, y = 25)
        
        self.home_frame_withdraw = customtkinter.CTkFrame(self.home_frame, corner_radius = 20, width = 190, height = 200, fg_color= "transparent")
        self.home_frame_withdraw.place(x = 570, y = 25)
        self.home_frame_withdraw_amount = customtkinter.CTkEntry(self.home_frame_withdraw, width = 180, height = 50, placeholder_text = "Quantidade", 
                                                                 justify = "center", font = customtkinter.CTkFont(size = 20, weight = "normal"))
        self.home_frame_withdraw_amount.place(x = 5, y = 35)
        self.home_frame_withdraw_confirm = customtkinter.CTkButton(self.home_frame_withdraw, text = "Levantar", width = 130, height = 50, 
                                                                   image = self.withdraw_icon, compound = "left", text_color = ("gray10", "gray90"), 
                                                                   font = customtkinter.CTkFont(size = 13, weight = "normal"), command = self.account_withdraw_trigger)
        self.home_frame_withdraw_confirm.place(x = 30, y = 120)
    
        self.home_frame_transfer = customtkinter.CTkFrame(self.home_frame, corner_radius = 20, width = 300, height = 265, fg_color= "transparent")
        self.home_frame_transfer.place(x = 30, y = 250)
        self.home_frame_transfer_number = customtkinter.CTkEntry(self.home_frame_transfer, width = 220, height = 50, placeholder_text = "ID da conta", 
                                                                 justify = "center", font = customtkinter.CTkFont(size = 20, weight = "normal"))
        self.home_frame_transfer_number.place(x = 40, y = 30)
        self.home_frame_transfer_amount = customtkinter.CTkEntry(self.home_frame_transfer, width = 180, height = 50, placeholder_text = "Quantidade", 
                                                                 justify = "center", font = customtkinter.CTkFont(size = 20, weight = "normal"))
        self.home_frame_transfer_amount.place(x = 60, y = 100)
        self.home_frame_transfer_confirm = customtkinter.CTkButton(self.home_frame_transfer, text = "Transferir", width = 180, height = 50, 
                                                                   image = self.transfer_icon, compound = "left", text_color = ("gray10", "gray90"), 
                                                                   font = customtkinter.CTkFont(size = 13, weight = "normal"), command = self.account_transfer_trigger)
        self.home_frame_transfer_confirm.place(x = 60, y = 185)
        
        self.home_frame_separator2 = customtkinter.CTkLabel(self.home_frame, corner_radius = 2.5, text = "", width = 2.5, height = 265, 
                                                            fg_color= ("gray75", "gray25"))
        self.home_frame_separator2.place(x = 340, y = 250)
        
        self.home_frame_historic_title = customtkinter.CTkLabel(self.home_frame, text = "  Histórico", image = self.historic_icon, 
                                                                fg_color = "transparent", compound = "left", text_color = ("gray10", "gray90"), 
                                                                font = customtkinter.CTkFont(size = 15, weight = "normal"))
        self.home_frame_historic_title.place(x = 370, y = 255)
        self.home_frame_historic = customtkinter.CTkFrame(self.home_frame, corner_radius = 20, width = 380, height = 225, 
                                                          fg_color = ("gray75", "gray25"))
        self.home_frame_historic.place(x = 370, y = 290)
    
        # HISTORIC FRAME #
        self.historic_frame = customtkinter.CTkFrame(self, corner_radius = 0, fg_color = "transparent")
        self.historic_frame_historic_title = customtkinter.CTkLabel(self.historic_frame, text = "  Histórico", image = self.historic_icon, 
                                                                    fg_color = "transparent", compound = "left", text_color = ("gray10", "gray90"), 
                                                                    font = customtkinter.CTkFont(size = 15, weight = "normal"))
        self.historic_frame_historic_title.place(x = 30, y = 20)
        self.historic_frame_historic = customtkinter.CTkFrame(self.historic_frame, corner_radius = 20, width = 720, height = 460, 
                                                              fg_color = ("gray75", "gray25"))
        self.historic_frame_historic.place(x = 30, y = 55)
    
        # DEFAULT FRAME #
        self.select_frame_by_name("home")
    
    def select_frame_by_name(self, name):
        self.nav_home_frame_button.configure(fg_color = ("gray75", "gray25") if name == "home" else "transparent")
        self.nav_historic_frame_button.configure(fg_color = ("gray75", "gray25") if name == "historic" else "transparent")
    
        if name == "home":
            self.home_frame.grid(row = 0, column = 1, sticky = "nsew")
        else:
            self.home_frame.grid_forget()
            
        if name == "historic":
            self.historic_frame.grid(row = 0, column = 1, sticky = "nsew")
        else:
            self.historic_frame.grid_forget()
            
    def select_home_frame(self):
        self.select_frame_by_name("home")

    def select_historic_frame(self):
        self.select_frame_by_name("historic")
    
    def change_appearance_mode(self, new_appearance_mode):
        if new_appearance_mode == "Claro":
            appearance_mode = "Light"
        elif new_appearance_mode == "Escuro":
            appearance_mode = "Dark"
        customtkinter.set_appearance_mode(appearance_mode)
        
    def logged_account(self, name, number, balance):
        self.logged_number = number
        
        self.close_createaccount_window()
        self.close_loginaccount_window()
        self.close_notification_window()
        
        self.home_frame_account_create.destroy()
        self.home_frame_account_login.destroy()
        
        self.home_frame_account_name = customtkinter.CTkLabel(self.home_frame_account, text = name, width = 260, height = 25, 
                                                              justify = "left", anchor = "w", 
                                                              font = customtkinter.CTkFont(size = 20, weight = "bold"), 
                                                              text_color = ("gray10", "gray90"))
        self.home_frame_account_name.place(x = 20, y = 15)
        self.home_frame_account_number = customtkinter.CTkLabel(self.home_frame_account, text = number, width = 260, height = 25, 
                                                                justify = "left", anchor = "w", 
                                                                font = customtkinter.CTkFont(size = 15, weight = "normal"), 
                                                                text_color = ("gray10", "gray90"))
        self.home_frame_account_number.place(x = 20, y = 40)
        self.home_frame_account_pin = customtkinter.CTkLabel(self.home_frame_account, text = "****", width = 260, height = 25, 
                                                              justify = "left", anchor = "w", 
                                                              font = customtkinter.CTkFont(size = 15, overstrike = True), 
                                                              text_color = ("gray10", "gray90"))
        self.home_frame_account_pin.place(x = 20, y = 60)
        self.home_frame_account_amount = customtkinter.CTkLabel(self.home_frame_account, text = f"{balance}€", width = 260, height = 25, 
                                                                justify = "center", anchor = "w", 
                                                                font = customtkinter.CTkFont(size = 25, weight = "bold"), 
                                                                text_color = ("gray10", "gray90"))
        self.home_frame_account_amount.place(x = 20, y = 105)
        self.home_frame_account_edit = customtkinter.CTkButton(self.home_frame_account, text = "", width = 20, height = 20, image = self.edit_icon,
                                                                 fg_color = "transparent", hover_color = ("gray75", "gray25"), command = self.open_edit_account)
        self.home_frame_account_edit.place(x = 12.5, y = 160)
        self.home_frame_account_logout = customtkinter.CTkButton(self.home_frame_account, text = "", width = 20, height = 20, image = self.logout_icon,
                                                                 fg_color = "transparent", hover_color = ("gray75", "gray25"), command = self.logout_account)
        self.home_frame_account_logout.place(x = 252.5, y = 157.5)
        
    def load_historic(self, historic):
        home_historic = historic.loc[historic['account_number'] == self.logged_number, ['action', 'destination', 'amount']].tail(3).values.tolist()
        home_historic = home_historic[::-1]
        self.historic_len = len(home_historic)

        for i in range(0, len(home_historic)):
            if home_historic[i][0] == "deposit":
                image = self.deposit_icon
            elif home_historic[i][0] == "withdraw":
                image = self.withdraw_icon
            elif home_historic[i][0] == "transfer":
                image = self.transfer_icon
            
            if i == 0:
                self.home_frame_historic_1 = customtkinter.CTkFrame(self.home_frame_historic, corner_radius = 10, width = 350, height = 60, 
                                                                  fg_color = ("gray90", "gray10"))
                self.home_frame_historic_1.place(x = 15, y = 15)
                self.home_frame_historic_1_icon = customtkinter.CTkButton(self.home_frame_historic_1, text = "", width = 40, height = 40, 
                                                                          image = image, state = "DISABLED")
                self.home_frame_historic_1_icon.place(x = 10, y = 10)
                if home_historic[i][0] == "transfer":
                    self.home_frame_historic_1_number = customtkinter.CTkLabel(self.home_frame_historic_1, text = home_historic[i][1], width = 150, height = 40, 
                                                                               fg_color = "transparent", text_color = ("gray10", "gray90"), anchor = "e", 
                                                                               font = customtkinter.CTkFont(size = 15, weight = "bold"))
                    self.home_frame_historic_1_number.place(x = 60, y = 10)
                self.home_frame_historic_1_amount = customtkinter.CTkLabel(self.home_frame_historic_1, text = f"{home_historic[i][2]}€", width = 90, height = 40, 
                                                                           fg_color = "transparent", text_color = ("gray10", "gray90"), anchor = "e", 
                                                                           font = customtkinter.CTkFont(size = 20, weight = "bold"))
                self.home_frame_historic_1_amount.place(x = 245, y = 10)
                
            elif i == 1:
                self.home_frame_historic_2 = customtkinter.CTkFrame(self.home_frame_historic, corner_radius = 10, width = 350, height = 60, 
                                                                  fg_color = ("gray90", "gray10"))
                self.home_frame_historic_2.place(x = 15, y = 82.5)
                self.home_frame_historic_2_icon = customtkinter.CTkButton(self.home_frame_historic_2, text = "", width = 40, height = 40, 
                                                                          image = image, state = "DISABLED")
                self.home_frame_historic_2_icon.place(x = 10, y = 10)
                if home_historic[i][0] == "transfer":
                    self.home_frame_historic_2_number = customtkinter.CTkLabel(self.home_frame_historic_2, text = home_historic[i][1], width = 150, height = 40, 
                                                                                fg_color = "transparent", text_color = ("gray10", "gray90"), anchor = "e", 
                                                                                font = customtkinter.CTkFont(size = 15, weight = "bold"))
                    self.home_frame_historic_2_number.place(x = 60, y = 10)
                self.home_frame_historic_2_amount = customtkinter.CTkLabel(self.home_frame_historic_2, text = f"{home_historic[i][2]}€", width = 90, height = 40, 
                                                                            fg_color = "transparent", text_color = ("gray10", "gray90"), anchor = "e", 
                                                                            font = customtkinter.CTkFont(size = 20, weight = "bold"))
                self.home_frame_historic_2_amount.place(x = 245, y = 10)
                
            elif i == 2:
                self.home_frame_historic_3 = customtkinter.CTkFrame(self.home_frame_historic, corner_radius = 10, width = 350, height = 60, 
                                                                  fg_color = ("gray90", "gray10"))
                self.home_frame_historic_3.place(x = 15, y = 150)
                self.home_frame_historic_3_icon = customtkinter.CTkButton(self.home_frame_historic_3, text = "", width = 40, height = 40, 
                                                                          image = image, state = "DISABLED")
                self.home_frame_historic_3_icon.place(x = 10, y = 10)
                if home_historic[i][0] == "transfer":
                    self.home_frame_historic_3_number = customtkinter.CTkLabel(self.home_frame_historic_3, text = home_historic[i][1], width = 150, height = 40, 
                                                                                fg_color = "transparent", text_color = ("gray10", "gray90"), anchor = "e", 
                                                                                font = customtkinter.CTkFont(size = 15, weight = "bold"))
                    self.home_frame_historic_3_number.place(x = 60, y = 10)
                self.home_frame_historic_3_amount = customtkinter.CTkLabel(self.home_frame_historic_3, text = f"{home_historic[i][2]}€", width = 90, height = 40, 
                                                                            fg_color = "transparent", text_color = ("gray10", "gray90"), anchor = "e", 
                                                                            font = customtkinter.CTkFont(size = 20, weight = "bold"))
                self.home_frame_historic_3_amount.place(x = 245, y = 10)
         
    def logout_account(self):   
        bankUI.close_edit_account()
        bankUI.unload_historic()
        self.logged_number = ""
        
        self.home_frame_account_name.destroy()
        self.home_frame_account_number.destroy()
        self.home_frame_account_pin.destroy()
        self.home_frame_account_amount.destroy()
        self.home_frame_account_edit.destroy()
        self.home_frame_account_logout.destroy()
        
        self.home_frame_account_create = customtkinter.CTkButton(self.home_frame_account, text = "Criar Conta", width = 150, height = 50, 
                                                                 image = self.create_icon, compound = "left", text_color = ("gray10", "gray90"),
                                                                 command = self.open_createaccount_window)
        self.home_frame_account_create.place(x = 75, y = 40)
        self.home_frame_account_login = customtkinter.CTkButton(self.home_frame_account, text = "Entrar", width = 150, height = 50, 
                                                                image = self.login_icon, compound = "left", text_color = ("gray10", "gray90"), 
                                                                font = customtkinter.CTkFont(size = 13, weight = "normal"),
                                                                command = self.open_loginaccount_window)
        self.home_frame_account_login.place(x = 75, y = 110)
        
    def unload_historic(self):
        if self.historic_len >= 1:
            self.home_frame_historic_1.destroy()
            
        if self.historic_len >= 2:
            self.home_frame_historic_2.destroy()
            
        if self.historic_len >= 3:
            self.home_frame_historic_3.destroy()
        
    def account_deposit_trigger(self):
        bank.deposit_account(self.logged_number, self.money_on_hand, self.home_frame_deposit_amount.get())

    def account_withdraw_trigger(self):
        bank.withdraw_account(self.logged_number, self.money_on_hand, self.home_frame_withdraw_amount.get())
        
    def account_transfer_trigger(self):
        bank.transfer_account(self.logged_number, self.home_frame_transfer_number.get(), self.home_frame_transfer_amount.get())
        
    def get_logged_number(self):
        return self.logged_number
        
    def change_money_on_hand(self, amount):
        self.money_hand.configure(text = f" {amount}€")
        self.money_on_hand = amount
        
    def change_bank_name(self, name):
        self.home_frame_account_name.configure(text = name)
        
    def change_bank_balance(self, amount):
        self.home_frame_account_amount.configure(text = f"{amount}€")

    def open_createaccount_window(self): 
        if not self.createaccount_state and not self.loginaccount_state:
            self.createaccount_state = True
            self.createaccount_window = BankUI_CreateAccount(self)
            self.createaccount_window.protocol("WM_DELETE_WINDOW", bankUI.close_createaccount_window)
            self.after(500, lambda: self.createaccount_window.focus())
            
        if self.createaccount_state:
            self.createaccount_window.focus()
        
    def close_createaccount_window(self): 
        if self.createaccount_state:
            self.createaccount_state = False
            self.createaccount_window.destroy()
            self.createaccount_window = None

    def open_loginaccount_window(self):
        if not self.loginaccount_state and not self.createaccount_state:
            self.loginaccount_state = True
            self.loginaccount_window = BankUI_LoginAccount(self)
            self.loginaccount_window.protocol("WM_DELETE_WINDOW", bankUI.close_loginaccount_window)
            self.after(500, lambda: self.loginaccount_window.focus())
            
        if self.loginaccount_state:
            self.loginaccount_window.focus()

    def close_loginaccount_window(self): 
        if self.loginaccount_state:
            self.loginaccount_state = False
            self.loginaccount_window.destroy()  
            self.loginaccount_window = None
            
    def open_edit_account(self):
        if not self.editaccount_state:
            self.editaccount_state = True
            self.editaccount_window = BankUI_EditAccount(self)
            self.editaccount_window.protocol("WM_DELETE_WINDOW", bankUI.close_edit_account)
            self.after(500, lambda: self.editaccount_window.focus())
            
        if self.editaccount_state:
            self.editaccount_window.focus()
            
    def close_edit_account(self):
        if self.editaccount_state:
            self.editaccount_state = False
            self.editaccount_window.destroy()
            self.editaccount_window = None

    def open_notification_window(self, message):
        if not self.notification_state:
            self.last_notify = message
            self.notification_state = True
            self.notification_window = BankUI_Notification(self)
            BankUI_Notification.notify(self.notification_window, message)
            self.notification_window.protocol("WM_DELETE_WINDOW", bankUI.close_notification_window)
            self.after(500, lambda: self.notification_window.focus())
        else:
            if not self.last_notify == message:
                BankUI_Notification.notify(self.notification_window, message)
            self.notification_window.focus()

    def close_notification_window(self):
        if self.notification_state:
            self.notification_state = False
            self.notification_window.destroy()  
            self.notification_window = None
            
class Bank:
    def __init__(self):
        self.get_data()
        self.new_historic = pd.DataFrame(columns = ["account_number", "action", "destination", "amount"])
        
    def get_data(self):
        self.connection = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '',
            database = 'bank'
        )
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("SELECT * FROM accounts")
        data = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        self.accounts = pd.DataFrame(data, columns = columns)
        
        self.cursor.execute("SELECT * FROM historic")
        data = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        self.historic = pd.DataFrame(data, columns = columns)
        
        self.cursor.close()
        self.connection.close()
        
    def save_data(self):
        self.connection = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '',
            database = 'bank'
        )
        self.cursor = self.connection.cursor()

        for _, data in self.accounts.iterrows():
            name = data['account_name']
            pin = data['account_pin']
            balance = data['balance']
            number = data['account_number']
            
            check_query = "SELECT * FROM accounts WHERE account_number = %s"
            self.cursor.execute(check_query, (number,))
            result = self.cursor.fetchone()
    
            if result:
                update_query = "UPDATE accounts SET account_name = %s, account_pin = %s, balance = %s WHERE account_number = %s"
                values = (name, pin, balance, number)
                self.cursor.execute(update_query, values)
            else:
                insert_query = "INSERT INTO accounts (account_name, account_pin, balance, account_number) VALUES (%s, %s, %s, %s)"
                values = (name, pin, balance, number)
                self.cursor.execute(insert_query, values)
                
            self.connection.commit()

        for _, data in self.new_historic.iterrows():
            number = data['account_number']
            action = data['action']
            destination = data['destination']
            amount = data['amount']

            insert_query = "INSERT INTO historic (account_number, action, destination, amount) VALUES (%s, %s, %s, %s)"
            values = (number, action, destination, amount)
            self.cursor.execute(insert_query, values)
                
            self.connection.commit()

        self.cursor.close()
        self.connection.close()

        bankUI.destroy()

    def create_account(self, name, pin, number = "", balance = 0):
        if len(name) <= 0 or len(name) > 26:
            return bankUI.open_notification_window("Nome inválido!")
        
        if len(pin) != 4 and math.isnan(pin):
            return bankUI.open_notification_window("PIN inválido!")
        
        if not self.accounts.loc[self.accounts['account_name'] == name].empty:
            return bankUI.open_notification_window("Conta já existente!")
        
        while number == "" or not self.accounts.loc[self.accounts['account_number'] == number].empty:
            for i in range(16):
                digit = random.randint(0, 9)
                number += str(digit)
                
                if (i + 1) % 4 == 0 and (i + 1) != 16:
                    number += " "
        
        new_account = pd.DataFrame([{'account_name': name, 'account_pin': pin, 'account_number': number, 'balance': balance}])
        self.accounts = pd.concat([self.accounts, new_account], ignore_index = True)

        bankUI.logged_account(name, number, balance)
        bankUI.load_historic(pd.concat([self.historic, self.new_historic], ignore_index = True))
        
    def login_account(self, name, pin):
        if len(name) <= 0 or len(name) > 26:
            return bankUI.open_notification_window("Nome inválido!")
        
        if len(pin) != 4 and math.isnan(pin):
            return bankUI.open_notification_window("PIN inválido!")
        
        if self.accounts.loc[(self.accounts['account_name'] == name) & (self.accounts['account_pin'] == pin)].empty:
            return bankUI.open_notification_window("Credenciais incorretas!")
        
        filter_account_number = self.accounts[(self.accounts['account_name'] == name) & (self.accounts['account_pin'] == pin)]
        number = filter_account_number['account_number'].values[0]
        
        filter_balance = self.accounts[(self.accounts['account_name'] == name) & (self.accounts['account_pin'] == pin)]
        balance = filter_balance['balance'].values[0]
        
        bankUI.logged_account(name, number, balance)
        bankUI.load_historic(pd.concat([self.historic, self.new_historic], ignore_index = True))
        
    def edit_account(self, name, pin, number):
        if len(name) <= 0 or len(name) > 26:
            return bankUI.open_notification_window("Nome inválido!")
        
        if len(pin) != 4 and math.isnan(pin):
            return bankUI.open_notification_window("PIN inválido!")
        
        if not number in self.accounts['account_number'].values:
            return bankUI.open_notification_window("Número de conta inválido!")
        
        self.accounts.loc[self.accounts['account_number'] == number, 'account_name'] = name
        self.accounts.loc[self.accounts['account_number'] == number, 'account_pin'] = pin
        bankUI.change_bank_name(self.accounts['account_name'][self.accounts['account_number'] == number].values[0])
        bankUI.close_edit_account()
        bankUI.open_notification_window("Alterações realizados com sucesso!")
        
    def update_new_historic(self, number, action, destination, amount):
        new_transaction = pd.DataFrame([{'account_number': number, 'action': action, 'destination': destination, 'amount': amount}])
        self.new_historic = pd.concat([self.new_historic, new_transaction], ignore_index = True)

        bankUI.load_historic(pd.concat([self.historic, self.new_historic], ignore_index = True))
        
    def deposit_account(self, number, money_hand, deposit_amount):
        if number != "":
            try:
                amount = int(deposit_amount)
            except ValueError:
                bankUI.open_notification_window("Quantidade inválida!")
            else:
                if amount > 0:
                    if amount <= money_hand:
                        money_hand -= amount
                        self.accounts.loc[self.accounts['account_number'] == number, 'balance'] += amount
                        bankUI.open_notification_window(f"Depósito de {amount}€ com sucesso!")
                        bank.update_new_historic(number, "deposit", None, amount)
                        bankUI.change_money_on_hand(money_hand)
                        bankUI.change_bank_balance(self.accounts['balance'][self.accounts['account_number'] == number].values[0])
                    else:
                        bankUI.open_notification_window("Dinheiro insuficiente!")
                else:
                    bankUI.open_notification_window("Quantidade inválida!")
        else:
            bankUI.open_notification_window("Necessitas de estar numa conta!")

    def withdraw_account(self, number, money_hand, withdraw_amount):
        if number != "":
            try:
                amount = int(withdraw_amount)
            except ValueError:
                bankUI.open_notification_window("Quantidade inválida!")
            else:
                if amount > 0:
                    filter_balance = self.accounts[self.accounts['account_number'] == number]
                    balance = filter_balance['balance'].values[0]
    
                    if amount <= balance:
                        money_hand += amount
                        self.accounts.loc[self.accounts['account_number'] == number, 'balance'] -= amount
                        bankUI.open_notification_window(f"Levantamento de {amount}€ com sucesso!")
                        bank.update_new_historic(number, "withdraw", None, amount)
                        bankUI.change_money_on_hand(money_hand)
                        bankUI.change_bank_balance(self.accounts['balance'][self.accounts['account_number'] == number].values[0])
                    else:
                        bankUI.open_notification_window("Dinheiro insuficiente!")
                else:
                    bankUI.open_notification_window("Quantidade inválida!")
        else:
            bankUI.open_notification_window("Necessitas de estar numa conta")
        
    def transfer_account(self, number, number_to, transfer_amount):
        if number != "":
            if number_to != "" and number != number_to and number_to in self.accounts['account_number'].values:
                try: 
                    amount = int(transfer_amount)
                except ValueError:
                    bankUI.open_notification_window("Quantidade inválida!")
                else:
                    if amount > 0:
                        filter_balance = self.accounts[self.accounts['account_number'] == number]
                        balance = filter_balance['balance'].values[0]
        
                        if amount <= balance:
                            self.accounts.loc[self.accounts['account_number'] == number, 'balance'] -= amount
                            self.accounts.loc[self.accounts['account_number'] == number_to, 'balance'] += amount
                            bankUI.open_notification_window(f"Transferido {amount}€ com sucesso!")
                            bank.update_new_historic(number, "transfer", number_to, amount)
                            bankUI.change_bank_balance(self.accounts['balance'][self.accounts['account_number'] == number].values[0])
                        else:
                            bankUI.open_notification_window("Dinheiro insuficiente!")
                    else:
                        bankUI.open_notification_window("Quantidade inválida!")
            else:
                bankUI.open_notification_window("Número de destinatário inválido!")
        else:
            bankUI.open_notification_window("Necessitas de estar numa conta!")

if __name__ == "__main__":
    bank = Bank()
    bankUI = BankUI()
    bankUI.protocol("WM_DELETE_WINDOW", bank.save_data)
    bankUI.mainloop()
    
#TODO HISTORIC TAB 