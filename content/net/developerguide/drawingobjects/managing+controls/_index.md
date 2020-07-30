---
title : "Managing Controls" 
description : "" 
weight : 12287 
toc : false
type: docs
url: /net/developerguide/drawingobjects/managing+controls/
---

# Aspose.Cells for .NET : Managing Controls


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Adding Text Box Control to a Worksheet](#adding-text-box-control-to-a-worksheet)
*   3 [Manipulating Text Box Controls in Designer Spreadsheets](#manipulating-text-box-controls-in-designer-spreadsheets)
*   4 [Adding Check Box Control to a Worksheet](#adding-check-box-control-to-a-worksheet)
    *   4.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   4.2 [Using Aspose.Cells](#using-aspose.cells)
*   5 [Adding Radio Button Control to the Worksheet](#adding-radio-button-control-to-the-worksheet)
    *   5.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   5.2 [Using Aspose.Cells](#using-aspose.cells)
*   6 [Adding Combo Box Control to a Worksheet](#adding-combo-box-control-to-a-worksheet)
    *   6.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   6.2 [Using Aspose.Cells](#using-aspose.cells)
*   7 [Adding Label Control to a Worksheet](#adding-label-control-to-a-worksheet)
*   8 [Adding List Box Control to a Worksheet](#adding-list-box-control-to-a-worksheet)
    *   8.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   8.2 [Using Aspose.Cells](#using-aspose.cells)
*   9 [Adding Button Control to a Worksheet](#adding-button-control-to-a-worksheet)
    *   9.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   9.2 [Using Aspose.Cells](#using-aspose.cells)
*   10 [Adding Line Control to the Worksheet](#adding-line-control-to-the-worksheet)
    *   10.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   10.2 [Using Aspose.Cells](#using-aspose.cells)
    *   10.3 [Adding an Arrow Head to a Line](#adding-an-arrow-head-to-a-line)
*   11 [Adding Rectangle Control to a Worksheet](#adding-rectangle-control-to-a-worksheet)
    *   11.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   11.2 [Using Aspose.Cells](#using-aspose.cells)
*   12 [Adding Arc Control to the Worksheet](#adding-arc-control-to-the-worksheet)
    *   12.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   12.2 [Using Aspose.Cells](#using-aspose.cells)
*   13 [Adding Oval Control to a Worksheet](#adding-oval-control-to-a-worksheet)
    *   13.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   13.2 [Using Aspose.Cells](#using-aspose.cells)
*   14 [Adding Spinner Control to the Worksheet](#adding-spinner-control-to-the-worksheet)
    *   14.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   14.2 [Using Aspose.Cells](#using-aspose.cells)
*   15 [Adding Scroll Bar Control to a Worksheet](#adding-scroll-bar-control-to-a-worksheet)
    *   15.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   15.2 [Using Aspose.Cells](#using-aspose.cells)
*   16 [Adding GroupBox Control to Group Controls in a Worksheet](#adding-groupbox-control-to-group-controls-in-a-worksheet)
    *   16.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   16.2 [Using Aspose.Cells](#using-aspose.cells)
{{< /panel >}}
 

## Introduction

Developers can add different drawing objects such as text boxes, check boxes, radio buttons, combo boxes, labels, buttons, lines, rectangles, arcs, ovals, spinners, scroll bars, group boxes etc. Aspose.Cells provides the `Aspose.Cells.Drawing` namespace which contains all the drawing objects. However, there are a few drawing objects or shapes that are not supported yet. Create these drawing objects in a designer spreadsheet using Microsoft Excel and then import the designer spreadsheet to Aspose.Cells. Aspose.Cells allows you to load these drawing objects from a designer spreadsheet and write them to a generated file.

## Adding Text Box Control to a Worksheet

One way to stress important information in a report is to use a text box. For example, add text to highlight the company name or to indicate the geographic region with the highest sales etc. Aspose.Cells provides the `TextBoxCollection` class, used to add a new text box to the collection. There is another class, `TextBox`, which represents a text box used to define all types of settings. It has some important members:

*   The `TextFrame` property returns a `MsoTextFrame` object used to adjust the contents of the text box.
*   The `Placement` property specifies the placement type.
*   The `Font` property specifies the font attributes.
*   The `AddHyperlink` method adds a hyperlink for the text box.
*   The `FillFormat` property returns an `MsoFillFormat` object used to set the fill format for the text box.
*   The `LineFormat` property returns the `MsoLineFormat` object usually used to style and weight of the text box line.
*   The `Text` property specifies the input text for the text box.

The following example creates two textboxes in the first worksheet of the workbook. The first text box is well-furnished with differnt format settings. The second is a simple one.

## Manipulating Text Box Controls in Designer Spreadsheets

Aspose.Cells also lets you access textboxes in the desinger worksheets and manipulate them. Use the `Worksheet.TextBoxes` property to get the textboxes collection in the sheet.

The following example uses the Microsoft Excel file that we created in the above example. It gets the text strings of the two textboxes and changes the text of the second textbox to save the file.

## Adding Check Box Control to a Worksheet

Check boxes are handy if you want to provide a way for a user to choose between two options, such as true or false; yes or no. Aspose.Cells allows you to use check boxes in worksheets. For instance, you may have developed a financial projection worksheet in which you can either account for a particular acquisition or not. In this case, you might want to place a check box at the top of the worksheet. You can then link the status of this check box to another cell, so that if the check box is selected, the value of the cell is True; if it is not selected, the value of the cell is False.

### Using Microsoft Excel

To place a check box control in your worksheet, follow these steps:

1.  Make sure the Forms toolbar is displayed.
2.  Click the **Check Box** tool on the Forms toolbar.
3.  In your worksheet area, click and drag to define the rectangle that will hold the check box and the label beside the check box.
4.  Once the check box is placed, move the mouse cursor into the label area and change the label.
5.  In the **Cell Link** field, specify the address of the cell to which this check box should be linked.
6.  Click on **OK**.

### Using Aspose.Cells

Aspose.Cells provides the `CheckBoxCollection` class, which is used to add a new check box to the collection. There is another class, `Aspose.Cells.Drawing.CheckBox`, which represents a check box. It has some important members:

*   The `LinkedCell` property specifies a cell which is linked to the check box.
*   The `Text` property specifies the text string associated with the check box. It is the label of the check box.
*   The `Value` property specifies if the check box is checked or not.

The following example shows how to add a checkbox to the worksheet.

## Adding Radio Button Control to the Worksheet

A radio button, or an option button, is a control made of a round box. The user makes his or her decision by selecting the round box. A radio button is usually, if not always, accompanied by others. Such radio buttons appear and behave as a group. The user decides which button is valid by selecting only one of them. When the user clicks one button, it is filled. When one button in the group is selected, buttons of the same group are empty.

### Using Microsoft Excel

To place a Radio Button control in your worksheet, follow these steps:

1.  Make sure the **Forms** toolbar is displayed.
2.  Click the **Option Button** tool.
3.  In the worksheet, click and drag to define the rectangle that will hold the option button and the label beside the option button.
4.  Once the radio button is placed in the worksheet, move the mouse cursor into the label area and change the label.
5.  In the **Cell Link** field, specify the address of the cell to which this radio button should be linked.
6.  Click **OK**.

### Using Aspose.Cells

`Aspose.Cells.Drawing.ShapeCollection` class provides a method named `AddRadioButton`, which is used to add a radio button control to a worksheet. The method returns an `Aspose.Cells.Drawing.RadioButton` object. The class `Aspose.Cells.Drawing.RadioButton` represents an option button. It has some important members:

*   The `LinkedCell` property specifies a cell which is linked to the radio button.
*   The `Text` property specifies the text string associated with the radio button. It is the label of the radio button.
*   The `IsChecked` property specifies if the radio button is checked or not.
*   The `FillFormat` property specifies the fill format of the radio button.
*   The `LineFormat` property specifies the line format styles of the option button.

The following example shows how to add radio buttons to a worksheet. The example adds three radio buttons representing age groups.

## Adding Combo Box Control to a Worksheet

To make data entry easier, or to limit entries to certain items that you define, you can create a combo box, or drop-down list of valid entries that is compiled from cells elsewhere on the worksheet. When you create a drop-down list for a cell, it displays an arrow next to that cell. To enter information in that cell, click the arrow, and then click the entry that you want.

### Using Microsoft Excel

To place a combo box control in your worksheet, follow these steps:

1.  Make sure the **Forms** toolbar is displayed.
2.  Click on the **Combo Box** tool.
3.  In your worksheet area, click and drag to define the rectangle that will hold the combo box.
4.  Once the combo box is placed in the worksheet, right-click the control to click **Format Control** and specify the input range.
5.  In the **Cell Link** field, specify the address of the cell to which this combo box should be linked.
6.  Click on **OK**.

### Using Aspose.Cells

The `Aspose.Cells.Drawing.ShapeCollection` class provides a method named `AddComboBox`, which is used to add a combo box control to a worksheet. The method returns an `Aspose.Cells.Drawing.ComboBox` object. The class `Aspose.Cells.Drawing.ComboBox` represents a combo box. It has some important members:

*   The `LinkedCell` property specifies a cell which is linked to the combo box.
*   The `InputRange` property specifies the worksheet range of cells used to fill the combo box.
*   The `DropDownLines` property specifies the number of list lines displayed in the drop-down portion of a combo box.
*   The `Shadow` property indicates whether the combo box has 3D shading.

The following example shows how to add a combo box to the worksheet.

## Adding Label Control to a Worksheet

Labels ar a means of give users information about a speadsheet's contents. Aspose.Cells makes it possible to add and manipulate labels in a worksheet. The `ShapeCollection` class provides a method named `addShape`, used to add a label control to the worksheet. The method returns a `Label` object. The class `Label` represents a label in the worksheet. It has some important members:

*   The `Text` method specifies a label's caption string.
*   The `Placement` method specifies the `PlacementType`, the way the label is attached to the cells in the worksheet.

The following example shows how to add a label to the worksheet.

## Adding List Box Control to a Worksheet

A list box control creates a list control that allows single or multiple item selection.

### Using Microsoft Excel

To place a list box control in a worksheet:

1.  Make sure the **Forms** toolbar is displayed.
2.  Click on the **List Box** tool.
3.  In your worksheet area, click and drag to define the rectangle that will hold the list box.
4.  Once the list box is placed in the worksheet, right-click on the control to click **Format Control** and specify the input range.
5.  In the **Cell Link** field, specify the address of the cell to which this list box should be linked and set the selection type (Single, Multi, Extend) attribute
6.  Click **OK**.

### Using Aspose.Cells

The `ShapeCollection` class provides a method named `AddListBox`, which is used to add a list box control to a worksheet. The method returns a `Aspose.Cells.Drawing.ListBox` object. The class `ListBox` represents a list box. It has some important members:

*   The `LinkedCell` method specifies a cell which is linked to the list box.
*   The `InputRange` method specifies the worksheet range of cells used to fill the list box.
*   The `SelectionType` method specifies the selection mode of the the list box.
*   The `Shadow` method indicates whether the list box has 3D shading.

The following example shows how to add a list box to the worksheet.

## Adding Button Control to a Worksheet

Buttons are useful to perform some actions. Sometimes, it is useful to assign a VBA Macro to the button or assign a hyperlink to open a web page.

### Using Microsoft Excel

To place a button control in your worksheet:

1.  Make sure the **Forms** toolbar is displayed.
2.  Click on the **Button** tool.
3.  In your worksheet area, click and drag to define the rectangle that will hold the button.
4.  Once the list box is placed in the worksheet, right-click on the control and select **Format Control**, then specify a VBA Macro and attributes related font, alignment, size, margin etc.
5.  Click on **OK**.

### Using Aspose.Cells

The `Aspose.Cells.Drawing.ShapeCollection` class provides a method named `AddButton`, used to add a button control to the worksheet. The method returns an `Aspose.Cells.Drawing.Button` object. The class `Aspose.Cells.Drawing.Button` represents a button. It has some important members:

*   The `Text` property specifies the caption of button.
*   The `Font` property specifies the font attributes for the label of the button control.
*   The `Placement` property specifies the `PlacementType`, the way the button is attached to the cells in the worksheet.
*   The `AddHyperlink` property adds a hyperlink for the button control. Clicking on the button will navigate to related URL.

The following example shows how to add a button to the worksheet.

## Adding Line Control to the Worksheet

### Using Microsoft Excel

1.  On the **Drawing** toolbar, click **AutoShapes**, point to **Lines**, and select the line style you want.
2.  Drag to draw the line.
3.  Do one or both of the following:
    *   To constrain the line to draw at 15-degree angles from its starting point, hold down SHIFT as you drag.
    *   To lengthen the line in opposite directions from the first end point, hold down CTRL as you drag.

### Using Aspose.Cells

The `Aspose.Cells.Drawing.ShapeCollection` class provides a method named `AddLine`, which is used to add a line shape to the worksheet. The method return a `LineShape` object. The class `LineShape` represents a line. It has some important members:

*   The `LineFormat` method specifies the format of a line.
*   The `Placement` method specifies the `PlacementType`, the way the line is attached to the cells in the worksheet.

The following example shows how to add lines to the worksheet. It creates three lines with different styles.

### Adding an Arrow Head to a Line

Aspose.Cells also allows you to draw arrow lines. It is possible to add an arrowhead to a line, and to format the line. For example, you can change the color of the line, or specify the weight and style of the line.

The following example shows how to add an arrowhead to a line.

## Adding Rectangle Control to a Worksheet

Aspose.Cells allows you to draw rectangle shapes in your worksheets. You may create a rectangle, square etc. You are also allowed to format the filling color and border line color of the control. For example, you can change the color of the rectangle, set the shading color, specify the weight and style of the rectangle for your need.

### Using Microsoft Excel

1.  On the **Drawing** toolbar, click **Rectangle**.
2.  Drag to draw the rectangle.
3.  Do one or both of the following:
    *   To constrain the rectangle to draw a square from its starting point, hold down SHIFT as you drag.
    *   To draw a rectangle from a center point, hold down CTRL as you drag.

### Using Aspose.Cells

The `Aspose.Cells.Drawing.ShapeCollection` class provides a method named `AddRectangle`, which is used to add a rectangle shape to a worksheet. The method returns `Aspose.Cells.Drawing.RectangleShape*` object. The class `Aspose.Cells.Drawing.RectangleShape` represents a rectangle. It has some important members:

*   The `LineFormat` property specifies the line format attributes of a rectangle.
*   The `Placement` property specifies the `PlacementType`, the way the rectangle is attached to the cells in the worksheet.
*   The `FillFormat` property specifies the fill format styles of a rectangle.

The following example shows how to add a rectangle to the worksheet.

## Adding Arc Control to the Worksheet

Aspose.Cells allows you to draw arc shapes in your worksheets. You may create simple and filled arcs. You are allowed to format the filling color and border line color of the control. For example, you can specify / change the color of the arc, set the shading color, specify the weight and style of the shape for your need.

### Using Microsoft Excel

1.  On the **Drawing** toolbar, click **Arc** in the **AutoShapes**.
2.  Drag to draw the arc.

### Using Aspose.Cells

The `Aspose.Cells.Drawing.ShapeCollection` class provides a method named `AddArc`, which is used to add an arc shape to a worksheet. The method returns an `Aspose.Cells.Drawing.ArcShape` object. The class `Aspose.Cells.Drawing.ArcShape` represents an arc. It has some important members:

*   The `LineFormat` property specifies the line format attributes of an arc shape.
*   The `Placement` property specifies the `PlacementType`, the way the arc is attached to the cells in the worksheet.
*   The `FillFormat` property specifies the fill format styles of the shape.
*   The `LowerRightRow` property specifies the lower right corner row index.
*   The `LowerRightColumn` property specifies the lower right corner column index.

The following example shows how to add arc shapes to the worksheet. The example creates two arc shapes: one is filled and other is simple.

## Adding Oval Control to a Worksheet

Aspose.Cells allows you to draw oval shapes in worksheets. Create simple and filled oval shapes and format the filling color and border line color of the control. For example, you can specify / change the color of the oval, set the shading color, specify the weight and style of the shape.

### Using Microsoft Excel

*   On the \*Drawing\* toolbar, click \*Oval\*.
*   Drag to draw the oval.
*   Do one or both of the following:
*   To constrain the oval to draw a circle from its starting point, hold down SHIFT as you drag.
*   To draw an oval from a center point, hold down CTRL as you drag.

### Using Aspose.Cells

The Aspose.Cells.Drawing.ShapeCollection class provides a method named AddOval, which is used to add an oval shape to a worksheet. The method returns an Aspose.Cells.Drawing.Oval object. The class Aspose.Cells.Drawing.Oval represents an oval shape. It has some important members:

*   The {{LineFormat}} property specifies the line format attributes of an oval shape.
*   The {{Placement}} property specifies the {{PlacementType}}, the way the oval is attached to the cells in the worksheet.
*   The {{FillFormat}} property specifies the fill format styles of the shape.
*   The {{LowerRightRow}} property specifies the lower right corner row index.
*   The {{LowerRightColumn}} property specifies the lower right corner column index.

The following example shows how to add oval shapes to the worksheet. The example creates two oval shapes: one is filled oval other is a simple circle.

## Adding Spinner Control to the Worksheet

A spin box is a text box attached to a button (called a spin button) consisting of an up arrow and down arrow that you click to incrementally change the value in the text box. By using spin boxes, you can see how input changes to your financial model will alter the model outputs. You can attach a spin button to a specific input cell. While you click the up arrow or down arrow on the spin button, the integer value in the targeted input cell increases or decreases. \*Aspose.Cells\* allows you to create spinners in your worksheets.

### Using Microsoft Excel

To place a spin box control in your worksheet:

*   Make sure the \*Forms\* toolbar is displayed.
*   Click the \*Spinner\* tool.
*   In your worksheet area, click and drag to define the rectangle that will hold the spinner.
*   Once the spinner is placed in the worksheet, right-click the control and click \*Format Control\* and specify the maximum, minimum and incremental values.
*   In the \*Cell Link\* field, specify the address of the cell to which this spin box should be linked.
*   Click on \*OK\*.

### Using Aspose.Cells

The {{Aspose.Cells.Drawing.ShapeCollection}} class provides a method named {{AddSpinner}}, which is used to add a spin box control to a worksheet. The method returns an {{Aspose.Cells.Drawing.Spinner}} object. The class {{Aspose.Cells.Drawing.Spinner}} represents a spin box. It has some important members:

*   The {{LinkedCell}} property specifies a cell which is linked to the spin box.
*   The {{Max}} property specifies the maximum value for the spin box range.
*   The {{Min}} property specifies the minimum value for the spin box range.
*   The {{IncrementalChange}} property specifies the value amount for which a spinner is incremented a line scroll.
*   The {{Shadow}} property indicates whether the spin box has 3D shading.
*   The {{CurrentValue}} property specifies the current value of the spin box.

The following example shows how to add a spin box to the worksheet.

## Adding Scroll Bar Control to a Worksheet

A scroll bar control is used to help select data on a worksheet in a similar way to a spin box control. By adding the control to a worksheet and linking it to a cell, it is possible to return a numeric value for the current position of the control.

### Using Microsoft Excel

*   To add a scroll bar in Excel 2003 and in earlier versions, click the \*Scroll Bar\* button on the \*Forms\* toolbar, and then create a scroll bar that covers cells B2:B6 in height and is about one-fourth of the width of the column.
*   To add a scroll bar in Excel 2007, click the \*Developer\* tab, click \*Insert\*, and then click \*Scroll Bar\* in the Form Controls section.
*   Right-click the scroll bar, and then click \*Format Control\*.
*   Type the following information, and click \*OK\*:
    *   In the \*Current value\* box, type 1.
    *   In the \*Minimum value\* box, type 1. This value restricts the top of the scroll bar to the first item in the list.
    *   In the \*Maximum value\* box, type 20. This number specifies the maximum number of entries in the list.
    *   In the \*Incremental change\* box, type 1. This value controls how many numbers the scroll bar control increments the current value.
    *   In the \*Page change\* box, type 5. This entry controls how much the current value will be incremented if you click inside the scroll bar on either side of the scroll box.
    *   To put a number value in cell G1 (depending on which item is selected in the list), type G1 in the \*Cell link\* box.
*   Click any cell so that the scroll bar is not selected.

When you click the up or down control on the scroll bar, cell G1 is updated to a number that indicates the current value of the scroll bar plus or minus the incremental change of the scroll bar.

### Using Aspose.Cells

The {{Aspose.Cells.Drawing.ShapeCollection}} class provides a method named {{AddScrollBar}}, which is used to add a scroll bar control to the worksheet. The method returns an {{Aspose.Cells.Drawing.ScrollBar}} object. The class {{Aspose.Cells.Drawing.ScrollBar}} represents a scroll bar. It has some important members:

*   The {{LinkedCell}} property specifies a cell which is linked to the scroll bar.
*   The {{Max}} property specifies the maximum value for the scroll bar range.
*   The {{Min}} property specifies the minimum value for the scroll bar range.
*   The {{IncrementalChange}} property specifies the value amount for which a scroll bar is incremented a line scroll.
*   The {{Shadow}} property indicates whether the scroll bar has 3D shading.
*   The {{CurrentValue}} property specifies the current value of the scroll bar.
*   The {{PageChange}} property specifies how much the current value will be incremented if you click inside the scroll bar on either side of the scroll box.

The following example shows how to add a scroll bar to the worksheet.

## Adding GroupBox Control to Group Controls in a Worksheet

Sometimes you do need to implement radio buttons or other controls which belong to a certain group, you can implement by including either a group box or rectangle control. Any of these two objects would serve as the delimiter of the group. After adding one of these shapes, you can then add two or more radio buttons or other group objects.

### Using Microsoft Excel

To place a group box control in your worksheet and place controls in it:

*   To start a form, on the main menu, click \*View\*, followed by \*Toolbars\* and \*Forms\*.
*   On the \*Forms\* toolbar, click the \*Group Box\* and draw a rectangle on the worksheet.
*   Type a caption string for the box.
*   On the \*Forms\* toolbar, click \*Option Button\* and click inside the \*Group Box\* just under the caption string.
*   From the \*Forms\* toolbar again, click \*Option Button\* and click inside the \*Group Box\* under the first radio button.
*   Once again on the \*Forms\* toolbar, click \*Option Button\* and click inside the \*Group Box\* under the previous radio button.

### Using Aspose.Cells

The {{Aspose.Cells.Drawing.ShapeCollection}} class provides a method named {{AddGroupBox}}, which is used to add a group box control to the worksheet. The method returns an {{Aspose.Cells.Drawing.GroupBox}} object. Moreover, the {{Group}} method of the {{Aspose.Cells.Drawing.ShapeCollection}} class groups the shapes, it takes a {{Shape}} array as parameter and returns a {{GroupShape}} object. The class {{Aspose.Cells.Drawing.GroupBox}} represents a group box. It has some important members:

*   The {{Text}} property specifies the group box's caption string.
*   The {{Shadow}} property indicates whether the group box has 3D shading.

The following example shows how to add a group box and group the controls in the worksheet.

