---
title: Handle Column Filter Server Side Events
type: docs
weight: 90
url: /net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: This article introduces how to handle column filter event in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Data filtering is probably the most widely used Excel feature that allows you to filter the data based on a specific criterion. Filtered data displays only the rows that meet the condition by hiding the rows that do not meet the criterion.  
Aspose.Cells.GridWeb component provides the ability to perform data filtering using its interface. In order to extend its capabilities, Aspose.Cells.GridWeb component also provides two events that can serve as callbacks to the filtering mechanism performed through the GridWeb UI.

{{% /alert %}} 
## **Handling Server‑Side Events When Applying Column Filters**
There are two main events as detailed below.

1. **OnBeforeColumnFilter**: Fires before the filter is applied to a column.  
2. **OnAfterColumnFilter**: Fires after the filter has been applied to a column.

Here is the ASPX script of the Aspose.Cells.GridWeb component to add and assign the aforementioned events.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}

These events can be used to obtain useful information about the filtering process, such as the column index and the value on which the filter has to be applied. The following snippet demonstrates the usage of the **OnBeforeColumnFilter** event to retrieve the column index and value that the user has selected on the GridWeb UI for filtering.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}

On the other hand, if the requirement is to get the number of filtered rows after the filter has been applied, you can use the **OnAfterColumnFilter** event as demonstrated below.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

See the introduction to all [Working with GridWeb Events](/cells/net/aspose-cells-gridweb/working-with-gridweb-events/) along with details on how to handle these events.

{{% /alert %}}
