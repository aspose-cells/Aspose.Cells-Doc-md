---
title: 使用C++管理控件
linktitle: 控件管理
type: docs
weight: 150
url: /zh/cpp/managing-controls/
description: 学习如何使用Aspose.Cells与C++在工作表中添加和管理各种控件，如线条、矩形、弧、椭圆、旋钮、滚动条和组框。
---

## **介绍**

开发者可以添加不同的绘图对象，比如文本框、复选框、单选按钮、组合框、标签、按钮、线条、矩形、弧、椭圆、旋钮、滚动条、组框等。Aspose.Cells提供了 `Aspose::Cells::Drawing` 命名空间，其中包含所有绘图对象。然而，有些绘图对象或形状尚未支持。可以在Microsoft Excel中用设计器工作簿创建这些绘图对象，然后导入到Aspose.Cells中。Aspose.Cells允许你从设计师工作簿加载这些绘图对象，并写入生成的文件中。

## **将文本框控件添加到工作表**

在报告中强调重要信息的一种方法是使用文本框。例如，添加文本以突出显示公司名称或指示地理区域的最高销售额等。Aspose.Cells 提供 [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/) 类，用于向集合添加新的文本框。还有另一个类 [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/)，表示用于定义所有类型设置的文本框。它具有一些重要成员：

- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) 属性指定放置类型。
- [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) 属性指定字体属性。
- [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) 方法为文本框添加超链接。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) 属性返回一个 [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/) 对象，用于设置文本框的填充格式。
- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) 属性返回用于设置文本框线条样式和粗细的 [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/) 对象。
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) 属性指定文本框的输入文本。

以下示例在工作簿的第一个工作表中创建了两个文本框。第一个文本框配有不同的格式设置。第二个是一个简单的文本框。

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

## **在设计器电子表格中操作文本框控件**

Aspose.Cells还允许您访问设计器工作表中的文本框并对其进行操作。使用[**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/)属性获取工作表中的文本框集合。

以下示例使用上面示例中创建的 Microsoft Excel 文件。它获取了两个文本框的文本字符串，并将第二个文本框的文本更改后保存了文件。

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

## **将复选框控件添加到工作表**

如果您希望为用户提供在两个选项之间进行选择的方式，例如true或false；yes或no，复选框非常有用。Aspose.Cells允许您在工作表中使用复选框。例如，您可能已经开发了一个财务预测工作表，在其中您可以选择是否考虑某个收购。在这种情况下，您可能想要在工作表顶部放置一个复选框。然后，您可以将该复选框的状态链接到另一个单元格，以便如果选择了复选框，则单元格的值为True；如果未选择，则单元格的值为False。

### **使用Microsoft Excel**

要在工作表中放置复选框控件，请按照以下步骤进行：

1. 确保显示“表单”工具栏。
1. 单击“表单”工具栏上的**复选框**工具。
1. 在工作表区域，单击并拖动以定义容纳复选框和复选框旁边标签的矩形。
1. 放置复选框后，将鼠标光标移至标签区域并更改标签。
1. 在**单元格链接**字段中，指定应链接到该复选框的单元格地址。
1. 单击**确定**。

### **使用Aspose.Cells**

Aspose.Cells提供了[**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/)类，用于添加新的复选框到集合中。还有另一个类[**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/)，代表一个复选框。它具有一些重要成员：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)属性指定与复选框链接的单元格。
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)属性指定与复选框关联的文本字符串。它是复选框的标签。
- [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/)属性指定复选框是否已选中。

以下示例显示如何向工作表添加复选框。

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

## **向工作表添加单选按钮控件**

单选按钮，或选项按钮，是一个由圆形框制成的控件。用户通过选择圆形框来做出选择。单选按钮通常，如果不是总是，会以其他形式出现和表现。这样的单选按钮会以组的形式出现和表现。用户可以通过只选择其中一个来决定哪一个按钮是有效的。当用户点击其中一个按钮时，它会被填充。当组中的一个按钮被选中时，同一组的按钮是空的。

### **使用Microsoft Excel**

要在工作表中放置单选按钮控件，请按照以下步骤执行：

1. 确保**表单**工具栏已显示。
1. 单击 **选项按钮** 工具。
1. 在工作表中，单击并拖动以定义将容纳选项按钮和选项按钮旁边标签的矩形。
1. 一旦单选按钮放置在工作表中，将鼠标光标移入标签区域并更改标签。
1. 在 **单元格链接** 字段中，指定应与此单选按钮链接的单元格的地址。
1. 点击**确定**。

### **使用Aspose.Cells**

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) 类提供一个名为 [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/) 的方法，用于向工作表添加单选按钮控件。该方法返回一个 [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) 对象。类 [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) 代表一个选项按钮。它具有一些重要成员：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) 属性指定与单选按钮关联的单元格。
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) 属性指定与单选按钮相关联的文本字符串。它是单选按钮的标签。
- [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) 属性指定单选按钮是否选中。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) 属性指定单选按钮的填充格式。
- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) 属性指定选项按钮的线条格式样式。

以下示例显示了如何向工作表添加单选按钮。该示例添加了代表年龄组的三个单选按钮。

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

## **向工作表添加组合框控件**

为了更容易进行数据输入，或者将输入限制为您定义的某些项，您可以创建一个组合框或下拉列表，这些有效条目是从工作表上的其他单元格编制而成的。当您为单元格创建下拉列表时，它会在该单元格旁边显示一个箭头。要在该单元格中输入信息，单击箭头，然后单击所需的条目。

### **使用Microsoft Excel**

要在工作表中放置组合框控件，请按照以下步骤执行：

1. 确保**表单**工具栏已显示。
1. 单击 **组合框** 工具。
1. 在您的工作表区域，单击并拖动以定义将容纳组合框的矩形。
1. 一旦组合框放置在工作表中，请右键单击控件，选择**设置控件格式**并指定输入范围。
1. 在**单元格链接**字段中，指定应链接到该组合框的单元格地址。
1. 单击**确定**。

### **使用Aspose.Cells**

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) 类提供了一个名为 [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/) 的方法，用于向工作表添加组合框控件。该方法返回一个 [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) 对象。类 [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) 表示一个组合框。它有一些重要成员：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) 属性指定与组合框关联的单元格。
- [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) 属性指定用于填充组合框的工作表单元格范围。
- [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) 属性指定下拉部分中显示的列表行数。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/)属性指示下拉框是否具有3D阴影。

以下示例显示如何向工作表添加下拉框。

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

## **将标签控件添加到工作表**

标签是向用户提供有关电子表格内容的信息的手段。Aspose.Cells使得可以向工作表中添加和操作标签。[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)类提供了一个名为[**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/)的方法，用于向工作表添加标签控件。该方法返回一个[**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/)对象。[**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/)类表示工作表中的标签。它有一些重要成员：

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)方法指定标签的标题字符串。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)方法指定[**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)，即标签附加到工作表中的单元格的方式。

以下示例显示如何向工作表添加标签。

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

## **将列表框控件添加到工作表**

列表框控件创建一个列表控件，允许选择单个或多个项目。

### **使用Microsoft Excel**

要在工作表中放置列表框控件:

1. 确保**表单**工具栏已显示。
1. 点击**列表框**工具。
1. 在工作表区域，单击并拖动以定义将容纳列表框的矩形。
1. 将列表框放置在工作表中后，右键单击控件，然后点击**格式控件**，并指定输入范围。
1. 在**单元格链接**字段中，指定应将该列表框链接到的单元格地址，并设置选择类型（单选，多选，扩展）属性
1. 点击**确定**。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)类提供了一个名为[**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/)的方法，用于向工作表添加列表框控件。该方法返回一个[**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/)对象。[**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/)类表示列表框。它有一些重要成员：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)方法指定与列表框链接的单元格。
- [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/)方法指定用于填充列表框的工作表单元格范围。
- [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/)方法指定列表框的选择模式。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/)方法指示列表框是否具有3D阴影。

以下示例显示了如何向工作表中添加列表框。

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

## **向工作表添加按钮控件**

按钮对于执行某些操作非常有用。有时，将VBA宏分配给按钮或分配超链接以打开网页非常有用。

### **使用Microsoft Excel**

要在工作表中放置按钮控件：

1. 确保**表单**工具栏已显示。
1. 单击**按钮**工具。
1. 在工作表区域，单击并拖动以定义将容纳按钮的矩形。
1. 将按钮放置在工作表中后，右键单击控件并选择**格式控件**，然后指定VBA宏和相关字体、对齐、大小、边距等属性。
1. 单击**确定**。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)类提供了一个名为[**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/)的方法，用于向工作表中添加按钮控件。该方法返回一个[**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/)对象。类[**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/)表示按钮，具有一些重要成员：

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)属性指定按钮的标题。
- [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)属性指定按钮控件标签的字体属性。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)属性指定[**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)，按钮与工作表中的单元格的连接方式。
- [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/)属性为按钮控件添加超链接。单击按钮将导航到相关的URL。

以下示例显示了如何向工作表中添加按钮。

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

## **向工作表添加线控件**

### **使用Microsoft Excel**

1. 在 **绘图** 工具栏上，单击 **自选图形**，指向 **线条**，然后选择所需的线条样式。
1. 拖动以绘制线条。
1. 执行以下操作中的一个或两个：
   1. 要限制线条以与起点呈15度角的方式绘制，请在拖动时按住 SHIFT 键。
   1. 要使线条从第一个端点向相反方向延伸，请在拖动时按住 CTRL 键。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) 类提供一个名为 [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/) 的方法，用于向工作表添加线条形状。该方法返回一个 [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) 对象。类 [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) 代表一条线。它具有一些重要成员：

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) 方法指定线的格式。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) 方法指定 [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)，线如何连接到工作表中的单元格。

以下示例展示了如何向工作表添加线条。它创建了三条具有不同样式的线。

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

### **向线条添加箭头**

Aspose.Cells 还允许您绘制箭头线条。您可以向一条线条添加箭头，并格式化该线。例如，您可以更改线条的颜色，或指定线条的粗细和样式。

以下示例展示了如何向线添加箭头。

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

## **在工作表中添加矩形控件**

Aspose.Cells允许您在工作表中绘制矩形形状。您可以创建矩形、正方形等形状，还可以格式化控件的填充颜色和边框线颜色。例如，您可以更改矩形的颜色，设置阴影颜色，指定矩形的重量和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**矩形**。
1. 拖动绘制矩形。
1. 执行以下操作中的一个或两个：
   1. 若要从起点绘制正方形并约束矩形，请按住SHIFT键并拖动。
   1. 若要从中心点绘制矩形，请按住CTRL键并拖动。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) 类提供了一个名为 [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/) 的方法，用于向工作表添加矩形形状。该方法返回一个 [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) 对象。类 [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) 表示一个矩形。它有一些重要成员:

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) 属性指定矩形的线条格式属性。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) 属性指定 [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)，矩形如何连接到工作表中的单元格。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) 属性指定矩形的填充格式样式。

以下示例展示了如何向工作表添加矩形。

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

## **向工作表添加弧形控件**

Aspose.Cells允许您在工作表中绘制弧形。您可以创建简单的填充弧形。您可以格式化控件的填充颜色和边框线颜色。例如，您可以指定/更改弧形的颜色，设置阴影颜色，指定形状的重量和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**AutoShapes**中的**弧形**。
1. 拖动绘制弧形。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) 类提供了一个名为 [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/) 的方法，用于向工作表添加弧形状。该方法返回一个 [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) 对象。类 [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) 表示一条弧。它有一些重要成员:

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) 属性指定弧形状的线条格式属性。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) 属性指定 [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)，弧形状如何连接到工作表中的单元格。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) 属性指定了形状的填充格式样式。
- [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) 属性指定右下角行索引。
- [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) 属性指定右下角列索引。

以下示例显示了如何将弧形形状添加到工作表。该示例创建了两个弧形形状：一个填充，另一个是简单的。

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

## **向工作表添加椭圆控件**

Aspose.Cells允许您在工作表中绘制椭圆形状。创建简单和填充的椭圆形状，并格式化控件的填充颜色和边框线颜色。例如，您可以指定/更改椭圆的颜色，设置阴影颜色，指定形状的宽度和样式。

### **使用Microsoft Excel**

- 在*绘图*工具栏上，单击*椭圆*。
- 拖动以绘制椭圆。
- 可以执行以下操作中的一个或者两个：
- 要使椭圆从起点处绘制成圆形，请按住SHIFT键并拖动。
- 要从中心点绘制椭圆，请按住CTRL键并拖动。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) 类提供了一个名为 [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/) 的方法，该方法用于向工作表添加椭圆形状。该方法返回一个 [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) 对象。类 [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) 表示椭圆形状。它具有一些重要成员：

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) 属性指定椭圆形状的线条格式属性。
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) 属性指定了 [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)，即椭圆形状附加到工作表中的单元格的方式。
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) 属性指定了形状的填充格式样式。
- [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) 属性指定右下角行索引。
- [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) 属性指定右下角列索引。

以下示例显示了如何将椭圆形状添加到工作表。该示例创建了两个椭圆形状：一个填充的椭圆和一个简单的圆形。

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

## **向工作表添加微调控件**

微调框是附加到按钮（称为微调按钮）的文本框，由上箭头和下箭头组成，点击它们可以逐渐改变文本框中的值。通过使用微调框，您可以查看输入对财务模型的变化将如何改变模型输出。您可以将微调按钮附加到特定输入单元格。当您点击微调按钮上的上箭头或下箭头时，目标输入单元格中的整数值增加或减少。*Aspose.Cells*允许您在工作表中创建微调器。

### **使用Microsoft Excel**

在工作表中放置微调框控件：

- 确保*表单*工具栏已显示。
- 单击*微调*工具。
- 在工作表区域，单击并拖动以定义将容纳微调器的矩形。
将微调按钮放置在工作表中后，右键单击控件，然后单击*格式控件*，指定最大、最小和递增值。
在*单元格链接*字段中，指定与此微调按钮应链接的单元格的地址。
单击*确定*。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)类提供一个名为[**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/)的方法，用于向工作表添加微调按钮控件。该方法返回一个[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/)对象。[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/)类表示微调按钮，具有一些重要成员：

[**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)属性指定与微调按钮关联的单元格。
[**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/)属性指定微调按钮范围的最大值。
[**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/)属性指定微调按钮范围的最小值。
[**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/)属性指定微调按钮递增一行滚动的值。
[**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/)属性指示微调按钮是否具有3D阴影。
[**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/)属性指定微调按钮的当前值。

以下示例显示了如何向工作表添加微调按钮。

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

## **向工作表添加滚动条控件**

滚动条控件用于帮助以类似于微调按钮控件的方式选择工作表上的数据。通过向工作表添加控件并将其链接到单元格，可以返回控件当前位置的数值。

### **使用Microsoft Excel**

- 若要在Excel 2003及更早版本中添加滚动条，请单击*表单*工具栏上的*滚动条*按钮，然后创建一个覆盖B2:B6单元格高度并且大约为列宽四分之一的滚动条。
- 若要在Excel 2007中添加滚动条，请单击*开发人员*选项卡，单击*插入*，然后在“表单控件”部分单击*滚动条*。
- 右键单击滚动条，然后单击*格式控件*。
- 键入以下信息，然后单击*确定*：
  - 在*当前数值*框中，键入1。
  - 在*最小值*框中，键入1。此值限制滚动条的顶部到列表中的第一项。
  - 在*最大值*框中，键入20。此数字指定列表中的条目最大数量。
  - 在*增量更改*框中，键入1。该值控制滚动条控制当前值增加多少个数字。
  - 在*页面更改*框中，键入5。这个条目控制当前值的增量，如果你在滚动条内部点击滚动条两侧。
  - 将一个数字值放入G1单元格（根据列表中选择的项目），在*单元格链接*框中输入G1。
- 单击任何单元格，以便滚动条未被选择。

当你单击滚动条上或下的控制时，单元格G1会更新为指示当前滚动条值加/减滚动条的增量的数字。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)类提供了一个名为[**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/)的方法，用于在工作表中添加滚动条控件。该方法返回一个[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/)对象。类[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/)表示一个滚动条。它有一些重要成员：

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)属性指定与滚动条链接的单元格。
- [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/)属性指定滚动条范围的最大值。
- [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/)属性指定滚动条范围的最小值。
- [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/)属性指定滚动条增量的值。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/)属性指示滚动条是否具有3D阴影。
- [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/)属性指定滚动条的当前值。
- [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/)属性指定如果在滚动条滚动框两侧点击，将要增加多少当前值。

下面的示例展示了如何将滚动条添加到工作表。

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

## **在工作表中对组控件添加GroupBox控件**

有时候你确实需要实现单选按钮或其他属于某个组的控件，可以通过包括一个组框或矩形控件来实现。这两个对象中的任何一个都将作为组的分隔符。添加其中一个形状后，然后你可以添加两个或两个以上的单选按钮或其他组对象。

### **使用Microsoft Excel**

要在工作表中放置一个组框控件并在其中放置控件：

- 要开始一个窗体，在主菜单上，点击*查看*，然后依次点击*工具栏*和*窗体*。
- 在*窗体*工具栏上，点击*组框*并在工作表上绘制一个矩形。
- 为框输入说明字符串。
- 在*表单*工具栏上，点击*选项按钮*，并点击*位于标题字符串下方的*分组框内。
- 再次从*表单*工具栏上，点击*选项按钮*，并点击*位于第一个单选按钮下方的*分组框内。
- 再次从*表单*工具栏上，点击*选项按钮*，并点击*位于上一个单选按钮下方的*分组框内。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)类提供了一个名为[**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/)的方法，用于向工作表中添加一个分组框控件。该方法返回一个[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/)对象。此外，[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)类的[**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/)方法将形状分组，它以[**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/)数组作为参数并返回一个[**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/)对象。[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/)类代表一个分组框。它有一些重要成员:

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)属性指定分组框的标题字符串。
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/)属性指示分组框是否具有3D阴影。

下面的示例演示了如何在工作表中添加一个分组框和对控件进行分组。

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

## **高级主题**
- [使用Aspose.Cells添加ActiveX控件](/cells/zh/cpp/add-activex-controls-using-aspose-cells/)
- [移除ActiveX控件](/cells/zh/cpp/remove-activex-control/)
- [更新ActiveX ComboBox控件](/cells/zh/cpp/update-activex-combobox-control/)
{{< app/cells/assistant language="cpp" >}}
