---
title: Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells with C++
linktitle: Read Numbers Spreadsheet
type: docs
weight: 140
url: /cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Learn how to read Numbers spreadsheet files developed by Apple Inc. using Aspose.Cells with C++.
---

## **Possible Usage Scenarios**

Numbers is a spreadsheet application developed by Apple Inc. Aspose.Cells can read Numbers spreadsheets but it does not support writing to them. It can read Numbers spreadsheet's Data, Style, and Formulas.

## **Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells**

The following sample code loads the [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) and converts it to [Output PDF Format](outputNumbersByAppleInc.pdf). You will have to use the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) class and specify [**LoadFormat.Numbers**](https://reference.aspose.com/cells/cpp/aspose.cells/loadformat/) as a parameter in its constructor to load it successfully. Please download both of them from the given links. You can try the code with any Numbers spreadsheet. Please also read the comments of the code for more help.

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

    // Specify load options, we want to load Numbers spreadsheet
    LoadOptions opts(LoadFormat::Numbers);

    // Load the Numbers spreadsheet in workbook with above load options
    Workbook wb(srcDir + u"sampleNumbersByAppleInc.numbers", opts);

    // Save the workbook to pdf format
    wb.Save(outDir + u"outputNumbersByAppleInc.pdf", SaveFormat::Pdf);

    std::cout << "Numbers spreadsheet converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```