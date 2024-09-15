import geocoder
from geopy.geocoders import Nominatim
import datetime
from astropy.time import Time
from tkinter import Tk, Label

def get_gmt():
    return datetime.datetime.utcnow()

def get_location():
    # Automatically get your location using your IP address
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng[0], g.latlng[1]
    else:
        return None, None

def calculate_julian_day():
    return Time(datetime.datetime.utcnow()).jd

def calculate_sidereal_time(longitude):
    now = Time(datetime.datetime.utcnow())
    gst = now.sidereal_time('mean', 'greenwich').degree
    if longitude is not None:
        lst = (gst + longitude) % 360
        return lst / 15  # Convert to hours
    else:
        return None

def update_widget():
    gmt = get_gmt().strftime('%Y-%m-%d %H:%M:%S')
    latitude, longitude = get_location()
    julian_day = calculate_julian_day()
    sidereal_time = calculate_sidereal_time(longitude)
    
    label_gmt.config(text=f"GMT: {gmt}")
    if latitude is not None and longitude is not None:
        label_location.config(text=f"Location: {latitude:.4f}, {longitude:.4f}")
        label_sidereal.config(text=f"Sidereal Time: {sidereal_time:.4f} hrs")
    else:
        label_location.config(text="Location: Not Found")
        label_sidereal.config(text="Sidereal Time: N/A")
    label_julian.config(text=f"Julian Day: {julian_day:.5f}")

    root.after(1000, update_widget)

root = Tk()
root.title("Astronomy Widget")

label_gmt = Label(root, font=("Helvetica", 16))
label_gmt.pack()

label_location = Label(root, font=("Helvetica", 16))
label_location.pack()

label_julian = Label(root, font=("Helvetica", 16))
label_julian.pack()

label_sidereal = Label(root, font=("Helvetica", 16))
label_sidereal.pack()

update_widget()
root.mainloop()
