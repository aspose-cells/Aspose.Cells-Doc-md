---
title: Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format with C++
linktitle: Trim Leading Blank Rows and Columns
type: docs
weight: 100
url: /cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Learn how to trim leading blank rows and columns while exporting spreadsheets to CSV format using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Sometimes, your Excel or CSV file has leading blank columns or rows. For example, consider this line:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Here the first three cells or columns are blank. When you open such a CSV file in Microsoft Excel, then Microsoft Excel discards these leading blank rows and columns.

By default, Aspose.Cells does not discard leading blank columns and rows on saving but if you want to remove them just like Microsoft Excel does, then Aspose.Cells provides [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/trimleadingblankrowandcolumn/) property. Please set it to **true** and then all the leading blank rows and columns will be discarded on saving.

{{% alert color="primary" %}}

Prior to the release of Aspose.Cells for C++ 20.4, the default value of [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/trimleadingblankrowandcolumn/) was **false**. Since the 20.4 release, the default value of [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/trimleadingblankrowandcolumn/) is **true.**

{{% /alert %}}

## **Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format**

The following sample code loads the [source excel file](sampleTrimBlankColumns.xlsx) which has two leading blank columns. It first saves the excel file in CSV format without any changes and then it sets [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/trimleadingblankrowandcolumn/) property to **true** and saves it again. The screenshot shows the [source excel file](sampleTrimBlankColumns.xlsx), [output CSV file without trimming](outputWithoutTrimBlankColumns.csv), and the [output CSV file with trimming](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleTrimBlankColumns.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Save in csv format without trimming blank columns
    wb.Save(outDir + u"outputWithoutTrimBlankColumns.csv", SaveFormat::Csv);

    // Create TxtSaveOptions and set TrimLeadingBlankRowAndColumn to true
    TxtSaveOptions opts;
    opts.SetTrimLeadingBlankRowAndColumn(true);

    // Save in csv format with trimming blank columns
    wb.Save(outDir + u"outputTrimBlankColumns.csv", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```