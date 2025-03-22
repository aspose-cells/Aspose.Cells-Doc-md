---
title: Ignore Errors while Rendering Excel to PDF with C++
linktitle: Ignore Errors while Rendering Excel to PDF
type: docs
weight: 80
url: /cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Learn how to ignore errors during Excel to PDF conversion using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Sometimes when you convert your Excel file to PDF, errors or exceptions occur and the conversion process terminates. You can ignore all such errors during the conversion process by using the [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/ignoreerror/) property. This way, the conversion process will complete smoothly without throwing any error or exception but the loss of data may occur. Therefore, please use this property only if the loss of data is not critical for you.

## **Ignore Errors while Rendering Excel to PDF**

The following code loads the [sample Excel file](55541778.xlsx) but the sample Excel file is erroneous and throws an error during [conversion to PDF](55541779.pdf) in 17.11 but since we are using [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/ignoreerror/) property, it does not throw an error. However, one *rounded red arrow like shape* as shown in this screenshot is lost.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

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
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```