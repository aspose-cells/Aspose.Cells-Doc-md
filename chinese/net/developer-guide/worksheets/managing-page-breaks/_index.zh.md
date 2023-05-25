---
title: 管理分页符
type: docs
weight: 30
url: /zh/net/managing-page-breaks/
description: 本文提供示例代码并说明如何使用 C# API 或 .NET 库以编程方式在 Excel 工作表中添加分页符、清除分页符或删除特定分页符。
keywords: page breaks c#, excel page breaks c#, clear page break c#, delete specific page break c#
---
{{% alert color="primary" %}}

根据定义，分页符是文本流中一页结束而下一页开始的位置。 Microsoft Excel 允许用户将分页符添加到工作表的任何选定单元格中。

添加分页符的单元格位置，打印时页面结束，分页符后的剩余数据打印到下一页。简而言之，分页符根据您的规范将您的工作表分成多个页面。您还可以使用 Aspose.Cells 在运行时向工作表添加分页符。Aspose.Cells 允许开发人员添加两种分页符：

- 水平分页符
- 垂直分页符

在接下来的讨论中，我们将介绍如何使用 Aspose.Cells 在工作表中添加水平或垂直分页符。

{{% /alert %}}

##  **分页符**

Aspose.Cells提供了[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Excel 文件的类。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的用于管理工作表的属性和方法。

要添加分页符，请使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**水平分页符**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)和[**垂直分页符**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)特性。

这[**水平分页符**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)和[**垂直分页符**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)属性是可能包含多个分页符的集合。每个集合都包含几种用于管理水平和垂直分页符的方法。

###  **添加分页符**

要在工作表中添加分页符，请通过调用[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index)和[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index)方法。每个**添加**方法采用应添加中断的单元格的名称。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页是如何工作的。

{{% /alert %}}

###  **清除所有分页符**

要清除工作表中的所有分页符，请调用[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection)和[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection)收藏品'[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

###  **删除特定分页符**

要删除特定的分页符，请调用[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat)和[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat)方法。每个**移除位置**方法采用即将删除的分页符的索引。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

##  **重要须知**

当你设置**适合页面**属性（即[**适合页面高**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)和[**适合页面宽度**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)在页面设置中，分页符设置会受到影响，因此，如果您打印工作表，则不会考虑分页符设置，尽管它们仍处于设置状态。
