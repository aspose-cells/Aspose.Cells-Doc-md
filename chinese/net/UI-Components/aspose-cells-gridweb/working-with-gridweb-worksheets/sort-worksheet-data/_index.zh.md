---
title: 对工作表数据进行排序
type: docs
weight: 80
url: /zh/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb，排序
description: 本文介绍如何在GridWeb中对数据进行排序。
---

{{% alert color="primary" %}} 

数据处理时，排序是非常有价值的功能。未排序的数据在搜索特定信息时对用户来说是一个痛点。Aspose.Cells.GridWeb支持强大的排序功能。本主题讨论使用Aspose.Cells.GridWeb API对数据进行排序。

{{% /alert %}} 
## **数据排序**
Aspose.Cells.GridWeb允许开发人员按水平和垂直方向对数据进行排序，使开发人员可以从上到下或从左到右对数据进行排序。
### **从上到下**
要按从上到下的方向对数据进行排序：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问要进行排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。确保选择从上到下的方向。

以下示例按降序对工作表中的四列数据进行排序。仅排序了四列的前二十行，排序为从上到下。

在应用代码之前，工作表包含无序数据。

![todo:image_alt_text](sort-worksheet-data_1.png)

执行代码后，数据按升序排序。

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **从左到右**
要按从左到右的方向对数据进行排序：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问要进行排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。确保选择从左到右的方向。

以下示例按升序对四行数据进行排序。仅对七列中的四行进行排序，排序为从左到右。

在应用代码之前，工作表包含无序数据。

![todo:image_alt_text](sort-worksheet-data_3.png)

执行代码后，数据按升序排序。

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

重要提示：上述示例演示了根据一列（从上到下）或行（从左到右）排序数据的基础。 Aspose.Cells.GridWeb还可以根据多个列或行对数据进行排序。为此，请将列或行索引数组传递给Sort方法。还支持混合数据类型排序。

{{% /alert %}}
