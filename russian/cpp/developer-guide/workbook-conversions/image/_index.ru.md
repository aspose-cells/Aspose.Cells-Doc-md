---
title: Преобразование Excel в изображение с помощью C++
linktitle: Преобразовать Excel в изображение
type: docs
weight: 300
url: /ru/cpp/convert-excel-to-image/
description: Узнайте, как преобразовать рабочие листы Excel в изображения, включая форматы TIFF и SVG, с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать лист из книги Excel и преобразовать его в различные форматы. В этой статье объясняется, как преобразовать лист в различные форматы.

{{% /alert %}}

## Преобразование книги в TIFF

Файл Excel может содержать несколько листов с несколькими страницами. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) позволяет преобразовать Excel в TIFF с несколькими страницами. Также вы можете контролировать несколько вариантов для TIFF, такие как [Сжатие](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Разрешение ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

В следующем фрагменте кода показано, как конвертировать Excel в TIFF с несколькими страницами. [Исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и [созданное изображение TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) приложены для вашего справки.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Преобразование Рабочего листа в изображение**

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоги, проценты, исключения и вычисления.

Как разработчик вам может понадобиться представить рабочие листы в виде изображений. Например, вам может потребоваться использовать изображение рабочего листа в приложении или на веб-странице. Вам может понадобиться вставить изображение в документ Microsoft Word, файл PDF, презентацию PowerPoint или в другой тип документа. Просто говоря, вам нужно, чтобы рабочий лист был отображен в виде изображения, чтобы вы могли его использовать в другом месте.

Aspose.Cells поддерживает преобразование листов Excel в изображения. Для использования этой функции необходимо импортировать пространство имён [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) в вашу программу или проект. В нем есть несколько полезных классов для рендеринга и печати, например [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) и другие.

Класс [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) представляет собой лист для рендеринга в виде изображений. В нем есть перегруженный метод [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), который может преобразовать лист в один или несколько файлов изображений с разными атрибутами или опциями. Он возвращает объект `System.Drawing.Bitmap`, и вы можете сохранить изображение в файл или поток. Поддерживаются несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Ниже приведен фрагмент кода, демонстрирующий, как преобразовать рабочий лист в Excel-файле в файл изображения.

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

В настоящее время API для преобразования листов в изображения не поддерживает 3D-графики в виде пузырьков.

{{% /alert %}}

## **Преобразование Рабочего листа в SVG**

SVG означает масштабируемую векторную графику. SVG является спецификацией на основе стандартов XML для двумерной векторной графики. Это открытый стандарт, над разработкой которого работает Консорциум Всемирной паутины (W3C) с 1999 года.

Aspose.Cells for C++ поддерживает преобразование листов в SVG изображения с версии 7.1.0. Следующий пример показывает, как преобразовать лист из файла Excel в SVG изображение.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Конвертировать диаграмму Excel в изображение](/cells/ru/cpp/convert-an-excel-chart-to-image/)
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/cpp/converting-chart-to-image-in-svg-format/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/cpp/track-conversion-progress-of-excel-to-tiff/)
