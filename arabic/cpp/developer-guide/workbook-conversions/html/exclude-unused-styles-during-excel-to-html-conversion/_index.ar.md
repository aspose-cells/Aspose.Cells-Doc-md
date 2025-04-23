---
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML باستخدام C++
linktitle: استبعاد الأنماط غير المستخدمة
type: docs
weight: 30
url: /ar/cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: تعلم كيفية استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

قد تحتوي ملفات Microsoft Excel على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى صيغة HTML، يتم أيضًا تصدير هذه الأنماط غير المستخدمة، مما قد يزيد من حجم HTML. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملف Excel إلى HTML باستخدام خاصية [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/). عند ضبطها على **true**، يتم استبعاد جميع الأنماط غير المستخدمة من HTML الناتج. تعرض الصورة أدناه عينة من نمط غير مستخدم داخل HTML الناتج.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**

يُنشئ الكود النموذجي التالي دفتر عمل ويقوم أيضًا بإنشاء نمط مسمى غير مستخدم. نظرًا لضبط [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) على **true**، لن يتم تصدير هذا النمط المسمى غير المستخدم إلى [HTML الناتج](61767778.zip). ومع ذلك، إذا قمت بضبطه على **false**، فسيكون هذا النمط غير المستخدم موجودًا داخل HTML الناتج، والذي يمكنك رؤيته بعد ذلك في ترميز HTML كما هو موضح في الصورة أعلاه.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create an unused named style
    Style unusedStyle = wb.CreateStyle();
    unusedStyle.SetName(u"UnusedStyle_XXXXXXXXXXXXXX");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some value in cell C7
    ws.GetCells().Get(u"C7").PutValue(u"This is sample text.");

    // Specify html save options, we want to exclude unused styles
    HtmlSaveOptions opts;

    // Comment this line to include unused styles
    opts.SetExcludeUnusedStyles(true);

    // Save the workbook in html format
    wb.Save(u"outputExcludeUnusedStylesInExcelToHTML.html", opts);

    std::cout << "Workbook saved successfully with unused styles excluded!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
