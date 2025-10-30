---
title: Grafik Sayfası için PdfBookmarkEntry Oluşturma (C++)
linktitle: Grafik Sayfası için PdfBookmarkEntry Oluşturma
type: docs
weight: 50
url: /tr/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Aspose.Cells for C++ kullanarak grafik sayfaları için PdfBookmarkEntry oluşturmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Önceden, Aspose.Cells bir normal sayfa için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) oluştururdu. Ancak şimdi Aspose.Cells, aynı zamanda bir grafik sayfası için de [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) oluşturabilir. Çünkü grafik sayfasının, A1 hücresi dışında başka hiçbir hücresi olmadığından, yalnızca A1 hücresi için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) oluşturacaktır.

## **Grafik Tablosu için PdfBookmarkEntry Oluştur**

Aşağıdaki örnek kod, dört sayfa içeren [örnek Excel dosyasını](61767756.xlsx) yükler. İki tanesi normal sayfalar, diğer ikisi grafik sayfalarıdır. Aşağıdaki gibi dört yer imi girişleri oluşturur:

- Yer İmi-I
- Yer İmi-II-Chart1
- Yer İmi-III
- Yer İmi-IV-Chart2

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan [çıktı PDF'yi](61767757.pdf) göstermektedir.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Örnek Kod**

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
