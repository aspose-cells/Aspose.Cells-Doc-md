---
title: Adding Cell Controls in Worksheets
type: docs
weight: 120
url: /net/adding-cell-controls-in-worksheets/
---

{{% alert color="primary" %}} 

Cell controls are in fact those controls that can be added to worksheets. We call them **Cell Controls** because these controls are displayed in cells. In this topic, we will discuss about adding and handling the events of these cell controls.

{{% /alert %}} 
## **Introduction**
Currently, Aspose.Cells.GridDesktop support adding three types of cell controls, which include the following:

- **Button**
- **CheckBox**
- **ComboBox**

All of these controls are derived from an abstract class, **CellControl**. Each worksheet contains a collection of **Controls**. New cell controls can be added and existing ones can be accessed using this **Controls** collection easily.

**IMPORTANT:** If you want to add cell controls to all cells of a column instead of adding one by one then you can refer to [Managing Cell Controls in Columns.](/cells/net/adding-cell-controls-in-worksheets/)
### **Adding Button**
To add a button into the worksheet using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **Button** to the **Controls** collection of the **Worksheet**



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


While adding **Button** , we can specify the cell's location (where to display it), width & height and the caption of the button.
#### **Event Handling of Button**
We have discussed about adding **Button** control to the **Worksheet** but what is the advantage of just having a button in the worksheet if we cannot use it. So, here comes the need of event handling of the button.

To handle the **Click** event of the **Button** control, Aspose.Cells.GridDesktop provides **CellButtonClick** event that should be implemented by the developers according to their needs. For an instance, we have just displayed a message when the button is clicked as shown below:



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Specifying a Background Image for the Button Control**
We can set background image/picture for the button control with its label/text as shown in the code below:



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**IMPORTANT:** All events of cell controls contain a **CellControlEventArgs** argument that provides the row and column numbers of the cell that contains the cell control (whose event is triggered).
### **Adding CheckBox**
To add a checkbox into the worksheet using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **CheckBox** to the **Controls** collection of the **Worksheet**



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


While adding **CheckBox** , we can specify the cell's location (where to display it) and state of the checkbox.
#### **Event Handling of CheckBox**
Aspose.Cells.GridDesktop provides **CellCheckedChanged** event that is triggered when the **Checked** state of the checkbox is changed. Developers can handle this event according to their requirements. For an instance, we have just displayed a message to show the **Checked** state of the checkbox in the code below:



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Adding ComboBox**
To add a combobox into the worksheet using Aspose.Cells.GridDesktop , please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Create an array of items (or values) that will be added to **ComboBox**
- Add **ComboBox** to the **Controls** collection of the **Worksheet** by specifying the location of cell (where combobox will be displayed) and the items/values that will be displayed when the combobox will be clicked



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Event Handling of ComboBox**
Aspose.Cells.GridDesktop provides **CellSelectedIndexChanged** event that is triggered when the **Selected Index** of combobox is changed. Developers can handle this event according to their desires. For an instance, we have just displayed a message to show the **Selected Item** of the combobox:



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
