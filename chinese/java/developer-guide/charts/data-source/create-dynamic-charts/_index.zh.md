---
title: 创建动态图表
type: docs
weight: 200
url: /zh/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

动态（或交互式）图表具有在更改数据范围时更改的能力。换句话说，当数据源更改时，动态图表可以自动反映更改。为了触发数据源的更改，可以使用Excel表的筛选选项或使用诸如ComboBox或下拉列表之类的控件。

本文演示了使用Aspose.Cells for Java API来创建动态图表的方法。

{{% /alert %}}

## **使用Excel表**

{{% alert color="primary" %}}

在Aspose.Cells的视角中，Excel表被称为ListObjects，因此我们将使用"ListObject"一词以明确。请详细阅读如何使用Aspose.Cells for .NET API[创建ListObjects](/cells/zh/java/creating-a-list-object/)。

{{% /alert %}}

ListObjects 提供了内置功能，可以根据用户交互对数据进行排序和过滤。排序和过滤选项都通过下拉列表提供，这些下拉列表会自动添加到 ListObject 的标题行中。由于这些特性（排序和过滤），ListObject 似乎是作为动态图表的数据源的完美候选者，因为当排序或过滤更改时，图表中的数据表示将随着 ListObject 的当前状态而更改。

为了使演示简单易懂，我们将从头开始创建工作簿，并按照下面的步骤一步步地前进。

1. 创建一个空白工作簿。
1. 访问工作簿中的第一个工作表中的单元格。
1. 向单元格插入一些数据。
1. 根据插入的数据创建ListObject。
1. 根据ListObject的数据范围创建图表。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **使用动态公式**

如果您不希望将ListObjects作为动态图表的数据源，另一个选择是使用Excel函数(或公式)创建动态数据范围，并使用控件(如ComboBox)触发数据的变化。在这种情况下，我们将使用VLOOKUP函数根据ComboBox的选择获取适当的值。当选择更改时，VLOOKUP函数将刷新单元格值。如果一系列单元格使用VLOOKUP函数，则可以在用户交互时刷新整个范围，因此可以用作动态图表的源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按照下面的步骤一步步地前进。

1. 创建一个空白工作簿。
1. 访问工作簿中的第一个工作表中的单元格。
1. 通过创建一个命名区域向单元格中插入一些数据。这些数据将作为动态图表的系列。
1. 根据上一步创建的命名区域创建ComboBox。
1. 向单元格中插入一些更多的数据，这些数据将作为VLOOKUP函数的源。
1. 向一系列单元格中插入VLOOKUP函数(带有适当的参数)。这一系列将作为动态图表的源。
1. 根据前一步创建的范围创建图表。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
