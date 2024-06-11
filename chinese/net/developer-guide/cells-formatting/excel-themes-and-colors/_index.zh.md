---
title: Excel 主题和颜色
type: docs
weight: 100
url: /zh/net/excel-themes-and-colors/
description: 用 C# 代码使用 Aspose.Cells for .NET API 的 Excel 颜色方案。
keywords: 使用C#创建和应用颜色方案，使用C#以编程方式创建自定义颜色方案，以编程方式如何应用自定义颜色方案，使用C#如何在Excel中使用颜色方案
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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

### **如何在Aspose.Cells中应用主题颜色**

下面的示例根据工作簿的默认主题颜色类型，应用单元格的前景色和字体颜色。它还将Excel文件保存到磁盘。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

### **如何在Aspose.Cells中获取和设置主题颜色**
 以下是实现主题颜色的几种方法和属性。

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor)：用来设置前景色。
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor)：用来设置背景色。
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor)：用来设置字体颜色。
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor)：用来获取主题颜色。
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor)：用来设置主题颜色。

以下示例演示如何获取和设置主题颜色。

以下示例使用了一个模板 XLSX 文件，获取了不同主题颜色类型的颜色，更改了颜色，然后保存了 Microsoft Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

## **高级主题**
- [从Excel文件中提取主题数据](/cells/zh/net/extract-theme-data-from-excel-file/)
