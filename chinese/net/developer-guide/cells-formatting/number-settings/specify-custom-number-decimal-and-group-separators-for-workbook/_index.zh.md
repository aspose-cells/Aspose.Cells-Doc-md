---
title: 为工作簿指定自定义数字小数点和分组分隔符
type: docs
weight: 110
url: /zh/net/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 在MS Excel和C#代码中使用Aspose.Cells for .NET API更改数字小数点和分组分隔符。
keywords: 指定自定义小数分隔符Excel，指定自定义小数分隔符Excel C#，指定自定义组分隔符Excel，指定自定义组分隔符Excel C#，指定自定义小数和组分隔符Excel，指定自定义小数分隔符Excel C#，更改小数和组分隔符Excel C#，更改小数和组分隔符Excel，更改小数分隔符Excel，更改小数分隔符Excel C#，更改组分隔符Excel，更改组分隔符Excel C#
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在**高级Excel选项**中指定自定义小数和千位分隔符，而不是使用系统分隔符，如下图所示。

Aspose.Cells提供了[**WorkbookSettings.NumberDecimalSeparator**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/numberdecimalseparator)和[**WorkbookSettings.NumberGroupSeparator**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/numbergroupseparator)属性以设置用于格式化/解析数字的自定义分隔符。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

以下截图显示了**高级Excel选项**并突出显示了指定**自定义分隔符**的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用Aspose.Cells指定自定义分隔符**

以下示例代码演示了如何使用Aspose.Cells API指定自定义分隔符。它将自定义数字小数点和组分隔符分别设置为点和空格。

### C#代码指定自定义数字小数点和分组分隔符

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CustomDecimalAndGroupSeparator-CustomDecimalAndGroupSeparator.cs" >}}
