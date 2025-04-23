---
title: Fehler beim Rendern von Excel nach PDF mit C++ ignorieren
linktitle: Fehler ignorieren beim Umsetzen von Excel in PDF
type: docs
weight: 80
url: /de/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Erfahren Sie, wie Sie Fehler während der Excel zu PDF Konvertierung mit Aspose.Cells for C++ ignorieren.
---

## **Mögliche Verwendungsszenarien**

Manchmal treten beim Konvertieren Ihrer Excel-Datei in PDF Fehler oder Ausnahmen auf, und der Konvertierungsprozess wird beendet. Sie können alle solchen Fehler während des Konvertierungsprozesses mit der Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) ignorieren. Auf diese Weise wird der Konvertierungsprozess reibungslos abgeschlossen, ohne Fehler oder Ausnahmen zu verursachen, aber es kann zum Datenverlust kommen. Verwenden Sie diese Eigenschaft daher nur, wenn der Datenverlust für Sie nicht kritisch ist.

## **Ignorieren Sie Fehler beim Rendern von Excel in PDF**

Der folgende Code lädt die [Beispieldatei Excel](55541778.xlsx), jedoch ist diese Excel-Datei fehlerhaft und verursacht während der [Konvertierung in PDF](55541779.pdf) am 17.11 einen Fehler. Da wir jedoch die Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) verwenden, wird kein Fehler ausgelöst. Ein *abgerundeter roter Pfeil*-ähnlicher Shape, wie in diesem Screenshot gezeigt, geht jedoch verloren.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Beispielcode**

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
