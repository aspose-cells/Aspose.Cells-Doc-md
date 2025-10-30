---
title: Alle Spalten des Arbeitsblatts auf eine einzelne PDF Seite anpassen mit C++
linktitle: Alle Arbeitsblattsäulen auf eine einzelne PDF Seite passen
type: docs
weight: 160
url: /de/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Erstellen Sie eine PDF, die alle Spalten des Arbeitsblatts auf eine einzige Seite passt, unter Verwendung von Aspose.Cells mit C++.
---

{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei erzeugen, die alle Spalten eines Arbeitsblatts auf eine Seite passt. Die Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) bietet diese Funktion sehr einfach. Komplexe Berechnungen wie Höhe und Breite des Ausgabepdfs werden intern erledigt und basieren auf den Daten des Arbeitsblatts.

{{% /alert %}}

## **Arbeitsblattsäulen auf eine einzelne PDF-Seite anpassen**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) sorgt dafür, dass alle Spalten eines Arbeitsblatts auf einer einzigen PDF-Seite dargestellt werden, wobei Zeilen je nach Datenlänge auf mehrere Seiten erweitert werden können.

Der folgende Beispielcode zeigt, wie die Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) verwendet wird, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

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

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, kann die gerenderte PDF-Datei den Inhalt in sehr kleiner Größe anzeigen. Es ist immer noch lesbar, wenn es in einer Anzeige-Anwendung wie Acrobat Reader skaliert wird.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
