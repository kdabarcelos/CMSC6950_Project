#Task 2 (ACF example 2): analyze seasonal keyword trends, such as 'gym', 'weight', 'diet', 'money', and 'travel' using its time autocorrelation function (acf) from its time series.

#About this script
        #It generates an intermediate file with acf results from bond length

#Run command-line [python3 script.py output_file_name.txt]
        #Example: $python3 create_acf_keyword_trends.py acf_keyword_trends.txt

#Where the input data are from?
	#The keyword data denote values calculated on a scale from 0 to 100, where 100 is the location with the most popularity 
	#as a fraction of total searches in that location, a value of 50 indicates a location which is half as popular. 
	#A value of 0 indicates a location where there was not enough data for this term.


# import modules - the TrendReq method from the pytrends request module
from pytrends.request import TrendReq
import pandas as pd
import tidynamics
import sys

args = sys.argv[1:]
output = args[0]

#defining main funtion
def main(output):
    '''
    Create intermediate file with dates, keywords popularity (scale from 0 to 100), and ACF of each keyword
    '''

    # execute the TrendReq method by passing the host language (hl) and timezone (tz) parameters
    pytrends = TrendReq(hl='en-CA', tz=360)

    # build list of keywords
    kw_list = ['diet', 'gym','weight','travel','money'] 

    # build the payload
    pytrends.build_payload(kw_list, timeframe='2004-01-01 2019-12-31', geo='CA')

    # store interest over time information in df
    df = pytrends.interest_over_time()

    #create columns and apply acf
    df["diet_autocorr"] = (tidynamics.acf(df[["diet"]]) / float(tidynamics.acf(df[["diet"]]).max()))
    df["gym_autocorr"] = (tidynamics.acf(df[["gym"]]) / float(tidynamics.acf(df[["gym"]]).max()))
    df["weight_autocorr"] = (tidynamics.acf(df[["weight"]]) / float(tidynamics.acf(df[["weight"]]).max()))
    df["travel_autocorr"] = (tidynamics.acf(df[["travel"]]) / float(tidynamics.acf(df[["travel"]]).max()))
    df["money_autocorr"] = (tidynamics.acf(df[["money"]]) / float(tidynamics.acf(df[["money"]]).max()))

    #save output with comma delimiter and headers
    df.to_csv(output, index=False)

if __name__ == "__main__":
    main(output)
