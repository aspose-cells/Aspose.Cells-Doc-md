---
title: Темы и цвета Excel с C++
linktitle: Темы и цвета Excel
type: docs
weight: 100
url: /ru/cpp/excel-themes-and-colors/
description: Код C++ для использования схемы цветов Excel с API Aspose.Cells for C++
keywords: Создание и применение схем цветов с C++, программное создание пользовательской схемы цветов, как программно применить пользовательскую схему цветов, как использовать схему цветов в Excel с C++
---

## **Как применить и создать цветовую схему в Excel**
Темы документов позволяют легко координировать цвета, шрифты и графические эффекты форматирования документов Excel и быстро обновлять их. 
Темы предоставляют единообразный вид с именованными стилями, графическими эффектами и другими объектами, используемыми в рабочей книге. Например, стиль Accent1 в темах Office и Apex выглядит по-разному. Часто вы применяете тему документа, а затем изменяете ее в соответствии с вашими запросами.

### **Как применить цветовую схему в Excel**
1. Откройте Excel и перейдите на вкладку "Разметка страницы" на ленте Excel.
1. Нажмите кнопку "Цвета" в разделе "Темы".
<br>
<img src="color.png" width=70% />
1. Выберите цветовую палитру, которая соответствует вашим требованиям, или наведите курсор на схему, чтобы увидеть предварительный просмотр.

### **Как создать пользовательскую цветовую схему в Excel**
Вы можете создать собственный набор цветов, чтобы придать вашему документу свежий, уникальный вид или соответствовать корпоративному стилю вашей организации.

1. Откройте Excel и перейдите на вкладку "Разметка страницы" на ленте Excel.
1. Нажмите кнопку "Цвета" в разделе "Темы".
1. Нажмите кнопку "Настроить цвета...".
<br>
<img src="color2.png" width=70% />

1. В диалоговом окне "Создание новых тем цветов" вы можете выбрать цвета для каждого элемента, нажав на выпадающие списки цветов рядом с ними. Вы можете выбрать цвета из палитры или определить пользовательские цвета, используя опцию "Другие цвета".
<br>
<img src="color3.png" width=70% />
1. После выбора всех желаемых цветов укажите имя для вашей пользовательской цветовой схемы в поле "Имя".

1. Нажмите кнопку "Сохранить", чтобы сохранить вашу пользовательскую цветовую схему. Ваша пользовательская цветовая схема теперь будет доступна в раскрывающемся меню "Цвета" для последующего использования.

## **Как создать и применить цветовую схему в Aspose.Cells**
Aspose.Cells предоставляет возможности настройки тем и цветов.

### **Как создать пользовательскую цветовую тему в Aspose.Cells**
Если цвета темы используются в файле, нам не нужно изменять каждую ячейку индивидуально, мы просто должны изменить цвета в теме.

Приведенный ниже пример показывает, как применить пользовательские темы с желаемыми цветами. Мы используем образец файла шаблона, созданный вручную в Microsoft Excel 2007.

Приведенный ниже пример загружает шаблонный файл XLSX, определяет цвета для различных типов цвета темы, применяет пользовательские цвета и сохраняет файл Excel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как применить цвета темы в Aspose.Cells**

Приведенный ниже пример применяет передний план ячейки и цвета шрифта на основе цветов темы по умолчанию (рабочей книги). Он также сохраняет файл Excel на диск.

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

    // Create workbook
    Workbook workbook;

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как получить и установить цвета темы в Aspose.Cells**
 Ниже приведены несколько методов и свойств, реализующих цвета темы.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): Используется для установки цвета переднего плана.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): Используется для установки цвета фона.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): Используется для установки цвета шрифта.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): Используется для получения цвета темы.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): Используется для установки цвета темы.

В следующем примере показано, как получить и установить цвета темы.

В следующем примере используется шаблонный файл XLSX, получаются цвета для различных типов цветов темы, изменяются цвета и сохраняется файл Microsoft Excel.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Извлечение данных о теме из файла Excel](/cells/ru/cpp/extract-theme-data-from-excel-file/)
