---
title: Manage data of Excel files with C++
linktitle: Cells Data
type: docs
weight: 110
url: /cpp/view-and-edit-excel-data/
description: This article describes how to view and edit data of Excel files with Aspose.Cells library using C++.
keywords: Aspose.Cells C++ Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---

{{% alert color="primary" %}}

In [Accessing Cells of a Worksheet](/cells/cpp/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.

{{% /alert %}}

## **How to Add Data to Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

Aspose.Cells allows developers to add data to the cells in worksheets by calling the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class' [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) method. Aspose.Cells provides overloaded versions of the [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) method that lets developers add different kinds of data to cells. Using these overloaded versions of the [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) method, it is possible to add a Boolean, string, double, integer or date/time, etc. values to the cell.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);


    worksheet.GetCells().Get(U16String(u"A1")).PutValue(U16String(u"Hello World"));
    worksheet.GetCells().Get(U16String(u"A2")).PutValue(20.5);
    worksheet.GetCells().Get(U16String(u"A3")).PutValue((int32_t)15);
    worksheet.GetCells().Get(U16String(u"A4")).PutValue(true);

    Cell cellA1 = worksheet.GetCells().Get(U16String(u"A4"));
    Style style = cellA1.GetStyle();
    style.SetNumber(15);
    cellA1.SetStyle(style);

    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Data inserted and workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **How to Improve Efficiency**

If you use [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) method to put a large amount of data to a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.

## **How to Retrieve Data from Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to worksheets in the file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

The [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class provides several properties that allow developers to retrieve values from the cells according to their data types. These properties include:

- [**StringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/): returns the string value of the cell.
- [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/): returns the double value of the cell.
- [**BoolValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/): returns the boolean value of the cell.
- [**DateTimeValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/): returns the date/time value of the cell.
- [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/): returns the float value of the cell.
- [**IntValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/): returns the integer value of the cell.

When a field is not filled, cells with [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) or [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) throws an exception.

The type of data contained in a cell can also be checked by using the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class' [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) property. In fact, the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class' [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) property is based on the [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) enumeration whose pre-defined values are listed below:

|**Cell Value Types**|**Description**|
| :- | :- |
|IsBool|Specifies that cell value is Boolean.|
|IsDateTime|Specifies that cell value is date/time.|
|IsNull|Represents a blank cell.|
|IsNumeric|Specifies that cell value is numeric.|
|IsString|Specifies that cell value is a string.|
|IsUnknown|Specifies that cell value is unknown.|

You can also use the above pre-defined cell value types to compare with the Type of data present in each cell.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int maxRow = worksheet.GetCells().GetMaxDataRow();
    int maxCol = worksheet.GetCells().GetMaxDataColumn();

    for (int row = 0; row <= maxRow; row++)
    {
        for (int col = 0; col <= maxCol; col++)
        {
            Cell cell = worksheet.GetCells().Get(row, col);

            U16String stringValue;
            double doubleValue = 0.0;
            bool boolValue = false;

            switch (cell.GetType())
            {
                case CellValueType::IsString:
                    stringValue = cell.GetStringValue();
                    std::cout << "String Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNumeric:
                    doubleValue = cell.GetDoubleValue();
                    std::cout << "Double Value: " << doubleValue << std::endl;
                    break;

                case CellValueType::IsBool:
                    boolValue = cell.GetBoolValue();
                    std::cout << "Bool Value: " << boolValue << std::endl;
                    break;

                case CellValueType::IsDateTime:
                    stringValue = cell.GetStringValue();
                    std::cout << "DateTime Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsUnknown:
                    stringValue = cell.GetStringValue();
                    std::cout << "Unknown Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNull:
                    break;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

While working on worksheets, users may add different types of data in the cells. These data types may include Boolean, integer, floating point, text or date/time values. With Aspose.Cells, you can get the appropriate values from the cells according to their data types.

{{% /alert %}}

## **Advance topics**
- [Accessing Cells of a Worksheet](/cells/cpp/accessing-cells-of-a-worksheet/)
- [Convert Text Numeric Data to Number](/cells/cpp/convert-text-numeric-data-to-number/)
- [Creating Subtotals](/cells/cpp/creating-subtotals/)
- [Data Filtering](/cells/cpp/data-filtering/)
- [Data Sorting](/cells/cpp/sort-data-of-excel/)
- [Data Validation](/cells/cpp/data-validation/)
- [Find or Search Data](/cells/cpp/find-or-search-data/)
- [Get Cell String Value with and without Formatting](/cells/cpp/get-cell-string-value-with-and-without-formatting/)
- [Adding HTML Rich Text inside the Cell](/cells/cpp/adding-html-rich-text-inside-the-cell/)
- [Insert Hyperlinks into Excel or OpenOffice](/cells/cpp/insert-hyperlinks-to-excel/)
- [How and Where to Use Enumerators](/cells/cpp/how-and-where-to-use-enumerators/)
- [Measure the Width and Height of the Cell Value in Unit of Pixels](/cells/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Reading Cell Values in Multiple Threads Simultaneously](/cells/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion between cell name and row/column index](/cells/cpp/names-and-indices/)
- [Populate Data First by Row then by Column](/cells/cpp/populate-data-first-by-row-then-by-column/)
- [Preserve Single Quote Prefix of Cell Value or Range](/cells/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Access and Update the Portions of Rich Text of Cell](/cells/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="cpp" >}}