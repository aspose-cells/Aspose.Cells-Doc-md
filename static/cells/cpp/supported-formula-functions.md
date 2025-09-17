##Supported Excel Functions with C++
Supported Excel functions for reading, setting, and calculating formulas using Aspose.Cells with C++.
Aspose.Cells APIs support most of the standard functions and Excel's built-in formulas. Below, you can find all the supported functions in alphabetical order.
| | | | | | | | | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **[A](#a)** | **[B](#b)** | **[C](#c)** | **[D](#d)** | **[E](#e)** | **[F](#f)** | **[G](#g)** | **[H](#h)** | **[I](#i)** | **[J](#j)** | **[K](#k)** | **[L](#l)** | **[M](#m)** |
| **[N](#n)** | **[O](#o)** | **[P](#p)** | **[Q](#q)** | **[R](#r)** | **[S](#s)** | **[T](#t)** | **[U](#u)** | **[V](#v)** | **[W](#w)** | **[X](#x)** | **[Y](#y)** | **[Z](#z)** |
Aspose.Cells' Formula Calculation Engine allows you to set, read, and calculate the results of the following formulas and functions.
###### **A**
|**Function**|**Summary**|
| :- | :- |
|ABS|**Math and trigonometry**: Returns the absolute value of a number
|ACCRINT|**Financial**: Returns the accrued interest for a security that pays periodic interest
|ACCRINTM|**Financial**: Returns the accrued interest for a security that pays interest at maturity
|ACOS|**Math and trigonometry**: Returns the arccosine of a number
|ACOSH|**Math and trigonometry**: Returns the inverse hyperbolic cosine of a number
|ADDRESS|**Lookup and reference**: Returns a reference as text to a single cell in a worksheet
|AGGREGATE|**Math and trigonometry**: Returns an aggregate in a list or database
|AMORDEGRC|**Financial**: Returns the depreciation for each accounting period by using a depreciation coefficient
|AMORLINC|**Financial**: Returns the depreciation for each accounting period
|ANCHORARRAY|**Lookup and reference**: Returns the entire spilled range for the dynamic array in cell
|AND|**Logical**: Returns TRUE if all of its arguments are TRUE
|AREAS|**Lookup and reference**: Returns the number of areas in a reference
|ARRAYTOTEXT|**Text**: Returns an array of text values from any specified range
|ASC|**Text**: Changes full-width (double-byte) English letters or katakana within a character string to half-width (single-byte) characters
|ASIN|**Math and trigonometry**: Returns the arcsine of a number
|ASINH|**Math and trigonometry**: Returns the inverse hyperbolic sine of a number
|ATAN|**Math and trigonometry**: Returns the arctangent of a number
|ATAN2|**Math and trigonometry**: Returns the arctangent from x- and y-coordinates
|ATANH|**Math and trigonometry**: Returns the inverse hyperbolic tangent of a number
|AVEDEV|**Statistical**: Returns the average of the absolute deviations of data points from their mean
|AVERAGE|**Statistical**: Returns the average of its arguments
|AVERAGEA|**Statistical**: Returns the average of its arguments, including numbers, text, and logical values
|AVERAGEIF|**Statistical**: Returns the average (arithmetic mean) of all the cells in a range that meet a given criteria
|AVERAGEIFS|**Statistical**: Returns the average (arithmetic mean) of all cells that meet multiple criteria.
###### **B**
|**Function**|**Summary**|
| :- | :- |
|BESSELI|**Engineering**: Returns the modified Bessel function In(x)
|BESSELJ|**Engineering**: Returns the Bessel function Jn(x)
|BESSELK|**Engineering**: Returns the modified Bessel function Kn(x)
|BESSELY|**Engineering**: Returns the Bessel function Yn(x)
|BETADIST|**Compatibility**: Returns the beta cumulative distribution
|BETA.DIST|**Statistical**: Returns the beta cumulative distribution
|BETAINV|**Compatibility**: Returns the inverse of the cumulative distribution function for a specified beta distribution
|BETA.INV|**Statistical**: Returns the inverse of the cumulative distribution function for a specified beta distribution
|BIN2DEC|**Engineering**: Converts a binary number to decimal
|BIN2HEX|**Engineering**: Converts a binary number to hexadecimal
|BIN2OCT|**Engineering**: Converts a binary number to octal
|BINOMDIST|**Compatibility**: Returns the individual term binomial distribution probability
|BINOM.DIST|**Statistical**: Returns the individual term binomial distribution probability
|BITAND|**Engineering**: Returns a 'Bitwise And' of two numbers
|BITLSHIFT|**Engineering**: Returns a value number shifted left by shift_amount bits
|BITOR|**Engineering**: Returns a bitwise OR of 2 numbers
|BITRSHIFT|**Engineering**: Returns a value number shifted right by shift_amount bits
|BITXOR|**Engineering**: Returns a bitwise 'Exclusive Or' of two numbers
|BYCOL|**Logical**: Applies a LAMBDA to each column and returns an array of the results
|BYROW|**Logical**: Applies a LAMBDA to each row and returns an array of the results
###### **C**
|**Function**|**Summary**|
| :- | :- |
|CEILING|**Compatibility**: Rounds a number to the nearest integer or to the nearest multiple of significance
|CEILING.MATH|**Math and trigonometry**: Rounds a number up, to the nearest integer or to the nearest multiple of significance
|CEILING.PRECISE|**Math and trigonometry**: Rounds a number the nearest integer or to the nearest multiple of significance. Regardless of the sign of the number, the number is rounded up.
|CELL|**Information**: Returns information about the formatting, location, or contents of a cell
|CHAR|**Text**: Returns the character specified by the code number
|CHIDIST|**Compatibility**: Returns the one-tailed probability of the chi-squared distribution
|CHIINV|**Compatibility**: Returns the inverse of the one-tailed probability of the chi-squared distribution
|CHITEST|**Compatibility**: Returns the test for independence
|CHISQ.DIST|**Statistical**: Returns the cumulative beta probability density
|CHISQ.DIST.RT|**Statistical**: Returns the one-tailed probability of the chi-squared distribution
|CHISQ.INV.RT|**Statistical**: Returns the inverse of the one-tailed probability of the chi-squared distribution
|CHISQ.TEST|**Statistical**: Returns the test for independence
|CHOOSE|**Lookup and reference**: Chooses a value from a list of values
|CHOOSECOLS|**Lookup and reference**: Returns the specified columns from an array
|CHOOSEROWS|**Lookup and reference**: Returns the specified rows from an array
|CLEAN|**Text**: Removes all nonprintable characters from text
|CODE|**Text**: Returns a numeric code for the first character in a text string
|COLUMN|**Lookup and reference**: Returns the column number of a reference
|COLUMNS|**Lookup and reference**: Returns the number of columns in a reference
|COMBIN|**Math and trigonometry**: Returns the number of combinations for a given number of objects
|COMPLEX|**Engineering**: Converts real and imaginary coefficients into a complex number
|CONCAT|**Text**: Combines the text from multiple ranges and/or strings, but it doesn't provide the delimiter or IgnoreEmpty arguments.
|CONCATENATE|**Text**: Joins several text items into one text item
|CONFIDENCE|**Compatibility**: Returns the confidence interval for a population mean
|CONFIDENCE.NORM|**Statistical**: Returns the confidence interval for a population mean
|CONVERT|**Engineering**: Converts a number from one measurement system to another
|CORREL|**Statistical**: Returns the correlation coefficient between two data sets
|COS|**Math and trigonometry**: Returns the cosine of a number
|COSH|**Math and trigonometry**: Returns the hyperbolic cosine of a number
|COUNT|**Statistical**: Counts how many numbers are in the list of arguments
|COUNTA|**Statistical**: Counts how many values are in the list of arguments
|COUNTBLANK|**Statistical**: Counts the number of blank cells within a range
|COUNTIF|**Statistical**: Counts the number of cells within a range that meet the given criteria
|COUNTIFS|**Statistical**: Counts the number of cells within a range that meet multiple criteria
|COUPDAYBS|**Financial**: Returns the number of days from the beginning of the coupon period to the settlement date
|COUPDAYS|**Financial**: Returns the number of days in the coupon period that contains the settlement date
|COUPDAYSNC|**Financial**: Returns the number of days from the settlement date to the next coupon date
|COUPNCD|**Financial**: Returns the next coupon date after the settlement date
|COUPNUM|**Financial**: Returns the number of coupons payable between the settlement date and maturity date
|COUPPCD|**Financial**: Returns the previous coupon date before the settlement date
|COVAR|**Compatibility**: Returns covariance, the average of the products of paired deviations
|COVARIANCE.P|**Statistical**: Returns covariance, the average of the products of paired deviations
|COVARIANCE.S|**Statistical**: Returns the sample covariance, the average of the products deviations for each data point pair in two data sets
|CRITBINOM|**Compatibility**: Returns the smallest value for which the cumulative binomial distribution is less than or equal to a criterion value
|CUMIPMT|**Financial**: Returns the cumulative interest paid between two periods
|CUMPRINC|**Financial**: Returns the cumulative principal paid on a loan between two periods
###### **D**
|**Function**|**Summary**|
| :- | :- |
|DATE|**Date and time**: Returns the serial number of a particular date
|DATEDIF|**Date and time**: Calculates the number of days, months, or years between two dates. This function is useful in formulas where you need to calculate an age.
|DATEVALUE|**Date and time**: Converts a date in the form of text to a serial number
|DAVERAGE|**Database**: Returns the average of selected database entries
|DAY|**Date and time**: Converts a serial number to a day of the month
|DAYS|**Date and time**: Returns the number of days between two dates
|DAYS360|**Date and time**: Calculates the number of days between two dates based on a 360-day year
|DB|**Financial**: Returns the depreciation of an asset for a specified period by using the fixed-declining balance method
|DCOUNT|**Database**: Counts the cells that contain numbers in a database
|DCOUNTA|**Database**: Counts nonblank cells in a database
|DDB|**Financial**: Returns the depreciation of an asset for a specified period by using the double-declining balance method or some other method that you specify
|DEC2BIN|**Engineering**: Converts a decimal number to binary
|DEC2HEX|**Engineering**: Converts a decimal number to hexadecimal
|DEC2OCT|**Engineering**: Converts a decimal number to octal
|DEGREES|**Math and trigonometry**: Converts radians to degrees
|DELTA|**Engineering**: Tests whether two values are equal
|DEVSQ|**Statistical**: Returns the sum of squares of deviations
|DGET|**Database**: Extracts from a database a single record that matches the specified criteria
|DISC|**Financial**: Returns the discount rate for a security
|DMAX|**Database**: Returns the maximum value from selected database entries
|DMIN|**Database**: Returns the minimum value from selected database entries
|DOLLAR|**Text**: Converts a number to text, using the $ (dollar) currency format
|DOLLARDE|**Financial**: Converts a dollar price, expressed as a fraction, into a dollar price, expressed as a decimal number
|DOLLARFR|**Financial**: Converts a dollar price, expressed as a decimal number, into a dollar price, expressed as a fraction
|DPRODUCT|**Database**: Multiplies the values in a particular field of records that match the criteria in a database
|DROP|**Lookup and reference**: Excludes a specified number of rows or columns from the start or end of an array
|DSTDEV|**Database**: Estimates the standard deviation based on a sample of selected database entries
|DSTDEVP|**Database**: Calculates the standard deviation based on the entire population of selected database entries
|DSUM|**Database**: Adds the numbers in the field column of records in the database that match the criteria
|DURATION|**Financial**: Returns the annual duration of a security with periodic interest payments
|DVAR|**Database**: Estimates variance based on a sample from selected database entries
|DVARP|**Database**: Calculates variance based on the entire population of selected database entries
###### **E**
|**Function**|**Summary**|
| :- | :- |
|EDATE|**Date and time**: Returns the serial number of the date that is the indicated number of months before or after the start date
|EFFECT|**Financial**: Returns the effective annual interest rate
|ENCODEURL|**Web**: Returns a URL-encoded string
|EOMONTH|**Date and time**: Returns the serial number of the last day of the month before or after a specified number of months
|ERF|**Engineering**: Returns the error
|ERFC|**Engineering**: Returns the complementary error
|ERROR.TYPE|**Information**: Returns a number corresponding to an error type
|EVEN|**Math and trigonometry**: Rounds a number up to the nearest even integer
|EXACT|**Text**: Checks to see if two text values are identical
|EXP|**Math and trigonometry**: Returns e raised to the power of a given number
|EXPONDIST|**Compatibility**: Returns the exponential distribution
###### **F**
|**Function**|**Summary**|
| :- | :- |
|FACT|**Math and trigonometry**: Returns the factorial of a number
|FACTDOUBLE|**Math and trigonometry**: Returns the double factorial of a number
|FALSE|**Logical**: Returns the logical value FALSE
|F.DIST|**Statistical**: Returns the F probability distribution
|FDIST|**Compatibility**: Returns the F probability distribution
|F.DIST.RT|**Statistical**: Returns the F probability distribution
|FILTER|**Lookup and reference**: Filters a range of data based on criteria you define
|FIND|**Text**: Finds one text value within another (case-sensitive)
|FINDB|**Text**: Finds one text value within another (case-sensitive)
|F.INV.RT|**Statistical**: Returns the inverse of the F probability distribution
|FINV|**Compatibility**: Returns the inverse of the F probability distribution
|FISHER|**Statistical**: Returns the Fisher transformation
|FISHERINV|**Statistical**: Returns the inverse of the Fisher transformation
|FIXED|**Text**: Formats a number as text with a fixed number of decimals
|FLOOR|**Compatibility**: Rounds a number down, toward zero
|FLOOR.MATH|**Math and trigonometry**: Rounds a number down, to the nearest integer or to the nearest multiple of significance
|FORECAST|**Statistical**: Returns a value along a linear trend(In Excel 2016, this function is replaced with FORECAST.LINEAR as part of the new Forecasting functions)
|FORECAST.LINEAR|**Statistical**: Returns a future value based on existing values
|FORMULATEXT|**Lookup and reference**: Returns the formula at the given reference as text
|FREQUENCY|**Statistical**: Returns a frequency distribution as a vertical array
|FV|**Financial**: Returns the future value of an investment
|FVSCHEDULE|**Financial**: Returns the future value of an initial principal after applying a series of compound interest rates
###### **G**
|**Function**|**Summary**|
| :- | :- |
|GAMMA.DIST|**Statistical**: Returns the gamma distribution
|GAMMADIST|**Compatibility**: Returns the gamma distribution
|GAMMA.INV|**Statistical**: Returns the inverse of the gamma cumulative distribution
|GAMMAINV|**Compatibility**: Returns the inverse of the gamma cumulative distribution
|GAMMALN|**Statistical**: Returns the natural logarithm of the gamma function, ��(x)
|GCD|**Math and trigonometry**: Returns the greatest common divisor
|GEOMEAN|**Statistical**: Returns the geometric mean
|GESTEP|**Engineering**: Tests whether a number is greater than a threshold value
|GETPIVOTDATA|**Lookup and reference**: Returns data stored in a PivotTable report
|GROW
