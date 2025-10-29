---
title: 用C++更改HTML链接目标类型
linktitle: 更改HTML链接的目标类型
type: docs
weight: 320
url: /zh/cpp/change-the-html-link-target-type/
description: 学习如何使用编号Aspose.Cells for C++更改HTML链接的目标类型，程序化控制HTML链接中的target属性。
---

{{% alert color="primary" %}}

Aspose.Cells 允许您更改 HTML 链接的目标类型。 HTML 链接看起来像这样

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如您所见，上述HTML链接中的target属性是**_self**。您可以使用[**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/)属性来控制此target属性。此属性采用了[**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/)枚举，其具有以下值。

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::顶部

{{% /alert %}}

以下代码说明了 [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/) 属性的用法。 它将链接目标类型更改为 **blank**。 默认情况下，它是 **parent**。

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
