---
title: Change the HTML Link Target Type with C++
linktitle: Change the HTML Link Target Type
type: docs
weight: 320
url: /cpp/change-the-html-link-target-type/
description: Learn how to change the HTML link target type using Aspose.Cells for C++. Control the target attribute in HTML links programmatically.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to change the HTML link target type. HTML link looks like this

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

As you can see the target attribute in the above HTML link is **_self**. You can control this target attribute using the [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/) property. This property takes the [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) enum which has the following values.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

The following code illustrates the usage of [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/) property. It changes the link target type to **blank**. By default, it is the **parent**.

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
