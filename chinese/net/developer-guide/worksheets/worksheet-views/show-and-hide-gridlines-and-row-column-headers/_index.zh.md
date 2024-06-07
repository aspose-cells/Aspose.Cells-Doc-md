---
title: 显示和隐藏网格线和行列标题
type: docs
weight: 30
url: /zh/net/show-and-hide-gridlines-and-row-column-headers/
description: 本文提供了使用C# API或.NET库以编程方式隐藏或显示Excel工作表的网格线、行和列标题的示例代码。
---

{{% alert color="primary" %}}

Aspose.Cells支持隐藏和显示工作表的网格线，这些线默认情况下是可见的。它还提供控制工作表的行列标题可见性。

{{% /alert %}}

## **显示和隐藏网格线**

所有 Excel 工作表默认具有网格线。它们帮助划定单元格，使得数据输入到特定单元格变得容易。网格线使我们能够将工作表视为单元格的集合，其中每个单元格都很容易识别。

### **控制网格线的可见性**

Aspose.Cells 提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许开发人员访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供广泛的属性和方法来管理工作表。为了控制网格线的可见性，请使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 属性。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 是一个布尔属性，只能存储 **true** 或 **false** 值。

#### **使网格线可见**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 属性设置为 **true** 来使网格线可见。

#### **隐藏网格线**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 属性设置为 **false** 来隐藏网格线。

下面给出了一个完整的示例，演示了通过打开 Excel 文件（book1.xls），隐藏第一个工作表上的网格线并将修改后的文件保存为 output.xls，使用 [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 属性的用法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **显示和隐藏行列标题**

Excel 文件中的所有工作表都由按行和列排列的单元格组成。所有行和列都有用于识别它们和识别单个单元格的唯一值。例如，行被编号为 - 1、2、3、4 等 - 列按字母顺序排列 - A、B、C、D 等 - 行和列的值显示在标题中。使用 Aspose.Cells，开发人员可以控制这些行和列标题的可见性。

### **控制工作表的可见性**

Aspose.Cells 提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许开发人员访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供广泛的属性和方法来管理工作表。为了控制行和列标题的可见性，请使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 属性。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 是一个布尔属性，只能存储 **true** 或 **false** 值。

#### **显示行/列标题**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 属性设置为 **true** 来显示行和列标题。

#### **隐藏行/列标题**

通过将 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 属性设置为 **false** 来隐藏行和列标题。

下面给出了一个完整的示例，演示了如何使用 [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 属性，通过打开 Excel 文件（book1.xls），在第一个工作表上隐藏行和列标题，并将修改后的文件保存为 output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

还可以使用 [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) 和 [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) 的方法，来使多行和多列可见。

{{% /alert %}}
