---
title: 查找或搜索数据
type: docs
weight: 50
url: /zh/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel 允许用户在包含指定数据的工作表中查找单元格。

{{% /alert %}}

## **查找包含指定数据的 Cells**

### **使用 Microsoft Excel**

 Microsoft Excel 允许用户在包含指定数据的工作表中查找单元格。如果你选择**编辑**来自**寻找**Microsoft Excel 中的菜单，您将看到一个对话框，您可以在其中指定搜索值。

在这里，我们正在寻找值“Oranges”。 Aspose.Cells 还允许开发人员在工作表中查找包含指定值的单元格。

### **使用 Aspose.Cells**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)代表工作表中所有单元格的集合。这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection 提供了多种方法来查找包含用户指定数据的工作表中的单元格。下面将更详细地讨论其中一些方法。

{{% alert color="primary" %}}

所有 Find 方法都返回包含要搜索的指定数据的单元格的引用。

{{% /alert %}}

## **查找包含公式的 Cells**

开发者可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法。通常，[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法接受三个参数：

- **目的：**要搜索的对象。类型应为 int、double、DateTime、string、bool。
- **上一个单元格：**具有相同对象的上一个单元格。如果从头开始搜索，这个参数可以设置为空。
- FindOptions：用于查找所需对象的选项。

下面的示例使用工作表数据来练习查找方法：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **使用 FindOptions 查找数据或公式**

可以使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法与各种[**查找选项**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).通常，[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法接受以下参数：

- **搜索值**要搜索的数据或值。
- **上一个单元格**，包含相同值的最后一个单元格。从头开始搜索时可以将此参数设置为空。
- **查找选项**查找选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **查找包含指定字符串值或数字的 Cells**

可以通过调用相同的方法来查找指定的字符串值[**寻找**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)中找到的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收集各种[**查找选项**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

指定[**查找选项.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype)和[**查找选项.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)特性。下面的示例代码说明了如何使用这些属性来查找具有不同数量字符串的单元格**开始**或在**中央**或在**结尾**单元格的字符串。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **推进主题**
- [查找具有特定样式的 Cells](/cells/zh/net/find-cells-with-specific-style/)
- [查找单元格值是否以单引号开头](/cells/zh/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [使用原始值搜索数据](/cells/zh/net/search-data-using-original-values/)
