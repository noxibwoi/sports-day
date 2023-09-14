from typing import Optional, Tuple, Union
import customtkinter

list1 = ['shotput','highjump','longjump','100m','200m','4x100m']

class homepage(customtkinter.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Home")
        self.geometry('1200x800')

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=250,)
        self.tabview.grid(row=0,column=0,rowspan=4,columnspan=4,sticky="nsew")
        
        self.tabview.add("Sub Juniors")
        self.tabview.add("Juniors")
        self.tabview.add("Seniors")
        self.tabview.add('Super Seniors')

        def tabwidgets(age_group,event_list):

            self.tabview.tab(age_group).grid_columnconfigure((0,1,2,3), weight=1)
            self.tabview.tab(age_group).grid_rowconfigure((0,1,2,3,4,5), weight=1)

            gender_title = customtkinter.CTkLabel(self.tabview.tab(age_group),text='Gender')
            gender_title.grid(row=1,column=0)
            gender = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=['Male','Female'],width=150, height = 50)
            gender.set('Select Gender')
            gender.grid(row=2,column=0)

            event_title = customtkinter.CTkLabel(self.tabview.tab(age_group),text='Event')
            event_title.grid(row=1,column=1)
            event = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=event_list,width=150, height = 50)
            event.set('Select Event')
            event.grid(row=2,column=1)

            first_title = customtkinter.CTkLabel(self.tabview.tab(age_group),text='First')
            first_title.grid(row=1,column=2)
            first = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=event_list,width=150, height = 50)
            first.set('First Place')
            first.grid(row=1,column=3)
            first_house = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=['Aravaly','Satpura','Shivalik','Vindhya'],width=150, height = 50)
            first_house.set('House')
            first_house.grid(row=1,column=4)

            second_title = customtkinter.CTkLabel(self.tabview.tab(age_group),text='Second')
            second_title.grid(row=2,column=2)
            second = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=event_list,width=150, height = 50)
            second.set('Second Place')
            second.grid(row=2,column=3)
            second_house = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=['Aravaly','Satpura','Shivalik','Vindhya'],width=150, height = 50)
            second_house.set('House')
            second_house.grid(row=2,column=4)

            third_title = customtkinter.CTkLabel(self.tabview.tab(age_group),text='Third')
            third_title.grid(row=3,column=2)
            third = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=event_list,width=150, height = 50)
            third.set('Third Place')
            third.grid(row=3,column=3)   
            third_house = customtkinter.CTkOptionMenu(self.tabview.tab(age_group),values=['Aravaly','Satpura','Shivalik','Vindhya'],width=150, height = 50)
            third_house.set('House')
            third_house.grid(row=3,column=4)     


            submit_button = customtkinter.CTkButton(self.tabview.tab(age_group),text='Submit',width=150, height = 50)
            submit_button.place(relx=.50, rely=.95, anchor='center')
        


        tabwidgets("Sub Juniors",list1)
        tabwidgets("Juniors",list1)
        tabwidgets("Seniors",list1)
        tabwidgets("Super Seniors",list1)


mainwindow = homepage()
mainwindow.mainloop()