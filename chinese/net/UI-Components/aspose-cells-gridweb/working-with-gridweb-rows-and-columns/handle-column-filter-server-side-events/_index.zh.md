---
title: 处理列过滤服务器端事件
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb，filter，OnBeforeColumnFilter，OnAfterColumnFilter
description: 本文介绍如何处理 GridWeb 中的列过滤事件。
---

{{% alert color="primary" %}} 

数据过滤可能是最常用的 Excel 功能之一，允许您根据特定条件过滤数据。经过过滤的数据仅显示符合条件的行，隐藏不满足条件的行。
Aspose.Cells.GridWeb 组件提供了使用其界面进行数据过滤的功能。为了扩展其功能，Aspose.Cells.GridWeb 组件还提供了两个事件，可作为回调用于通过 GridWeb UI 执行的过滤机制。

{{% /alert %}} 
## **处理应用列过滤的服务器端事件**
下面详细介绍了两个主要事件。

1. OnBeforeColumnFilter: 在对列应用过滤之前触发。
1. OnAfterColumnFilter: 在对列应用过滤后触发。

以下是 Aspose.Cells.GridWeb 组件的 ASPX 脚本，用于添加和分配上述事件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



这些事件可用于获取有关过滤进程的有用信息，例如用户在 GridWeb UI 中选择用于过滤的列索引和值。以下是演示如何使用 OnBeforeColumnFilter 事件检索用户在 GridWeb UI 中选择的列索引和值的代码片段。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


另一方面，如果需要在应用过滤后获取过滤行数，则可以使用下面的演示使用 OnAfterColumnFilter 事件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

查看[使用GridWeb事件](/cells/zh/net/aspose-cells-gridweb/working-with-gridweb-events/)的简介，以及如何处理这些事件的详细信息。

{{% /alert %}}
