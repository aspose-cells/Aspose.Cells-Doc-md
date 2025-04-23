---
title: Создайте PdfBookmarkEntry для листа с графиком на C++
linktitle: Создание PdfBookmarkEntry для листа с диаграммой
type: docs
weight: 50
url: /ru/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Узнайте, как создавать PdfBookmarkEntry для листов с графиками, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Ранее Aspose.Cells создавала [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) для обычного листа. Но теперь Aspose.Cells также может создавать [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) для листа диаграммы. Поскольку лист диаграммы не содержит никаких других ячеек, кроме ячейки A1, то она создаст [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) только для ячейки A1.

## **Создание PdfBookmarkEntry для листа с диаграммой**

Следующий пример кода загружает [пробный файл Excel](61767756.xlsx), содержащий четыре листа. Два из них — обычные листы и еще два — графические листы. Он создает четыре пункта закладок следующим образом:

- Закладка-I
- Закладка-II-Chart1
- Закладка-III
- Закладка-IV-Chart2

На следующем скриншоте показан [выходной PDF-файл](61767757.pdf), сгенерированный примером кода для справки.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Образец кода**

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
