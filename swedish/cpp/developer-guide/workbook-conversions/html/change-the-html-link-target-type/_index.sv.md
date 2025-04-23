---
title: Ändra HTML länkmålstyp med C++
linktitle: Ändra HTML länkens målknapptype
type: docs
weight: 320
url: /sv/cpp/change-the-html-link-target-type/
description: Lär dig hur man ändrar HTML länkmålstyp med Aspose.Cells for C++. Kontrollera mål attributet i HTML länkar programatiskt.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ändra målet för HTML-länken. HTML-länken ser ut så här

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se är målattributet i ovanstående HTML-länk **_self**. Du kan kontrollera det här målattributet med hjälp av egenskapen [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Den här egenskapen tar [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) uppräkningen som har följande värden.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Följande kod illustrerar användningen av egenskapen [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Den ändrar länkens måltyp till **blank**. Som standard är det **parent**.

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
