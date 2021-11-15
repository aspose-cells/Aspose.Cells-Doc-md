---
title: Adding Cell Controls in Columns
type: docs
weight: 90
url: /net/adding-cell-controls-in-columns/
---

{{% alert color="primary" %}} 

In our later discussions, we have discussed about adding and managing cell controls in worksheet. But, using those approaches, we can add cell controls to single cells one by one. What if someone would like to add cell controls to all cells of one or more columns? In such cases, to reduce the efforts of developers, Aspose.Cells.GridDesktop provides the feature of adding cell controls per column basis. It means that developers can only select a desired column and specify any cell control. The specified cell control will be added to all cells of the specified column. Let's see how can we use this feature.

{{% /alert %}} 
## **Introduction**
Currently, Aspose.Cells.GridDesktop support adding three types of cell controls, which include the following:

- **Button**
- **CheckBox**
- **ComboBox**

All of these controls are derived from an abstract class, **CellControl**.

**IMPORTANT:** If you want to add cell controls to a single cell instead of the whole column then you can refer to [Adding Cell Controls in Worksheets.](/cells/net/adding-cell-controls-in-worksheets/)
### **Adding Button**
To add buttons into a column using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **Button** to any specified **Column** of the **Worksheet**

**NOTE:** While adding **Button**, we can specify the width, height and caption of the button.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


Above code snippet adds buttons to all cells of the specified column. Whenever any cell of that specific column is selected, a button becomes visible. For more information about the event handling of buttons, please refer to the [Event Handling of a Button Control.](/cells/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Adding CheckBox**
To add checkboxes into a column using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **CheckBox** to any specified **Column** of the **Worksheet**

**NOTE:** While adding **CheckBox**, we can also specify the state of the checkbox.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


Above code snippet adds checkboxes to all cells of the specified column. For more information about the event handling of checkboxes, please refer to the [Event Handling of a CheckBox Control.](/cells/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Adding ComboBox**
To add comboboxes into a column using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Create an array of items (or values) that will be added to **ComboBox**
- Add **ComboBox** (containing items or values) to any specified **Column** of the **Worksheet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


Above code snippet adds comboboxes to all cells of the specified column. Whenever any cell of that specific column is selected, a combobox becomes visible. For more information about the event handling of comboboxes, please refer to the [Event Handling of a ComboBox Control.](/cells/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
