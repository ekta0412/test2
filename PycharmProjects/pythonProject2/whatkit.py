import pywhatkit as pw   # import pywhatkit and flask


a ='''There are times when u dont feel good about yourself
     But sometimes its ok'''

#pw.text_to_handwriting( a ) ----It did not work

pw.sendwhatmsg("+919810666378","Hi Cutie...This is send from Python, Golu,Tinde,Rabbit",10,23)

#pw.sendwhatmsg("+919810666030","Hi Browser will close after 5 secs since True is mentioned",10,46,True)---did not work

pw.sendwhatmsg_to_group("sisis","Hey there",11,9)
#pw.sendwhats_image("+919810666030","Media/tipu.jpg") Did not work

pw.playonyt("moosewala")  # searches on you tube

pw.search("water") # searches on google

print("END OF FILE")