---
title: تحويل ملف Excel إلى صيغة PDF متوافقة مع PDFA 1a باستخدام C++
linktitle: تحويل ملف Excel إلى صيغة PDF متوافقة مع PDFA 1a
type: docs
weight: 130
url: /ar/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: تعلم كيفية تحويل ملفات Excel إلى صيغة PDF / A 1a المتوافقة باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

 PDF/A هو نوع فريد من PDF مصمم للحفاظ طويل الأمد على المستندات. PDF / A هو إصدار قياسي من تنسيق المستندات المحمولة (PDF) وهو تنسيق أرشيفي لـ PDF يدمج جميع الخطوط المستخدمة في المستند داخل ملف PDF. يختلف PDF / A عن PDF من خلال حظر الميزات، مثل ربط الخطوط (مقابل تضمين الخطوط) والتشفير. يمكّنك Aspose.Cells من حفظ ملفات Excel بصيغة PDF / A متوافقة (PDF / A-1a، PDF / A-1b، PDF / A-2a، PDF / A-2b، PDF / A-2u، PDF / A-3a، PDF / A-2ab، وPDF / A-3u مدعومة). يصف هذا الموضوع كيف تحفظ دفتر عمل Excel إلى ملف PDF متوافق مع PDF / A (PDF / A-1a).

## **تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a**

يمكن للمطورين استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) لضبط سمات مختلفة للتحويل. ضبط خصائص مختلفة من فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان، والضغط لملف PDF الناتج. الخاصية الأهم هي [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) التي تمكنك من حفظ ملفات Excel إلى ملفات PDF / A متوافقة.

يشرح الكود النموذجي التالي كيفية تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a. يرجى الاطلاع على [المخرج PDF](outputCompliancePdfA1a.pdf) بالإضافة إلى لقطة الشاشة للرجوع إليها.

## **لقطة شاشة**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **الكود المثالي**

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
