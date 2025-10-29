---
title: 使用 C++ 将工作表渲染到图形上下文
linktitle: 将工作表呈现到图形上下文
type: docs
weight: 300
url: /zh/cpp/render-worksheet-to-graphic-context/
description: 学习如何使用 Aspose.Cells for C++ 将工作表渲染到图形上下文。
---

{{% alert color="primary" %}}

 Aspose.Cells 现在可以将工作表渲染到图形上下文。图形上下文可以是任何东西，例如图像文件、屏幕或打印机等。请使用以下两种方法之一将工作表渲染到图形上下文中。

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

 以下代码演示了如何使用 Aspose.Cells 将工作表渲染到图形上下文。一旦执行代码，它将打印整个工作表，并用蓝色填充剩余的空白区域，并将图像保存为 **OutputImage_out_.png** 文件。你可以使用任何源Excel文件来尝试此代码。请同时阅读代码中的注释以获得更好的理解。

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
