---
title: Handle Column Filter Server Side Events
type: docs
weight: 90
url: /net/handle-column-filter-server-side-events/
---

{{% alert color="primary" %}} 

Data filtering is probably the most widely used Excel feature that allows you to filter the data based on a specific criteria. Filtered data displays only the rows that meet the condition by hiding the rows that do not fulfill the criteria.
Aspose.Cells.GridWeb component provides the ability to perform the data filtering using its interface. In order to extend its capabilities, Aspose.Cells.GridWeb component also provides two events that can serve as callback to the filtering mechanism done through the GridWeb UI.

{{% /alert %}} 
## **Handling Server Side Event on Applying Column Filter**
There are two main events as detailed below.

1. OnBeforeColumnFilter: Fires before the filter is going to be applied on a column.
1. OnAfterColumnFilter: Fires after the filter has been applied on a column.

Here is the ASPX script of the Aspose.Cells.GridWeb component to add and assign the aforementioned events.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



These events can be used to get useful information about the filtering process such as column index and value on which filter has to be applied. Following is the snippet demonstrating the usage of OnBeforeColumnFilter event to retrieve the column index and value which user has selected on GridWeb UI for filtering.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


On the other hand, if the requirement is to get number of filtered rows after the filter has been applied then you can use the OnAfterColumnFilter event as demonstrated below.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Check introduction to all [Working with GridWeb Events](http://www.aspose.com/docs/display/cellsnet/Working+with+GridWeb+Events) along with some details on how to handle these event.

{{% /alert %}}
