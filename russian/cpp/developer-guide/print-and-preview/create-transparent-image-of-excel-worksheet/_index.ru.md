--- 
title: Создание прозрачного изображения рабочего листа Excel с помощью C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /ru/cpp/create-transparent-image-of-excel-worksheet/ 
description: Создавайте прозрачные изображения рабочих листов Excel с помощью Aspose.Cells и C++. 
--- 

{{% alert color="primary" %}} 

Иногда вам может потребоваться создать изображение вашего листа как прозрачное изображение. Вы хотите применить прозрачность ко всем ячейкам без цвета заливки. Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/) для применения прозрачности к изображению листа. Когда это свойство имеет значение **false**, то ячейки без цвета заливки рисуются белым цветом, а когда оно имеет значение **true**, то ячейки без цвета заливки рисуются прозрачными. 

{{% /alert %}} 

На следующем изображении листа прозрачность не была применена. Ячейки без цвета заливки рисуются белым цветом.

|**Вывод без прозрачности: фон ячейки белый**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

Тогда как на следующем изображении листа прозрачность была применена. Ячейки без цвета заливки рисуются прозрачными.

|**Вывод со включенной прозрачностью**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

Следующий образец кода генерирует прозрачное изображение из листа Excel.

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
