---
title: 设置 Style.Custom 属性时检查自定义数字格式
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库，它支持在样式设置时检查自定义数字格式。本文将向您展示如何使用 Aspose.Cells 库检查自定义数字格式以确保样式正确。
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /zh/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **可能的使用场景**

如果您指定无效的自定义数字格式[**风格.定制**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)属性，那么 Aspose.Cells 不会抛出任何异常。但如果您希望 Aspose.Cells 检查指定的自定义数字格式是否有效，那么请设置[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)属性为 *true**。

##  **设置 Style.Custom 属性时检查自定义数字格式**

以下示例代码将无效的自定义数字格式分配给[**风格.定制**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)财产。因为，我们已经设定了[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)属性为*true**，因此它会抛出异常，例如无效的数字格式。请阅读代码内的注释以获得更多帮助。

##  **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
