--- 
title: 使用C++创建Excel工作表的透明图像 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /zh/cpp/create-transparent-image-of-excel-worksheet/ 
description: 使用Aspose.Cells与C++生成Excel工作表的透明图像。 
--- 

{{% alert color="primary" %}} 

有时，您需要将工作表的图像生成为透明图像。您希望将透明度应用于所有没有填充颜色的单元格。Aspose.Cells提供[**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/)属性以将透明度应用于工作表图像。当此属性为**false**时，没有填充颜色的单元格将以白色绘制，当为**true**时，没有填充颜色的单元格将以透明绘制。 

{{% /alert %}} 

在下面的工作表图片中，没有应用透明度。没有填充颜色的单元格绘制成了白色。

|**没有透明度的输出：单元格背景为白色**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

而在下面的工作表图片中，应用了透明度。没有填充颜色的单元格是透明的。

|**启用透明度输出**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

下面的示例代码从 Excel 工作表生成一个透明的图像。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleCreateTransparentImage.xlsx");

    // Apply different image or print options
    ImageOrPrintOptions imgOption;
    imgOption.SetImageType(static_cast<ImageType>(5)); // Png
    imgOption.SetHorizontalResolution(200);
    imgOption.SetVerticalResolution(200);
    imgOption.SetOnePagePerSheet(true);

    // Apply transparency to the output image
    imgOption.SetTransparent(true);

    // Create image after applying image or print options
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOption);
    sr.ToImage(0, outputDir + u"outputCreateTransparentImage.png");

    std::cout << "Image created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
