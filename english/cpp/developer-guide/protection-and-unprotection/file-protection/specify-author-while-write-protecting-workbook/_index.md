---
title: Specify Author while Write Protecting Workbook with C++
linktitle: Specify Author while Write Protecting Workbook
type: docs
weight: 40
url: /cpp/specify-author-while-write-protecting-workbook/
description: Learn how to specify an author name while write protecting a workbook using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

You can specify the author name while write protecting your workbook using Aspose.Cells API. Please use the [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) property for this purpose.

## **Specify Author while Write Protecting Workbook**

The following sample code explains the usage of the [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) property. The code creates an empty workbook, write protects it with a password, specifies the author name, and saves it as an [output Excel file](67338582.xlsx). The following screenshot illustrates the effect of the sample code on the output Excel file for your reference.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}