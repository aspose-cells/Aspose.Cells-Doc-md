---
title: تعيين الخط الافتراضي أثناء تحويل جدول البيانات إلى صور باستخدام C++
linktitle: تعيين الخط الافتراضي
type: docs
weight: 360
url: /ar/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: تعلم كيفية تعيين الخط الافتراضي أثناء تحويل جداول البيانات إلى صور باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يرجى استخدام خاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) لتعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور. ستكون هذه الخاصية فعالة فقط عندما لا يمكن للخط الافتراضي للدفتر تقديم حروفك. يتم استخدام الخط الافتراضي المحدد بواسطة الخاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) لجميع تلك الخلايا التي تحتوي على خطوط غير صحيحة أو غير موجودة.

{{% /alert %}}

## تعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور

الشيفرة النموذجية التالية تنشئ دفتر عمل، تضيف بعض النص في الخلية A4 من الورقة العمل الأولى، وتعين خطه إلى خط غير صحيح أو غير موجود. ثم، تأخذ صورتين للورقة العمل. تُأخذ الصورة الأولى من خلال تعيين الخاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) إلى *Courier New* وتُأخذ الصورة الثانية من خلال تعيين الخاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) إلى *Times New Roman*.

هذه الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) إلى *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

هذه الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) إلى *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## كود عينة

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Set default font of the workbook to none
    Style s = wb.GetDefaultStyle();
    s.GetFont().SetName(u"");
    wb.SetDefaultStyle(s);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"A4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell A4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    st.SetIsTextWrapped(true);
    cell.SetStyle(st);

    // Set first column width and fourth column height
    ws.GetCells().SetColumnWidth(0, 80);
    ws.GetCells().SetRowHeight(3, 60);

    // Create image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    // Render worksheet image with Courier New as default font
    opts.SetDefaultFont(u"Courier New");
    SheetRender sr(ws, opts);
    sr.ToImage(0, outDir + u"out_courier_new_out.png");

    // Render worksheet image again with Times New Roman as default font
    opts.SetDefaultFont(u"Times New Roman");
    SheetRender sr2(ws, opts);
    sr2.ToImage(0, outDir + u"times_new_roman_out.png");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
