---  
title: How to Manage Dates and Times
type: docs  
weight: 600  
url: /nodejs-cpp/how-to-manage-dates-and-times/  
description: Learn how to manage dates and times through the Aspose.Cells for Node.js via C++ API.  
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.  
---  

## **How to store Dates and Times in Excel**  
Dates and times are stored in cells as numbers. Thus, the values of cells that contain dates and times are of the numeric type. A number that specifies a date and time consists of the date (integer part) and time (fractional part) components. The Cell.DoubleValue property returns this number.  

## **How to Display Dates and Times in Aspose.Cells**  
To display a number as a date and time, apply the required date and time format to a cell via the [Style.Number](https://reference.aspose.com/cells/nodejs-cpp/style/#number-string-number-) or [Style.Custom]() property. The CellValue.DateTimeValue property returns the DateTime object, which specifies the date and time that is represented by the number contained in a cell.  
<br>  
<image src="1.png" width="70%" />  

## **How to switch two date systems in Aspose.Cells**  
MS-Excel stores dates as numbers that are called serial values. A serial value is an integer that is the number of elapsed days from the first day in the date system. Excel supports the following date systems for serial values:  

1. The 1900 date system. The first date is January 1, 1900, and its serial value is 1. The last date is December 31, 9999, and its serial value is 2,958,465. This date system is used in the workbook by default.  
1. The 1904 date system. The first date is January 1, 1904, and its serial value is 0. The last date is December 31, 9999, and its serial value is 2,957,003. To use this date system in the workbook, set the [Workbook.Settings.Date1904](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#date1904-) property to true.  

This example shows that the serial values stored on the same date in different date systems are different.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SwitchTwoDateSystems.js" >}}


Output result:  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **How to Set DateTime Value in Aspose.Cells**  
This example sets a DateTime value in cell A1 and A2, sets custom format of A1 and number format of A2, and then outputs the value types.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SetDateTimeValue.js" >}}


Output result:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **How to Get DateTime Value in Aspose.Cells**  
This example sets a DateTime value in cell A1 and A2, sets custom format of A1 and number format of A2, checks the value types of two cells, and then outputs the DateTime value and formatted string.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-GetDateTimeValue.js" >}}


Output result:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A1 DateTime Value: 11/23/2023 5:59:09 PM  
A1 DateTime String Value: 11-23-23 17:59:09  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
A2 DateTime Value: 11/23/2023 5:59:09 PM  
A2 DateTime String Value: 11/23/2023 17:59  
```  
  