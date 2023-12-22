---
title: 查找或搜索数据
type: docs
weight: 50
url: /zh/net/find-or-search-data/
description: 了解如何通过 Aspose.Cells for .NET API 查找或搜索工作表中包含指定数据的单元格。
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel 允许用户在工作表中查找包含指定数据的单元格。

{{% /alert %}}

##  **查找Cells包含指定数据**

###  **使用 Microsoft Excel**

Microsoft Excel 允许用户在工作表中查找包含指定数据的单元格。如果您选择**编辑**来自**寻找**在 Microsoft Excel 中的菜单中，您将看到一个对话框，您可以在其中指定搜索值。

在这里，我们正在寻找值“Oranges”。 Aspose.Cells 还允许开发人员在工作表中查找包含指定值的单元格。

###  **使用Aspose.Cells**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)代表工作表中所有单元格的集合。这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了多种在工作表中查找包含用户指定数据的单元格的方法。下面将更详细地讨论其中一些方法。

{{% alert color="primary" %}}

所有 Find 方法都会返回包含要搜索的指定数据的单元格的引用。

{{% /alert %}}

##  **发现Cells含有公式**

开发者可以通过调用函数在工作表中查找指定的公式[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法。通常，[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法接受三个参数：

- **目的：**要搜索的对象。类型应为 int、double、DateTime、string、bool。
- **上一个单元格：**具有相同对象的上一个单元格。如果从头开始查找，则该参数可以设置为空。
- FindOptions：用于查找所需对象的选项。

下面的示例使用工作表数据来练习查找方法：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **使用 FindOptions 查找数据或公式**

可以使用以下命令查找指定值[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法与各种[**查找选项**](https://reference.aspose.com/cells/net/aspose.cells/findoptions)。通常，[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法接受以下参数：

- *搜索值**，要搜索的数据或值。
- *上一个单元格**，包含相同值的最后一个单元格。从头开始查找时，该参数可以设置为空。
- *查找选项**，查找选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **查找Cells包含指定的字符串值或数字**

可以通过调用相同的方法来查找指定的字符串值[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法中找到的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收集各种[**查找选项**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

指定[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype)和[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)特性。以下示例代码说明了如何使用这些属性来查找具有不同数量字符串的单元格**开始**或在**中心**或在**结尾**单元格的字符串。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **高级主题**
- [查找特定款式的Cells](/cells/zh/net/find-cells-with-specific-style/)
- [查找单元格值是否以单引号开头](/cells/zh/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [使用原始值搜索数据](/cells/zh/net/search-data-using-original-values/)
