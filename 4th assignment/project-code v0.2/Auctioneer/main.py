from tkinter import *
import tkinter as tk
import os
import random
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class LoginWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Auctioneer Login")
        self.parent.option_add("*Font", "Helvetica 14")
        self.parent.iconbitmap("logo0.4.ico")
        self.parent.geometry("540x400")
        self.parent.configure(bg="#1C1F25")

        canvas_width = 540
        canvas_height = 400

        self.canvas = tk.Canvas(self.parent, width=canvas_width, height=canvas_height, bg='#1C1F25',
                                highlightthickness=0)
        self.canvas.pack()

        self.image = tk.PhotoImage(file="logo0.2_rb_-removebg-preview.png")

        self.canvas.create_image(150, 200, image=self.image)

        self.username_label = tk.Label(self.canvas, fg="#ac9152", bg='#1C1F25', bd=3, text="Username:")
        self.username_entry = tk.Entry(self.canvas, width=20, fg="black", bg="#ac9152", bd=1)
        self.password_label = tk.Label(self.canvas, fg="#ac9152", bg='#1C1F25', bd=3, text="Password:")
        self.password_entry = tk.Entry(self.canvas, width=20, fg="black", bg="#ac9152", bd=1, show="*")
        self.login_button = tk.Button(self.canvas, text="Login", fg="black", bg="#ac9152", bd=3, command=self.login)
        self.create_account_button = tk.Button(self.canvas, text="Create an Account", fg="black", bg="#ac9152", bd=3,
                                               command=self.create_account)

        self.canvas.create_window(420, 80, window=self.username_label)
        self.canvas.create_window(420, 120, window=self.username_entry)
        self.canvas.create_window(420, 160, window=self.password_label)
        self.canvas.create_window(420, 200, window=self.password_entry)
        self.canvas.create_window(420, 240, window=self.login_button)
        self.canvas.create_window(420, 290, window=self.create_account_button)

    def login(self):
        self.parent.destroy()
        MainWindow()

        '''username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "Xionatos" and password == "TL2023":
            messagebox.showinfo("Login", "Login Successful!")
            self.parent.destroy()
            MainWindow()
        else:
            messagebox.showerror("Login", "Invalid username or password")
        print("Try Again")'''

    def create_account(self):
        self.registration_window = tk.Toplevel(self.parent)
        self.registration_window.title("Auctioneer Registration")

        canvas_width = 500
        canvas_height = 400
        self.canvas = tk.Canvas(self.registration_window, width=canvas_width, height=canvas_height, bg='#242424')
        self.canvas.pack()

        self.image = tk.PhotoImage(file="logo0.2_rb_-removebg-preview.png")

        self.canvas.create_image(canvas_width / 3, canvas_height / 2, image=self.image)

        self.username_label = tk.Label(self.canvas, fg="black", bg="#ac9152", bd=3, text="Username:")
        self.username_entry = tk.Entry(self.canvas, fg="black", bg="#ac9152", bd=0)
        self.password_label = tk.Label(self.canvas, fg="black", bg="#ac9152", bd=3, text="Password:")
        self.password_entry = tk.Entry(self.canvas, fg="black", bg="#ac9152", bd=0, show="*")
        self.login_button = tk.Button(self.canvas, text="Login", fg="black", bg="#ac9152", bd=3, command=self.login)
        self.create_account_button = tk.Button(self.canvas, text="Create an Account", fg="black", bg="#ac9152", bd=3,
                                               command=self.create_account)


        self.register_button = tk.Button(self.registration_window, text="Register", fg="black", bg="#ac9152", bd=3,
                                         command=self.register)
        self.register_button.pack()

    def register(self):
        print("Registering a new account...")


class MainWindow:

    def __init__(self):
        self.current_image = None
        self.images = None
        self.photo_images = None
        self.arrow_image = None
        self.home_box = None
        self.home_btn = None
        self.canvas = None
        self.sidebar_frame = None
        self.arrow_button = None
        self.sidebar_state = "expanded"

        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Auctioneer App")
        self.root.wm_state('zoomed')
        self.root.option_add("*Font", "Helvetica 14")
        self.root.iconbitmap("logo0.4.ico")

        bg = PhotoImage(file="background.png")

        # root background
        background_label = Label(self.root, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # logo
        logo_img = ImageTk.PhotoImage(Image.open("logo0.4.png").resize((150, 150)))

        self.logo_canvas = tk.Canvas(self.root, width=160, height=160, bg='#1C1F25', highlightthickness=0)
        self.logo_canvas.place(x=10, y=10)

        self.logo_canvas.create_image(5, 5, anchor="nw", image=logo_img)
        # welcome back label
        self.welcome_label = tk.Label(self.root, text="Welcome Back, Michail", bg="#1C1F25", fg='white')
        self.welcome_label.place(x=250, y=25)

        # search box

        self.search_frame = tk.Canvas(self.root, width=330, height=40, bg='#1C1F25', highlightthickness=0)
        self.search_frame.place(x=550, y=20)

        search_img = Image.open("search.png")
        search_img = search_img.resize((25, 25))
        searchvec = ImageTk.PhotoImage(search_img)
        self.search_canvas = tk.Canvas(self.search_frame, width=30, height=40, bg="#1C1F25", highlightthickness=0)
        self.search_canvas.create_image(12.5, 12.5, image=searchvec)
        self.search_canvas.place(x=5, y=5)

        self.search_text = tk.StringVar(value="Search")
        self.search_entry = tk.Entry(self.search_frame, textvariable=self.search_text, width=80, fg="white",
                                     bg="#1c1f25",
                                     bd=0, insertbackground='white')
        self.search_entry.place(x=60, y=8)
        self.search_entry.bind("<FocusIn>", lambda event: self.search_text.set(""))
        self.search_entry.bind("<FocusOut>", lambda event: self.search_text.set("Search"))
        # User
        self.profile_frame = tk.Frame(self.root, width=400, height=40, bg='#1c1f25')
        self.profile_frame.place(x=1060, y=20)

        # available funds
        self.funds_label = tk.Label(self.profile_frame, text="143.50€", fg="white", bg="#1c1f25")
        self.funds_label.place(x=5, y=6)

        # wallet
        wallet_img = Image.open("wallet.png")
        wallet_img = wallet_img.resize((25, 25))
        walletvec = ImageTk.PhotoImage(wallet_img)
        self.wallet_canvas = tk.Canvas(self.profile_frame, width=30, height=30, bg="#1c1f25", highlightthickness=0)
        self.wallet_canvas.create_image(12.5, 12.5, image=walletvec)
        self.wallet_canvas.place(x=80, y=6)

        # profile line
        self.prof_line = tk.Canvas(self.profile_frame, width=0, height=40, highlightbackground="#ac9152")
        self.prof_line.place(x=110, y=0)

        # line
        x1, y1 = 0, 0
        x2, y2 = 0, 40
        self.prof_line.create_line(x1, y1, x2, y2)

        # notifications
        notif_img = Image.open("notif.png")
        notif_img = notif_img.resize((25, 25))
        notifvec = ImageTk.PhotoImage(notif_img)
        self.wallet_canvas = tk.Canvas(self.profile_frame, width=30, height=30, bg="#1c1f25", highlightthickness=0)
        self.wallet_canvas.create_image(12.5, 12.5, image=notifvec)
        self.wallet_canvas.place(x=120, y=6)

        # username
        self.username_label = tk.Label(self.profile_frame, text="Xionatos", bg="#1c1f25", fg="white")
        self.username_label.place(x=150, y=6)

        # profile picture
        prof_img = Image.open("mikeprof.png")
        prof_img = prof_img.resize((35, 35))
        profvec = ImageTk.PhotoImage(prof_img)
        self.profile_pic_canvas = tk.Canvas(self.profile_frame, height=30, width=30, bg="#ac9152", highlightthickness=2,
                                            highlightbackground="#ac9152")
        self.profile_pic_canvas.create_image(17.5, 17.5, image=profvec)
        self.profile_pic_canvas.place(x=260, y=3)

        # side nav menu
        self.sidebar_frame = tk.Frame(self.root, bg='#1c1f25')
        self.sidebar_frame.place(x=0, y=200, width=210, height=950)

        # Home
        home_image = PhotoImage(file="homepng.png")
        home_image = home_image.subsample(3, 3)
        self.home_button = Button(self.sidebar_frame, image=home_image, text='Home', anchor='w', compound='left',
                                  fg='white', padx=20,
                                  bg="#ac9152", activebackground="#ac9152", activeforeground='white', bd=0,
                                  highlightthickness=0, command=self.show_home_frame)
        self.home_button.place(x=0, y=0, width=250, height=70)

        # Browse Auctions
        browse_image = PhotoImage(file="browse.png")
        browse_image = browse_image.subsample(2, 2)
        self.browse_button = Button(self.sidebar_frame, image=browse_image, text='Browse Auctions', anchor='w',
                                    compound='left',
                                    fg='white', padx=20,
                                    bg="#1c1f25", activebackground="#ac9152", activeforeground='white', bd=0,
                                    highlightthickness=0, command=self.show_browse_frame)
        self.browse_button.place(x=0, y=70, width=250, height=70)

        # My Bids
        mybids_image = PhotoImage(file="mybids.png")
        mybids_image = mybids_image.subsample(2, 2)
        self.mybids_button = Button(self.sidebar_frame, image=mybids_image, text='My Bids', anchor='w', compound='left',
                                    fg='white', padx=20,
                                    bg="#1c1f25", activebackground="#ac9152", activeforeground='white', bd=0,
                                    highlightthickness=0, command=self.show_mybids_frame)
        self.mybids_button.place(x=0, y=140, width=250, height=70)
        # My Auctions
        myauctions_image = PhotoImage(file="myauctions.png")
        myauctions_image = myauctions_image.subsample(2, 2)
        self.myauctions_button = Button(self.sidebar_frame, image=myauctions_image, text='My Auctions', anchor='w',
                                        compound='left',
                                        fg='white', padx=20,
                                        bg="#1c1f25", activebackground="#ac9152", activeforeground='white', bd=0,
                                        highlightthickness=0, command=self.show_myauctions_frame)
        self.myauctions_button.place(x=0, y=210, width=250, height=70)

        # My Account
        myaccount_image = PhotoImage(file="myaccount.png")
        myaccount_image = myaccount_image.subsample(16, 16)
        self.myaccount_button = Button(self.sidebar_frame, image=myaccount_image, text='My Account', anchor='w',
                                       compound='left',
                                       fg='white', padx=20,
                                       bg="#1c1f25", activebackground="#ac9152", activeforeground='white', bd=0,
                                       highlightthickness=0, command=self.show_myaccount_frame)
        self.myaccount_button.place(x=0, y=280, width=250, height=70)

        # Log out
        logout_image = PhotoImage(file="logout.png")
        self.logout_button = Button(self.sidebar_frame, image=logout_image, text='Log Out', anchor='w',
                                    compound='left', fg='white', padx=20,
                                    bg="#1c1f25", activebackground="#ac9152", bd=0, highlightthickness=0,
                                    command=self.log_out)
        self.logout_button.place(x=0, y=350, width=250, height=70)

        # arrow button
        self.arrow_image = PhotoImage(file="arrowLeft.png")
        self.arrow_image = self.arrow_image.subsample(2, 2)
        self.arrow_button = Button(self.sidebar_frame, image=self.arrow_image, bg="#1c1f25", bd=0, highlightthickness=0,
                                   command=self.toggle_sidebar)
        self.arrow_button.place(x=180, y=450)

        # Home frame
        self.home_frame = tk.Frame(self.root, bg='#1c1f25')
        self.home_frame.place(x=220, y=80, width=1140, height=620)

        # location-live-bid

        def show_dropdown():
            dropdown_var = tk.StringVar(self.search_entry)
            dropdown = None

            if dropdown is not None:
                dropdown.destroy()

            def search_images(query):
                folder_path = "locations"

                matching_files = [f for f in os.listdir(folder_path) if query in f and f.endswith(".png")]

                return [os.path.join(folder_path, f) for f in matching_files]

            def set_image(image_path, label):
                self.loc_image = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))
                label.configure(image=self.loc_image)
                label.image = self.loc_image

            def update_dropdown():
                global dropdown_var, dropdown
                query = dropdown_var.get()
                image_paths = search_images(query)

                if dropdown is not None:
                    dropdown.destroy()

                dropdown_var.set('')
                dropdown = tk.OptionMenu(self.loc_changer, dropdown_var, *image_paths,
                                         command=lambda image_path: set_image(image_path, self.loc))

            self.search_entry = tk.Entry(self.loc_changer, textvariable=dropdown_var, width=30)
            self.search_entry.place(x=0, y=60)
            self.loc_search = tk.Button(self.loc_changer, text='Search', command=update_dropdown, width=10,
                                      height=10)
            self.loc_search.place(x=30, y=60)

        self.loc_image = ImageTk.PhotoImage(Image.open('locations/worldwide.png').resize((40, 40)))
        self.loc_changer = tk.Label(self.home_frame, bg='white', width=100, height=100)
        self.loc_changer.place(x=0, y=0)

        self.loc = tk.Label(self.loc_changer, image=self.loc_image, bg='grey', width=40, height=40)
        self.loc.pack(side='left')
        self.loc_button = tk.Button(self.loc_changer, text='▼', bg='white', bd=0, command=show_dropdown)
        self.loc_button.pack(side='left', padx=(5, 0))

        # live-bid
        staff_dir = "Staff"
        items_dir = "items"
        photo_images = []

        def create_bid_label():
            name = random.choice(
                ["John", "Jane", "Bob", "Sam", "Paul", "Chris", "Sasha", "Eli", "David", "Jonas", "Duke",
                 "Justin", "Mike", "Samuel", "Kirk", "Aaron", "Harrison", "De'Andre", "Anthony", "Byron",
                 "James", "Garret", "Ezra", "Brian", "Ed", "Ivan", "Andre"])  # random name
            profile_image_path = os.path.join(staff_dir, random.choice(os.listdir(staff_dir)))  # random profile image
            item_image_path = os.path.join(items_dir, random.choice(os.listdir(items_dir)))  # random item image
            price = f"{random.randint(1, 500)} €"  # random price

            profile_image = ImageTk.PhotoImage(Image.open(profile_image_path).resize((50, 50)))
            item_image = ImageTk.PhotoImage(Image.open(item_image_path).resize((30, 30)))
            photo_images.extend([profile_image, item_image])

            live_bid_frame = tk.Frame(self.home_frame, width=200, height=100, bg='#1C1F25')
            live_bid_frame.pack(side='right', anchor='ne', fill='x')
            bidon_frame = tk.Frame(live_bid_frame, width=200, height=100, bg='#1C1F25')
            bidon_frame.pack(side='right', anchor='nw', fill='x')

            bidon_label = tk.Label(bidon_frame, text=f"{name} bid {price} on:", fg='white', bg='#1C1F25')
            profile_label = tk.Label(bidon_frame, image=profile_image, bg='#1C1F25', highlightthickness=2,
                                     highlightbackground="#ac9152")
            item_label = tk.Label(bidon_frame, image=item_image, bg='#1C1F25')

            profile_label.pack(side="left", padx=5)
            bidon_label.pack(side="left", padx=5)
            item_label.pack(side="left", padx=5)

            self.root.after(15000, lambda: (live_bid_frame.destroy(), photo_images.pop(0), photo_images.pop(0)))

            # repeat every 5 seconds
            self.root.after(5000, create_bid_label)

        self.root.after(0, create_bid_label)

        # carousel
        self.carousel_frame = tk.Frame(self.home_frame, bg='#1c1f25')
        self.carousel_frame.place(x=10, y=60, width=1120, height=320)

        trend0 = ImageTk.PhotoImage(Image.open("Auctions/trending/trend0.png").resize((220, 220)))
        trend1 = ImageTk.PhotoImage(Image.open("Auctions/trending/trend1.jpg").resize((220, 220)))
        trend2 = ImageTk.PhotoImage(Image.open("Auctions/trending/trend2.png").resize((220, 220)))
        trend3 = ImageTk.PhotoImage(Image.open("Auctions/trending/trend3.jpg").resize((220, 220)))
        trend4 = ImageTk.PhotoImage(Image.open("Auctions/trending/trend4.png").resize((220, 220)))
        trend5 = ImageTk.PhotoImage(Image.open("Auctions/trending/trend5.png").resize((220, 220)))
        trend_list = [trend0, trend1, trend2, trend3, trend4, trend5]

        self.trend_count = 2

        def carousel_right():
            self.trend_count = (self.trend_count + 1) % len(trend_list)
            trend_left.config(image=trend_list[(self.trend_count - 1) % len(trend_list)])
            trend_centerl.config(image=trend_list[self.trend_count])
            trend_centerr.config(image=trend_list[(self.trend_count + 1) % len(trend_list)])
            trend_right.config(image=trend_list[(self.trend_count + 2) % len(trend_list)])

        def carousel_left():
            self.trend_count = (self.trend_count - 1) % len(trend_list)
            trend_left.config(image=trend_list[(self.trend_count - 1) % len(trend_list)])
            trend_centerl.config(image=trend_list[self.trend_count])
            trend_centerr.config(image=trend_list[(self.trend_count + 1) % len(trend_list)])
            trend_right.config(image=trend_list[(self.trend_count + 2) % len(trend_list)])

        trend_left = Label(self.carousel_frame, image=trend1)
        trend_left.place(x=40, y=85, width=220, height=220)
        trend_centerl = Label(self.carousel_frame, image=trend2)
        trend_centerl.place(x=300, y=80, width=220, height=210)
        trend_centerr = Label(self.carousel_frame, image=trend3)
        trend_centerr.place(x=580, y=80, width=220, height=210)
        trend_right = Label(self.carousel_frame, image=trend4)
        trend_right.place(x=850, y=85, width=220, height=220)
        self.trend_left = tk.Button(self.carousel_frame, text="<", command=carousel_left)
        self.trend_left.pack(side=tk.LEFT)
        self.trend_right = tk.Button(self.carousel_frame, text=">", command=carousel_right)
        self.trend_right.pack(side=tk.RIGHT)

        # trending
        self.trending_frame = tk.Frame(self.carousel_frame, bg='#1c1f25', padx=10, pady=10)
        self.trending_frame.pack(side='top')

        # Load the left and right images
        fire = ImageTk.PhotoImage(Image.open("fire.png").resize((50, 50)))
        trendup = ImageTk.PhotoImage(Image.open("trendup.png").resize((50, 50)))

        self.trend_l_label = tk.Label(self.trending_frame, bg='#1c1f25', image=fire)
        self.trend_l_label.pack(side='left')
        self.trend_r_label = tk.Label(self.trending_frame, bg='#1c1f25', image=trendup)
        self.trend_r_label.pack(side='right')

        text_label = tk.Label(self.trending_frame, text='Trending Auction', font=('Arial', 20), fg='white',
                              bg='#1c1f25')
        text_label.pack(side='left', padx=(10, 0))
        # Browse frame
        self.browse_frame = tk.Frame(self.root, bg='black')
        self.browse_frame.place(x=2250, y=100, width=1100, height=600)
        self.browse_label = tk.Label(self.browse_frame, text='Browse Auctions Page (TBD)', font=('Helvetica', 36),
                                     bg='black', fg='white')
        self.browse_label.pack(side=TOP, padx=200, pady=200)

        # MyBids frame
        self.mybids_frame = tk.Frame(self.root, bg='black')
        self.mybids_frame.place(x=2250, y=100, width=1100, height=600)
        self.mybids_label = tk.Label(self.mybids_frame, text='My Bids Page (TBD)', font=('Helvetica', 36),
                                     bg='black', fg='white')
        self.mybids_label.pack(side=TOP, padx=200, pady=200)
        # MyAuctions frame
        self.myauctions_frame = tk.Frame(self.root, bg='black')
        self.myauctions_frame.place(x=2250, y=100, width=1100, height=600)
        self.myauctions_label = tk.Label(self.myauctions_frame, text='My Auctions Page (TBD)', font=('Helvetica', 36),
                                         bg='black', fg='white')
        self.myauctions_label.pack(side=TOP, padx=200, pady=200)
        # MyAccount frame
        self.myaccount_frame = tk.Frame(self.root, bg='black')
        self.myaccount_frame.place(x=2250, y=100, width=1100, height=600)
        self.myaccount_label = tk.Label(self.myaccount_frame, text='My Account Page (TBD)', font=('Helvetica', 36),
                                        bg='black', fg='white')
        self.myaccount_label.pack(side=TOP, padx=200, pady=200)
        self.root.mainloop()

    def show_home_frame(self):
        self.browse_frame.place(x=2250, y=100)
        self.browse_button.configure(bg='#1c1f25')
        self.mybids_frame.place(x=2250, y=100)
        self.mybids_button.configure(bg='#1c1f25')
        self.myauctions_frame.place(x=2250, y=100)
        self.myauctions_button.configure(bg='#1c1f25')
        self.myaccount_frame.place(x=2250, y=100)
        self.myaccount_button.configure(bg='#1c1f25')

        self.home_frame.place(x=250, y=100)
        self.home_button.configure(bg='#ac9152')

    def show_browse_frame(self):
        self.home_frame.place(x=2250, y=100)
        self.home_button.configure(bg='#1c1f25')
        self.mybids_frame.place(x=2250, y=100)
        self.mybids_button.configure(bg='#1c1f25')
        self.myauctions_frame.place(x=2250, y=100)
        self.myauctions_button.configure(bg='#1c1f25')
        self.myaccount_frame.place(x=2250, y=100)
        self.myaccount_button.configure(bg='#1c1f25')

        # show frame
        self.browse_frame.place(x=250, y=100)
        self.browse_button.configure(bg='#ac9152')

    def show_mybids_frame(self):
        self.home_frame.place(x=2250, y=100)
        self.home_button.configure(bg='#1c1f25')
        self.browse_frame.place(x=2250, y=100)
        self.browse_button.configure(bg='#1c1f25')
        self.myauctions_frame.place(x=2250, y=100)
        self.myauctions_button.configure(bg='#1c1f25')
        self.myaccount_frame.place(x=2250, y=100)
        self.myaccount_button.configure(bg='#1c1f25')

        # show frame
        self.mybids_frame.place(x=250, y=100)
        self.mybids_button.configure(bg='#ac9152')

    def show_myauctions_frame(self):
        self.home_frame.place(x=2250, y=100)
        self.home_button.configure(bg='#1c1f25')
        self.browse_frame.place(x=2250, y=100)
        self.browse_button.configure(bg='#1c1f25')
        self.mybids_frame.place(x=2250, y=100)
        self.mybids_button.configure(bg='#1c1f25')
        self.myaccount_frame.place(x=2250, y=100)
        self.myaccount_button.configure(bg='#1c1f25')

        self.myauctions_frame.place(x=250, y=100)
        self.myauctions_button.configure(bg='#ac9152')

    def show_myaccount_frame(self):
        self.home_frame.place(x=2250, y=100)
        self.home_button.configure(bg='#1c1f25')
        self.browse_frame.place(x=2250, y=100)
        self.browse_button.configure(bg='#1c1f25')
        self.mybids_frame.place(x=2250, y=100)
        self.mybids_button.configure(bg='#1c1f25')
        self.myauctions_frame.place(x=2250, y=100)
        self.myauctions_button.configure(bg='#1c1f25')

        self.myaccount_frame.place(x=250, y=100)
        self.myaccount_button.configure(bg='#ac9152')

    def toggle_sidebar(self):
        if self.sidebar_state == "expanded":
            # Minimize sidebar
            self.sidebar_frame.place(x=0, y=200, width=60, height=950)
            self.arrow_image = PhotoImage(file="arrowRight.png")
            self.arrow_image = self.arrow_image.subsample(2, 2)
            self.arrow_button = Button(self.sidebar_frame, image=self.arrow_image, bg="#1c1f25", bd=0,
                                       highlightthickness=0,
                                       command=self.toggle_sidebar)
            self.arrow_button.place(x=25, y=450)

            self.sidebar_state = "minimized"
        else:
            # Expand sidebar
            self.sidebar_frame.place(x=0, y=200, width=210, height=950)
            self.arrow_image = PhotoImage(file="arrowLeft.png")
            self.arrow_image = self.arrow_image.subsample(2, 2)
            self.arrow_button = Button(self.sidebar_frame, image=self.arrow_image, bg="#1c1f25", bd=0,
                                       highlightthickness=0,
                                       command=self.toggle_sidebar)
            self.arrow_button.place(x=180, y=450)
            self.sidebar_state = "expanded"

    def log_out(self):
        self.root.destroy()
        root = tk.Tk()
        login_window = LoginWindow(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()  # create the root window
    login_window = LoginWindow(root)

    root.mainloop()
