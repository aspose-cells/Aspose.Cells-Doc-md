---
title: منع تصدير محتوى ورقة العمل المخفي عند الحفظ إلى HTML مع C++
linktitle: منع تصدير محتوى ورقة العمل المخفي
type: docs
weight: 210
url: /ar/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: تعلم كيف تمنع تصدير محتوى ورقة العمل المخفي عند حفظ ملفات إكسل إلى HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكنك حفظ سجلات العمل في Excel إلى HTML. ومع ذلك، إذا كانت سجلات العمل تحتوي على أوراق عمل مخفية، فإن Aspose.Cells بشكل افتراضي يصدر محتويات ورقة العمل المخفية إلى دليل الإخراج الخاص ب HTML (_files) الذي يحتوي على ملفات مثل أوراق العمل، الصور، tabstrip.htm، stylesheet.css إلخ. في بعض الأحيان، سيصدر محتوى أوراق العمل المخفية بهذه الطريقة ليس مناسبًا. على سبيل المثال، إذا كانت ورقة العمل المخفية تحتوي على صور يجب عدم تصديرها إلى دليل _files.

{{% /alert %}}

يوفر Aspose.Cells خاصية [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/). بشكل افتراضي، يتم تعيينها على **true** ويتم صدور أوراق العمل المخفية إلى HTML. إذا قمت بتعيينها على **false**، فإن Aspose.Cells لن يصدر محتويات ورقة العمل المخفية.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
