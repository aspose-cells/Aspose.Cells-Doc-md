---
title: 为工作簿指定自定义数字小数点和分组分隔符
linktitle: 为工作簿指定自定义数字小数点和分组分隔符
type: docs
weight: 110
url: /zh/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 使用Aspose.Cells for Node.js via C++在Excel中更改数字的小数点和分组符号分隔符。 
keywords: 通过 C++ 在Excel中指定自定义的小数点和分组符号分隔符，使用 Node.js 实现
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在“高级Excel选项”中指定自定义十进制和千位分隔符，而不是使用系统分隔符，如下面的屏幕截图所示。

Aspose.Cells 提供 [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) 和 [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) 方法，用于设置数字格式化/解析的自定义分隔符。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

下面的屏幕截图显示了“高级Excel选项”，并突出显示了指定“自定义分隔符”的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用Aspose.Cells for Node.js via C++指定自定义分隔符**

下面的示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。它将十进制和组分隔符分别指定为点和空格。

### Node.js 代码示例：指定自定义数字的小数点和分组符号

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
