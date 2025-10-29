---
title: Фильтрация проекта VBA при загрузке книги в C++
linktitle: Фильтрация проекта VBA при загрузке книги
type: docs
weight: 140
url: /ru/cpp/filter-vba-project-while-loading-a-workbook/
description: Узнайте, как фильтровать проекты VBA при загрузке книги Excel с помощью Aspose.Cells и C++.
---

## **Фильтр проекта VBA при загрузке книги Excel в C++**

Некоторые файлы .xlsm/.xslb содержат чрезвычайно большое количество макросов (или очень длинных макросов). Aspose.Cells безусловно загружает эти метаданные при открытии таких книг. Однако вы можете управлять этим, используя [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions), если вам нужно только извлечь имена листов, пропуская ненужный содержимое. Этот фильтр реализуется с помощью нового параметра, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions).

## **Образец кода**

Приведенный ниже образец кода загружает книгу так, чтобы было выполнено только фильтрование VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
