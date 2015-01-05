def intro_string(ticker):
    return "The following variables will help you with performing a" \
           " fundamental analysis of the company you are researching, " \
           "as well as assessing the true value of that company's stock. " \
           "So, by the numbers, just how cheap or expensive is" + ticker + "really?"


def days_of_sales_outstanding(ticker, days_of_sales_outstanding,
                              industry_days_of_sales_outstanding):
    text = ticker + "'s average collection period for the length of time it takes " \
                    "the company's customers to pay their bills is %s days." + \
                    "Since this average collection period is" % days_of_sales_outstanding

    if days_of_sales_outstanding > .8 * industry_days_of_sales_outstanding:
        if days_of_sales_outstanding < 1.2 * industry_days_of_sales_outstanding:
            text += "close to the industry norm, the firm is extending just enough credit" \
                    " to its customers to maximize sales and is in a desirable position."

    elif .8 * industry_days_of_sales_outstanding > days_of_sales_outstanding:
        text += "well below the industry norm, the firm might not be extending enough credit" \
                " to its customers and this rigid credit policy may actually be limiting %s's" \
                " sales, ultimately reducing the firm's profitability." % ticker

