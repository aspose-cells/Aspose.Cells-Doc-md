---
title: إضافة النص الغني HTML داخل الخلية باستخدام C++
linktitle: قيمة سلسلة HTML
type: docs
weight: 50
url: /ar/cpp/adding-html-rich-text-inside-the-cell/
description: تعلم كيفية إضافة النص الغني HTML داخل الخلية من خلال واجهة برمجة تطبيقات Aspose.Cells for C++.
keywords: إضافة Rich Text HTML داخل الخلية، تعيين Rich Text HTML داخل الخلية، إضافة Rich Text HTML في الخلية
---

{{% alert color="primary" %}}

Aspose.Cells يدعم تحويل HTML موجه من Microsoft Excel إلى تنسيق XLS/XLSX. يعني أن HTML الذي تم إنشاؤه بواسطة Microsoft Excel يمكن تحويله مرة أخرى إلى تنسيق XLS/XLSX باستخدام Aspose.Cells.

 بالمثل، إذا كان هناك HTML بسيط، يمكن لـ Aspose.Cells تحويله إلى نص غني بصيغة HTML. توفر Aspose.Cells طريقة [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) التي يمكنها أخذ هذا HTML البسيط وتحويله إلى نص خلية منسق.

{{% /alert %}}

تُظهر الشيفرة العينية أدناه كيفية إضافة نص HTML غني داخل الخلية. يرجى الاطلاع على لقطة شاشة لملف الإكسل الناتج.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## مقالات ذات صلة

- [عرض الرموز باستخدام قيمة الخلية باستخدام HTML](/cells/ar/cpp/display-bullets-by-setting-cell-value-using/)
- [الحصول على سلسلة HTML5 من الخلية](/cells/ar/cpp/get-html5-string-from-cell/)
