---
title: تصدير خصائص المستند ودفتر العمل وورقة العمل في تحويل Excel إلى HTML باستخدام C++
linktitle: تصدير خصائص المستند ودفتر العمل وورقة العمل في تحويل Excel إلى HTML
type: docs
weight: 50
url: /ar/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: تعلم كيف تصدر أو تتجنب تصدير خصائص المستند ودفتر العمل وورقة العمل عند تحويل ملفات Excel إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند تصدير ملف Microsoft Excel إلى HTML باستخدام Microsoft Excel أو Aspose.Cells، يتم أيضًا تصدير أنواع مختلفة من خصائص المستند ودفتر العمل وورقة العمل كما هو موضح في الصورة أدناه. يمكنك تجنب تصدير هذه الخصائص بضبط [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/)، [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/)، و[**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) على **false**. القيمة الافتراضية لهذه الخصائص هي **true**. تُظهر الصورة أدناه كيف تبدو هذه الخصائص في HTML المصدّر.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **تصدير خصائص مستند التصدير، كتاب العمل، وورقة العمل في تحويل إكسل إلى HTML**

يحمل رمز المثال التالي ملف Excel النموذجي ويحوّله إلى HTML بدون تصدير خصائص المستند ودفتر العمل وورقة العمل في [HTML الناتج](61767779.zip).

## **الكود المثالي**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html";

    // Load the sample Excel file
    Workbook workbook(inputFilePath);

    // Specify Html Save Options
    HtmlSaveOptions options;

    // We do not want to export document, workbook and worksheet properties
    options.SetExportDocumentProperties(false);
    options.SetExportWorkbookProperties(false);
    options.SetExportWorksheetProperties(false);

    // Export the Excel file to Html with Html Save Options
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file exported to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
