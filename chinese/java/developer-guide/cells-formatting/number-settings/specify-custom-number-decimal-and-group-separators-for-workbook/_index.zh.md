---
title: 为工作簿指定自定义数字小数和组分隔符
type: docs
weight: 100
url: /zh/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 本文介绍如何使用 Aspose.Cells for Java API 在 MS Excel 和 Java 代码中更改数字小数点和组分隔符。
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

在 Microsoft Excel 中，您可以指定自定义小数和千位分隔符，而不是使用来自**高级 Excel 选项**如下面的屏幕截图所示。

Aspose.Cells 提供了[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator)和[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator)属性来设置用于格式化/解析数字的自定义分隔符。

{{% /alert %}}

## **使用 Microsoft Excel 指定自定义分隔符**

1. 打开**选项**在里面**文件**标签。
1. 打开**先进的**标签。
1. 更改设置中的**编辑选项**部分。

以下屏幕截图显示了**高级 Excel 选项**并突出显示指定的部分**自定义分隔符**.

![待办事项：图像_替代_文本](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用 Aspose.Cells 指定自定义分隔符**

以下示例代码说明了如何使用 Aspose.Cells API 指定自定义分隔符。它将自定义数字小数和组分隔符分别指定为点和空格。所以数**123,456.789**将显示为**123 456.789**如显示代码生成的输出 PDF 的屏幕截图所示。

![待办事项：图像_替代_文本](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
