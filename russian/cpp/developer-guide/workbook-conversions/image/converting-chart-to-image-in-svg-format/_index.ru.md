---
title: Преобразование диаграммы в изображение в формате SVG с C++
linktitle: Преобразование диаграммы в изображение в формате SVG
type: docs
weight: 240
url: /ru/cpp/converting-chart-to-image-in-svg-format/
description: Узнайте, как конвертировать диаграммы в SVG изображения с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Масштабируемая векторная графика (SVG) - это формат векторных изображений на основе XML для двумерной графики, который также поддерживает интерактивность и анимацию. Спецификация SVG является открытым стандартом, разработанным Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определены в XML-текстовых файлах. Это означает, что их можно искать, индексировать, сценаризировать и сжимать. Как XML-файлы, изображения SVG могут быть созданы и отредактированы с использованием любого текстового редактора, но их чаще создают с помощью графического программного обеспечения.

Aspose.Cells может сохранять диаграммы в виде изображений в различных форматах, таких как BMP, JPEG, PNG, GIF, SVG и др. В этой статье объясняется, как сохранить диаграмму в формате SVG.

{{% /alert %}}

В следующем образце кода объясняется, как использовать Aspose.Cells для преобразования диаграммы в изображение в формате SVG. Код загружает исходный файл Microsoft Excel, а затем сохраняет первую найденную диаграмму на первом листе в SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
