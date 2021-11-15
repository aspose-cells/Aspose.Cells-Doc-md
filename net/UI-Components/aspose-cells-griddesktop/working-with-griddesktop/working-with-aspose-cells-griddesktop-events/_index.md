---
title: Working with Aspose.Cells.GridDesktop Events
type: docs
weight: 30
url: /net/working-with-aspose-cells-griddesktop-events/
---

{{% alert color="primary" %}} 

Events are used to send notifications when a change occurs in a control or class. Aspose.Cells.GridDesktop has several events that are used to perform specific tasks when certain changes occur in the control. This topic provides an introduction to all events supported by the Aspose.Cells.GridDesktop control and explains how can to handle those events.

{{% /alert %}} 
## **Introduction**
The Aspose.Cells.GridDesktop control supports several events that provide more control for performing operations when specific events are triggered. Below is a complete list of events supported by the Aspose.Cells.GridDesktop control.

{{% alert color="primary" %}} 

This list doesn't include those events that are inherited by Aspose.Cells.GridDesktop from Control class.

{{% /alert %}} 

|**Events**|**Description**|
| :- | :- |
|SelectedSheetIndexChanged|Occurs when a user selects a new worksheet, that is, when the selected sheet changes from one worksheet to another. This event can also be triggered programmatically if the GridDesktop control's ActiveSheetIndex property changes.|
|RowHeaderClick|Occurs when the row header is clicked.|
|RowHeaderDoubleClick|Occurs when the row header is double clicked.|
|RowColumnHiddenChanged|Occurs when the row or column hidden status is changed.|
|ColumnHeaderClick|Occurs when the column header is clicked.|
|ColumnHeaderDoubleClick|Occurs when the column header is double clicked.|
|FocusedCellChanged|Occurs whenever a cell's focus is changed.|
|CellDataChanged|Occurs when the data or value inside a Grid cell is changed. This event can also be triggered if a cell's value is changed programmatically using the Value property or the SetCellValue method of a GridCell.|
|CellButtonClick|Occurs when the cell button is clicked.|
|CellCheckedChanged|Occurs when the Checked property of cell checkbox is changed.|
|CellSelectedIndexChanged|Occurs when the SelectedIndex property of cell combo-box is changed.|
|CellClick|Occurs when a Grid cell is clicked.|
|CellDoubleClick|Occurs when a Grid cell is double clicked.|
|CellKeyPressed|Occurs when a key is pressed while a cell has focus. If you want to create an event handler for CellKeyPressed event then set the Handled property of CellKeyEventArgs argument to true for preventing the GridDesktop control from handling the key event.|
|AfterInsertRows|Occurs when a row is inserted. You may get the row index by using the Aspose.Cells.GridDesktop.WorksheetEventArgs argument's Index property.|
|AfterInsertColumns|Occurs when a column is inserted. You may get the column index by using the Aspose.Cells.GridDesktop.WorksheetEventArgs argument's Index property.|
## **Handling Grid Events**
To perform a specific operation when a specific event is triggered, create an event handler. An event handler performs a particular task when a certain event is triggered. Below, an event handler is set up to handle a simple Grid event using Visual Studio.NET.

**Step 1: Selecting an Event of Aspose.Cells.GridDesktop Control**

1. In Visual Studio, select the Aspose.Cells.GridDesktop control and open its **Properties** dialog.
1. Click the **Events** tab.
1. Select an event. (for this example, the **CellClick** event is selected).

**Step 2: Creating an Event Handler**

1. Double-click a selected event in the **Properties** dialog.
1. When the event is double clicked, an event handler is created by Visual Studio.NET. Following is designer generated code which shows that an event is created for the GridControl Control.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


Now Add code to perform the desired operation inside the event handler. For this example, we have added a line of code that displays a message box for notifications. 
Have a look at the event handler that visual Studio has added to the GridDesktop control's CellClick event. It'll look something like the code below.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Step 3: Running the Application**

1. Build and run the application.
1. Whenever a grid cell is clicked, a message box with the message "Cell is Clicked" appears.
