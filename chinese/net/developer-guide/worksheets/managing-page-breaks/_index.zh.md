---
title: 管理分页
type: docs
weight: 30
url: /zh/net/managing-page-breaks/
description: 本文提供示例代码并解释了如何使用C# API或.NET库以编程方式在Excel工作表中添加分页符、清除分页符或删除特定分页符。
keywords: 分页符c#，Excel分页符c#，清除分页符c#，删除特定分页符c#
---

{{% alert color="primary" %}}

根据定义，分页是文本流中一个页面结束并另一个页面开始的地方。Microsoft Excel允许用户将分页符添加到工作表的任何选定单元格中。

添加分页符的位置，页面结束并在打印时分页符后的数据打印在下一页。简单来说，分页符根据您的规范将工作表分成多个页面。您还可以在运行时使用Aspose.Cells添加分页符。Aspose.Cells允许开发人员添加两种类型的分页符：

- 水平分页
- 垂直分页

在下面的讨论中，我们将描述如何使用Aspose.Cells将水平或垂直分页符添加到工作表中。

{{% /alert %}}

## **分页符**

Aspose.Cells提供了一个代表Excel文件的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了用于管理工作表的广泛的属性和方法。

要添加分页符，请使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)和[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)属性。

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)和[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)属性是可能包含多个分页符的集合。每个集合都包含用于管理水平和垂直分页符的多个方法。

### **添加分页符**

要在工作表中添加分页符，通过调用[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index)和[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index)方法在指定单元格插入垂直和水平分页符。每个**Add**方法都接受应添加分页符的单元格名称。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

在分页符预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}

### **清除所有分页符**

要清除工作表中的所有分页符，请调用[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection)和[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection)集合的[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **移除特定分页符**

要移除特定的分页符，请调用[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat)和[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat)方法。每个**RemoveAt**方法都需要要移除的分页符的索引。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **重要提示**

当您在页面设置中设置**FitToPages**属性（即[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)和[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)）时，会影响分页符设置，因此，如果打印工作表，则不会考虑分页符设置，尽管它们仍然已设置。
