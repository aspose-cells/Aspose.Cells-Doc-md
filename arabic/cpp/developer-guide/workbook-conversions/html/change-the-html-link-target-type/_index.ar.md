---
title: تغيير نوع هدف رابط HTML باستخدام C++
linktitle: تغيير نوع الوجهة للرابط HTML
type: docs
weight: 320
url: /ar/cpp/change-the-html-link-target-type/
description: تعلم كيفية تغيير نوع هدف رابط HTML باستخدام Aspose.Cells for C++. التحكم في سمة الهدف في روابط HTML برمجياً.
---

{{% alert color="primary" %}}

تُتيح Aspose.Cells لك تغيير نوع الوجهة للرابط HTML. يبدو الرابط HTML على النحو التالي

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترون، فإن سمة الوجهة في الرابط HTML أعلاه هي **_self**. يمكنك التحكم في هذه سمة الوجهة باستخدام ال [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). تأخذ هذه الخاصية ال [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) الذي يحتوي على القيم التالية.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

الشفرة العينية التالية توضح استخدام ال [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). يغيّر نوع الوجهة للرابط إلى **blank**. بشكل افتراضي، يكون هو الـ **الرئيسي**.

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
    U16String inputPath = srcDir + u"Sample1.xlsx";

    // Path of output HTML file
    U16String outputPath = outDir + u"Output.out.html";

    // Create workbook
    Workbook workbook(inputPath);

    // Create HTML save options
    HtmlSaveOptions opts;
    opts.SetLinkTargetType(HtmlLinkTargetType::Self);

    // Save the workbook to HTML format
    workbook.Save(outputPath, opts);

    std::cout << "File saved: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
