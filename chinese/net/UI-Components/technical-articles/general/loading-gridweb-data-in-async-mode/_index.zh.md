---
title: 以异步模式加载 GridWeb 数据
type: docs
weight: 40
url: /zh/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

在创建包含大型数据集的工作簿或读取大型 Microsoft Excel 文件时，肯定会花费更多的时间和资源。该进程将占用的总内存始终是一个问题。可以采取一些措施来应对挑战。 Aspose.Cells.GridWeb 提供了一些相关的选项和 API 来降低、减少和优化内存使用。此外，它还可以帮助流程更有效地工作并运行得更快。对于包含大单元格数据的工作表，您可以异步加载数据集，这可以提高用户体验的整体性能。

{{% /alert %}} 

使用 GridWeb.EnableAsync 选项优化单元格数据的内存和性能。为细胞构建大型数据集时。当您将该选项设置为 true 时，数据加载将仅基于当前可见的 Windows 区域。简而言之，当您在 GridWeb 中滚动工作表的单元格数据时，它将仅根据当前滚动位置加载新的 Windows 数据。

以下示例显示如何启用 GridWeb 的异步模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
