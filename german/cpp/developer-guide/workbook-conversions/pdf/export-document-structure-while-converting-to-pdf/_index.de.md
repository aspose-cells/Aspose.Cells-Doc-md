---  
title: Exportieren der Dokumentenstruktur bei der Umwandlung in PDF mit C++  
linktitle: Exportieren der Dokumentstruktur beim Konvertieren in PDF  
type: docs  
weight: 360  
url: /de/cpp/export-document-structure-while-converting-to-pdf/  
description: Erfahren Sie, wie Sie die Dokumentenstruktur beim Konvertieren in PDF mit Aspose.Cells in C++ exportieren.  
---  

Die PDF-logische Struktur-Funktion ermöglicht die Integration von Informationen über die Dokumentenstruktur in eine PDF-Datei. Aspose.Cells erhält Infos zur Struktur aus einem Microsoft Excel-Dokument, z.B. Zelle, Zeile, Tabelle, Arbeitsblatt, Bild, Shape, Header/Footer usw.  

Mit der Option [PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/) können Sie eine getaggte PDF-Datei mit exportierter Dokumentenstruktur speichern.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the Excel file with image, shape, chart, etc.
    Workbook workbook(u"document-structure-example.xlsx");

    // Set to export document structure.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetExportDocumentStructure(true);

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully with document structure!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  


{{< app/cells/assistant language="cpp" >}}
