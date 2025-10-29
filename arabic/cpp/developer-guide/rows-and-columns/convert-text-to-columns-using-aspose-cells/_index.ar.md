---
title: تحويل النص إلى أعمدة باستخدام Aspose.Cells مع C++
linktitle: تحويل النص إلى أعمدة
type: docs
weight: 30
url: /ar/cpp/convert-text-to-columns-using-aspose-cells/
description: تعلم كيفية تحويل النص إلى أعمدة في ملفات إكسل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تحويل نصك إلى أعمدة باستخدام برنامج Microsoft Excel. تتوفر هذه الميزة من خلال أدوات البيانات تحت علامة تبويب البيانات. من أجل تقسيم محتويات العمود إلى أعمدة متعددة, يجب أن يحتوي البيانات على فاصل محدد مثل الفاصلة (أو أي حرف آخر) على أساسه يقوم Microsoft Excel بتقسيم محتويات الخلية إلى خلايا متعددة. توفر Aspose.Cells أيضاً هذه الميزة من خلال الطريقة [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/).

## **تحويل النص إلى أعمدة باستخدام Aspose.Cells**

 يوضح رمز النموذج التالي استخدام طريقة [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/). يضيف الكود أولاً بعض أسماء الأشخاص في العمود أ من ورقة العمل الأولى. يتم فصل الاسم الأول والأخير بواسطة حرف فراغ. ثم يطبق طريقة [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) على العمود أ ويحفظه كملف إكسل مخرجات. إذا فتحت ملف إكسل المخرجات ([output Excel file](25395213.xlsx))، سترى أن الأسماء الأولى في العمود أ والأسماء الأخيرة في العمود ب كما يظهر في هذه الصورة.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **الكود المثالي**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
