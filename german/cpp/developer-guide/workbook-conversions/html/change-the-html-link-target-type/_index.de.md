---
title: HTML Linkzieltyp mit C++ ändern
linktitle: Ändern Sie den HTML Linkzieltyp
type: docs
weight: 320
url: /de/cpp/change-the-html-link-target-type/
description: Lernen Sie, wie man den HTML Linkzieltyp mit Aspose.Cells for C++ ändert. Kontrollieren Sie das Zielattribut in HTML Links programmatisch.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, den Typ des HTML-Links zu ändern. Ein HTML-Link sieht so aus

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Wie Sie sehen können, ist das target-Attribut im obigen HTML-Link **_self**. Sie können dieses target-Attribut mit der [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/)-Eigenschaft steuern. Diese Eigenschaft nimmt das [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/)-Enum, das folgende Werte hat.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Der folgende Code veranschaulicht die Verwendung der [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/)-Eigenschaft. Er ändert den Link-Zieltyp auf **blank**. Standardmäßig ist es **parent**.

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
