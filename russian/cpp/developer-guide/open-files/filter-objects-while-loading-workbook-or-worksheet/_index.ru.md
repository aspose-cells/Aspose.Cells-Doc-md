---
title: Фильтрация объектов при загрузке книги или листа с помощью C++
linktitle: Фильтрование объектов при загрузке книги Excel или листа
type: docs
weight: 330
url: /ru/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Узнайте, как фильтровать объекты такие как диаграммы, фигуры и условное форматирование при загрузке книг или листов с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Пожалуйста, используйте свойство [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) для фильтрации данных при загрузке книги. Но если нужно фильтровать данные из отдельных листов, необходимо переопределить метод [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Укажите соответствующее значение из перечисления [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) при создании или работе с [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

Перечисление [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) имеет следующие возможные значения.

- Все
- Настройки книги
- Пустая ячейка
- Булева ячейка
- Данные ячейки
- Ошибка ячейки
- Числовая ячейка
- Строковая ячейка
- Значение ячейки
- Chart
- Условное форматирование
- Проверка данных
- Определенные имена
- Свойства документа
- Формула
- Гиперссылки
- ОбъединеннаяОбласть
- СводнаяТаблица
- Настройки
- Фигура
- ДанныеЛиста
- НастройкиЛиста
- Структура
- Стиль
- Таблица
- VBA
- XmlMap

## **Фильтрование объектов при загрузке книги Excel**
Приведенный ниже образец кода демонстрирует, как фильтровать диаграммы из книги Excel. Пожалуйста, проверьте [образец excel файла](5115258.xlsx), использованный в этом коде, и [выходной PDF](5115257.pdf), сгенерированный им. Как видно из выходного PDF, все диаграммы были отфильтрованы из книги Excel.

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

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Фильтрование объектов при загрузке Листа**
Приведенный ниже образец кода загружает [исходный файл Excel](5115255.xlsx) и фильтрует следующие данные из его листов, используя пользовательский фильтр.

- Он фильтрует Диаграммы из листа с именем NoCharts.
- Он фильтрует формы из листа с именем NoShapes.
- Он фильтрует Условное форматирование из листа с именем NoConditionalFormatting.

После загрузки [исходного файла Excel](5115255.xlsx) с пользовательским фильтром он берет изображения со всех листов один за другим. Здесь представлены изображения для вашего ознакомления. Как видно, на первом изображении нет диаграмм, на втором - нет фигур, на третьем - нет условного форматирования.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

Вот как использовать класс CustomLoadFilter согласно именам листов.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
