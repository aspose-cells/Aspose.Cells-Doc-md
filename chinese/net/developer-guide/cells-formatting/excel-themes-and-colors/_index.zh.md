---
title: Excel 主题和颜色
type: docs
weight: 100
url: /zh/net/excel-themes-and-colors/
description: C# 使用 Excel 配色方案的代码 Aspose.Cells for .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **如何在 Excel 中应用和创建配色方案**
文档主题可以轻松协调 Excel 文档的颜色、字体和图形格式效果并快速更新。
主题通过命名样式、图形效果和工作簿中使用的其他对象提供统一的外观。例如，Accent1 样式在 Office 和 Apex 主题中看起来不同。通常，您应用文档主题，然后将其修改为您想要的方式。

###  **如何在 Excel 中应用配色方案**
1. 打开 Excel 并转到 Excel 功能区中的“页面布局”选项卡。
1. 单击“主题”部分中的“颜色”按钮。
<br>
<img src="color.png" width=70% />
1. 选择符合您要求的调色板或将鼠标悬停在方案上以查看实时预览。

###  **如何在 Excel 中创建自定义配色方案**
您可以创建自己的颜色集，使您的文档具有清新、独特的外观或符合您组织的品牌标准。

1. 打开 Excel 并转到 Excel 功能区中的“页面布局”选项卡。
1. 单击“主题”部分中的“颜色”按钮。
1. 单击“自定义颜色...”按钮。
<br>
<img src="color2.png" width=70% />

1. 在“创建新主题颜色”对话框中，您可以通过单击每个元素旁边的颜色下拉列表来选择每个元素的颜色。您可以从调色板中选择颜色或使用“更多颜色”选项定义自定义颜色。
<br>
<img src="color3.png" width=70% />
1. 选择所有所需的颜色后，在“名称”字段中为您的自定义配色方案提供名称。

1. 单击“保存”按钮保存您的自定义配色方案。您的自定义配色方案现在将在“颜色”下拉菜单中提供，以供将来使用。

##  **如何在 Aspose.Cells 中创建和应用配色方案**
Aspose.Cells 提供自定义主题和颜色的功能。

###  **如何在Aspose.Cells中创建自定义颜色主题**
如果文件中使用了主题颜色，我们不需要单独修改每个单元格，只需要修改主题中的颜色即可。

以下示例展示了如何应用具有所需颜色的自定义主题。我们使用在 Microsoft Excel 2007 中手动创建的示例模板文件。

以下示例加载模板 XLSX 文件，定义不同主题颜色类型的颜色，应用自定义颜色并保存 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **如何在Aspose.Cells中应用主题颜色**

以下示例根据（工作簿的）默认主题颜色类型应用单元格的前景色和字体颜色。它还将 Excel 文件保存到磁盘。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **如何在Aspose.Cells中获取和设置主题颜色**
下面是一些实现主题颜色的方法和属性。

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor)：用于设置前景色。
- [**样式.背景主题颜色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor)：用于设置背景颜色。
- [**字体.主题颜色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor)：用于设置字体颜色。
- [**工作簿.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor)：用于获取主题颜色。
- [**工作簿.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor)：用于设置主题颜色。

以下示例演示如何获取和设置主题颜色。

以下示例使用模板 XLSX 文件，获取不同主题颜色类型的颜色，更改颜色并保存 Microsoft Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **高级主题**
- [从 Excel 文件中提取主题数据](/cells/zh/net/extract-theme-data-from-excel-file/)
