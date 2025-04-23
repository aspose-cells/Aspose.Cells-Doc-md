---
title: Hinzugefügte Neuberechnung von Bildern  Excel nach PDF Konvertierung mit C++
linktitle: Hinzufügen von neu abgetasteten Bildern  Excel in PDF Konvertierung
type: docs
weight: 150
url: /de/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie zusätzlich eingefügte Bilder neu sampeln, um die PDF Größe mit Aspose.Cells und C++ zu reduzieren.
---

{{% alert color="primary" %}}

Bei der Arbeit mit großen Microsoft Excel-Dateien mit vielen Bildern müssen Sie möglicherweise Bilder komprimieren, die hinzugefügt wurden, um die Größe der Ausgabepdf-Datei zu reduzieren und die Gesamtwandlungsleistung zu verbessern. Aspose.Cells unterstützt das Neuabtasten von hinzugefügten Bildern, um die Größe der Ausgabepdf-Datei zu reduzieren und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte beachten Sie den folgenden Beispiellcode, der beschreibt, wie die Aufgabe mithilfe der Aspose.Cells-API ausgeführt wird. Das Beispiel konvertiert eine Microsoft Excel-Datei in eine PDF-Datei und komprimiert dabei die Bilder in der Datei.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputPath = srcDir + u"input.xlsx";
    Workbook workbook(inputPath);

    // Instantiate the PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set Image Resample properties
    pdfSaveOptions.SetImageResample(300, 70);

    // Save the PDF file
    U16String outputPath = outDir + u"OutputFile_out_pdf.pdf";
    workbook.Save(outputPath, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Die Verwendung der [**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/)-Option minimiert die Größe der Ausgabe-PDF, kann aber die Bildqualität etwas beeinträchtigen.

{{% /alert %}} 

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}

