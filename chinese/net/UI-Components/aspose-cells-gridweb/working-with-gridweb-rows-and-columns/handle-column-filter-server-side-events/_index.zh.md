---
title: 处理列过滤器服务器端事件
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: 本文介绍如何处理GridWeb中的列过滤事件。
---

{{% alert color="primary" %}} 

数据筛选可能是最常用的Excel功能之一，它允许您根据特定条件对数据进行筛选。经过筛选的数据仅显示满足条件的行，而隐藏不符合条件的行。
Aspose.Cells.GridWeb 组件通过其界面提供了执行数据筛选的能力。为了扩展其功能，Aspose.Cells.GridWeb 组件还提供了两个事件，可作为通过GridWeb UI进行筛选机制的回调。

{{% /alert %}} 
## **处理应用列过滤器的服务器端事件**
以下是两个主要事件的详细信息。

OnBeforeColumnFilter: 在对列应用筛选器之前触发。
OnAfterColumnFilter: 在对列应用筛选器后触发。

以下是 Aspose.Cells.GridWeb 组件的 ASPX 脚本，用于添加和分配上述事件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



这些事件可用于获取有关筛选过程的有用信息，例如用户为筛选在GridWeb UI上选择的列索引和值。以下是演示如何使用 OnBeforeColumnFilter 事件检索列索引和用户为筛选而选择的值的代码片段。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


另一方面，如果需求是在应用筛选器后获取筛选行的数量，则可以使用如下所示的 OnAfterColumnFilter 事件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

查看有关 [使用GridWeb事件](/cells/zh/net/aspose-cells-gridweb/working-with-gridweb-events/) 的介绍，以及如何处理这些事件的一些详细信息。

{{% /alert %}}
