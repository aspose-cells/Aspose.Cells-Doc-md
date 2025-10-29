---
title: Фильтрация типа данных при загрузке книги из файла шаблона с помощью C++
linktitle: Фильтрация данных при загрузке книги
type: docs
weight: 400
url: /ru/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Узнайте, как фильтровать определённые типы данных при загрузке книги из файла шаблона с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Иногда вы хотите указать, какой именно вид данных должен быть загружен при построении книги из файла-шаблона. Фильтрация загруженных данных может улучшить производительность для ваших целей, особенно при использовании [LightCells API](/cells/ru/cpp/using-lightcells-api/). Пожалуйста, используйте свойство [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) для этой цели.

{{% /alert %}}

Приведенный ниже образец кода загружает только объекты формы при загрузке книги из [файла шаблона](5115552.xlsx), который вы можете скачать по указанной ссылке. На следующем снимке экрана показано содержимое [файла шаблона](5115552.xlsx) и также объясняется, что данные красного цвета и с желтым фоном не будут загружены, потому что свойство [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) установлено на [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

На следующем снимке экрана показан [выходной PDF](5115555.pdf), который вы можете скачать по указанной ссылке. Здесь вы можете видеть, что данные красного цвета и с желтым фоном отсутствуют, но все формы присутствуют.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
