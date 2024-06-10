# ARANweather

These files were in preparation for a ML model using Iowa State University's ARAN rural wireless network. Multiple sensors on the network have the ability to take detailed readings of weather and power parameters. The concept was to pull these readings and feed them to a ML model baselining optimal conditions. This work is mine and all code has been developed by me, the data is derived from IAState equipment and software.

## Code descriptions.
1. **wx_pwr.json** is an example of the weather data pulled from Wilson Hall.
2. **wx_pwr.py** is the method to automate the data pulls.
3. **wx_pwrtest.json** is the end result of the aggregated data set.
4. **data_cond.py** is an attempt to condition the data to be ingested into the ML model and output the Mean Squared Error (MSE) to baseline.
