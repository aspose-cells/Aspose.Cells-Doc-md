---
title: 为工作簿指定自定义数字小数点和分组分隔符
type: docs
weight: 100
url: /zh/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 本文介绍了如何使用Aspose.Cells for Java API通过Java代码更改MS Excel中的数字小数点和分组分隔符。
keywords: 在Excel中指定自定义小数分隔符、在Excel Java中指定自定义小数分隔符、在Excel中指定自定义组分隔符、在Excel Java中指定自定义组分隔符、在Excel中指定自定义小数和组分隔符、在Excel Java中指定自定义小数和组分隔符、更改Excel Java中的小数和组分隔符、更改Excel中的小数和组分隔符、更改Excel中的小数分隔符、更改Excel中的小数分隔符Java、更改Excel中的组分隔符Java、更改Excel中的组分隔符
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在**高级Excel选项**中指定自定义小数和千位分隔符，而不是使用系统分隔符，如下图所示。

Aspose.Cells提供了[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator)和[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator)属性，用于设置数字的自定义分隔符以进行格式化/解析。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

1. 在**文件**选项卡中打开**选项**。
1. 打开**高级**选项卡。
1. 更改**编辑选项**部分中的设置。

以下截图显示了**高级Excel选项**并突出显示了指定**自定义分隔符**的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用Aspose.Cells指定自定义分隔符**

以下示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。它将自定义的数字小数和组分隔符分别指定为点和空格。因此，数字**123,456.789**将显示为**123 456.789**，如代码生成的输出PDF中所示。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
