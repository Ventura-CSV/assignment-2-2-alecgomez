def main():

    celcius = (int(input('Enter a temperature in Celsius: ')))

    fahrenheit = (celcius * 1.8 + 32)

    print(f'Fahrenheit: {fahrenheit:.2f}')

    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
