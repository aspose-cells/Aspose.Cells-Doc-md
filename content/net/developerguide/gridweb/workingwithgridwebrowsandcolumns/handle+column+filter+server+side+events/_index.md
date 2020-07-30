---
title : "Handle Column Filter Server Side Events" 
description : "" 
weight : 16707 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebrowsandcolumns/handle+column+filter+server+side+events/
---

# Aspose.Cells for .NET : Handle Column Filter Server Side Events


Data filtering is probably the most widely used Excel feature that allows you to filter the data based on a specific criteria. Filtered data displays only the rows that meet the condition by hiding the rows that do not fulfill the criteria.  
Aspose.Cells.GridWeb component provides the ability to perform the data filtering using its interface. In order to extend its capabilities, Aspose.Cells.GridWeb component also provides two events that can serve as callback to the filtering mechanism done through the GridWeb UI.

## Handling Server Side Event on Applying Column Filter

There are two main events as detailed below.

1.  `OnBeforeColumnFilter`: Fires before the filter is going to be applied on a column.
2.  `OnAfterColumnFilter`: Fires after the filter has been applied on a column.

Here is the ASPX script of the Aspose.Cells.GridWeb component to add and assign the aforementioned events.

These events can be used to get useful information about the filtering process such as column index and value on which filter has to be applied. Following is the snippet demonstrating the usage of `OnBeforeColumnFilter` event to retrieve the column index and value which user has selected on GridWeb UI for filtering.

  
On the other hand, if the requirement is to get number of filtered rows after the filter has been applied then you can use the `OnAfterColumnFilter` event as demonstrated below.

Check introduction to all [Working with GridWeb Events](http://www.aspose.com/docs/display/cellsnet/Working+with+GridWeb+Events) along with some details on how to handle these event.

