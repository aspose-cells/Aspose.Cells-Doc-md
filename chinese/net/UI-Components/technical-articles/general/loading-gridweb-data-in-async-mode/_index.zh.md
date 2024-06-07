---
title: 以异步模式加载GridWeb数据
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: 本文介绍了如何在GridWeb中使用异步模式以获得更好的性能。
keywords: GridWeb，性能，异步，异步模式
---

{{% alert color="primary" %}} 

创建带有大数据集的工作簿，或读取大型Microsoft Excel文件时，所需的时间和资源肯定会更多。进程占用的总内存一直是个问题。可以采取措施来应对这个挑战。Aspose.Cells.GridWeb提供了一些相关选项和API，以降低、减少和优化内存使用量。此外，它还可以帮助进程更高效地运行，运行更快。对于包含大型单元格数据的工作表，可以异步加载数据集，以提高用户体验的整体性能。

{{% /alert %}} 

使用GridWeb.EnableAsync选项来优化单元格数据的内存和性能。在构建用于单元格的大型数据集时。当将选项设置为true时，数据加载将仅基于当前可见的窗口区域。简而言之，当在GridWeb中滚动工作表的单元格数据时，它将仅基于当前滚动位置加载新的窗口数据。

以下示例显示了如何启用GridWeb的异步模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
