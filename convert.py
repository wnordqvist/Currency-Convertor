#CurrencyConverter.py
import requests
import json
from tkinter import *

# Create window 
root=Tk()
root.geometry("300x280")
#places window in the center of the screen
root.eval('tk::PlaceWindow . center')
root.title('Currency converter')

# creating global variables 
fromCurrency = StringVar(root) 
toCurrency = StringVar(root) 

# initializing variables for currencies
fromCurrency.set("currency") 
toCurrency.set("currency") 

	
# Function to perform real time conversion from two different currencies
def RealTimeCurrencyConversion(): 

	# currency code 
	from_currency = fromCurrency.get() 
	to_currency = toCurrency.get() 

	# enter your api key here 
	#api_key = "https://rapidapi.com/fyhao/api/currency-exchange"
	
	# base_url variable store base url 
	base_url = r"https://rapidapi.com/fyhao/api/currency-exchange"

	# main_url variable store complete url 
	main_url = base_url + "&from_currency =" + from_currency +"&to_currency =" + to_currency

	# get method of requests module 
	# return response object 
	req_ob = requests.get(main_url) 

	# json method return json format 
	# data into python dictionary data type. 
	
	# result contains list of nested dictionaries 
	result = req_ob.json() 

	# parsing information 
	Exchange_Rate = float(result["Realtime Currency Exchange Rate"]
	 ['5. Exchange Rate']) 

	# get method of Entry widget 
	# returns current text as a 
	# string from text entry box. 
	amount = float(fromCurrency_field.get()) 

	# calculation for the conversion 
	new_amount = round(amount * Exchange_Rate, 3) 

	# insert method inserting the 
	# value in the text entry box. 
	convertedAmount_field.insert(0, str(new_amount)) 


# Function to clear entry fields
def clear_all() : 
	fromCurrency_field.delete(0, END) 
	convertedAmount_field.delete(0, END) 
	

# Driver code 
if __name__ == "__main__" : 

	# Create a "From Currency :" label 
	fromCurrency_label = Label(root, text = "From Currency: ", fg = 'black', bg = 'lightblue') 
	fromCurrency_label.place(x=80, y=30, anchor='center')

	# Create a "To Currency: " label 
	toCurrency_label = Label(root, text = "To Currency: ", fg = 'black', bg = 'lightblue') 
	toCurrency_label.place(x = 220, y = 30, anchor='center') 

	# list of currency codes 
	CurrenyCode_list = ["SEK", "USD", "EUR"]

	# create a drop down menu using OptionMenu function 
	FromCurrency_dropdown = OptionMenu(root, fromCurrency, *CurrenyCode_list)
	FromCurrency_dropdown.place(x = 80, y = 60, anchor='center')

	ToCurrency_option = OptionMenu(root, toCurrency, *CurrenyCode_list) 
	ToCurrency_option.place(x = 220, y = 60, anchor='center') 

	# Create Amount label 
	amount_label = Label(root, text = "Amount: ", fg = 'black', bg = 'lightgray') 
	amount_label.place(x = 60, y = 100, anchor='center')

	#Create a text entry box
	fromCurrency_field = Entry(root, font='Arial 12')
	fromCurrency_field.place(x = 200, y = 100, anchor='center') 

	# Button for conversion using RealTimeCurrencyExchangeRate function
	btnConvert = Button(root, text = "Convert", command = RealTimeCurrencyConversion, width=10) 
	btnConvert.place(x = 140, y = 140, anchor='center')

	# Create a "Converted Amount :" label 
	convertedAmount_label = Label(root, text = "Converted Amount :", fg = 'black', bg = 'lightblue') 
	convertedAmount_label.place(x = 140, y = 180, anchor='center')

	convertedAmount_field = Entry(root, font='Arial 12') 
	convertedAmount_field.place(x = 140, y = 220, anchor='center') 
	convertedAmount_field.configure(state='disabled')

	
	# Button for clearing all input fields
	btnClear = Button(root, text = "Clear",width=10, command = clear_all) 
	btnClear.place(x = 140, y = 255, anchor='center')
	
	# Start the GUI 
	root.mainloop() 
