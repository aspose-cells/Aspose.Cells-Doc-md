---
title: Фильтрация данных с помощью C++
linktitle: Фильтрация данных
type: docs
weight: 85
url: /ru/cpp/data-filtering/
description: Узнайте, как добавить фильтр данных с помощью API Aspose.Cells for C++.
keywords: Добавить фильтр по цвету, добавить фильтры по дате, добавить числовые фильтры, добавить динамический фильтр, добавить текстовые фильтры, добавить пользовательский фильтр с содержанием, добавить пользовательский фильтр с исключением содержания, добавить пользовательский фильтр с началом, добавить пользовательский фильтр с окончанием
---

{{% alert color="primary" %}}

Microsoft Excel предоставляет некоторые хорошие функции для автофильтрации данных на листе. Aspose.Cells полностью поддерживает автофильтрацию Microsoft Excel. В этой статье объясняется, как использовать функции в Microsoft Excel и как написать код для их использования с помощью Aspose.Cells.

{{% /alert %}}

## **Автофильтрация данных**

Автофильтрация - самый быстрый способ выбрать только те элементы с листа, которые вы хотите отображать в списке. Функция автофильтрации позволяет фильтровать элементы в списке в соответствии с набором критериев. Отфильтруйте на основе текста, чисел или дат.

### **Автофильтр в Microsoft Excel**

Чтобы активировать функцию автофильтра в Microsoft Excel:

1. Щелкните строку заголовка на листе.
1. В меню **Данные** выберите **Фильтр**, а затем **Автофильтр**.

При применении автофильтра к листу появляются переключатели фильтра (черные стрелки) справа от заголовков столбцов.

1. Щелкните стрелку фильтра, чтобы увидеть список вариантов фильтра.

Некоторые из вариантов автофильтра:

|**Опции**|**Описание**|
| :- | :- |
|All|Показать все элементы в списке один раз.|
|Custom|Настроить критерии фильтрации, такие как содержит/не содержит.|
|Filter by Color|Фильтрация на основе заполненного цвета.|
|Date Filters|Фильтрация строк на основе различных критериев по дате.|
|Number Filters|Несколько видов фильтров для чисел, таких как сравнение, средние значения и Топ-10 и т.д.|
|Text Filters|Различные фильтры, такие как начинается с, заканчивается на, содержит и т. д.|
|Blanks/Non Blanks|Эти фильтры могут быть применены с помощью пустого текстового фильтра.|

Пользователи вручную фильтруют данные своего листа в Microsoft Excel, используя эти опции.

### **Автофильтр с Aspose.Cells**

Aspose.Cells предоставляет класс `Workbook`, который представляет файл Excel. Класс `Workbook` содержит коллекцию `Worksheets`, которая дает доступ к каждому листу в файле Excel.

Лист представлен классом `Worksheet`. Класс `Worksheet` предоставляет широкий набор свойств и методов для управления листами. Чтобы создать автофильтр, используйте свойство `AutoFilter` класса `Worksheet`. Свойство `AutoFilter` — это объект класса `AutoFilter`, который содержит свойство `Range` для указания диапазона ячеек, образующего заголовочную строку. Автофильтр применяется к диапазону ячеек, являющемуся заголовком.

На каждом листе можно указать только один диапазон фильтрации. Это ограничение Microsoft Excel. Для настройки пользовательской фильтрации данных используйте метод `AutoFilter.Custom`.

В приведенном ниже примере мы создали тот же AutoFilter, используя Aspose.Cells, что и создали с помощью Microsoft Excel в предыдущем разделе.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Различные типы фильтров**

Aspose.Cells предоставляет несколько вариантов применения различных типов фильтров, таких как Фильтр по цвету, Фильтр по дате, Фильтр по числам, Фильтр по тексту, Фильтры для заполненных ячеек и незаполненных ячеек.

##### **Цвет заливки**

Aspose.Cells предоставляет функцию `AddFillColorFilter`, чтобы фильтровать данные по цвету заливки ячеек. В приведенном ниже примере используется шаблонный файл с разными цветами заливки в первом столбце листа для тестирования функции цветового фильтра. Образцы файлов можно загрузить по следующим ссылкам.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Дата**

Можно реализовать различные типы фильтров по дате, например, фильтрацию всех строк с датами в январе 2018 года. Следующий пример демонстрирует этот фильтр с помощью функции `AddDateFilter`. Образцы файлов приведены ниже.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Динамическая дата**

Иногда требуются динамические фильтры на основе даты, например, все ячейки с датами в январе независимо от года. В таком случае используется функция `DynamicFilter`, как показано в следующем примере. Образцы файлов приведены ниже.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Число**

Можно применить пользовательские фильтры с помощью Aspose.Cells, например, выбрать ячейки с числом в определенном диапазоне. Следующий пример демонстрирует использование функции `Custom()` для фильтрации чисел. Образцы файлов приведены ниже.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Текст**

Если в столбце содержится текст и необходимо выбрать ячейки с определенным текстом, можно использовать функцию `Filter()`. В следующем примере шаблонный файл содержит список стран, и необходимо выбрать строку с определенным названием страны. Этот код демонстрирует фильтрацию текста. Образцы файлов приведены ниже.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

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
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Пустые**

Если столбец содержит текст, при этом некоторые ячейки пустые, и требуется фильтрация только тех строк, где присутствуют пустые ячейки, можно использовать функцию `MatchBlanks()` как показано ниже. Примеры файлов приведены ниже.

1. [Пустой.xlsx](72417324.xlsx)
1. [ОтфильтрованныйПустой.xlsx](72417325.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Не пустые**

Когда необходимо отфильтровать ячейки с любым текстом, используйте функцию фильтра `MatchNonBlanks`, как показано ниже. Примеры файлов приведены ниже.

1. [Пустой.xlsx](72417324.xlsx)
1. [ОтфильтрованныеНеПустой.xlsx](72417326.xlsx)

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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Пользовательский фильтр с содержит**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, содержащих определенную подстроку. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в примере файла. Приведены примеры файлов.

1. [ИсходныйОбразецНазванийСтран.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Пользовательский фильтр с не содержит**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, которые не содержат определенную строку. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в предоставленном образце файла.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Пользовательский фильтр с начинается с**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, которые начинаются с определенной строки. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в предоставленном образце файла.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Пользовательский фильтр с EndsWith**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, оканчивающихся определенной подстрокой. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в указанном примере файла.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Применение расширенного фильтра Microsoft Excel для отображения записей, удовлетворяющих сложным критериям](/cells/ru/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Получить все скрытые индексы строк после обновления автофильтра](/cells/ru/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="cpp" >}}
