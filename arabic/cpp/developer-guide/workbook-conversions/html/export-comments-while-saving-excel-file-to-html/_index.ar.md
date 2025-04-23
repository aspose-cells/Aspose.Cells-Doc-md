--- 
title: تصدير التعليقات عند حفظ ملف Excel إلى HTML باستخدام C++ 
linktitle: تصدير التعليقات أثناء حفظ ملف Excel إلى HTML 
type: docs 
weight: 40 
url: /ar/cpp/export-comments-while-saving-excel-file-to/ 
description: تعلم كيفية تصدير التعليقات عند حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells مع C++. 
--- 

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel بصيغة HTML، لا يتم تصدير التعليقات. ومع ذلك، توفر Aspose.Cells هذه الميزة باستخدام خاصية [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). إذا قمت بضبطها على **true**، فسيتم عرض التعليقات الموجودة في ملف Excel الخاص بك في HTML أيضًا.

## **تصدير التعليقات أثناء حفظ ملف Excel إلى HTML**

يشرح الكود النموذجي التالي استخدام خاصية [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). تُظهر الصورة تأثير الكود على HTML عند ضبطها على **true**. يرجى تنزيل [ملف Excel العيني](50528260.xlsx) و [HTML المولد](5052826.txt) كمراجع.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
