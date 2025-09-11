---
title: Render Office Add-Ins while converting Excel to PDF with C++
linktitle: Render Office Add-Ins while converting Excel to PDF
type: docs
weight: 100
url: /cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Learn how to render Office Add-Ins while converting Excel files to PDF using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Earlier, Aspose.Cells could not render Office Add-Ins when an Excel file was saved to PDF format. Now, Aspose.Cells renders it correctly. You do not need to use any special method or property to render Office Add-Ins in the output PDF. Simply save your Excel file to PDF format, and it will render the Office Add-Ins.

## **Render Office Add-Ins while converting Excel to PDF**

The following sample code saves the [sample Excel file](60489769.xlsx) which contains the Office Add-Ins. Please see the [output PDF generated with the previous version i.e. 17.11](60489770.pdf) and the [output PDF generated with the newer version i.e. 17.12 and onward](60489771.pdf). The previous version output PDF is blank, but the newer version output PDF shows the Office Add-In.

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}