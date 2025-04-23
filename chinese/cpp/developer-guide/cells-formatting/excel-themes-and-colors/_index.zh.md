---
title: 使用C++实现Excel主题和颜色
linktitle: Excel 主题和颜色
type: docs
weight: 100
url: /zh/cpp/excel-themes-and-colors/
description: 用C++代码使用带有Aspose.Cells for C++ API的Excel颜色方案
keywords: 用C++创建并应用颜色方案，C++程序化创建自定义颜色方案，程序化应用自定义颜色方案，C++中在Excel中使用颜色方案
---

## **如何在Excel中应用和创建颜色方案**
文档主题使得轻松协调Excel文档的颜色、字体和图形格式效果，并快速更新它们。 
主题提供了具有命名样式、图形效果和工作簿中使用的其他对象的统一外观。例如，Accent1样式在Office和Apex主题中看起来不同。通常，您应用文档主题，然后修改它以满足您的要求。

### **如何在Excel中应用颜色方案**
1. 打开Excel，并转到Excel功能区的"页面布局"选项卡。
1. 在"主题"部分的"颜色"按钮上单击。
<br>
<img src="color.png" width=70% />
1. 选择与您的要求相匹配的调色板，或将鼠标悬停在一个方案上以查看实时预览。

### **如何在Excel中创建自定义颜色方案**
您可以创建自己的颜色集，为您的文档带来新的、独特的外观，或者遵守您组织的品牌标准。

1. 打开Excel，并转到Excel功能区的"页面布局"选项卡。
1. 在"主题"部分的"颜色"按钮上单击。
1. 单击"自定义颜色..." 按钮。
<br>
<img src="color2.png" width=70% />

1. 在"创建新主题颜色"对话框中，您可以通过单击旁边的颜色下拉菜单来选择每个元素的颜色。您可以从调色板中选择颜色，或者使用"更多颜色"选项定义自定义颜色。
<br>
<img src="color3.png" width=70% />
1. 在选择所有所需的颜色后，在“名称”字段中提供自定义颜色方案的名称。

1. 点击“保存”按钮以保存您的自定义颜色方案。 您的自定义颜色方案现在将在“颜色”下拉菜单中可供将来使用。

## **如何在Aspose.Cells中创建和应用颜色方案**
Aspose.Cells提供了自定义主题和颜色的功能。

### **如何在Aspose.Cells中创建自定义颜色主题**
如果文件中使用主题颜色，则我们无需逐个修改每个单元格，我们只需要修改主题中的颜色。

以下示例显示如何应用具有您所需颜色的自定义主题。 我们使用在Microsoft Excel 2007中手动创建的示例模板文件。

下面的示例加载一个模板XLSX文件，为不同的主题颜色类型定义颜色，应用自定义颜色并保存Excel文件。

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

### **如何在Aspose.Cells中应用主题颜色**

下面的示例根据工作簿的默认主题颜色类型，应用单元格的前景色和字体颜色。它还将Excel文件保存到磁盘。

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

### **如何在Aspose.Cells中获取和设置主题颜色**
 以下是实现主题颜色的几种方法和属性。

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/)：用来设置前景色。
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/)：用来设置背景色。
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/)：用来设置字体颜色。
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/)：用来获取主题颜色。
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/)：用来设置主题颜色。

以下示例演示如何获取和设置主题颜色。

以下示例使用了一个模板 XLSX 文件，获取了不同主题颜色类型的颜色，更改了颜色，然后保存了 Microsoft Excel 文件。

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

## **高级主题**
- [从Excel文件中提取主题数据](/cells/zh/cpp/extract-theme-data-from-excel-file/)
