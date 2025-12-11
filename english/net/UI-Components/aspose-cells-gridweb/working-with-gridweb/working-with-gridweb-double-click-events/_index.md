---
title: Working with GridWeb Double Click Events
type: docs
weight: 80
url: /net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb,double click,click event,event
description: This article introduces how to use the double click event in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contains three types of double‑click events:

- CellDoubleClick, fired when a cell is double‑clicked.
- ColumnDoubleClick, fired when a column header is double‑clicked.
- RowDoubleClick, fired when a row header is double‑clicked.

This topic discusses how to enable double‑click events in Aspose.Cells.GridWeb. It also discusses creating event handlers for these events.

{{% /alert %}} 
## **Enabling Double Click Events**
All types of double‑click events can be enabled client‑side by setting the GridWeb control's EnableDoubleClickEvent property to true.

{{% alert color="primary" %}} 

By default, the EnableDoubleClickEvent property is set to false. This means that double‑click events are not enabled by default. To implement such events, first enable the feature.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Once double‑click events are enabled, it is possible to create event handlers for any double‑click event. These event handlers perform specific tasks when a given double‑click event is fired.
## **Handling Double Click Events**
To create an event handler in Visual Studio:

1. Double-click an event in the **Events** list in the Properties pane.

For this example, we implemented event handlers for various double‑click events.
### **Double-Click Cell**
The event handler for the CellDoubleClick event provides an argument of the CellEventArgs type, which provides complete information about the cell that is double‑clicked.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Double-Click Column Header**
The event handler for the ColumnDoubleClick event provides an argument of the RowColumnEventArgs type, which provides the index number of the column header that was double‑clicked and other information.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Double-Click Row Header**
The event handler for the RowDoubleClick event provides an argument of the RowColumnEventArgs type, which provides the index number of the row header that was double‑clicked and other related information.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
