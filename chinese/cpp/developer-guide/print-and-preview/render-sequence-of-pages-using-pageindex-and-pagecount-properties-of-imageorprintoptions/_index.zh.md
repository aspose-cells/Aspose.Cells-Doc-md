---
title: 使用ImageOrPrintOptions的PageIndex和PageCount属性渲染页面序列（C++）
linktitle: 渲染页面序列
type: docs
weight: 110
url: /zh/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
description: 使用 Aspose.Cells 和 C++ 将 Excel 文件的页面序列渲染为图像。
---

## **可能的使用场景**

您可以使用 Aspose.Cells 和 [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) 和 [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/) 属性将 Excel 文件的一系列页面呈现为图像。当您的工作表中有成千上万页但您只想呈现其中一些时，这些属性是有用的。这不仅可以节省处理时间，还可以节省呈现过程中的内存消耗。

## **使用ImageOrPrintOptions的PageIndex和PageCount属性呈现页面序列**

以下示例代码加载了[sample Excel file](55541781.xlsx)并仅使用[**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/)和[**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/)属性呈现了页面4、5、6和7。以下是代码生成的呈现页面。

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **示例代码**

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleImageOrPrintOptions_PageIndexPageCount.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetPageIndex(3);
    opts.SetPageCount(4);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(ws, opts);

    for (int i = opts.GetPageIndex(); i < sr.GetPageCount(); i++)
    {
        std::wstring pageNum = std::to_wstring(i + 1);
        U16String filePath = outDir + U16String(u"outputImage-") + 
            U16String(reinterpret_cast<const char16_t*>(pageNum.c_str())) + 
            U16String(u".png");
        sr.ToImage(i, filePath);
    }

    std::cout << "Images generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
