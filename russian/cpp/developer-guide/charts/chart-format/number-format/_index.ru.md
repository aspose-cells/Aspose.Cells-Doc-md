---
title: Настройка кода формата значений серии графика с помощью C++
linktitle: Формат числа
type: docs
weight: 100
url: /ru/cpp/set-the-values-format-code-of-chart-series/
description: Узнайте, как установить код формата значений серии графика в Aspose.Cells for C++. Наш гид поможет понять, как форматировать данные серии графика с помощью соответствующего кода, чтобы представить данные точно и профессионально.
keywords: Aspose.Cells for C++, серии графика, код формата значений, форматирование, представление данных, точность, профессионализм.
---

## **Возможные сценарии использования**
Вы можете установить код формата значений серии графика, используя свойство [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/). Это свойство не только полезно для серий, основанных на диапазоне внутри листа, но и отлично работает с сериями, созданными с помощью массива значений.

## **Установить код формата значений серии графика**
Следующий пример кода добавляет серию в пустой график, который ранее не содержал серий. Он добавляет серию с помощью массива значений. После добавления, серия форматируется с помощью кода `$#,##0`, используя свойство [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/), и число `10000` преобразуется в `$10,000`. Скриншот показывает эффект этого кода на [примере файла Excel](51740712.xlsx) и [выходном файле Excel](51740713.xlsx) после выполнения.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
