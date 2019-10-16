#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program checks checks if the
#   user's package is accepted


def main():
    # This function checks if user's package is accepted

    # input
    print("Welcome to CNL Delivery.")
    print("Please fill in the following for acceptance. ")
    print("")
    weight_as_string = input("Please enter the weight of your package (kg): ")

    # process
    try:
        weight = int(weight_as_string)
        if weight <= 27 and weight >= 0:
            # output
            length_as_string = input("Please enter the length of your"
                                     " package (cm): ")
            width_as_string = input("Please enter the width of your"
                                    " package (cm): ")
            height_as_string = input("Please enter the height of your"
                                     " package (cm): ")
            print("")

            # output
            try:
                length = int(length_as_string)
                width = int(width_as_string)
                height = int(height_as_string)
                # process
                volume = (length*width*height)
                if volume <= 10000 and volume > 0:
                    print("Volume: {} cm^3".format(volume))
                    print("")
                    print("Your package is accepted for delivery.")
                    print("Thank you for choosing CNL Delivery. "
                          "Until next time.")
                else:
                    print("Unfortunately, we can not accept "
                          "your package as it does not meet the"
                          " optimal volume of 10,000cm^3 and under.")
            except ValueError:
                print("Wrong input. Try again.")
        else:
            print("")
            print("Unfortunately, we can not accept your package as it"
                  " does not meet the optimal weight of 27 kg and under.")
    except ValueError:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
