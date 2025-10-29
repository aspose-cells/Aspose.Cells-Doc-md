---
title: تعيين عرض العمود إلى وحدة قابلة للتوسيع مثل em أو النسبة المئوية باستخدام C++
linktitle: تعيين عرض العمود إلى وحدة قابلة للتوسيع مثل em أو percent
type: docs
weight: 130
url: /ar/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: تعلم كيفية تعيين عرض العمود إلى وحدات قابلة للتوسيع مثل em أو النسبة المئوية باستخدام Aspose.Cells for C++.
---

إن إنشاء ملف HTML من جدول بيانات يعتبر شائعًا جدًا. يتم تعريف حجم الأعمدة بـ "pt" والذي يعمل في العديد من الحالات. ومع ذلك، يمكن أن يكون هناك حالة حيث قد لا يكون هذا الحجم الثابت مطلوبًا. على سبيل المثال، إذا كان عرض لوحة الحاوية 600 بكسل حيث يتم عرض صفحة HTML، فيجب تغيير هذا الحجم الثابت إلى وحدة قابلة للتوسيع مثل em أو percent للحصول على عرض عرض أفضل. يمكن استخدام الرمز العيني التالي حيث يُعين [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) على **true** لإنشاء عرض قابل للتوسيع.

يمكن تنزيل ملف المصدر العيني وملفات الإخراج من الروابط التالية:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```c++
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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
