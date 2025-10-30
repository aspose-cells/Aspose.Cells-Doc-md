---
title: Eine PDF Seite pro Excel Arbeitsblatt rendern  Excel nach PDF Konvertierung mit C++
type: docs
weight: 100
url: /de/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Excel Arbeitsblätter in PDF Format konvertieren mit einer Seite pro Arbeitsblatt unter Verwendung von Aspose.Cells mit C++.
---

{{% alert color="primary" %}} 

Beim Arbeiten mit großen Microsoft-Excel-Dateien (zum Beispiel Arbeitsmappen mit vielen Blättern, jeweils mit 50 Spalten und 300 oder mehr Zeilen Daten) möchten Sie möglicherweise, dass die PDF-Ausgabe auf einer Seite pro Arbeitsblatt angezeigt wird, unabhängig von der Größe des Arbeitsblatts. Dies bedeutet, dass jede Seite wahrscheinlich eine radikal unterschiedliche Seitengröße haben wird. Dies kann durch Verwendung von Aspose.Cells for C++ erreicht werden.

{{% /alert %}} 

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Wenn die Option [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) auf **true** gesetzt ist, wird der gesamte Tabelleninhalt auf einer PDF-Seite gerendert.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) direkt vor dem Rendern der Tabelle in das PDF-Format aufzurufen. Dies stellt sicher, dass die abhängigen Formelfeld-Werte neu berechnet werden und die korrekten Werte im PDF dargestellt werden.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
