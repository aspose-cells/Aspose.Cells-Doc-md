---
title: Показать и скрыть линий сетки и заголовки строк и столбцов с помощью C++
linktitle: Показывать и скрывать сетку и заголовки строк и столбцов
type: docs
weight: 30
url: /ru/cpp/show-and-hide-gridlines-and-row-column-headers/
description: Эта статья содержит пример кода для программного скрытия или отображения линий сетки и заголовков строк и столбцов листа Excel с помощью C++ API или библиотеки.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает скрытие и показ сетки листа Excel, которая обычно видна. Он также обеспечивает контроль видимости заголовков строк и столбцов листа.

{{% /alert %}}

## **Отображение и скрытие линий сетки**

Все листы Excel по умолчанию имеют сетку. Они помогают выделять клетки для удобства ввода данных. Сетка позволяет нам просматривать лист как коллекцию клеток, каждая клетка легко идентифицируется.

### **Управление видимостью сетки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую разработчикам обращаться к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр свойств и методов для управления листом. Чтобы управлять отображением линий сетки, используйте свойство класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) и свойство [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/). [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) — логическая переменная, которая может принимать значения только **true** или **false**.

#### **Отображение линий сетки**

Чтобы сделать линии сетки видимыми, установите свойство [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в значение **true**.

#### **Скрытие линий сетки**

Скрыть сеточные линии, установив свойство [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) равным **false**.

Полный пример приведен ниже, он демонстрирует использование свойства [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/), открыв файл Excel (book1.xls), скрыв линии сетки на первом листе и сохранив измененный файл как output.xls.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Показывать и скрывать заголовки строк и столбцов**

Все листы Excel состоят из клеток, расположенных в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и для идентификации отдельных клеток. Например, строки нумеруются - 1, 2, 3, 4 и т. д., а столбцы упорядочены по алфавиту - A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. С помощью Aspose.Cells разработчики могут управлять видимостью этих заголовков строк и столбцов.

### **Управление видимостью листов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет разработчикам получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий набор свойств и методов для управления листом. Чтобы управлять видимостью заголовков строк и столбцов, используйте свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) — булевое свойство, что означает, что оно может принимать только значения **true** или **false**.

#### **Отображение заголовков строк/столбцов**

Сделайте заголовки строк и столбцов видимыми, установив свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в **true**.

#### **Скрытие заголовков строк/столбцов**

Скрыть заголовки строк и столбцов, установив свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в **false**.

Приведен полный пример, показывающий, как использовать свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/), открыв файл Excel (book1.xls), скрыв заголовки строк и столбцов на первом листе и сохранив измененный файл как output.xls.

```cpp
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Также возможно использовать методы [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) и [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) класса [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) для отображения нескольких строк и столбцов.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
