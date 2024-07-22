# Define the Stock class
class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

# Main function to create a Stock instance and display information
def main():
    # Create a Stock instance for Microsoft
    microsoft_stock = Stock("MSFT", "Microsoft")
    
    # Display the symbol and company name
    print("Company:", microsoft_stock.get_company_name())
    print("Symbol:", microsoft_stock.get_symbol())

if __name__ == "__main__":
    main()
