---
title: Excel Datei in ein PDF Format konvertieren, das mit PDFA 1a kompatibel ist, mit C++
linktitle: Konvertieren Sie Excel Datei in das PDF Format, das mit PDFA 1a kompatibel ist
type: docs
weight: 130
url: /de/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Erfahren Sie, wie Sie Excel Dateien mit Aspose.Cells und C++ in das PDF/A 1a konforme PDF Format konvertieren.
---

## **Mögliche Verwendungsszenarien**

PDF/A ist eine spezielle Version des PDF, die für die langfristige Archivierung von Dokumenten entwickelt wurde. PDF/A ist eine ISO-standardisierte Version des Portable Document Format (PDF), die alle in einem Dokument verwendeten Schriftarten innerhalb der PDF-Datei embeddingiert. PDF/A unterscheidet sich von PDF durch das Verbot von Funktionen wie Schriftartenverlinkung (im Gegensatz zum Schriftart-Embedding) und Verschlüsselung. Aspose.Cells ermöglicht das Speichern von Excel-Dateien in PDF/A-konforme PDF-Dateien (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u werden unterstützt). Dieses Thema beschreibt, wie man die Excel-Arbeitsmappe in eine PDF/A-konforme (PDF/A-1a) PDF-Datei speichert.

## **Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertieren**

Entwickler können die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Das Ändern verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) ermöglicht die Kontrolle über die Druck-, Schriftarten-, Sicherheits- und Komprimierungseinstellungen für das Ausgabepdf. Die wichtigste Eigenschaft ist [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), die das Speichern von Excel-Dateien als PDF/A-konforme PDFs ermöglicht.

Der folgende Beispielcode erläutert, wie man eine Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertiert. Bitte sehen Sie sich die [Ausgabe-PDF](outputCompliancePdfA1a.pdf) sowie den Screenshot zur Referenz an.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
