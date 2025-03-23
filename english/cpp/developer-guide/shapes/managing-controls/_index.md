---
title: Managing Controls with C++
linktitle: Managing Controls
type: docs
weight: 150
url: /cpp/managing-controls/
description: Learn how to add and manage various controls like lines, rectangles, arcs, ovals, spinners, scroll bars, and group boxes in worksheets using Aspose.Cells with C++.
---

## **Introduction**

Developers can add different drawing objects such as text boxes, check boxes, radio buttons, combo boxes, labels, buttons, lines, rectangles, arcs, ovals, spinners, scroll bars, group boxes etc. Aspose.Cells provides the `Aspose::Cells::Drawing` namespace which contains all the drawing objects. However, there are a few drawing objects or shapes that are not supported yet. Create these drawing objects in a designer spreadsheet using Microsoft Excel and then import the designer spreadsheet to Aspose.Cells. Aspose.Cells allows you to load these drawing objects from a designer spreadsheet and write them to a generated file.

## **Adding Text Box Control to a Worksheet**

One way to stress important information in a report is to use a text box. For example, add text to highlight the company name or to indicate the geographic region with the highest sales etc. Aspose.Cells provides the [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/) class, used to add a new text box to the collection. There is another class, [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/), which represents a text box used to define all types of settings. It has some important members:

- The [**TextFrame**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/textframe/) property returns a [**MsoTextFrame**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msotextframe/) object used to adjust the contents of the text box.
- The [**Placement**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/placement/) property specifies the placement type.
- The [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/font/) property specifies the font attributes.
- The [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) method adds a hyperlink for the text box.
- The [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/fillformat/) property returns an [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/) object used to set the fill format for the text box.
- The [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lineformat/) property returns the [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/) object usually used to style and weight of the text box line.
- The [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/text/) property specifies the input text for the text box.

The following example creates two textboxes in the first worksheet of the workbook. The first text box is well-furnished with different format settings. The second is a simple one.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // The path to the documents directory.
    U16String dataDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get the first worksheet in the book.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new textbox to the collection.
    int32_t textboxIndex = worksheet.GetTextBoxes().Add(2, 1, 160, 200);

    // Get the textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Fill the text.
    textbox0.SetText(u"ASPOSE______The .NET & JAVA Component Publisher!");

    // Set the placement.
    textbox0.SetPlacement(PlacementType::FreeFloating);

    // Set the font color.
    textbox0.GetFont().SetColor(Color::Blue());

    // Set the font to bold.
    textbox0.GetFont().SetIsBold(true);

    // Set the font size.
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic.
    textbox0.GetFont().SetIsItalic(true);

    // Add a hyperlink to the textbox.
    textbox0.AddHyperlink(u"http://www.aspose.com/");

    // Get the fill format of the textbox.
    FillFormat fillFormat = textbox0.GetFill();

    // Get the line format type of the textbox.
    LineFormat lineFormat = textbox0.GetLine();

    // Set the line weight.
    lineFormat.SetWeight(6.0);

    // Set the dash style to squaredot.
    lineFormat.SetDashStyle(MsoLineDashStyle::SquareDot);

    // Add another textbox.
    textboxIndex = worksheet.GetTextBoxes().Add(15, 4, 85, 120);

    // Get the second textbox.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Input some text to it.
    textbox1.SetText(u"This is another simple text box");

    // Set the placement type as the textbox will move and resize with cells.
    textbox1.SetPlacement(PlacementType::MoveAndSize);

    // Save the excel file.
    workbook.Save(dataDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Manipulating Text Box Controls in Designer Spreadsheets**

Aspose.Cells also lets you access textboxes in the designer worksheets and manipulate them. Use the [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/textboxes/) property to get the textboxes collection in the sheet.

The following example uses the Microsoft Excel file that we created in the above example. It gets the text strings of the two textboxes and changes the text of the second textbox to save the file.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // The path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    
    // Open the existing excel file.
    Workbook workbook(srcDir + u"book1.xls");

    // Get the first worksheet in the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(0);

    // Obtain the text in the first textbox.
    U16String text0 = textbox0.GetText();

    // Get the second textbox object.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(1);

    // Obtain the text in the second textbox.
    U16String text1 = textbox1.GetText();

    // Change the text of the second textbox.
    textbox1.SetText(u"This is an alternative text");

    // Save the excel file.
    workbook.Save(srcDir + u"output.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

Aspose.Cells provides the [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/) class, which is used to add a new check box to the collection. There is another class, [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/), which represents a check box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/linkedcell/) property specifies a cell which is linked to the check box.
- The [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/text/) property specifies the text string associated with the check box. It is the label of the check box.
- The [**Value**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/value/) property specifies if the check box is checked or not.

The following example shows how to add a checkbox to the worksheet.

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a new Workbook instance
    Workbook excelbook = Workbook();

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);
    
    // Add a checkbox to the first worksheet in the workbook
    int32_t index = worksheet.GetCheckBoxes().Add(5, 5, 100, 120);

    // Get the checkbox object
    Drawing::CheckBox checkbox = worksheet.GetCheckBoxes().Get(index);

    // Set its text string
    checkbox.SetText(u"Click it!");

    // Get cells collection and set B1 cell value
    Cells cells = worksheet.GetCells();
    Cell cellB1 = cells.Get(u"B1");
    cellB1.PutValue(u"LnkCell");

    // Set B1 cell as a linked cell for the checkbox
    checkbox.SetLinkedCell(u"B1");

    // Check the checkbox by default
    checkbox.SetValue(true);

    // Save the excel file
    excelbook.Save(u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/), which is used to add a radio button control to a worksheet. The method returns an [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) object. The class [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) represents an option button. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/linkedcell/) property specifies a cell which is linked to the radio button.
- The [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/text/) property specifies the text string associated with the radio button. It is the label of the radio button.
- The [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) property specifies if the radio button is checked or not.
- The [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/fillformat/) property specifies the fill format of the radio button.
- The [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lineformat/) property specifies the line format styles of the option button.

The following example shows how to add radio buttons to a worksheet. The example adds three radio buttons representing age groups.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook excelbook;

    // Get the first worksheet
    Worksheet sheet = excelbook.GetWorksheets().Get(0);
    
    // Get cells collection
    Cells cells = sheet.GetCells();
    
    // Insert a value in C2
    Cell cellC2 = cells.Get(u"C2");
    cellC2.PutValue(u"Age Groups");

    // Set the font text bold.
    Style style = cellC2.GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    
    // Apply the style back
    cellC2.SetStyle(style);

    // Add radio buttons to the first sheet.
    ShapeCollection shapes = sheet.GetShapes();
    
    // Create first radio button
    RadioButton radio1= shapes.AddRadioButton(3, 0, 2, 0, 30, 110);
   
    
    // Set its text string.
    radio1.SetText(u"20-29");
    // Set A1 cell as a linked cell for the radio button.
    radio1.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio1.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line1 = radio1.GetLine();
    line1.SetWeight(4);
    // Set the dash style of the radio button.
    line1.SetDashStyle(MsoLineDashStyle::Solid);

    // Create second radio button
    RadioButton radio2 = shapes.AddRadioButton(6, 0, 2, 0, 30, 110);
    // Set its text string.
    radio2.SetText(u"30-39");
    // Set A1 cell as a linked cell for the radio button.
    radio2.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio2.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line2 = radio2.GetLine();
    line2.SetWeight(4);
    // Set the dash style of the radio button.
    line2.SetDashStyle(MsoLineDashStyle::Solid);

    // Create third radio button
    RadioButton radio3=shapes.AddRadioButton(9, 0, 2, 0, 30, 110);
    
    // Set its text string.
    radio3.SetText(u"40-49");
    // Set A1 cell as a linked cell for the radio button.
    radio3.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio3.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line3 = radio3.GetLine();
    line3.SetWeight(4);
    // Set the dash style of the radio button.
    line3.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file.
    excelbook.Save(srcDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

The [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/), which is used to add a combo box control to a worksheet. The method returns an [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) object. The class [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) represents a combo box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/linkedcell/) property specifies a cell which is linked to the combo box.
- The [**InputRange**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/inputrange/) property specifies the worksheet range of cells used to fill the combo box.
- The [**DropDownLines**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/dropdownlines/) property specifies the number of list lines displayed in the drop-down portion of a combo box.
- The [**Shadow**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/shadow/) property indicates whether the combo box has 3D shading.

The following example shows how to add a combo box to the worksheet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook.
    Workbook workbook;

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection.
    Cells cells = sheet.GetCells();

    // Input a value.
    Cell cellB3 = cells.Get(u"B3");
    cellB3.PutValue(u"Employee:");

    // Set it bold.
    Style style = cellB3.GetStyle();
    style.SetIsBorderApplied(true);
    cellB3.SetStyle(style);

    // Input some values that denote the input range for the combo box.
    cells.Get(u"A2").PutValue(u"Emp001");
    cells.Get(u"A3").PutValue(u"Emp002");
    cells.Get(u"A4").PutValue(u"Emp003");
    cells.Get(u"A5").PutValue(u"Emp004");
    cells.Get(u"A6").PutValue(u"Emp005");
    cells.Get(u"A7").PutValue(u"Emp006");

    // Add a new combo box.
    ComboBox comboBox = sheet.GetShapes().AddComboBox(2, 0, 2, 0, 22, 100);

    // Cleanup Aspose resources
    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Adding Label Control to a Worksheet**

Labels are a means of give users information about a speadsheet's contents. Aspose.Cells makes it possible to add and manipulate labels in a worksheet. The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/), used to add a label control to the worksheet. The method returns a [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) object. The class [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) represents a label in the worksheet. It has some important members:

- The [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/text/) method specifies a label's caption string.
- The [**Placement**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/placement/) method specifies the [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), the way the label is attached to the cells in the worksheet.

The following example shows how to add a label to the worksheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new label to the worksheet
    Label label = sheet.GetShapes().AddLabel(2, 0, 2, 0, 60, 120);

    // Set the caption of the label
    label.SetText(u"This is a Label");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Label added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/), which is used to add a list box control to a worksheet. The method returns a [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) object. The class [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) represents a list box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/linkedcell/) method specifies a cell which is linked to the list box.
- The [**InputRange**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/inputrange/) method specifies the worksheet range of cells used to fill the list box.
- The [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/selectiontype/) method specifies the selection mode of the the list box.
- The [**Shadow**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/shadow/) method indicates whether the list box has 3D shading.

The following example shows how to add a list box to the worksheet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection
    Cells cells = sheet.GetCells();

    // Input a value
    cells.Get(U16String(u"B3")).PutValue(U16String(u"Choose Dept:"));

    // Set it bold
    Style style = cells.Get(U16String(u"B3")).GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    cells.Get(U16String(u"B3")).SetStyle(style);

    // Input some values that denote the input range for the list box
    cells.Get(U16String(u"A2")).PutValue(U16String(u"Sales"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"Finance"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"MIS"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"R&D"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Marketing"));
    cells.Get(U16String(u"A7")).PutValue(U16String(u"HRA"));

    // Add a new list box
    ListBox listBox = sheet.GetShapes().AddListBox(2, 0, 3, 0, 122, 100);

    // Set the placement type
    listBox.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell
    listBox.SetLinkedCell(U16String(u"A1"));

    // Set the input range
    listBox.SetInputRange(U16String(u"A2:A7"));

    // Set the selection type
    listBox.SetSelectionType(SelectionType::Single);

    // Set the list box with 3-D shading
    listBox.SetShadow(true);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/), used to add a button control to the worksheet. The method returns an [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) object. The class [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) represents a button. It has some important members:

- The [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/text/) property specifies the caption of button.
- The [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/font/) property specifies the font attributes for the label of the button control.
- The [**Placement**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/placement/) property specifies the [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), the way the button is attached to the cells in the worksheet.
- The [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) property adds a hyperlink for the button control. Clicking on the button will navigate to related URL.

The following example shows how to add a button to the worksheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new button to the worksheet
    Drawing::Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);

    // Set the caption of the button
    button.SetText(u"Aspose");

    // Set the Placement Type, the way the Button is attached to the cells
    button.SetPlacement(PlacementType::FreeFloating);

    // Set the font name
    Font font = button.GetFont();
    font.SetName(u"Tahoma");

    // Set the caption string bold
    font.SetIsBold(true);

    // Set the color to blue
    font.SetColor(Color::Blue());

    // Set the hyperlink for the button
    button.AddHyperlink(u"http://www.aspose.com/");

    // Save the file
    workbook.Save(srcDir + u"book1.out.xls");

    std::cout << "Button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Adding Line Control to the Worksheet**

### **Using Microsoft Excel**

1. On the **Drawing** toolbar, click **AutoShapes**, point to **Lines**, and select the line style you want.
1. Drag to draw the line.
1. Do one or both of the following:
   1. To constrain the line to draw at 15-degree angles from its starting point, hold down SHIFT as you drag.
   1. To lengthen the line in opposite directions from the first end point, hold down CTRL as you drag.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/), which is used to add a line shape to the worksheet. The method returns a [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) object. The class [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) represents a line. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lineformat/) method specifies the format of a line.
- The [**Placement**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/placement/) method specifies the [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), the way the line is attached to the cells in the worksheet.

The following example shows how to add lines to the worksheet. It creates three lines with different styles.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new line to the worksheet
    LineShape line1 = worksheet.GetShapes().AddLine(5, 0, 1, 0, 0, 250);

    // Set the line dash style
    line1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line1.SetPlacement(PlacementType::FreeFloating);

    // Add another line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line dash style
    line2.GetLine().SetDashStyle(MsoLineDashStyle::DashLongDash);

    // Set the weight of the line
    line2.GetLine().SetWeight(4);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Add the third line to the worksheet
    LineShape line3 = worksheet.GetShapes().AddLine(13, 0, 1, 0, 0, 250);

    // Set the line dash style
    line3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line3.SetPlacement(PlacementType::FreeFloating);

    // Make the gridlines invisible in the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Lines added successfully to the worksheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Adding an Arrow Head to a Line**

Aspose.Cells also allows you to draw arrow lines. It is possible to add an arrowhead to a line, and to format the line. For example, you can change the color of the line, or specify the weight and style of the line.

The following example shows how to add an arrowhead to a line.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line color
    line2.GetLine().SetFillType(FillType::Solid);
    line2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the weight of the line
    line2.GetLine().SetWeight(3);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Set the line arrows
    line2.GetLine().SetEndArrowheadWidth(MsoArrowheadWidth::Medium);
    line2.GetLine().SetEndArrowheadStyle(MsoArrowheadStyle::Arrow);
    line2.GetLine().SetEndArrowheadLength(MsoArrowheadLength::Medium);
    line2.GetLine().SetBeginArrowheadStyle(MsoArrowheadStyle::ArrowDiamond);
    line2.GetLine().SetBeginArrowheadLength(MsoArrowheadLength::Medium);

    // Make the gridlines invisible in the first worksheet
    workbook.GetWorksheets().Get(0).SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Adding Rectangle Control to a Worksheet**

Aspose.Cells allows you to draw rectangle shapes in your worksheets. You may create a rectangle, square etc. You are also allowed to format the filling color and border line color of the control. For example, you can change the color of the rectangle, set the shading color, specify the weight and style of the rectangle for your need.

### **Using Microsoft Excel**

1. On the **Drawing** toolbar, click **Rectangle**.
1. Drag to draw the rectangle.
1. Do one or both of the following:
   1. To constrain the rectangle to draw a square from its starting point, hold down SHIFT as you drag.
   1. To draw a rectangle from a center point, hold down CTRL as you drag.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/), which is used to add a rectangle shape to a worksheet. The method returns [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) object. The class [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) represents a rectangle. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lineformat/) property specifies the line format attributes of a rectangle.
- The [**Placement**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/placement/) property specifies the [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), the way the rectangle is attached to the cells in the worksheet.
- The [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/fillformat/) property specifies the fill format styles of a rectangle.

The following example shows how to add a rectangle to the worksheet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a rectangle control to the first worksheet
    RectangleShape rectangle = excelbook.GetWorksheets().Get(0).GetShapes().AddRectangle(3, 0, 2, 0, 70, 130);

    // Set the placement of the rectangle
    rectangle.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    rectangle.GetLine().SetWeight(4);

    // Set the dash style of the rectangle
    rectangle.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the Excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Rectangle shape added and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Adding Arc Control to the Worksheet**

Aspose.Cells allows you to draw arc shapes in your worksheets. You may create simple and filled arcs. You are allowed to format the filling color and border line color of the control. For example, you can specify / change the color of the arc, set the shading color, specify the weight and style of the shape for your need.

### **Using Microsoft Excel**

1. On the **Drawing** toolbar, click **Arc** in the **AutoShapes**.
1. Drag to draw the arc.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/), which is used to add an arc shape to a worksheet. The method returns an [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) object. The class [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) represents an arc. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lineformat/) property specifies the line format attributes of an arc shape.
- The [**Placement**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/placement/) property specifies the [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), the way the arc is attached to the cells in the worksheet.
- The [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/fillformat/) property specifies the fill format styles of the shape.
- The [**LowerRightRow**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lowerrightrow/) property specifies the lower right corner row index.
- The [**LowerRightColumn**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lowerrightcolumn/) property specifies the lower right corner column index.

The following example shows how to add arc shapes to the worksheet. The example creates two arc shapes: one is filled and other is simple.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add an arc shape
    ArcShape arc1 = worksheet.GetShapes().AddArc(2, 0, 2, 0, 130, 130);

    // Set the fill shape color
    arc1.GetFill().SetFillType(FillType::Solid);
    arc1.GetFill().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc1.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another arc shape
    ArcShape arc2 = worksheet.GetShapes().AddArc(9, 0, 2, 0, 130, 130);

    // Set the line color
    arc2.GetLine().SetFillType(FillType::Solid);
    arc2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc2.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    U16String outputPath = outDir + u"book1.out.xls";
    excelbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Adding Oval Control to a Worksheet**

Aspose.Cells allows you to draw oval shapes in worksheets. Create simple and filled oval shapes and format the filling color and border line color of the control. For example, you can specify / change the color of the oval, set the shading color, specify the weight and style of the shape.

### **Using Microsoft Excel**

- On the *Drawing* toolbar, click *Oval*.
- Drag to draw the oval.
- Do one or both of the following:
- To constrain the oval to draw a circle from its starting point, hold down SHIFT as you drag.
- To draw an oval from a center point, hold down CTRL as you drag.

### **Using Aspose.Cells**

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/), which is used to add an oval shape to a worksheet. The method returns an [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) object. The class [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) represents an oval shape. It has some important members:

- The [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lineformat/) property specifies the line format attributes of an oval shape.
- The [**Placement**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/placement/) property specifies the [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), the way the oval is attached to the cells in the worksheet.
- The [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/fillformat/) property specifies the fill format styles of the shape.
- The [**LowerRightRow**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lowerrightrow/) property specifies the lower right corner row index.
- The [**LowerRightColumn**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/lowerrightcolumn/) property specifies the lower right corner column index.

The following example shows how to add oval shapes to the worksheet. The example creates two oval shapes: one is filled oval other is a simple circle.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add an oval shape
    Oval oval1 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(2, 0, 2, 0, 130, 160);

    // Set the placement of the oval
    oval1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval1.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another oval (circle) shape
    Oval oval2 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(9, 0, 2, 15, 130, 130);

    // Set the placement of the oval
    oval2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval2.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/), which is used to add a spin box control to a worksheet. The method returns an [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) object. The class [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) represents a spin box. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/linkedcell/) property specifies a cell which is linked to the spin box.
- The [**Max**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/max/) property specifies the maximum value for the spin box range.
- The [**Min**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/min/) property specifies the minimum value for the spin box range.
- The [**IncrementalChange**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/incrementalchange/) property specifies the value amount for which a spinner is incremented a line scroll.
- The [**Shadow**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/shadow/) property indicates whether the spin box has 3D shading.
- The [**CurrentValue**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/currentvalue/) property specifies the current value of the spin box.

The following example shows how to add a spin box to the worksheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Select Value:");

    // Set the font color of the cell
    Style styleA1 = cells.Get(u"A1").GetStyle();
    styleA1.GetFont().SetColor(Color::Red());

    // Set the font text bold
    styleA1.GetFont().SetIsBold(true);

    // Input value into A2 cell
    cells.Get(u"A2").PutValue(0);

    // Set the shading color to black with solid background
    Style styleA2 = cells.Get(u"A2").GetStyle();
    styleA2.SetForegroundColor(Color::Black());
    styleA2.SetPattern(BackgroundType::Solid);

    // Set the font color of the cell
    styleA2.GetFont().SetColor(Color::White());

    // Set the font text bold
    styleA2.GetFont().SetIsBold(true);

    // Add a spinner control
    Spinner spinner = worksheet.GetShapes().AddSpinner(1, 0, 1, 0, 20, 18);

    // Set the placement type of the spinner
    spinner.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    spinner.SetLinkedCell(u"A2");

    // Set the maximum value
    spinner.SetMax(10);

    // Set the minimum value
    spinner.SetMin(0);

    // Set the incremental change for the control
    spinner.SetIncrementalChange(2);

    // Set it 3-D shading
    spinner.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/), which is used to add a scroll bar control to the worksheet. The method returns an [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) object. The class [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) represents a scroll bar. It has some important members:

- The [**LinkedCell**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/linkedcell/) property specifies a cell which is linked to the scroll bar.
- The [**Max**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/max/) property specifies the maximum value for the scroll bar range.
- The [**Min**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/min/) property specifies the minimum value for the scroll bar range.
- The [**IncrementalChange**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/incrementalchange/) property specifies the value amount for which a scroll bar is incremented a line scroll.
- The [**Shadow**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/shadow/) property indicates whether the scroll bar has 3D shading.
- The [**CurrentValue**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/currentvalue/) property specifies the current value of the scroll bar.
- The [**PageChange**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/pagechange/) property specifies how much the current value will be incremented if you click inside the scroll bar on either side of the scroll box.

The following example shows how to add a scroll bar to the worksheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Invisible the gridlines of the worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a value into A1 cell
    cells.Get(u"A1").PutValue(1);

    // Set the font color of the cell
    cells.Get(u"A1").GetStyle().GetFont().SetColor(Color::Maroon());

    // Set the font text bold
    cells.Get(u"A1").GetStyle().GetFont().SetIsBold(true);

    // Set the number format
    cells.Get(u"A1").GetStyle().SetNumber(1);

    // Add a scrollbar control
    ScrollBar scrollbar = worksheet.GetShapes().AddScrollBar(0, 0, 1, 0, 125, 20);

    // Set the placement type of the scrollbar
    scrollbar.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    scrollbar.SetLinkedCell(u"A1");

    // Set the maximum value
    scrollbar.SetMax(20);

    // Set the minimum value
    scrollbar.SetMin(1);

    // Set the incr. change for the control
    scrollbar.SetIncrementalChange(1);

    // Set the page change attribute
    scrollbar.SetPageChange(5);

    // Set it 3-D shading
    scrollbar.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Scrollbar added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

The [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class provides a method named [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/), which is used to add a group box control to the worksheet. The method returns an [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) object. Moreover, the [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) method of the [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) class groups the shapes, it takes a [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) array as parameter and returns a [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/) object. The class [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) represents a group box. It has some important members:

- The [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/text/) property specifies the group box's caption string.
- The [**Shadow**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/shadow/) property indicates whether the group box has 3D shading.

The following example shows how to add a group box and group the controls in the worksheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a group box to the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);
    GroupBox box = worksheet.GetShapes().AddGroupBox(1, 0, 1, 0, 300, 250);

    // Set the caption of the group box
    box.SetText(u"Age Groups");
    box.SetPlacement(PlacementType::FreeFloating);

    // Make it 2-D box
    box.SetShadow(false);

    // Add a radio button
    RadioButton radio1 = worksheet.GetShapes().AddRadioButton(3, 0, 2, 0, 30, 110);

    // Set its text string
    radio1.SetText(u"20-29");

    // Set A1 cell as a linked cell for the radio button
    radio1.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio1.SetShadow(true);

    // Set the weight of the radio button
    radio1.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio2 = worksheet.GetShapes().AddRadioButton(6, 0, 2, 0, 30, 110);

    // Set its text string
    radio2.SetText(u"30-39");

    // Set A1 cell as a linked cell for the radio button
    radio2.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio2.SetShadow(true);

    // Set the weight of the radio button
    radio2.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio3 = worksheet.GetShapes().AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string
    radio3.SetText(u"40-49");

    // Set A1 cell as a linked cell for the radio button
    radio3.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio3.SetShadow(true);

    // Set the weight of the radio button
    radio3.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Get the shapes
    Vector<Shape> shapeobjects{ box, radio1, radio2, radio3 };

    // Group the shapes
    GroupShape group = worksheet.GetShapes().Group(shapeobjects);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Add ActiveX Controls using Aspose.Cells](/cells/cpp/add-activex-controls-using-aspose-cells/)
- [Remove ActiveX Control](/cells/cpp/remove-activex-control/)
- [Update ActiveX ComboBox Control](/cells/cpp/update-activex-combobox-control/)