---
title: 为工作簿指定自定义数字小数点和分组分隔符，使用C++通过Golang
linktitle: 指定自定义数字小数点和组分隔符
type: docs
weight: 110
url: /zh/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 通过使用Aspose.Cells for C++ API，在MS Excel中以及使用C++通过Golang更改数字的小数点和分组分隔符。
keywords: 指定自定义小数点分隔符Excel，指定自定义小数点分隔符Excel C++，指定自定义组分隔符Excel，指定自定义组分隔符Excel C++，指定自定义十进制和组分隔符Excel，指定自定义十进制和组分隔符Excel C++，更改Excel的十进制和分组分隔符，更改十进制和分组分隔符Excel，更改十进制分隔符Excel，更改十进制分隔符Excel C++，更改组分隔符Excel，更改组分隔符Excel C++
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在“高级Excel选项”中指定自定义十进制和千位分隔符，而不是使用系统分隔符，如下面的屏幕截图所示。

Aspose.Cells提供[**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/)和[**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/)属性，以设置数字的自定义分隔符进行格式化/解析。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

下面的屏幕截图显示了“高级Excel选项”，并突出显示了指定“自定义分隔符”的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用Aspose.Cells指定自定义分隔符**

下面的示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。它将十进制和组分隔符分别指定为点和空格。

### 用C++指定自定义数字的小数点和分组分隔符的代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
