---
title: 管理分页
type: docs
weight: 30
url: /zh/net/managing-page-breaks/
description: 本文提供示例代码，说明如何使用C# API或.NET库以编程方式在Excel工作表中添加分页符，清除分页符或删除特定分页符。
keywords: 分页符 c#、Excel 分页符 c#、清除分页符 c#、删除特定分页符 c#
---

{{% alert color="primary" %}}

根据定义，分页是文本流中一页结束并另一页开始的地方。 Microsoft Excel允许用户在工作表的任何选定单元格中添加分页。 

分页符添加在单元格位置后，页面结束并在打印时分页符后的数据打印在下一页。简单地说，分页符根据您的设定将工作表分成多页。您还可以在运行时使用 Aspose.Cells 添加分页符。Aspose.Cells 允许开发人员添加两种分页符：

- 水平分页
- 垂直分页

在接下来的讨论中，我们将描述如何使用Aspose.Cells向工作表添加水平或垂直分页。

{{% /alert %}}

## **分页**

Aspose.Cells 提供了一个代表 Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了用于管理工作表的广泛的属性和方法。

要添加分页符，使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) 和 [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) 属性。

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) 和 [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) 属性是可能包含多个分页符的集合。每个集合都包含用于管理水平和垂直分页符的几种方法。

### **添加分页**

要在工作表中添加分页符，通过调用 [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) 和 [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) 方法，在指定的单元格插入垂直和水平分页符。每个 **Add** 方法都会取添加分页符的单元格名称。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}

### **清除所有分页符**

要清除工作表中的所有分页符，调用 [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) 和 [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) 集合的 [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear) 方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **移除特定的分页符**

要移除特定分页符，调用 [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) 和 [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) 方法。每个 **RemoveAt** 方法都会取要移除的分页符的索引。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **重要提示**

当您在页面设置中设置 **FitToPages** 属性（即 [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) 和 [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)）时，分页符设置会受影响，因此，如果您打印工作表，分页符设置不会考虑，尽管它们仍然被设置。
