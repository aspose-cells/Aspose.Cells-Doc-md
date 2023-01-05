---
title: 排序工作表数据
type: docs
weight: 80
url: /zh/net/sorting-worksheet-data/
---
{{% alert color="primary" %}} 

排序是我们在处理数据时最常使用的一项重要的日常任务。在本主题中，我们将借助一个简单示例讨论如何对工作表中的数据进行排序。

{{% /alert %}} 
## **排序工作表数据**
要使用 Aspose.Cells.GridDesktop 的 API 对工作表中的数据进行排序，请按照以下步骤操作：

- 首先创建一个全局对象**单元格范围**这样它就可以在你班级范围内的任何地方访问
- 为创建一个事件处理程序**选定的单元格范围已更改**的事件**网格桌面**. **选定的单元格范围已更改**每次更改用户选择的单元格范围时都会触发事件。例如，如果用户选择单元格（包含要排序的数据），那么每当他的选择范围发生变化时，都会触发此事件。
- 事件处理程序提供**CellRangeEventArgs**进一步以 a 的形式提供单元格（由用户选择）的更新范围的参数**单元格范围**目的。所以，在这个事件处理程序中，我们将分配这个**单元格范围**对象（包含更新的单元格范围）到全局**单元格范围**对象，以便它也可以在代码的其他部分中使用。为了确保我们不会丢失单元格范围，我们将在条件中编写事件处理程序代码
- 现在我们可以编写一些代码来对工作表数据进行排序。首先，访问所需的工作表
- 创建一个**排序范围**将保留其数据要排序的单元格范围的对象。在**排序范围**构造函数，我们可以指定工作表，起始行和列的索引，要排序的行数和列数，排序方向（如从上到下或从左到右）等。
- 现在我们可以打电话**种类**的方法**排序范围**对象来执行数据排序。在**种类**方法，我们可以指定要排序的列或行的索引和排序顺序（可以是**上升**要么**降序**根据您的要求）
- 最后，我们可以调用**无效**的方法**网格桌面**重绘单元格。

在下面给出的示例中，我们演示了如何对列中的数据进行排序。

创建 CellRange 的全局对象和**选定的单元格范围已更改**GridDesktop 的事件。现在编写如下所示的代码：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


现在我们为**升序排序**.您可以创建一个按钮**升序排序**并在其内部编写以下代码**点击**事件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


最后，我们写一些代码来实现**降序排序**功能。创建一个**降序排序**按钮并在其内部写入以下代码**点击**事件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
