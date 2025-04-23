---
title: Показать и скрыть листы и вкладки с помощью C++
linktitle: Показывать и скрывать рабочие листы и вкладки
type: docs
weight: 10
url: /ru/cpp/show-and-hide-worksheets-and-tabs/
description: В этой статье представлен пример кода для использования API или библиотеки C++ для программного отображения и скрытия листа Excel. Также объясняется, как показывать и скрывать вкладки книги Excel.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет пользователю показывать и скрывать элементы книги, включая рабочие листы и вкладки.

{{% /alert %}}

## **Показать и скрыть лист**

Файл Excel может содержать один или более листов. Всякий раз, когда мы создаем файл Excel, мы добавляем листы в файл Excel, в котором работаем. Каждый лист в файле Excel независим от другого листа и имеет свои собственные данные и настройки форматирования и т. д. Иногда разработчики могут захотеть скрыть несколько листов и сделать другие видимыми в файле Excel по своему усмотрению. Таким образом, **Aspose.Cells** позволяет разработчикам контролировать видимость листов в их файлах Excel.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), для доступа к каждому листу файла Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий набор свойств и методов для управления листами. Для управления видимостью листа используйте свойство [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) — логическое свойство, которое может хранить только значение **true** или **false**.

### **Сделать лист видимым**

Сделать лист видимым, установив свойство [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в **true**.

### **Скрыть лист**

Скрыть лист, установив свойство [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в **false**.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Показывать и скрывать вкладки**

Если вы внимательно посмотрите внизу файла Microsoft Excel, вы увидите ряд элементов управления. Среди них:

- Вкладки листов.
- Кнопки прокрутки вкладок.

Вкладки представляют листы Excel-файла. Щелкните на любой вкладке, чтобы переключиться на этот лист. Чем больше листов в книге Excel, тем больше вкладок. Если в Excel-файле большое количество листов, вам понадобятся кнопки для перемещения по ним. Поэтому Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки по вкладкам.

С помощью Aspose.Cells разработчики могут контролировать видимость вкладок листов и кнопок прокрутки в файле Excel.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) предлагает широкий набор свойств и методов для управления файлом Excel. Для управления видимостью вкладок в файле Excel разработчики могут использовать свойство [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) — логическое свойство, которое может хранить только значение **true** или **false**.

### **Отображение вкладок**

Сделайте вкладки видимыми, установив свойство [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) в **true**.

### **Скрытие вкладок**

Скрыть вкладки в файле Excel, установив свойство [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) в **false**.

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls. После выполнения кода вы увидите, что вкладки книги скрыты.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Управление Шириной Панели Вкладок**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
