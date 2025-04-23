---
title: تصدير إكسل إلى HTML مع خطوط الشبكة باستخدام C++
linktitle: تصدير Excel إلى HTML مع خطوط الشبكة
type: docs
weight: 40
url: /ar/cpp/export-excel-to-html-with-gridlines/
description: تعلم كيفية تصدير ملفات إكسل إلى HTML مع خطوط الشبكة باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

إذا كنت ترغب في تصدير ملف إكسل الخاص بك إلى HTML مع خطوط الشبكة، فالرجاء استخدام الخاصية [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) وتعيينها إلى **صحيح**.

{{% /alert %}} 

## **تصدير Excel إلى HTML مع خطوط الشبكة**
ينشئ رمز النموذج التالي مصنف العمل ويمتلئ ورقته ببعض القيم ثم يحفظه بتنسيق HTML بعد تعيين [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) إلى **صحيح**.

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

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Fill worksheet with some integer values
    for (int r = 0; r < 10; r++)
    {
        for (int c = 0; c < 10; c++)
        {
            ws.GetCells().Get(r, c).PutValue(r * 1);
        }
    }

    // Save workbook in HTML format and export gridlines
    HtmlSaveOptions opts;
    opts.SetExportGridLines(true);
    wb.Save(outDir + u"ExportToHTMLWithGridLines_out.html", opts);

    std::cout << "Workbook exported to HTML with gridlines successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
