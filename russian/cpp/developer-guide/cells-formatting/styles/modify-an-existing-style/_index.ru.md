---
title: Изменение существующего стиля с помощью C++
description: Aspose.Cells — это библиотека на C++ для работы с файлами электронных таблиц, которая позволяет изменять существующие стили ячеек. В этой статье расскажем, как изменить существующий стиль ячейки с помощью библиотеки Aspose.Cells, чтобы пользователи могли менять внешний вид ячеек по необходимости.
keywords: Изменение существующих стилей, настройка внешнего вида вашего приложения, руководства, учебные пособия, справочная документация, документация по разработке, ссылки на API, образцы кода, загрузки, поддержка.
type: docs
weight: 90
url: /ru/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Для применения одинаковых параметров форматирования к ячейкам создайте новый объект стиля форматирования. Объект стиля форматирования представляет собой комбинацию параметров форматирования, таких как шрифт, размер шрифта, отступ, номер, граница, узоры и т. д., названных и сохраненных в виде набора. При применении все форматирование в этом стиле применяется.

Вы также можете использовать существующий стиль, сохранить его с книгой и использовать его для форматирования информации с теми же атрибутами.

Когда ячейки не явно форматируются, применяется стиль **Обычный** (стандартный стиль книги). В Microsoft Excel предопределено несколько стилей, кроме стиля Нормальный, включая запятую, валюту и процент.

Aspose.Cells позволяет изменять любой из этих стилей или любой другой стиль, который вы определяете с желаемыми атрибутами.

{{% /alert %}}

## **Использование Microsoft Excel**

Для обновления стиля в Microsoft Excel 97-2003:

1. В меню **Формат**, выберите **Стиль**.
1. Выберите стиль, который вы хотите изменить в списке **Имя стиля**.
1. Нажмите **Изменить**.
1. Выберите параметры стиля, которые вы хотите с помощью вкладок в диалоговом окне Формат ячеек.
1. Нажмите **ОК**.
1. В разделе **Стиль включает**, укажите нужные особенности стиля.
1. Нажмите **OK**, чтобы сохранить стиль и применить его к выбранному диапазону.

## **Использование Aspose.Cells**

Следующие примеры демонстрируют, как использовать метод [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/).

### **Создание и изменение стиля**

Этот пример создает объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/), применяет его к диапазону ячеек и изменяет объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Изменения автоматически применяются к ячейке и диапазону, к которому был применен стиль.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Изменение существующего стиля**

В этом примере используется простой шаблонный файл Excel, к которому уже был применен стиль Percent к диапазону. Пример:

1. получает стиль,
1. создает объект стиля и
1. изменяет форматирование стиля.

Изменения автоматически применяются к диапазону, к которому был применен стиль.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
