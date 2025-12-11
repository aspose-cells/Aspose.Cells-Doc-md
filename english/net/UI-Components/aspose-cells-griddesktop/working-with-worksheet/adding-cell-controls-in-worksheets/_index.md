---
title: Adding Cell Controls in Worksheets
type: docs
weight: 120
url: /net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: This article introduces how to add control in worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Cell controls are, in fact, those controls that can be added to worksheets. We call them **Cell Controls** because these controls are displayed in cells. In this topic, we will discuss adding and handling the events of these cell controls.

{{% /alert %}} 

## **Introduction**
Currently, Aspose.Cells.GridDesktop **supports** adding three types of cell controls, which include the following:

- **Button**
- **CheckBox**
- **ComboBox**

All of these controls are derived from an abstract class, **CellControl**. Each worksheet contains a collection of **Controls**. New cell controls can be added and existing ones can be accessed using this **Controls** collection easily.

**IMPORTANT:** If you want to add cell controls to all cells of a column instead of adding them one by one, then you can refer to [Managing Cell Controls in Columns.](/cells/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)

### **Adding a Button**
To add a button to the worksheet using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **Button** to the **Controls** collection of the **Worksheet**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}

While adding a **Button**, we can specify the cell's location (where to display it), width and height, and the caption of the button.

#### **Event Handling for the Button**
We have discussed adding a **Button** control to the **Worksheet**, but what is the advantage of just having a button in the worksheet if we cannot use it? Therefore, event handling for the button is necessary.

To handle the **Click** event of the **Button** control, Aspose.Cells.GridDesktop provides the **CellButtonClick** event that should be implemented by developers according to their needs. For instance, we have displayed a message when the button is clicked, as shown below:

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}

#### **Specifying a Background Image for the Button Control**
We can set a background image/picture for the button control while keeping its label/text, as shown in the code below:

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}

**IMPORTANT:** All events of cell controls contain a **CellControlEventArgs** argument that provides the row and column numbers of the cell that contains the cell control (whose event is triggered).

### **Adding a CheckBox**
To add a checkbox to the worksheet using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **CheckBox** to the **Controls** collection of the **Worksheet**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}

While adding a **CheckBox**, we can specify the cell's location (where to display it) and the state of the checkbox.

#### **Event Handling for the CheckBox**
Aspose.Cells.GridDesktop provides the **CellCheckedChanged** event that is triggered when the **Checked** state of the checkbox changes. Developers can handle this event according to their requirements. For instance, we have displayed a message to show the **Checked** state of the checkbox in the code below:

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}

### **Adding a ComboBox**
To add a ComboBox to the worksheet using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Create an array of items (or values) that will be added to **ComboBox**
- Add **ComboBox** to the **Controls** collection of the **Worksheet** by specifying the cell location (where the ComboBox will be displayed) and the items/values that will appear when the ComboBox is clicked

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}

#### **Event Handling for the ComboBox**
Aspose.Cells.GridDesktop provides the **CellSelectedIndexChanged** event that is triggered when the **Selected Index** of the ComboBox changes. Developers can handle this event according to their desires. For instance, we have displayed a message to show the **Selected Item** of the ComboBox:

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
