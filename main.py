voucher_list = {
    "jgm95mgn": "True",
    "Rga0Jpq3": "True",
    "rqzaOlBX": "True",
    "rqzlVba1": "True",
    "rqzrrYpq": "True",
    "rqzk6OgX": "True",
    "rqz07a1X": "True",
    "rqz34rYpq": "True",
    "rqz78QgX": "True",
    "r3478QgX": "True",
    "r50z78QgX": "True",

}

voucher_count = len(voucher_list)
print(voucher_count)


user_key = "1-rqz07a1X"

counting_voucher = 0
for y in voucher_list:
    counting_voucher += 1
    if y == user_key:
        counting_voucher -= 1
        print("found key")
        with open('vouchercodes.txt', 'r')  as r:
            reading = r.readlines()
            print(reading)
            length = len(reading)

        for i in reading:
            take = i.strip()
            count +=1
            # print(take)
            if user_key in take:
                print("redeemed BEFORE   " + user_key)
                break

            else:
                if count == length:
                    with open("vouchercodes.txt", 'a') as e:
                        # e.write(user_key+"\n")
                        e.write("{}\n".format(user_key))
                        print("CODE REDEEM SUCCESSFULLY")
                        break

    elif counting_voucher == 10:
        # print("this is an invalid key")
        print("this is an invalid key")






