---
title: Загрузить исходный Excel файл без диаграмм с помощью C++
linktitle: Загрузить исходный файл Excel без диаграмм
type: docs
weight: 420
url: /ru/cpp/load-source-excel-file-without-charts/
description: Узнайте, как загрузить Excel файл без диаграмм с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет загружать ваши файлы Excel без диаграмм. Используйте свойство [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) для этого.

{{% /alert %}}

## **Загрузить электронную таблицу без диаграмм**

Следующий пример кода загружает пример файла Excel без диаграмм и сохраняет его в формате PDF.

```c++
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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
