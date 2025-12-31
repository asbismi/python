
receipt = "BOOKSTORE RECEIPT\n\t-------------------\n"

book1_title = "Python Basics"
book1_price = 450

book2_title = "Data Science Intro"
book2_price = 600

receipt += "\t{}:\t₹{}\n".format(book1_title, book1_price)
receipt += "\t{}:\t₹{}\n".format(book2_title, book2_price)

total_price = book1_price + book2_price

receipt += "\t-------------------\n"
receipt += "\tTOTAL:\t₹{}\n".format(total_price)

receipt += "\n\tThank you for shopping with us!"

print(receipt.upper())
