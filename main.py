import coefficient_acm
import coefficient_alpha
import coefficient_ethereum
import matplotlib.pyplot as plt


def main():

    # Modules have functions to calculate the coefficients values
    value_from_a = coefficient_alpha.coefficient_alpha()  
    value_from_b = coefficient_acm.coefficient_acm() 
    value_from_c = coefficient_ethereum.coefficient_ethereum()     

    # Token names and their corresponding engagement coefficients
    tokens = ['Alpha', 'ACM', 'Ethereum']
    coefficients = [value_from_a, value_from_b , value_from_c]

    plt.figure(figsize=(8, 6))
    plt.bar(tokens, coefficients, color=['blue', 'green' , 'orange'])
    plt.title('Engagement Coefficients of Tokens')
    plt.xlabel('Tokens')
    plt.ylabel('Engagement Coefficient')
    plt.show()

if __name__ == "__main__":
    main()