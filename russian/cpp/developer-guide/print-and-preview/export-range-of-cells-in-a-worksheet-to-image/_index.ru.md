---
title: Экспорт диапазона ячеек в рабочем листе в изображение с помощью C++
linktitle: Экспорт диапазона ячеек в изображение
type: docs
weight: 60
url: /ru/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Узнайте, как экспортировать определенный диапазон ячеек в рабочем листе в изображение с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Вы можете создать изображение листа с помощью Aspose.Cells. Однако иногда вам может потребоваться экспортировать только диапазон ячеек листа в изображение. В этой статье объясняется, как это сделать.

## **Экспорт диапазона ячеек листа в изображение**

Для создания изображения диапазона установите область печати в нужный диапазон, затем установите все поля в 0. Также установите [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) в значение **true**. Ниже приведен скриншот [образца файла Excel](47153160.xlsx), используемого в коде. Вы можете попробовать код с любым файлом Excel.

## **Скриншот образца файла Excel и его экспортированного изображения**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Выполнение кода создает изображение только для диапазона D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Образец кода**

```cpp
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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
