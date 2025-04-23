---
title: Begrenzung der generierten Seitenzahl  Excel zu PDF Konvertierung mit C++
linktitle: Begrenzung der generierten Seitenzahl
type: docs
weight: 180
url: /de/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie die Anzahl der beim Konvertieren von Excel in PDF mit Aspose.Cells für C++ generierten Seiten begrenzen.
---

{{% alert color="primary" %}}

Manchmal möchten Sie einen Bereich von Seiten in eine Ausgabe-PDF-Datei drucken. Aspose.Cells hat die Möglichkeit, eine Begrenzung festzulegen, wie viele Seiten generiert werden, wenn eine Excel-Tabelle in die PDF-Dateiformat umgesetzt wird.

{{% /alert %}}

## **Begrenzen der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Bereich von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF umgesetzt wird.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Wenn in der Tabelle Formeln enthalten sind, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) kurz vor der Umsetzung in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die korrekten Werte in der Ausgabedatei dargestellt.

{{% /alert %}}
