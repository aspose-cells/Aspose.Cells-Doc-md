---
title: Render Worksheet to Graphic Context with C++
linktitle: Render Worksheet to Graphic Context
type: docs
weight: 300
url: /cpp/render-worksheet-to-graphic-context/
description: Learn how to render a worksheet to a graphic context using Aspose.Cells for C++.
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
#include "Aspose.Cells/Rendering/ImageOrPrintOptions.h"
#include "Aspose.Cells/Rendering/SheetRender.h"
#include "Aspose.Cells/Systems/Drawing/Graphics.h"
#include "Aspose.Cells/Systems/Drawing/Bitmap.h"
#include "Aspose.Cells/Systems/Drawing/Color.h"
#include "Aspose.Cells/Systems/Drawing/Imaging/ImageFormat.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Systems::Drawing;
using namespace Aspose::Cells::Systems::Drawing::Imaging;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object from source file
    Workbook workbook(srcDir + u"SampleBook.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create empty Bitmap
    std::shared_ptr<Bitmap> bmp = std::make_shared<Bitmap>(1100, 600);

    // Create Graphics Context
    std::shared_ptr<Graphics> g = Graphics::FromImage(bmp);
    g->Clear(Color::Blue);

    // Set one page per sheet to true in image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);

    // Render worksheet to graphics context
    SheetRender sr(worksheet, opts);
    sr.ToImage(0, g.get(), 0, 0);

    // Save the graphics context image in Png format
    bmp->Save(outDir + u"OutputImage_out.png", ImageFormat::GetPng());

    Aspose::Cells::Cleanup();
}
```