---
title: How to Manage Dates and Times with C++
linktitle: How to Manage Dates and Times
type: docs
weight: 600
url: /cpp/how-to-manage-dates-and-times/
description: Learn how to manage dates and times through the Aspose.Cells for C++ API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to store Dates and Times in Excel**
Dates and times are stored in cells as numbers. Thus, the values of cells that contain dates and times are numeric. A number that specifies a date and time consists of a date (integer part) and a time (fractional part). The `Cell::GetDoubleValue()` method returns this number.

## **How to Display Dates and Times in Aspose.Cells**
To display a number as a date and time, apply the required date and time format to a cell via the `Style::SetNumber()` or `Style::SetCustom()` method. The `Cell::GetDateTimeValue()` method returns the `DateTime` object, which specifies the date and time that is represented by the number contained in a cell.
<br>
<image src="1.png" width="70%" />

## **How to switch between two date systems in Aspose.Cells**
MS-Excel stores dates as numbers that are called serial values. A serial value is an integer that is the number of elapsed days from the first day in the date system. Excel supports the following date systems for serial values:

1. The 1900 date system. The first date is January 1, 1900, and its serial value is 1. The last date is December 31, 9999, and its serial value is 2,958,465. This date system is used in the workbook by default.  
2. The 1904 date system. The first date is January 1, 1904, and its serial value is 0. The last date is December 31, 9999, and its serial value is 2,957,003. To use this date system in the workbook, set the `Workbook::GetSettings().SetDate1904(true)` property.

This example shows that the serial values stored on the same date in different date systems are different.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "Use the 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
Output result:
```
A1 is Numeric Value: 45253
Use the 1904 date system====================
A2 is Numeric Value: 43791
```

## **How to Set DateTime Value in Aspose.Cells**
This example sets a `DateTime` value in cell A1 and A2, sets a custom format for A1 and a number format for A2, and then outputs the value types.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Output result:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **How to Get DateTime Value in Aspose.Cells**
This example sets a `DateTime` value in cell A1 and A2, sets a custom format for A1 and a number format for A2, checks the value types of the two cells, and then outputs the `DateTime` value and the formatted string.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

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

{{< app/cells/assistant language="cpp" >}}
