---
title: Excel 主题和颜色
type: docs
weight: 130
url: /zh/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

主题提供了具有命名样式、图形效果和工作簿中使用的其他对象的统一外观。例如，在 Office 和 Apex 主题中，Accent1 样式看起来各不相同。通常，你应用文档主题，然后根据自己的需要进行修改。

**在 Microsoft Excel 中应用主题**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **获取和设置主题颜色**

Aspose.Cells API 提供了自定义主题和颜色的功能。以下是几种实现主题颜色的方法和属性。

- Style.ForegroundThemeColor 属性可用于设置前景色。
- Style.BackgroundThemeColor 属性可用于设置背景颜色。
- Font.ThemeColor 属性可用于设置字体颜色。
- Workbook.getThemeColor 方法可用于获取主题颜色。
- Workbook.setThemeColor 方法可用于设置主题颜色。

以下示例演示如何获取和设置主题颜色。

以下示例使用了一个模板 XLSX 文件，获取了不同主题颜色类型的颜色，更改了颜色，然后保存了 Microsoft Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **自定义主题**

以下示例演示如何应用带有您所需颜色的自定义主题。该示例使用了在 Microsoft Excel 2007 中手动创建的样本模板文件。

**模板 CustomThemeColor.xlsx 文件**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

下面的示例加载一个模板XLSX文件，为不同的主题颜色类型定义颜色，应用自定义颜色并保存Excel文件。

**使用自定义主题颜色生成的文件**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **使用主题颜色**

下面的示例根据工作簿的默认主题颜色类型，应用单元格的前景色和字体颜色。它还将Excel文件保存到磁盘。

执行代码时会生成以下输出。

**工作表的单元格 D3 应用的主题颜色** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **高级主题**
- [从Excel文件中提取主题数据](/cells/zh/java/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="java" >}}
