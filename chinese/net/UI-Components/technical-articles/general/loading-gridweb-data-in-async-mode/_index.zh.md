---
title: 在异步模式中加载GridWeb数据
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: 本文描述如何使用异步模式以获得更好的GridWeb性能。
keywords: GridWeb,性能,异步,异步模式
---

{{% alert color="primary" %}} 

当创建一个包含大型数据集的工作簿或读取一个庞大的 Microsoft Excel 文件时，这必定会花费更多时间和资源。进程将占用的总内存始终是一个问题。可以采取措施来应对这一挑战。Aspose.Cells.GridWeb提供了一些相关选项和API以降低、减少和优化内存使用。此外，它可以帮助进程更高效、运行得更快。对于包含大型单元格数据的工作表，您可以异步加载数据集，这可以改进用户体验的总体性能。

{{% /alert %}} 

使用GridWeb.EnableAsync选项来优化单元格数据的内存和性能。在构建大型数据集以供单元格使用时，当您将选项设置为真时，数据加载将基于当前可见的窗口区域。简而言之，当您在GridWeb的工作表中滚动单元格数据时，它将仅基于当前滚动位置加载新的窗口数据。

以下示例显示了如何启用GridWeb的异步模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
