---
title: 在使用 Golang 通过 C++ 设置样式的自定义属性时检查自定义数字格式
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库，支持在样式设置时检查自定义数字格式。本文将展示如何使用 Aspose.Cells 库检查自定义数字格式以确保样式正确。
keywords: Aspose.Cells，C++库，电子表格，样式，自定义数字格式，检查，验证
type: docs
weight: 170
url: /zh/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **可能的使用场景**

如果你为 [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) 属性分配了无效的自定义数字格式，Aspose.Cells 不会抛出任何异常。但是，如果你希望 Aspose.Cells 检查所分配的自定义数字格式是否有效，请将 [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) 属性设置为 **true**。

## **设置 Style.Custom 属性时检查自定义数字格式**

以下示例代码为 [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) 属性分配了无效的自定义数字格式。由于我们已经将 [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) 属性设置为 **true**，因此会抛出异常，例如：无效的数字格式。请查看代码中的注释以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
