---
title: Excel 主题和颜色
type: docs
weight: 130
url: /zh/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

主题通过命名样式、图形效果和工作簿中使用的其他对象提供统一的外观。例如，Accent1 样式在 Office 和 Apex 主题中看起来不同。通常，您会应用一个文档主题，然后根据您的需要对其进行修改。

**在 Microsoft Excel 中应用主题**

![待办事项：图像_替代_文本](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **获取和设置主题颜色**

Aspose.Cells API 提供自定义主题和颜色的功能。下面是一些实现主题颜色的方法和属性。

- Style.ForegroundThemeColor 属性可用于设置前景色。
- Style.BackgroundThemeColor 属性可用于设置背景颜色。
- Font.ThemeColor 属性可用于设置字体颜色。
- Workbook.getThemeColor 方法可用于获取主题颜色。
- Workbook.setThemeColor 方法可用于设置主题颜色。

以下示例显示如何获取和设置主题颜色。

以下示例使用模板 XLSX 文件，获取不同主题颜色类型的颜色，更改颜色并保存 Microsoft Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **自定义主题**

以下示例显示如何应用具有所需颜色的自定义主题。该示例使用在 Microsoft Excel 2007 中手动创建的示例模板文件。

**模板 CustomThemeColor.xlsx 文件**

![待办事项：图像_替代_文本](excel-2007-themes-and-colors_2.png)

以下示例加载模板 XLSX 文件，为不同的主题颜色类型定义颜色，应用自定义颜色并保存 excel 文件。

**生成的具有自定义主题颜色的文件**

![待办事项：图像_替代_文本](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **使用主题颜色**

以下示例根据（工作簿的）默认主题颜色类型应用单元格的前景色和字体颜色。它还将 excel 文件保存到磁盘。

执行代码时会生成以下输出。

**应用于工作表 D3 单元格的主题颜色** 

![待办事项：图像_替代_文本](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **推进主题**
- [从 Excel 文件中提取主题数据](/cells/zh/java/extract-theme-data-from-excel-file/)
