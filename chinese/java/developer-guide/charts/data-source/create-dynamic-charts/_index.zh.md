---
title: 创建动态图表
type: docs
weight: 200
url: /zh/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

动态（或交互式）图表具有在更改数据范围时进行更改的能力。换句话说，动态图表可以在数据源更改时自动反映变化。为了触发数据源的更改，可以使用Excel表的筛选选项或使用诸如下拉列表或下拉菜单等控件。

本文演示了使用Aspose.Cells for Java API创建动态图表的用途。

{{% /alert %}}

## **使用Excel表**

{{% alert color="primary" %}}

在Aspose.Cells的视角中，Excel表被称为ListObjects，因此我们将使用术语“ListObject”而不是“Table”，以便更清晰。请详细阅读有关如何使用Aspose.Cells for .NET API [创建ListObjects](/cells/zh/java/creating-a-list-object/)的内容。

{{% /alert %}}

ListObjects提供了内置功能，以根据用户交互进行排序和过滤数据。排序和过滤选项都是通过添加到ListObject的标题行的下拉列表提供的。由于这些功能（排序和过滤），ListObject似乎是作为动态图表的数据源的理想选择，因为当排序或过滤发生变化时，图表中的数据表示将会随着ListObject当前状态的变化而变化。

为了使演示简单易懂，我们将从头开始创建工作簿，然后按以下步骤继续。

1. 创建一个空工作簿。
1. 访问工作簿中第一个工作表的单元格。
1. 向单元格插入一些数据。
1. 基于插入的数据创建ListObject。
1. 基于ListObject的数据范围创建图表。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **使用动态公式**

如果不希望将ListObjects用作动态图表的数据源，则另一个选项是使用Excel函数（或公式）创建动态数据范围，以及使用控件（如ComboBox）来触发数据的更改。在这种情况下，我们将使用VLOOKUP函数根据ComboBox的选择获取适当的值。当选择发生变化时，VLOOKUP函数将刷新单元格值。如果一系列单元格使用了VLOOKUP函数，则在用户交互时可以刷新整个范围，因此可以用作动态图表的数据源。

为了使演示简单易懂，我们将从头开始创建工作簿，然后按以下步骤继续。

1. 创建一个空工作簿。
1. 访问工作簿中第一个工作表的单元格。
1. 通过创建命名范围将一些数据插入到单元格中。此数据将作为动态图表的系列。
1. 基于前一步中创建的命名范围创建ComboBox。
1. 向将作为VLOOKUP函数数据源的单元格中插入更多数据。
1. 向一系列单元格中插入VLOOKUP函数（使用适当的参数）。这个范围将作为动态图表的数据源。
1. 基于前一步中创建的范围创建图表。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
