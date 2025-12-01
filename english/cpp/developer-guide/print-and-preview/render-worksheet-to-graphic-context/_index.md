---
title: Render Worksheet to Graphic Context with C++
linktitle: Render Worksheet to Graphic Context
type: docs
weight: 300
url: /cpp/render-worksheet-to-graphic-context/
description: Learn how to render a worksheet to a graphic context using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells can now render a worksheet to a graphic context. The graphic context can be anything like an image file, screen, or printer, etc. Please use one of the following two methods to render a worksheet to a graphic context.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

The following code illustrates how to use Aspose.Cells to render a worksheet to a graphic context. Once you execute the code, it will print the entire worksheet and fill the leftover empty space with blue color in the graphics context and save the image as **OutputImage_out_.png** file. You can use any source Excel file to try this code. Please also read the comments inside the code for better understanding.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
