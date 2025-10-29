---
title: 在设置Style.Custom属性时检查自定义数字格式
description: Aspose.Cells 是一个用于处理电子表格文件的Python库，支持在样式设置时检查自定义数字格式。本文将演示如何使用Aspose.Cells库检查自定义数字格式，以确保样式正确。
keywords: Aspose.Cells，Python库，电子表格，样式，自定义数字格式，检查，验证
type: docs
weight: 170
url: /zh/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **可能的使用场景**

如果将无效的自定义数字格式分配给 [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) 属性，则Aspose.Cells不会抛出任何异常。但如果您希望Aspose.Cells检查分配的自定义数字格式是否有效，则请将 [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) 属性设置为**true**。

## **设置 Style.Custom 属性时检查自定义数字格式**

以下示例代码向 [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) 属性分配了一个无效的自定义数字格式。由于我们已将 [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) 属性设置为 **true**，因此会抛出异常，例如无效的数字格式。请阅读代码内的注释以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

{{< app/cells/assistant language="python-net" >}}
