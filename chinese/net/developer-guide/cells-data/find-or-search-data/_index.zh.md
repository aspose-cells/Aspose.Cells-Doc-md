---
title: 查找或搜索数据
type: docs
weight: 50
url: /zh/net/find-or-search-data/
description: 学习如何通过 Aspose.Cells for .NET API 查找或搜索包含指定数据的工作表中的单元格。
keywords: 查找数据，搜索数据，查找包含公式的单元格，搜索包含公式的单元格，使用FindOptions查找数据或公式，在数据或公式中搜索使用FindOptions，查找或搜索包含指定字符串值或数字的单元格，在包含指定数据的单元格中查找或搜索
---

{{% alert color="primary" %}}

Microsoft Excel 允许用户查找工作表中包含指定数据的单元格。

{{% /alert %}}

## **查找包含指定数据的单元格**

### **使用Microsoft Excel**

Microsoft Excel 允许用户查找工作表中包含指定数据的单元格。 如果您在 Microsoft Excel 中的 **查找** 菜单中选择 **编辑**，您将看到一个对话框，您可以在其中指定搜索值。

在这里，我们正在查找值"橙子"。 Aspose.Cells 还允许开发人员查找工作表中包含指定值的单元格。

### **使用Aspose.Cells**

Aspose.Cells 提供一个 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类，表示 Microsoft Excel 文件。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问 Excel 文件中的每个工作表。 工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合，表示工作表中的所有单元格。 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合提供了用于查找工作表中包含用户指定数据的单元格的几种方法。 下面更详细地讨论了其中一些方法。

{{% alert color="primary" %}}

所有查找方法返回包含指定数据的单元格的引用。

{{% /alert %}}

## **查找包含公式的单元格**

开发人员可以通过调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合的 [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) 方法在工作表中找到指定的公式。通常，[**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) 方法接受三个参数：

- **对象：** 要搜索的对象。类型应为int、double、DateTime、string、bool。
- **前一个单元格：** 具有相同对象的前一个单元格。如果从开头开始搜索，可以将此参数设置为null。
- FindOptions：查找所需对象的选项。

以下示例使用工作表数据来练习查找方法：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **使用 FindOptions 查找数据或公式**

可以使用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合的 [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) 方法结合各种 [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) 找到指定的值。通常，[**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) 方法接受以下参数：

- **搜索值**，要搜索的数据或值。
- **前一个单元格**，上一个包含相同值的单元格。如果从开头开始搜索，可以将此参数设置为null。
- **查找选项**，查找选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **查找包含指定字符串值或数字的单元格**

可以使用在 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合中找到的相同 [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) 方法结合各种 [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) 找到指定的字符串值。

指定 [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) 和 [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) 属性。以下示例代码演示了如何使用这些属性来查找**开始**、**中间**或**结尾**位置的单元格中不同数量的字符串。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **高级主题**
- [查找具有特定样式的单元格](/cells/zh/net/find-cells-with-specific-style/)
- [查找单元格值是否以单引号开始](/cells/zh/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [使用原始值搜索数据](/cells/zh/net/search-data-using-original-values/)
{{< app/cells/assistant language="csharp" >}}
