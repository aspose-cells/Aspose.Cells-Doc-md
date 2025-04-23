---
title: 为工作簿指定自定义数字小数点和分组分隔符
type: docs
weight: 100
url: /zh/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 本文显示了如何通过使用 Aspose.Cells for Java API 以及 Java 代码来更改 MS Excel 中的数字小数和组分隔符。
keywords: 指定Excel的自定义小数分隔符、指定Excel的自定义小数分隔符（Java）、指定Excel的自定义分组分隔符、指定Excel的自定义分组分隔符（Java）、指定Excel的自定义小数和分组分隔符、指定Excel的自定义小数和分组分隔符（Java）、更改Excel的小数和分组分隔符（Java）、更改Excel的小数和分组分隔符、更改Excel的小数分隔符、更改Excel的小数分隔符（Java）、更改Excel的分组分隔符、更改Excel的分组分隔符（Java）
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在“高级Excel选项”中指定自定义十进制和千位分隔符，而不是使用系统分隔符，如下面的屏幕截图所示。

Aspose.Cells提供了[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator)和[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator)属性，用于设置格式化/解析数字的自定义分隔符。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

1. 在**文件**选项卡中**选项**打开。
1. 打开**高级**选项卡。
1. 更改**编辑选项**部分中的设置。

下面的屏幕截图显示了“高级Excel选项”，并突出显示了指定“自定义分隔符”的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用Aspose.Cells指定自定义分隔符**

以下示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。它将自定义数字小数和分组分隔符分别设置为点和空格。因此，数字**123,456.789**会显示为**123 456.789**，如屏幕截图所示，显示了代码生成的输出PDF。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
{{< app/cells/assistant language="java" >}}
