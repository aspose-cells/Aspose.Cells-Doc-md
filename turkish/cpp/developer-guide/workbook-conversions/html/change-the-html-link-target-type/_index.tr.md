---
title: HTML Bağlantı Hedef Türünü Değiştir
linktitle: HTML Bağlantısı Hedef Türünü Değiştirme
type: docs
weight: 320
url: /tr/cpp/change-the-html-link-target-type/
description: Aspose.Cells for C++ kullanarak HTML bağlantı hedef türünü nasıl değiştireceğinizi öğrenin. Bağlantıların hedef özniteliğini programlı olarak kontrol edin.
---

{{% alert color="primary" %}}

Aspose.Cells, HTML bağlantı hedef türünü değiştirmenize olanak tanır. HTML bağlantısı şuna benzer

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısında hedef özniteliği **_self** olarak gösterilir. Bu hedef özniteliğini [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/) özelliğini kullanarak kontrol edebilirsiniz. Bu özellik, aşağıdakileri içeren [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) enumunu alır.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Aşağıdaki kod, [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/) özelliğinin kullanımını gösterir. Bağlantı hedef türünü varsayılan olarak **parent** olarak değiştirir.

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
