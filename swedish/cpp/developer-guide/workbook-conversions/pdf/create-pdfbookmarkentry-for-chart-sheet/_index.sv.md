---
title: Skapa PdfBookmarkEntry för diagramblad med C++
linktitle: Skapa PdfBookmarkEntry för diagramkalkylblad
type: docs
weight: 50
url: /sv/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Lär dig hur man skapar PdfBookmarkEntry för diagramblad med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Tidigare skulle Aspose.Cells skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) för ett normalt blad. Men nu kan även Aspose.Cells skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) för diagramblad. Eftersom diagrambladet inte har någon annan cell än cell A1, kommer det att skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) endast för cell A1.

## **Skapa PdfBookmarkEntry för diagramblad**

Följande exempel laddar [exempel-Excelfilen](61767756.xlsx) som innehåller fyra blad. Två av dem är vanliga blad och de andra två är diagramblad. Det skapas fyra bokmärkesinlägg enligt följande:

- Bokmärke-I
- Bokmärke-II-Chart1
- Bokmärke-III
- Bokmärke-IV-Chart2

Följande skärmbild visar [utdata PDF](61767757.pdf) genererad av exemplet.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exempelkod**

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
