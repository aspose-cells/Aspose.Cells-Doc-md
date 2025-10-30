---
title: Erstellen Sie PdfBookmarkEntry für Chart Sheet mit C++
linktitle: PdfBookmarkEntry für Diagrammblatt erstellen
type: docs
weight: 50
url: /de/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Erfahren Sie, wie Sie PdfBookmarkEntry für Diagrammblätter mit Aspose.Cells for C++ erstellen.
---

## **Mögliche Verwendungsszenarien**

Früher erstellte Aspose.Cells [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) für ein normales Blatt. Jetzt kann Aspose.Cells auch [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) für ein Diagrammblatt erstellen. Da das Diagrammblatt außer der Zelle A1 keine andere Zelle hat, wird es nur [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) für die Zelle A1 erstellen.

## **Erstellen Sie PdfBookmarkEntry für Diagrammblatt**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767756.xlsx), die vier Blätter enthält. Zwei davon sind normale Blätter und die anderen beiden Diagrammblätter. Es erstellt vier Lesezeichen-Einträge wie folgt:

- Lesezeichen-I
- Lesezeichen-II-Diagramm1
- Lesezeichen-III
- Lesezeichen-IV-Diagramm2

Der folgende Screenshot zeigt die [Ausgabe-PDF](61767757.pdf), die vom Beispielcode zur Referenz erzeugt wird.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath = u"sampleCreatePdfBookmarkEntryForChartSheet.xlsx";
    Workbook wb(inputFilePath);

    // Access all four worksheets
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet1 = sheets.Get(0);
    Worksheet sheet2 = sheets.Get(1);
    Worksheet sheet3 = sheets.Get(2);
    Worksheet sheet4 = sheets.Get(3);

    // Create Pdf Bookmark Entry for Sheet1
    PdfBookmarkEntry ent1;
    ent1.SetDestination(sheet1.GetCells().Get(u"A1"));
    ent1.SetText(u"Bookmark-I");

    // Create Pdf Bookmark Entry for Sheet2 - Chart 
    PdfBookmarkEntry ent2;
    ent2.SetDestination(sheet2.GetCells().Get(u"A1"));
    ent2.SetText(u"Bookmark-II-Chart1");

    // Create Pdf Bookmark Entry for Sheet3 
    PdfBookmarkEntry ent3;
    ent3.SetDestination(sheet3.GetCells().Get(u"A1"));
    ent3.SetText(u"Bookmark-III");

    // Create Pdf Bookmark Entry for Sheet4 - Chart 
    PdfBookmarkEntry ent4;
    ent4.SetDestination(sheet4.GetCells().Get(u"A1"));
    ent4.SetText(u"Bookmark-IV-Chart2");

    // Arrange all Bookmark Entries
    std::vector<PdfBookmarkEntry> lst;
    lst.push_back(ent2);
    lst.push_back(ent3);
    lst.push_back(ent4);

    // Create Pdf Save Options with Bookmark Entries
    PdfSaveOptions opts;
    opts.SetBookmark(ent1);

    // Save the output Pdf
    U16String outputFilePath = u"outputCreatePdfBookmarkEntryForChartSheet.pdf";
    wb.Save(outputFilePath, opts);

    std::cout << "PDF with bookmarks created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
