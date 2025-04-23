---  
title: 在没有内容时输出空白页面（C++）  
linktitle: 当没有要打印的内容时输出空白页  
type: docs  
weight: 90  
url: /zh/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: 使用C++处理空工作表并打印空白页面  
---  

## **可能的使用场景**  

如果工作表为空，Aspose.Cells在导出工作表为图像时不会打印任何内容。可以通过设置[**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/)属性改变此行为。当将其设置为**true**时，将会打印空白页面。  

## **当没有要打印的内容时输出空白页**  

以下示例代码创建了一个空工作簿，其包含一个空工作表，并在设置[**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/)属性为**true**后将其渲染为图像。因此，生成了空白页面，你可以在下方的图片中看到。  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **示例代码**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
