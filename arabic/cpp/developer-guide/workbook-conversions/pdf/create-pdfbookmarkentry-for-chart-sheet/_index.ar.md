---
title: إنشاء مدخل إشارات مرجعية لـ Pdf لمخطط ورقة العمل باستخدام C++
linktitle: إنشاء إدخال PdfBookmarkEntry لورقة الرسم البياني
type: docs
weight: 50
url: /ar/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: تعلم كيفية إنشاء PdfBookmarkEntry لورق المخطط باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

سابقًا، كان Aspose.Cells سيقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) لورقة عادية. ولكن الآن يمكن لـ Aspose.Cells أيضًا إنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) لورقة الرسم البياني. نظرًا لعدم وجود خلية أخرى غير الخلية A1 في رقم الرسم البياني، سيقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) للخلية A1 فقط.

## **إنشاء PdfBookmarkEntry لورقة الرسم البياني**

يُحمّل هذا المثال البرمجي عينة من ملف Excel ([sample Excel file](61767756.xlsx)) الذي يحتوي على أربعة أوراق. ورقتان منهما أوراق عادية والأخريين أوراق مخططات. ينشئ أربع إدخالات علامة مرجعية على النحو التالي:

- إشارة-I
- إشارة-II-Chart1
- إشارة-III
- إشارة-IV-Chart2

تظهر الصورة الملتقطة التالية [PDF المولد](61767757.pdf) بواسطة الكود النموذجي للإشارة.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **الكود المثالي**

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
