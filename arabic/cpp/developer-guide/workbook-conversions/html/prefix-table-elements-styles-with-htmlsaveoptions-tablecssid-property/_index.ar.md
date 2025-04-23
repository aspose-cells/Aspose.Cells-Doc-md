---
title: إضافة بادئة لأساليب عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId مع C++
linktitle: بادئة لأساليب عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /ar/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: تعلم كيفية بادئة أنماط عناصر الجدول باستخدام Aspose.Cells for C++ مع خاصية HtmlSaveOptions.TableCssId.
---

## **سيناريوهات الاستخدام المحتملة**

يتيح Aspose.Cells لك بادئة أنماط عناصر الجدول باستخدام مكان خاصية [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). فرضًا، إذا قمت بتعيين هذه الخاصية باسم مثل **MyTest_TableCssId**، ستجد أنماط عناصر الجدول كما هو موضح أدناه

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

اللقطة الشاشية التالية تظهر تأثير استخدام خاصية [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) على الإخراج الخاص بـ HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## ** بادئة لأساليب عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId**

يوضح الكود العينة التالي كيفية الاستفادة من خاصية [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). يرجى التحقق من [إخراج HTML](60489790.zip) الذي تم توليده بواسطة الكود للرجوع إليه.

## **الكود المثالي**

```c++
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

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - specify table css id
    HtmlSaveOptions opts;
    opts.SetTableCssId(u"MyTest_TableCssId");

    // Save the workbook in html
    wb.Save(u"outputTableCssId.html", opts);

    Aspose::Cells::Cleanup();
}
```
