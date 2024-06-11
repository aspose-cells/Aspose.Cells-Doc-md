---
title: 对工作表数据进行排序
type: docs
weight: 80
url: /zh/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb，排序
description: 本文介绍如何在GridWeb中对数据进行排序。
---

{{% alert color="primary" %}} 

排序是数据处理时非常宝贵的功能。未经排序的数据在用户搜索特定信息时非常痛苦。Aspose.Cells.GridWeb支持强大的排序功能。本主题讨论使用Aspose.Cells.GridWeb API排序数据。

{{% /alert %}} 
## **排序数据**
Aspose.Cells.GridWeb允许开发人员水平和垂直排序数据，以便开发人员可以从上到下或从左到右排序数据。
### **从上到下**
要从上到下方向排序数据：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问您要排序的工作表。
1. 以任意顺序（升序或降序）对数据范围进行排序。确保选择从上到下的方向。

下面的示例以降序方式对工作表的四列数据进行排序。仅对四列的二十行数据按从上到下的方向进行排序。

应用代码之前，工作表包含无序数据。

![todo:image_alt_text](sort-worksheet-data_1.png)

执行代码后，数据按升序排序。

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **从左到右**
要从左到右排序数据：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问您要排序的工作表。
1. 以任意顺序（升序或降序）对数据范围进行排序。确保选择从左到右的方向。

下面的示例以升序方式对四行数据进行排序。仅对七列的四行数据按从左到右的方向进行排序。

应用代码之前，工作表包含无序数据。

![todo:image_alt_text](sort-worksheet-data_3.png)

执行代码后，数据按升序排序。

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

重要提示：上述示例演示了根据一列（从上到下）或一行（从左到右）的基础上排序数据。Aspose.Cells.GridWeb还可以根据多于一列或行对数据进行排序。要这样做，将列或行的索引数组传递给Sort方法。还支持混合数据类型排序。

{{% /alert %}}
