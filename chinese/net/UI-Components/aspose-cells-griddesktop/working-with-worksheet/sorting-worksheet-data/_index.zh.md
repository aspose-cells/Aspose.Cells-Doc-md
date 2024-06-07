---
title: 排序工作表数据
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop,排序,排序,排序数据,数据排序
description: 本文介绍了如何在GridDesktop中对工作表中的数据进行排序。
---

{{% alert color="primary" %}} 

排序是一个重要的例行任务，在处理数据时通常会使用。 在本主题中，我们将通过一个简单的示例讨论如何对工作表中的数据进行排序。

{{% /alert %}} 
## **排序工作表数据**
要使用Aspose.Cells.GridDesktop的API对工作表中的数据进行排序，请按照以下步骤操作：

- 首先创建一个**CellRange**的全局对象，以便在类的范围内的任何位置都可以访问它。
- 为**GridDesktop**的**SelectedCellRangeChanged**事件创建一个事件处理程序。 每当用户更改所选单元格范围时，都会触发**SelectedCellRangeChanged**事件。 例如，如果用户选择包含要排序的数据的单元格，则每次他的选择范围更改时，此事件都会被触发。
- 事件处理程序提供**CellRangeEventArgs**参数，进一步以**CellRange**对象的形式提供用户选择的单元格的更新范围。 因此，在此事件处理程序中，我们将此**CellRange**对象（包含更新后的单元格范围）分配给全局**CellRange**对象，以便它也可以在代码的其他部分中使用。 为了确保不丢失单元格范围，我们将编写事件处理程序代码放在一个条件内
- 现在我们可以编写一些代码来对工作表数据进行排序。 首先，访问所需的工作表
- 创建一个**SortRange**对象，该对象将保留要对其数据进行排序的单元格范围。 在**SortRange**构造函数中，我们可以指定工作表、起始行和列的索引、要排序的行数和列数、排序的方向（例如从上到下或从左到右）等。
- 现在我们可以调用**SortRange**对象的**Sort**方法来执行数据的排序。 在**Sort**方法中，我们可以指定要排序的列或行的索引和排序顺序（根据您的要求可以是**升序**或**降序**）
- 最后，我们可以调用**GridDesktop**的**Invalidate**方法来重绘单元格。

在下面给出的示例中，我们演示了如何对列中的数据进行排序。

创建一个**CellRange**的全局对象和**GridDesktop**的**SelectedCellRangeChanged**事件。 现在编写以下代码：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


现在我们编写**升序排序**的方法。 您可以为**升序排序**创建一个按钮，并在其**Click**事件中编写以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


最后，我们编写一些代码来实现**降序排序**功能。创建一个**降序排序**按钮，并在其**单击**事件内编写以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
