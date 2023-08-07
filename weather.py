from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


'''GeoPy

from geopy.geocoders import Nominatim

def get_location_coordinates(location):
    geolocator = Nominatim(user_agent="my_geocoder")
    try:
        # Geocode the location input
        location_data = geolocator.geocode(location)
        if location_data:
            latitude, longitude = location_data.latitude, location_data.longitude
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        print("Error:", e)
        return None, None

def main():
    user_input = input("Enter a location: ")
    latitude, longitude = get_location_coordinates(user_input)

    if latitude is not None and longitude is not None:
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Location not found or geocoding failed.")

if __name__ == "__main__":
    main()'''

''' TimeZoneFinder.
timezonefinder works by utilizing shapefiles that define the boundaries of different time zones across the globe. 
These shapefiles contain geographical coordinates that outline the boundaries of each time zone. When you provide a 
latitude and longitude to timezonefinder, the library checks which time zone boundary the location falls within and
 hbf sarEQ  zreturns the corresponding time zone identifier.
def get_time_zone(latitude,longitude):
    tz_finder= TimezoneFinder()
    time_zone_str= tz_finder.timezone_at(lng=longitude, lat=latitude)
    return time_zone_str

latitude= 22.4337924
longitude= 91.7403944
time_zone= get_time_zone(latitude,longitude)

if time_zone:
    print(f"The time zone at ({latitude},{longitude}) is {time_zone}.")
else:
    print("Time zone not found for the given location.")'''

root= Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city= textfield.get()

        geolocator= Nominatim(user_agent="geopiExercises")
        location= geolocator.geocode(city)
        obj= TimezoneFinder()
        result= obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M: %p:")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

    # weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data= requests.get(api).json()
        condition= json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp= int(json_data['main']['temp']-273.15)
        pressure= json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind= json_data['wind']['speed']

        t.config(text=(temp,"°"))
        t.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"), font=("arial", 25, "bold"))


        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!")


#search Box
Search_image = PhotoImage(file="search_box.png")
myimage= Label(image=Search_image)
myimage.place(x=20,y=20)

textfield= tk.Entry(root,justify="center",width=17, font=("poppins",25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon= PhotoImage(file='search.png')
myimage_icon= Button(image=Search_icon,borderwidth=0, cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

#logo
Logo_iage= PhotoImage(file="logo.png")
logo=Label(image=Logo_iage)
logo.place(x=150,y=100)

#Bottom Box
Frame_image= PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5, side=BOTTOM)

#time
name= Label(root,font=("arial", 15, "bold"))
name.place(x=20, y=100)
clock=Label(root,font=("Helvetica",20,"bold"))
clock.place(x=20, y=130)

#label
label1= Label(root,text="Wind",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label1.place(x=120,y=400)

label2= Label(root,text="Humidity",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label2.place(x=250,y=400)

label3= Label(root,text="Description",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label3.place(x=430,y=400)

label4= Label(root,text="Pressure",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label4.place(x=650,y=400)

t= Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400, y=150)
c=Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)

p= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)


root.mainloop()
