---
title: 设置Style.Custom属性时检查自定义数字格式
description: Aspose.Cells是一个用于处理电子表格文件的.NET库，支持在设置样式时检查自定义数字格式。本文将向您展示如何使用Aspose.Cells库来检查自定义数字格式，以确保样式正确。
keywords: Aspose.Cells, .NET库, 电子表格, 样式, 自定义数字格式, 检查, 验证
type: docs
weight: 170
url: /zh/net/check-custom-number-format-when-setting-style-custom-property/
---

## **可能的使用场景**

如果将无效的自定义数字格式分配给[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)属性，则Aspose.Cells不会抛出任何异常。但如果要求Aspose.Cells检查分配的自定义数字格式是否有效，则请将[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)属性设置为**true**。

## **在设置Style.Custom属性时检查自定义数字格式**

以下示例代码将一个无效的自定义数字格式分配给[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)属性。由于我们已经将[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)属性设置为**true**，因此它会抛出异常，例如无效的数字格式。请阅读代码注释以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
