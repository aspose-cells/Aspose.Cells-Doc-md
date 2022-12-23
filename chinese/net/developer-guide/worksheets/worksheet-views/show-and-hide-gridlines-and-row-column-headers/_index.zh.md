---
title: 显示和隐藏网格线和行列标题
type: docs
weight: 30
url: /zh/net/show-and-hide-gridlines-and-row-column-headers/
description: 本文提供了使用 C# API 或 .NET 库以编程方式隐藏或显示 Excel 工作表的网格线、行和列标题的示例代码。
---
{{% alert color="primary" %}}

Aspose.Cells 支持隐藏和显示默认可见的工作表网格线。它还提供控制工作表行列标题的可见性。

{{% /alert %}}

## **显示和隐藏网格线**

默认情况下，所有 Excel 工作表都有网格线。它们有助于描绘单元格，以便轻松地将数据输入特定单元格。网格线使我们能够将工作表视为单元格的集合，其中每个单元格都很容易识别。

### **控制网格线的可见性**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许开发人员访问 Excel 文件中的每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要控制网格线的可见性，请使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**网格线是否可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)财产。[**网格线是否可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)是一个布尔属性，这意味着它只能存储一个**真的**要么**错误的**价值。

#### **使网格线可见**

通过设置使网格线可见[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**网格线是否可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)财产给**真的**.

#### **隐藏网格线**

通过设置隐藏网格线[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**网格线是否可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)财产给**错误的**.

下面给出了一个完整的示例，演示了[**网格线是否可见**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)通过打开一个 excel 文件（book1.xls），隐藏第一个工作表上的网格线并将修改后的文件保存为 output.xls 来修改属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **显示和隐藏行列标题**

Excel 文件中的所有工作表均由按行和列排列的单元格组成。所有行和列都具有用于标识它们和标识单个单元格的唯一值。例如，行编号 - 1、2、3、4 等 - 列按字母顺序排序 - A、B、C、D 等。行和列值显示在标题中。使用 Aspose.Cells，开发人员可以控制这些行和列标题的可见性。

### **控制工作表的可见性**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许开发人员访问 Excel 文件中的每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要控制行标题和列标题的可见性，请使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)财产。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)是一个布尔属性，这意味着它只能存储一个**真的**要么**错误的**价值。

#### **使行/列标题可见**

通过设置[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)财产给**真的**.

#### **隐藏行/列标题**

通过设置隐藏行和列标题[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)财产给**错误的**.

下面给出了一个完整的示例，说明如何使用[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)通过打开一个 excel 文件 (book1.xls)，隐藏第一个工作表上的行和列标题并将修改后的文件保存为 output.xls 来修改属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

也可以使用[**取消隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)和[**取消隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)使多行和多列可见的类。

{{% /alert %}}
