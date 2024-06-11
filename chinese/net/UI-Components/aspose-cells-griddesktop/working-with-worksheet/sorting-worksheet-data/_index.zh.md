---
title: 排序工作表数据
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop，排序，数据排序，排序数据
description: 本文介绍了如何在 GridDesktop 中对工作表中的数据进行排序。
---

{{% alert color="primary" %}} 

排序是处理数据时经常使用的重要例行任务。在本主题中，我们将通过一个简单的示例讨论如何在工作表中对数据进行排序。

{{% /alert %}} 
## **对工作表数据进行排序**
要使用Aspose.Cells.GridDesktop的API在工作表中对数据进行排序，请按以下步骤操作：

- 首先创建一个**CellRange**的全局对象，以便在类的范围内随时访问
- 为**GridDesktop**的**SelectedCellRangeChanged**事件创建事件处理程序。**SelectedCellRangeChanged**事件在用户更改已选择单元格范围时触发。例如，如果用户选择了包含要排序的数据的单元格，那么每次他选择的范围发生变化时，都会触发此事件。
- 事件处理程序提供**CellRangeEventArgs**参数，进一步提供单元格范围的更新（用户选择的）作为**CellRange**对象的形式。因此，在此事件处理程序中，我们将分配此**CellRange**对象（包含更新后的单元格范围）给全局**CellRange**对象，以便在代码的其他部分中也可以使用。为了确保我们不丢失单元格范围，我们将在一个条件中编写事件处理程序代码
- 现在我们可以编写一些代码来对工作表数据进行排序。首先访问所需的工作表
- 创建一个**SortRange**对象，用于存储要排序其数据的单元格范围。在**SortRange**构造函数中，我们可以指定工作表，起始行和列的索引，要排序的行数和列数，排序的方向（如从上到下或从左到右）等。
- 现在我们可以调用**SortRange**对象的**Sort**方法来执行数据排序。在**Sort**方法中，我们可以指定要排序的列或行的索引以及排序顺序（根据您的要求可以是**升序**或**降序**）
- 最后，我们可以调用**GridDesktop**的**Invalidate**方法来重绘单元格。

在下面的示例中，我们演示了如何按列对数据进行排序。

创建一个**CellRange**的全局对象和**GridDesktop**的**SelectedCellRangeChanged**事件。现在按照下面给出的代码编写：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


现在我们为**升序排序**编写方法。您可以创建一个**升序排序**按钮，并在其**Click**事件中编写下面的代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


最后，我们编写一些代码来实现**降序排序**功能。创建一个**降序排序**按钮，并在其**Click**事件中编写下面的代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
