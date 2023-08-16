# voucher-genator-checker
Stupid 😅 local voucher generator and checker....

#Not much going on..Just have the neccessary txt file put in name..

#DOCUMENTING OUR VOUCHER CODE
#voucher_list =>  contains basically our active voucher db code that is the mother for cross checking wether a voucher code is valid or not
#We created a for loop to iterate on our voucher list
#an if statement inside the for loop to cross check wether the user input for the voucher contains in voucher_list or not
#if it doesn't we our counting_voucher to counter again'st all the data on our voucher_list to check if exsit or not
#if it doesn't exsist we print our "this is an invalid key to the user to known"
#if reverse was the case we continue
#we open our voucher txt named [ vouchercodes.txt ] that contains all the code that has been redeem so far
#We read it using python readlines and strip to convert the lines in the txt file appropriately
#then we inititae a count that will be counting each sequence of voucher that iterate over our vouchercode.txt file to cross check wether the users input has been redeem or not
#basically this is where we check wether our voucher is redeem or not after checking the validity of the code
#if user_key in take: to check --- if true we break out of the for loop
#if false we keep counting until until all empty on the voucher_list
#then we write the code over to our vouchercode.txt then print to the users code has been redeeemed

