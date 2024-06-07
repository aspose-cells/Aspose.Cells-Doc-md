---
title: Excel主题和颜色
type: docs
weight: 130
url: /zh/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

主题提供具有命名样式、图形效果和工作簿中使用的其他对象的统一外观。例如，Accent1样式在Office和Apex主题中看起来不同。通常，您应用文档主题，然后根据需要进行修改。

在Microsoft Excel中应用主题

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **获取和设置主题颜色**

Aspose.Cells API提供了自定义主题和颜色的功能。以下是实现主题颜色的方法和属性。

- Style.ForegroundThemeColor属性可用于设置前景色。
- Style.BackgroundThemeColor属性可用于设置背景色。
- Font.ThemeColor属性可用于设置字体颜色。
- Workbook.getThemeColor方法可用于获取主题颜色。
- Workbook.setThemeColor方法可用于设置主题颜色。

以下示例显示如何获取和设置主题颜色。

以下示例使用模板XLSX文件，获取不同主题颜色类型的颜色，更改颜色并保存Microsoft Excel文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **自定义主题**

以下示例显示了如何应用自定义主题与所需颜色。 该示例使用在Microsoft Excel 2007中手动创建的示例模板文件。

**自定义主题颜色.xlsx文件**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

以下示例加载一个模板XLSX文件，为不同主题颜色类型定义颜色，应用自定义颜色并保存Excel文件。

**带有自定义主题颜色的生成文件**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **使用主题颜色**

以下示例根据工作簿的默认主题（颜色类型）设置单元格的前景色和字体颜色。它还将Excel文件保存到磁盘。

执行代码时生成以下输出。

**将主题颜色应用于工作表的D3单元格** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **高级主题**
- [从Excel文件中提取主题数据](/cells/zh/java/extract-theme-data-from-excel-file/)
