---
title: Excel 主题和颜色
type: docs
weight: 100
url: /zh/net/excel-themes-and-colors/
---
## **Excel 主题和颜色**

主题通过命名样式、图形效果和工作簿中使用的其他对象提供统一的外观。例如，Accent1 样式在 Office 和 Apex 主题中看起来不同。通常，您应用一个文档主题，然后将其修改为您想要的方式。

Aspose.Cells 提供自定义主题和颜色的功能。

### **获取和设置主题颜色**

下面是一些实现主题颜色的方法和属性。

- [**样式.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor)：用于设置前景色。
- [**样式.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor)：用于设置背景颜色。
- [**字体.主题颜色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor)：用于设置字体颜色。
- [**工作簿.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor)：用于获取主题颜色。
- [**工作簿.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor)：用于设置主题颜色。

以下示例显示如何获取和设置主题颜色。

以下示例使用模板 XLSX 文件，获取不同主题颜色类型的颜色，更改颜色并保存 Microsoft Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **自定义主题**

以下示例显示如何应用具有所需颜色的自定义主题。我们使用在 Microsoft Excel 2007 中手动创建的示例模板文件。

以下示例加载模板 XLSX 文件，为不同的主题颜色类型定义颜色，应用自定义颜色并保存 excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **使用主题颜色**

以下示例根据（工作簿的）默认主题颜色类型应用单元格的前景色和字体颜色。它还将 excel 文件保存到磁盘。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

## **推进主题**
- [从 Excel 文件中提取主题数据](/cells/zh/net/extract-theme-data-from-excel-file/)
