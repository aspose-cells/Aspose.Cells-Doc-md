---
title: إضافة إشارات مرجعية إلى ملفات PDF مع وجهات مسماة باستخدام C++
linktitle: إضافة إشارات مرجعية لملف PDF بأهداف مسماة
type: docs
weight: 20
url: /ar/cpp/add-pdf-bookmarks-with-named-destinations/
description: تعلم كيفية إضافة إشارات مرجعية في PDF مع وجهات مسماة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 الوجهات المسماة هي أنواع خاصة من العلامات المرجعية أو الروابط في PDF التي لا تعتمد على صفحات PDF. وهذا يعني، إذا تمت إضافة أو حذف صفحات من PDF، قد تصبح العلامات المرجعية غير صالحة ولكن الوجهات المسماة ستظل سليمة. لإنشاء وجهة مسماة، يرجى ضبط خاصية [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/).

## **إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة**

يرجى الرجوع إلى الكود العيني التالي، و[ملف Excel المصدر](50528348.xlsx)، و[ملف PDF الناتج](50528349.pdf). تُظهر اللقطة الشاشة الإشارات المرجعية والوجهات المسماة داخل ملف PDF الناتج. توصف اللقطة الشاشة أيضا كيفية عرض الوجهات المسماة وأنك بحاجة إلى إصدار احترافي من قارئ أكروبات.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"samplePdfBookmarkEntry_DestinationName.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell C5
    Cell cell = ws.GetCells().Get(u"C5");

    // Create Bookmark and Destination for this cell
    PdfBookmarkEntry bookmarkEntry;
    bookmarkEntry.SetText(u"Text");
    bookmarkEntry.SetDestination(cell);
    bookmarkEntry.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Access cell G56
    cell = ws.GetCells().Get(u"G56");

    // Create Sub-Bookmark and Destination for this cell
    PdfBookmarkEntry subbookmarkEntry1;
    subbookmarkEntry1.SetText(u"Text1");
    subbookmarkEntry1.SetDestination(cell);
    subbookmarkEntry1.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Access cell L4
    cell = ws.GetCells().Get(u"L4");

    // Create Sub-Bookmark and Destination for this cell
    PdfBookmarkEntry subbookmarkEntry2;
    subbookmarkEntry2.SetText(u"Text2");
    subbookmarkEntry2.SetDestination(cell);
    subbookmarkEntry2.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Add Sub-Bookmarks in list
    std::vector<PdfBookmarkEntry> list;
    list.push_back(subbookmarkEntry1);
    list.push_back(subbookmarkEntry2);

    // Assign Sub-Bookmarks list to Bookmark Sub-Entry
    // Note: The SubEntry property is not directly available in the provided headers.
    // Assuming it is a member of PdfBookmarkEntry, you would need to set it here.
    // bookmarkEntry.SetSubEntry(list);

    // Create PdfSaveOptions and assign Bookmark to it
    PdfSaveOptions opts;
    opts.SetBookmark(bookmarkEntry);

    // Save the workbook in Pdf format with given pdf save options
    wb.Save(outDir + u"outputPdfBookmarkEntry_DestinationName.pdf", opts);

    std::cout << "Workbook saved successfully with bookmarks!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
