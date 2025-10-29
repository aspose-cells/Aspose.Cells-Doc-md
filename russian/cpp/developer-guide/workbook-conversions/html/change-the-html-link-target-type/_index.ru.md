---
title: Изменение типа назначения ссылки HTML с помощью C++
linktitle: Изменить тип HTML ссылки
type: docs
weight: 320
url: /ru/cpp/change-the-html-link-target-type/
description: Узнайте, как изменить тип назначения ссылки HTML с помощью Aspose.Cells for C++. Управляйте атрибутом target в HTML ссылках программно.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет вам изменять тип целевой ссылки HTML. HTML-ссылка выглядит так

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как видно из атрибута target в указанной выше HTML-ссылке **_self**. Вы можете контролировать этот атрибут target, используя свойство [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Это свойство принимает перечисление [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/), которое имеет следующие значения.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Приведенный ниже код иллюстрирует использование свойства [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Он изменяет тип целевой ссылки на **blank**. По умолчанию это **parent**.

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
{{< app/cells/assistant language="cpp" >}}
