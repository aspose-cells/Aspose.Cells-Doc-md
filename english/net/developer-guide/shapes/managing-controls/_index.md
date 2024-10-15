---
title: Managing Controls
type: docs
weight: 150
url: /net/managing-controls/
---

## **Introduction**

Developers can add different drawing objects such as text boxes, check boxes, radio buttons, combo boxes, labels, buttons, lines, rectangles, arcs, ovals, spinners, scroll bars, group boxes etc. Aspose.Cells provides the Aspose.Cells.Drawing namespace which contains all the drawing objects. However, there are a few drawing objects or shapes that are not supported yet. Create these drawing objects in a designer spreadsheet using Microsoft Excel and then import the designer spreadsheet to Aspose.Cells. Aspose.Cells allows you to load these drawing objects from a designer spreadsheet and write them to a generated file.

## **Adding Text Box Control to a Worksheet**

One way to stress important information in a report is to use a text box. For example, add text to highlight the company name or to indicate the geographic region with the highest sales etc. Aspose.Cells provides the [**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) class, used to add a new text box to the collection. There is another class, [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), which represents a text box used to define all types of settings. It has some important members:

- The [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) property returns a [**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) object used to adjust the contents of the text box.
- The [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) property specifies the placement type.
- The [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) property specifies the font attributes.
- The [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) method adds a hyperlink for the text box.
- The [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) property returns an [**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) object used to set the fill format for the text box.
- The [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) property returns the [**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) object usually used to style and weight of the text box line.
- The [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) property specifies the input text for the text box.

The following example creates two textboxes in the first worksheet of the workbook. The first text box is well-furnished with different format settings. The second is a simple one.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Manipulating Text Box Controls in Designer Spreadsheets**

Aspose.Cells also lets you access textboxes in the designer worksheets and manipulate them. Use the [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) property to get the textboxes collection in the sheet.

The following example uses the Microsoft Excel file that we created in the above example. It gets the text strings of the two textboxes and changes the text of the second textbox to save the file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Adding Check Box Control to a Worksheet**

Check boxes are handy if you want to provide a way for a user to choose between two options, such as true or false; yes or no. Aspose.Cells allows you to use check boxes in worksheets. For instance, you may have developed a financial projection worksheet in which you can either account for a particular acquisition or not. In this case, you might want to place a check box at the top of the worksheet. You can then link the status of this check box to another cell, so that if the check box is selected, the value of the cell is True; if it is not selected, the value of the cell is False.

### **Using Microsoft Excel**

To place a check box control in your worksheet, follow these steps:

1. Make sure the Forms toolbar is displayed.
1. Click the **Check Box** tool on the Forms toolbar.
1. In your worksheet area, click and drag to define the rectangle that will hold the check box and the label beside the check box.
1. Once the check box is placed, move the mouse cursor into the label area and change the label.
1. In the **Cell Link** field, specify the address of the cell to which this check box should be linked.
1. Click on **OK**.

### **Using Aspose.Cells**

Aspose.Cells provides the [**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) class, which is used to add a new check box to the collection. There is another class, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), which represents a check box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) property specifies a cell which is linked to the check box.
- The [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) property specifies the text string associated with the check box. It is the label of the check box.
- The [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) property specifies if the check box is checked or not.

The following example shows how to add a checkbox to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Adding Radio Button Control to the Worksheet**

A radio button, or an option button, is a control made of a round box. The user makes his or her decision by selecting the round box. A radio button is usually, if not always, accompanied by others. Such radio buttons appear and behave as a group. The user decides which button is valid by selecting only one of them. When the user clicks one button, it is filled. When one button in the group is selected, buttons of the same group are empty.

### **Using Microsoft Excel**

To place a Radio Button control in your worksheet, follow these steps:

1. Make sure the **Forms** toolbar is displayed.
1. Click the **Option Button** tool.
1. In the worksheet, click and drag to define the rectangle that will hold the option button and the label beside the option button.
1. Once the radio button is placed in the worksheet, move the mouse cursor into the label area and change the label.
1. In the **Cell Link** field, specify the address of the cell to which this radio button should be linked.
1. Click **OK**.

### **Using Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton), which is used to add a radio button control to a worksheet. The method returns an [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) object. The class[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) represents an option button. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) property specifies a cell which is linked to the radio button.
- The [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) property specifies the text string associated with the radio button. It is the label of the radio button.
- The [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) property specifies if the radio button is checked or not.
- The [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) property specifies the fill format of the radio button.
- The [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) property specifies the line format styles of the option button.

The following example shows how to add radio buttons to a worksheet. The example adds three radio buttons representing age groups.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **Adding Combo Box Control to a Worksheet**

To make data entry easier, or to limit entries to certain items that you define, you can create a combo box, or drop-down list of valid entries that is compiled from cells elsewhere on the worksheet. When you create a drop-down list for a cell, it displays an arrow next to that cell. To enter information in that cell, click the arrow, and then click the entry that you want.

### **Using Microsoft Excel**

To place a combo box control in your worksheet, follow these steps:

1. Make sure the **Forms** toolbar is displayed.
1. Click on the **Combo Box** tool.
1. In your worksheet area, click and drag to define the rectangle that will hold the combo box.
1. Once the combo box is placed in the worksheet, right-click the control to click **Format Control** and specify the input range.
1. In the **Cell Link** field, specify the address of the cell to which this combo box should be linked.
1. Click on **OK**.

### **Using Aspose.Cells**

The [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox), which is used to add a combo box control to a worksheet. The method returns an [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) object. The class [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) represents a combo box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) property specifies a cell which is linked to the combo box.
- The [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) property specifies the worksheet range of cells used to fill the combo box.
- The [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) property specifies the number of list lines displayed in the drop-down portion of a combo box.
- The [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) property indicates whether the combo box has 3D shading.

The following example shows how to add a combo box to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Adding Label Control to a Worksheet**

Labels are a means of give users information about a speadsheet's contents. Aspose.Cells makes it possible to add and manipulate labels in a worksheet. The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel), used to add a label control to the worksheet. The method returns a [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) object. The class [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) represents a label in the worksheet. It has some important members:

- The [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) method specifies a label's caption string.
- The [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) method specifies the [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), the way the label is attached to the cells in the worksheet.

The following example shows how to add a label to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **Adding List Box Control to a Worksheet**

A list box control creates a list control that allows single or multiple item selection.

### **Using Microsoft Excel**

To place a list box control in a worksheet:

1. Make sure the **Forms** toolbar is displayed.
1. Click on the **List Box** tool.
1. In your worksheet area, click and drag to define the rectangle that will hold the list box.
1. Once the list box is placed in the worksheet, right-click on the control to click **Format Control** and specify the input range.
1. In the **Cell Link** field, specify the address of the cell to which this list box should be linked and set the selection type (Single, Multi, Extend) attribute
1. Click **OK**.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox), which is used to add a list box control to a worksheet. The method returns a [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) object. The class [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) represents a list box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) method specifies a cell which is linked to the list box.
- The [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) method specifies the worksheet range of cells used to fill the list box.
- The [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) method specifies the selection mode of the the list box.
- The [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) method indicates whether the list box has 3D shading.

The following example shows how to add a list box to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Adding Button Control to a Worksheet**

Buttons are useful to perform some actions. Sometimes, it is useful to assign a VBA Macro to the button or assign a hyperlink to open a web page.

### **Using Microsoft Excel**

To place a button control in your worksheet:

1. Make sure the **Forms** toolbar is displayed.
1. Click on the **Button** tool.
1. In your worksheet area, click and drag to define the rectangle that will hold the button.
1. Once the list box is placed in the worksheet, right-click on the control and select **Format Control**, then specify a VBA Macro and attributes related font, alignment, size, margin etc.
1. Click on **OK**.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton), used to add a button control to the worksheet. The method returns an [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) object. The class [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) represents a button. It has some important members:

- The [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) property specifies the caption of button.
- The [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) property specifies the font attributes for the label of the button control.
- The [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) property specifies the [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), the way the button is attached to the cells in the worksheet.
- The [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) property adds a hyperlink for the button control. Clicking on the button will navigate to related URL.

The following example shows how to add a button to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Adding Line Control to the Worksheet**

### **Using Microsoft Excel**

1. On the **Drawing** toolbar, click **AutoShapes**, point to **Lines**, and select the line style you want.
1. Drag to draw the line.
1. Do one or both of the following:
   1. To constrain the line to draw at 15-degree angles from its starting point, hold down SHIFT as you drag.
   1. To lengthen the line in opposite directions from the first end point, hold down CTRL as you drag.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline), which is used to add a line shape to the worksheet. The method return a [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) object. The class [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) represents a line. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) method specifies the format of a line.
- The [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) method specifies the [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), the way the line is attached to the cells in the worksheet.

The following example shows how to add lines to the worksheet. It creates three lines with different styles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Adding an Arrow Head to a Line**

Aspose.Cells also allows you to draw arrow lines. It is possible to add an arrowhead to a line, and to format the line. For example, you can change the color of the line, or specify the weight and style of the line.

The following example shows how to add an arrowhead to a line.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Adding Rectangle Control to a Worksheet**

Aspose.Cells allows you to draw rectangle shapes in your worksheets. You may create a rectangle, square etc. You are also allowed to format the filling color and border line color of the control. For example, you can change the color of the rectangle, set the shading color, specify the weight and style of the rectangle for your need.

### **Using Microsoft Excel**

1. On the **Drawing** toolbar, click **Rectangle**.
1. Drag to draw the rectangle.
1. Do one or both of the following:
   1. To constrain the rectangle to draw a square from its starting point, hold down SHIFT as you drag.
   1. To draw a rectangle from a center point, hold down CTRL as you drag.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle), which is used to add a rectangle shape to a worksheet. The method returns [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) object. The class [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) represents a rectangle. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) property specifies the line format attributes of a rectangle.
- The [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) property specifies the [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), the way the rectangle is attached to the cells in the worksheet.
- The [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) property specifies the fill format styles of a rectangle.

The following example shows how to add a rectangle to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Adding Arc Control to the Worksheet**

Aspose.Cells allows you to draw arc shapes in your worksheets. You may create simple and filled arcs. You are allowed to format the filling color and border line color of the control. For example, you can specify / change the color of the arc, set the shading color, specify the weight and style of the shape for your need.

### **Using Microsoft Excel**

1. On the **Drawing** toolbar, click **Arc** in the **AutoShapes**.
1. Drag to draw the arc.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc), which is used to add an arc shape to a worksheet. The method returns an [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) object. The class [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) represents an arc. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) property specifies the line format attributes of an arc shape.
- The [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) property specifies the [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), the way the arc is attached to the cells in the worksheet.
- The [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) property specifies the fill format styles of the shape.
- The [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) property specifies the lower right corner row index.
- The [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) property specifies the lower right corner column index.

The following example shows how to add arc shapes to the worksheet. The example creates two arc shapes: one is filled and other is simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Adding Oval Control to a Worksheet**

Aspose.Cells allows you to draw oval shapes in worksheets. Create simple and filled oval shapes and format the filling color and border line color of the control. For example, you can specify / change the color of the oval, set the shading color, specify the weight and style of the shape.

### **Using Microsoft Excel**

- On the *Drawing* toolbar, click *Oval*.
- Drag to draw the oval.
- Do one or both of the following:
- To constrain the oval to draw a circle from its starting point, hold down SHIFT as you drag.
- To draw an oval from a center point, hold down CTRL as you drag.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval), which is used to add an oval shape to a worksheet. The method returns an [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) object. The class [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) represents an oval shape. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) property specifies the line format attributes of an oval shape.
- The [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) property specifies the [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), the way the oval is attached to the cells in the worksheet.
- The [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) property specifies the fill format styles of the shape.
- The [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) property specifies the lower right corner row index.
- The [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) property specifies the lower right corner column index.

The following example shows how to add oval shapes to the worksheet. The example creates two oval shapes: one is filled oval other is a simple circle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Adding Spinner Control to the Worksheet**

A spin box is a text box attached to a button (called a spin button) consisting of an up arrow and down arrow that you click to incrementally change the value in the text box. By using spin boxes, you can see how input changes to your financial model will alter the model outputs. You can attach a spin button to a specific input cell. While you click the up arrow or down arrow on the spin button, the integer value in the targeted input cell increases or decreases. *Aspose.Cells* allows you to create spinners in your worksheets.

### **Using Microsoft Excel**

To place a spin box control in your worksheet:

- Make sure the *Forms* toolbar is displayed.
- Click the *Spinner* tool.
- In your worksheet area, click and drag to define the rectangle that will hold the spinner.
- Once the spinner is placed in the worksheet, right-click the control and click *Format Control* and specify the maximum, minimum and incremental values.
- In the *Cell Link* field, specify the address of the cell to which this spin box should be linked.
- Click on *OK*.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner), which is used to add a spin box control to a worksheet. The method returns an [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) object. The class [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) represents a spin box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) property specifies a cell which is linked to the spin box.
- The [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) property specifies the maximum value for the spin box range.
- The [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) property specifies the minimum value for the spin box range.
- The [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) property specifies the value amount for which a spinner is incremented a line scroll.
- The [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) property indicates whether the spin box has 3D shading.
- The [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) property specifies the current value of the spin box.

The following example shows how to add a spin box to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Adding Scroll Bar Control to a Worksheet**

A scroll bar control is used to help select data on a worksheet in a similar way to a spin box control. By adding the control to a worksheet and linking it to a cell, it is possible to return a numeric value for the current position of the control.

### **Using Microsoft Excel**

- To add a scroll bar in Excel 2003 and in earlier versions, click the *Scroll Bar* button on the *Forms* toolbar, and then create a scroll bar that covers cells B2:B6 in height and is about one-fourth of the width of the column.
- To add a scroll bar in Excel 2007, click the *Developer* tab, click *Insert*, and then click *Scroll Bar* in the Form Controls section.
- Right-click the scroll bar, and then click *Format Control*.
- Type the following information, and click *OK*:
  - In the *Current value* box, type 1.
  - In the *Minimum value* box, type 1. This value restricts the top of the scroll bar to the first item in the list.
  - In the *Maximum value* box, type 20. This number specifies the maximum number of entries in the list.
  - In the *Incremental change* box, type 1. This value controls how many numbers the scroll bar control increments the current value.
  - In the *Page change* box, type 5. This entry controls how much the current value will be incremented if you click inside the scroll bar on either side of the scroll box.
  - To put a number value in cell G1 (depending on which item is selected in the list), type G1 in the *Cell link* box.
- Click any cell so that the scroll bar is not selected.

When you click the up or down control on the scroll bar, cell G1 is updated to a number that indicates the current value of the scroll bar plus or minus the incremental change of the scroll bar.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar), which is used to add a scroll bar control to the worksheet. The method returns an [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) object. The class [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) represents a scroll bar. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) property specifies a cell which is linked to the scroll bar.
- The [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) property specifies the maximum value for the scroll bar range.
- The [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) property specifies the minimum value for the scroll bar range.
- The [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) property specifies the value amount for which a scroll bar is incremented a line scroll.
- The [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) property indicates whether the scroll bar has 3D shading.
- The [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) property specifies the current value of the scroll bar.
- The [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) property specifies how much the current value will be incremented if you click inside the scroll bar on either side of the scroll box.

The following example shows how to add a scroll bar to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Adding GroupBox Control to Group Controls in a Worksheet**

Sometimes you do need to implement radio buttons or other controls which belong to a certain group, you can implement by including either a group box or rectangle control. Any of these two objects would serve as the delimiter of the group. After adding one of these shapes, you can then add two or more radio buttons or other group objects.

### **Using Microsoft Excel**

To place a group box control in your worksheet and place controls in it:

- To start a form, on the main menu, click *View*, followed by *Toolbars* and *Forms*.
- On the *Forms* toolbar, click the *Group Box* and draw a rectangle on the worksheet.
- Type a caption string for the box.
- On the *Forms* toolbar, click *Option Button* and click inside the *Group Box* just under the caption string.
- From the *Forms* toolbar again, click *Option Button* and click inside the *Group Box* under the first radio button.
- Once again on the *Forms* toolbar, click *Option Button* and click inside the *Group Box* under the previous radio button.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class provides a method named [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox), which is used to add a group box control to the worksheet. The method returns an [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) object. Moreover, the [**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) method of the [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class groups the shapes, it takes a [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) array as parameter and returns a [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) object. The class [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) represents a group box. It has some important members:

- The [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) property specifies the group box's caption string.
- The [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) property indicates whether the group box has 3D shading.

The following example shows how to add a group box and group the controls in the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Advance topics**
- [Add ActiveX Controls using Aspose.Cells](/cells/net/add-activex-controls-using-aspose-cells/)
- [Remove ActiveX Control](/cells/net/remove-activex-control/)
- [Update ActiveX ComboBox Control](/cells/net/update-activex-combobox-control/)
{{< app/cells/assistant language="csharp" >}}