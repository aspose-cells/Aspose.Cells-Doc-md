---
title: 显示和隐藏网格线以及行列标题
type: docs
weight: 30
url: /zh/net/show-and-hide-gridlines-and-row-column-headers/
description: 本文提供了使用C#库或.NET库以编程方式隐藏或显示Excel工作表的网格线、行和列标题的示例代码。
---

{{% alert color="primary" %}}

Aspose.Cells支持隐藏和显示工作表中默认情况下可见的网格线。它还提供了控制工作表的行列标题的可见性。

{{% /alert %}}

## **显示和隐藏网格线**

所有Excel工作表默认情况下都有网格线。它们有助于划分单元格，便于将数据输入特定的单元格。网格线使我们能够将工作表视为单元格的集合，其中每个单元格都易于识别。

### **控制网格线的可见性**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许开发人员访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。要控制网格线的可见性，请使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)属性。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)是一个布尔属性，意味着它只能存储**true**或**false**值。

#### **使网格线可见**

通过将[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)属性设置为**true**，使网格线可见。

#### **隐藏网格线**

通过将[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)属性设置为**false**，隐藏网格线。

下面提供了一个完整的示例，演示了如何使用[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)属性，打开一个excel文件（book1.xls），隐藏第一个工作表上的网格线，并将修改后的文件保存为output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **显示和隐藏行列标题**

Excel文件中的所有工作表都由排列在行和列中的单元格组成。所有行和列都有用于标识它们和单个单元格的唯一值。例如，行编号为1、2、3、4等，列按字母顺序排列为A、B、C、D等。行和列值显示在标题中。使用Aspose.Cells，开发人员可以控制这些行和列标题的可见性。

### **控制工作表的可见性**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许开发人员访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。要控制行和列标题的可见性，请使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)属性。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)是一个布尔属性，意味着它只能存储**true**或**false**值。

#### **使行/列标头可见**

通过将[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)属性设置为**true**，使行和列标题可见。

#### **隐藏行/列标头**

通过将[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)属性设置为**false**，隐藏行和列标题。

下面提供了一个完整的示例，演示了如何使用[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)属性，打开一个excel文件（book1.xls），隐藏第一个工作表的行和列标题，并将修改后的文件保存为output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

也可以使用[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)和[**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)方法来使多行和列可见。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
