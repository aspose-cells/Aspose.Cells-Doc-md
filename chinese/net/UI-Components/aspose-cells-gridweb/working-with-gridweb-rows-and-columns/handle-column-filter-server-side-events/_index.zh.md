---
title: 处理列过滤器服务器端事件
type: docs
weight: 90
url: /zh/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

数据筛选可能是使用最广泛的 Excel 功能，它允许您根据特定条件筛选数据。过滤后的数据只显示符合条件的行，隐藏不符合条件的行。
Aspose.Cells.GridWeb 组件提供了使用其界面执行数据过滤的能力。为了扩展其功能，Aspose.Cells.GridWeb 组件还提供了两个事件，可以作为通过 GridWeb UI 完成的过滤机制的回调。

{{% /alert %}} 
## **在应用列过滤器时处理服务器端事件**
有两个主要事件，详述如下。

1. OnBeforeColumnFilter：在过滤器将应用于列之前触发。
1. OnAfterColumnFilter：在列上应用过滤器后触发。

这是 Aspose.Cells.GridWeb 组件的 ASPX 脚本，用于添加和分配上述事件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



这些事件可用于获取有关过滤过程的有用信息，例如必须应用过滤器的列索引和值。以下代码段演示了如何使用 OnBeforeColumnFilter 事件来检索用户在 GridWeb UI 上选择用于过滤的列索引和值。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


另一方面，如果需要在应用过滤器后获取过滤行数，则可以使用 OnAfterColumnFilter 事件，如下所示。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

查看所有介绍[使用 GridWeb 事件](/cells/zh/net/working-with-gridweb-events/)以及有关如何处理这些事件的一些细节。

{{% /alert %}}
