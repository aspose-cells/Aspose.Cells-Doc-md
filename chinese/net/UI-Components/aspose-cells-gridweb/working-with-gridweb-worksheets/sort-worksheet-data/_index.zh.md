---
title: 排序工作表数据
type: docs
weight: 80
url: /zh/net/sort-worksheet-data/
---
{{% alert color="primary" %}} 

在数据处理方面，排序是一项非常有价值的功能。在搜索特定信息时，未排序的数据对用户来说是一种痛苦。 Aspose.Cells.GridWeb支持强大的排序功能。本主题讨论使用 Aspose.Cells.GridWeb API 对数据进行排序。

{{% /alert %}} 
## **排序数据**
Aspose.Cells.GridWeb 允许开发者对数据进行水平和垂直排序，以便开发者可以从上到下或从左到右对数据进行排序。
### **从上到下**
要从上到下对数据进行排序：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。请务必选择从上到下的方向。

下面的示例按降序对工作表的四列中的数据进行排序。四列中只有二十行按从上到下的方向排序。

在应用代码之前，工作表包含无序数据。

![待办事项：图像_替代_文本](sort-worksheet-data_1.png)

执行代码后，数据按升序排序。

![待办事项：图像_替代_文本](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **从左到右**
从左到右对数据进行排序：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。一定要选择从左到右。

下面的示例按升序对四行中的数据进行排序。只有四行七列从左到右排序。

在应用代码之前，工作表包含无序数据。

![待办事项：图像_替代_文本](sort-worksheet-data_3.png)

执行代码后，数据按升序排序。

![待办事项：图像_替代_文本](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

重要提示：以上示例演示了根据一列（从上到下）或一行（从左到右）对数据进行排序。 Aspose.Cells.GridWeb 还可以根据多列或多行对数据进行排序。为此，将列或行索引数组传递给 Sort 方法。还支持混合数据类型排序。

{{% /alert %}}
