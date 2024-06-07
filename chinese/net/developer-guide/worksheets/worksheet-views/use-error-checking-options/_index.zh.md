---
title: 使用错误检查选项。
type: docs
weight: 140
url: /zh/net/use-error-checking-options/
description: 在本文中，您将找到使用C# API或.NET库以编程方式使用Excel工作表的错误检查选项的示例代码，例如作为文本存储的数字。
keywords: 使用C#在Excel中将数字存储为文本，错误检查Excel选项C#。
---

{{% alert color="primary" %}}

Microsoft Excel允许用户定义错误检查选项和规则。创建公式时，用户通常会看到错误检查，单元格右上角出现小三角形，在单元格存在问题时会突出显示。Excel提供帮助用户纠正常见问题的信息。

{{% /alert %}}

## **错误类型。**

意味着公式无法返回结果的错误-例如通过零除以数字-需要立即处理，并在单元格中显示错误值。单击绿色三角形会显示感叹号，单击后会打开选项列表。

可以使用选项解决错误，也可以忽略错误。忽略错误意味着该错误不会出现在后续的错误检查中。

Aspose.Cells提供了错误检查选项功能。[**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption)类管理不同类型的错误检查，例如作为文本存储的数字，公式计算错误和验证错误。使用[**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype)枚举设置所需的错误检查。

## **以文本形式存储的数字。**

有时，数字可能会以文本形式格式化并存储在单元格中。这可能会导致计算错误或产生混乱的排序顺序。以文本形式格式化的数字以文本左对齐而不是右对齐显示在单元格中。如果公式应在单元格上执行数学运算而没有返回值，则检查公式引用的单元格中的对齐方式-这些单元格中的一些或全部可能是作为文本格式化的数字。

可以使用错误检查选项快速将存储为文本的数字转换为真实数字。在Microsoft Excel 2003中：

1. 在**工具**菜单上，单击**选项**。
1. 选择错误检查选项卡。
   默认情况下选中**作为文本存储的数字**选项。
1. 禁用它。

以下示例代码展示了如何使用Aspose.Cells API在模板XLS文件中为工作表禁用以文本形式存储的数字错误检查选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
