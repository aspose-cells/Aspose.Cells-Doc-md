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
