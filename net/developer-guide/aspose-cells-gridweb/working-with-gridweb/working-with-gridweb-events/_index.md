---
title: Working with GridWeb Events
type: docs
weight: 70
url: /net/working-with-gridweb-events/
---

{{% alert color="primary" %}} 

All programmers must be familiar with events and their purpose. Events are used to send notifications of changes that may occur in a control or class. Aspose.Cells.GridWeb has several events that can be used to perform specific tasks when certain changes occur in the control.

This topic provides an introduction to all events supported by the Aspose.Cells.GridWeb control along with some details on how to handle these events.

{{% /alert %}} 
## **Working with Grid Events**
### **Introduction to Grid Events**
Aspose.Cells.GridWeb control supports several events that provide more control for performing operations when specific events are triggered in the control. A complete list of events supported by Aspose.Cells.GridWeb control can be found below.

{{% alert color="primary" %}} 

This list doesn't include events inherited by Aspose.Cells.GridWeb from the Control class.

{{% /alert %}} 

|**Events** |**Description** |
| :- | :- |
|CellCommand |Occurs when the command hyperlink of a cell is clicked. When this event is fired, its parameter e.Argument provides the command's name. |
|CellDoubleClick |Occurs when the cell is double clicked. |
|CellError |Occurs when a cell's input value has some error. |
|ColumnDeleted |Occurs when a user deletes a column from a worksheet using client side menu. |
|ColumnDeleting |Occurs when a user is trying to delete a column from a worksheet using client side menu. |
|ColumnDoubleClick |Occurs when the column header is double clicked. |
|ColumnInserted |Occurs when a user inserts a column into worksheet using client side menu. |
|CustomCommand |Occurs when a user clicks a custom command button. |
|LoadCustomData |Occurs when the control's EnableSession property is set to false and needs to load worksheet data. You may handle this event in sessionless mode to load worksheet data from a file or database. |
|PageIndexChanged |Occurs when the control's sheet page index is changed. |
|RowDeleted |Occurs when a user deletes a row from a worksheet using client side menu. |
|RowDeleting |Occurs when a user is trying to delete a row from a worksheet using client side menu. |
|RowDoubleClick |Occurs when the row header is double clicked. |
|RowInserted |Occurs when a user inserts a row into worksheet using client side menu. |
|SaveCommand |Occurs when the **Save** button is clicked. |
|SheetDataUpdated |Occurs when the control has loaded the posted data and updated the worksheet data. |
|SheetTabClick |Occurs when a sheet tab is clicked. |
|SubmitCommand |Occurs when the **Submit** button is clicked. |
|UndoCommand |Occurs when the **Undo** button is clicked. |
|AjaxCallFinished |Fires when the AJAX update of the control finished. (the EnableAJAX shall be set to true). |
|CellModifiedOnAjax |Fires when the cell is modified in AJAX call. |
|OnAfterColumnFilter |Fires after the filter has applied on a column. |
|OnBeforeColumnFilter |Fires before the filter is applied on a column. |
## **Handling Grid Events**
To perform a specific operation on triggering a specific event, we have to create an event handler. An event handler performs the desired task when a certain event is triggered. The steps illustrated below shows how to handle a simple grid event using Visual Studio.
### **Step 1: Selecting an Event of Aspose.Cells.GridWeb Control**
1. Select the Aspose.Cells.GridWeb control and open its Properties dialog on the right side.
1. Click the **Events Tab** button.
1. Select an event.
   For this example, the SaveCommand event is selected.
### **Step 2: Creating an Event Handler**
1. Double-click an event in the Properties dialog. 

   **Double clicking on a selected event** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




When the event is double-clicked, an event handler is automatically created by Visual Studio. 

**An event handler created by Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Add code to perform some action inside the event handler.

Here, a single line of code that saves the grid content to an Excel file when the **Save** button is clicked has been added.

To get more information, move the cursor above to see some code then you will find out that Visual Studio is intelligent enough to add an event handler to the GridWeb's SaveCommand event.
### **Step 3: Running Your Application**
1. Build and run the application.
1. Click **Save**.

The grid content is saved to an Excel file. 

**Application in running mode** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
