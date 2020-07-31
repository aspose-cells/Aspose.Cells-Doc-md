---
title : "Adding Cell Controls in Columns" 
description : "" 
weight : 16632 
toc : false
type: docs
url: /net/developerguide/griddesktop/rowsandcolumns/adding+cell+controls+in+columns/
---

# Aspose.Cells for .NET : Adding Cell Controls in Columns


In our later discussions, we have discussed about adding and managing cell controls in worksheet. But, using those approaches, we can add cell controls to single cells one by one. What if someone would like to add cell controls to all cells of one or more columns? In such cases, to reduce the efforts of developers, Aspose.Cells.GridDesktop provides the feature of adding cell controls per column basis. It means that developers can only select a desired column and specify any cell control. The specified cell control will be added to all cells of the specified column. Let's see how can we use this feature.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
    *   1.1 [Adding Button](#adding-button)
    *   1.2 [Adding CheckBox](#adding-checkbox)
    *   1.3 [Adding ComboBox](#adding-combobox)
{{< /panel >}}
 

 

## Introduction

Currently, Aspose.Cells.GridDesktop support adding three types of cell controls, which include the following:

*   **Button**
*   **CheckBox**
*   **ComboBox**

All of these controls are derived from an abstract class, **CellControl**.

**IMPORTANT:** If you want to add cell controls to a single cell instead of the whole column then you can refer to [Adding Cell Controls in Worksheets.](https://docs2.aspose.com/cells/net/developerguide/griddesktop/worksheet/adding+cell+controls+in+worksheets)

### Adding Button

To add buttons into a column using Aspose.Cells.GridDesktop, please follow the steps below:

*   Add Aspose.Cells.GridDesktop control to your **Form**
*   Access any desired **Worksheet**
*   Add **Button** to any specified **Column** of the **Worksheet**

**NOTE:** While adding **Button**, we can specify the width, height and caption of the button.

  
Above code snippet adds buttons to all cells of the specified column. Whenever any cell of that specific column is selected, a button becomes visible. For more information about the event handling of buttons, please refer to the [Event Handling of a Button Control.](http://www.aspose.com/docs/display/cellsnet/Adding+Cell+Controls+in+Worksheets#AddingCellControlsinWorksheets-EventHandlingofButton)

### Adding CheckBox

To add checkboxes into a column using Aspose.Cells.GridDesktop, please follow the steps below:

*   Add Aspose.Cells.GridDesktop control to your **Form**
*   Access any desired **Worksheet**
*   Add **CheckBox** to any specified **Column** of the **Worksheet**

**NOTE:** While adding **CheckBox**, we can also specify the state of the checkbox.

  
Above code snippet adds checkboxes to all cells of the specified column. For more information about the event handling of checkboxes, please refer to the [Event Handling of a CheckBox Control.](http://www.aspose.com/docs/display/cellsnet/Adding+Cell+Controls+in+Worksheets#AddingCellControlsinWorksheets-EventHandlingofCheckBox)

### Adding ComboBox

To add comboboxes into a column using Aspose.Cells.GridDesktop, please follow the steps below:

*   Add Aspose.Cells.GridDesktop control to your **Form**
*   Access any desired **Worksheet**
*   Create an array of items (or values) that will be added to **ComboBox**
*   Add **ComboBox** (containing items or values) to any specified **Column** of the **Worksheet**

  
Above code snippet adds comboboxes to all cells of the specified column. Whenever any cell of that specific column is selected, a combobox becomes visible. For more information about the event handling of comboboxes, please refer to the [Event Handling of a ComboBox Control.](http://www.aspose.com/docs/display/cellsnet/Adding+Cell+Controls+in+Worksheets#AddingCellControlsinWorksheets-EventHandlingofComboBox)

