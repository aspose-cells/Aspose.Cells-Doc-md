---
title: 为工作簿指定自定义数字小数点和分组分隔符
type: docs
weight: 110
url: /zh/net/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 使用 Aspose.Cells for .NET API 在 MS Excel 中更改数字的小数点和分组分隔符，并使用 C# 代码。
keywords: 指定Excel的自定义小数分隔符，指定Excel的自定义小数分隔符C＃，指定Excel的自定义组分隔符，指定Excel的自定义组分隔符C＃，指定Excel的自定义小数和组分隔符，指定Excel的自定义小数分隔符C＃，更改Excel的小数和组分隔符C＃，更改Excel的小数和组分隔符，更改Excel的小数分隔符，更改Excel的小数分隔符C＃，更改Excel的组分隔符，更改Excel的组分隔符C＃
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在“高级Excel选项”中指定自定义十进制和千位分隔符，而不是使用系统分隔符，如下面的屏幕截图所示。

Aspose.Cells提供[**WorkbookSettings.NumberDecimalSeparator**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/numberdecimalseparator)和[**WorkbookSettings.NumberGroupSeparator**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/numbergroupseparator)属性，以设置数字的自定义分隔符进行格式化/解析。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

下面的屏幕截图显示了“高级Excel选项”，并突出显示了指定“自定义分隔符”的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用Aspose.Cells指定自定义分隔符**

下面的示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。它将十进制和组分隔符分别指定为点和空格。

### 用于指定自定义数字小数点和分组分隔符的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CustomDecimalAndGroupSeparator-CustomDecimalAndGroupSeparator.cs" >}}
{{< app/cells/assistant language="csharp" >}}
