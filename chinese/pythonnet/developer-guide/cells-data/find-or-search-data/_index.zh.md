---
title: 查找或搜索数据
type: docs
weight: 50
url: /zh/python-net/find-or-search-data/
description: 通过 Aspose.Cells for Python via .NET API 学习如何在工作表中查找包含指定数据的单元格。
keywords: Python Excel Library, Python 查找数据, Python 搜索数据, Python 查找包含公式的单元格, Python 搜索包含公式的单元格, Python 使用 FindOptions 查找数据或公式, Python 使用 FindOptions 搜索数据或公式, Python 查找或搜索包含指定字符串值或数字的单元格, Python 查找或搜索包含指定数据的单元格
---

{{% alert color="primary" %}}

Microsoft Excel 允许用户查找工作表中包含指定数据的单元格。

{{% /alert %}}

## **查找包含指定数据的单元格**

### **使用Microsoft Excel**

Microsoft Excel 允许用户查找工作表中包含指定数据的单元格。 如果您在 Microsoft Excel 中的 **查找** 菜单中选择 **编辑**，您将看到一个对话框，您可以在其中指定搜索值。

在这里，我们正在查找值"橙子"。 Aspose.Cells 还允许开发人员查找工作表中包含指定值的单元格。

### **使用Aspose.Cells**

Aspose.Cells 提供一个 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类，表示 Microsoft Excel 文件。 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，允许访问 Excel 文件中的每个工作表。 工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合，表示工作表中的所有单元格。 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合提供了用于查找工作表中包含用户指定数据的单元格的几种方法。 下面更详细地讨论了其中一些方法。

{{% alert color="primary" %}}

所有查找方法返回包含指定数据的单元格的引用。

{{% /alert %}}

## **查找包含公式的单元格**

开发人员可以通过调用 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合的 [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) 方法在工作表中找到指定的公式。通常，[**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) 方法接受三个参数：

- **what:** 要搜索的对象。类型应为 int、double、DateTime、string、bool。
- **previous_cell:** 前一个包含相同对象的单元格。如果从头开始搜索，则可以将此参数设置为 null。
- **find_options:** 找到所需对象的选项。

以下示例使用工作表数据来练习查找方法：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **使用 FindOptions 查找数据或公式**

可以使用 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合的 [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) 方法结合各种 [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions) 找到指定的值。通常，[**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) 方法接受以下参数：

- **what:**，要搜索的数据或值。
- **previous_cell**，包含相同值的最后一个单元格。当从头开始搜索时，可以将此参数设置为 null。
- **find_options**，查找选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **查找包含指定字符串值或数字的单元格**

可以使用在 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合中找到的相同 [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) 方法结合各种 [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions) 找到指定的字符串值。

指定 [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) 和 [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/) 属性。以下示例代码演示了如何使用这些属性来查找**开始**、**中间**或**结尾**位置的单元格中不同数量的字符串。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **高级主题**
- [查找具有特定样式的单元格](/cells/zh/python-net/find-cells-with-specific-style/)
- [查找单元格值是否以单引号开始](/cells/zh/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [使用原始值搜索数据](/cells/zh/python-net/search-data-using-original-values/)
