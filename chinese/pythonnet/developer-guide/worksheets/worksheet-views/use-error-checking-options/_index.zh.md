---
title: 使用错误检查选项
type: docs
weight: 140
url: /zh/python-net/use-error-checking-options/
description: 本文中提供了示例代码，使用 Aspose.Cells for Python via .NET API 编程方式检测Excel工作表中的错误，例如将数字作为文本存储。
keywords: Python Excel库，Python在Excel中存储数字为文本，如何处理Excel中的错误检查选项。
---

{{% alert color="primary" %}}

Microsoft Excel允许用户定义错误检查选项和规则。当创建公式时，用户通常会看到错误检查，单元格右上角的小三角形突出显示当单元格存在问题时。Excel提供帮助用户纠正常见问题的信息。

{{% /alert %}}

## **错误类型**

表示公式无法返回结果的错误，比如通过零进行数字除法，需要立即关注并在单元格中显示错误值。单击绿色三角形显示一个感叹号，单击打开一个选项列表。

可以通过选项解决错误，也可以选择忽略错误。忽略错误意味着该错误在后续错误检查中不再显示。

Aspose.Cells for Python via .NET 提供了错误检查功能。[**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption) 类管理不同类型的错误检测，例如数字以文本存储、公式计算错误以及验证错误。使用 [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype) 枚举设置所需的错误检测类型。

## **作为文本存储的数字**

有时，数字可能被格式化并作为文本存储在单元格中。这可能会导致计算出现问题或产生令人困惑的排序顺序。格式为文本的数字在单元格中是左对齐而不是右对齐的。如果应执行单元格上的公式未返回值，则检查公式引用的单元格中的对齐方式 - 可能是其中一些或全部的单元格被格式为文本。

可以使用错误检查选项快速将作为文本存储的数字转换为实际数字。在Microsoft Excel 2003中：

1. 在“工具”菜单上，单击“选项”。
1. 选择错误检查标签页。默认勾选“数字存储为文本”选项。
1. 取消其选中状态。

以下示例代码演示了如何使用 Aspose.Cells for Python via .NET API 禁用工作表中“数字存储为文本”的错误检测选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
