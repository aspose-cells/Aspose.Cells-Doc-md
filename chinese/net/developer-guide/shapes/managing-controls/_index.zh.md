---
title: 管理控件
type: docs
weight: 150
url: /zh/net/managing-controls/
---

## **介绍**

开发人员可以添加不同的绘图对象，如文本框、复选框、单选按钮、组合框、标签、按钮、直线、矩形、弧线、椭圆形、微调按钮、滚动条、分组框等。Aspose.Cells提供了包含所有绘图对象的Aspose.Cells.Drawing命名空间。然而，有一些绘图对象或形状目前尚不支持。在Microsoft Excel中的设计表格中创建这些绘图对象，然后导入到Aspose.Cells中。Aspose.Cells允许您从设计表格加载这些绘图对象，然后将它们写入生成的文件中。

## **在工作表中添加文本框控件**

在报告中强调重要信息的一种方式是使用文本框。例如，添加文本以突出显示公司名称或指示具有最高销售额的地理区域等。Aspose.Cells提供了用于向集合中添加新文本框的[**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection)类。还有另一个类[**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)，它代表用于定义所有类型设置的文本框。它有一些重要成员:

- [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe)属性返回一个[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe)对象，该对象用于调整文本框的内容。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定放置类型。
- [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font)属性指定字体属性。
- [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)方法为文本框添加超链接。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性返回一个[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat)对象，用于设置文本框的填充格式。
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性返回一个[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat)对象，通常用于样式和粗细设置文本框线条。
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定文本框的输入文本。

以下示例在工作簿的第一个工作表中创建了两个文本框。第一个文本框具有不同的格式设置。第二个是一个简单的文本框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **在设计表格中操作文本框控件**

Aspose.Cells还允许您访问设计工作表中的文本框并对其进行操作。使用[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes)属性获取工作表中的文本框集合。

以下示例使用我们在上文中创建的Microsoft Excel文件。它获取两个文本框的文本字符串，并将第二个文本框的文本更改后保存文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **在工作表中添加复选框控件**

如果您想要为用户提供在两个选项之间进行选择的方式，如真或假; 是或否，复选框就非常方便。Aspose.Cells允许您在工作表中使用复选框。例如，您可能已经开发了一个财务预测工作表，在这个工作表中，您可以选择考虑一个特定的收购或不考虑。在这种情况下，您可能希望在工作表的顶部放置一个复选框。然后，您可以将此复选框的状态链接到另一个单元格，这样，如果选中复选框，则单元格的值为True；如果未选中，则单元格的值为False。

### **使用Microsoft Excel**

要在工作表中放置复选框控件，请按照以下步骤操作：

1. 确保显示“表单”工具栏。
1. 单击“复选框”工具栏上的**复选框**工具。
1. 在您的工作表区域，单击并拖动以定义将容纳复选框和复选框旁边标签的矩形。
1. 放置复选框后，将鼠标光标移动到标签区域并更改标签。
1. 在**单元格链接**字段中，指定应将此复选框链接到的单元格地址。
1. 单击**确定**。

### **使用Aspose.Cells**

Aspose.Cells提供了[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection)类，用于向集合中添加新的复选框。还有另一个类[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox)，它代表一个复选框。它有一些重要的成员：

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定与复选框关联的单元格。
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定与复选框相关联的文本字符串。这是复选框的标签。
- [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value)属性指定复选框是否被选中。

以下示例显示了如何将复选框添加到工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **向工作表添加单选按钮控件**

单选按钮，或选项按钮，是由一个圆框组成的控件。用户通过选择圆框来做出决定。单选按钮通常与其他单选按钮一起出现并表现为一组。用户通过仅选择其中一个按钮来决定哪个按钮是有效的。当用户单击一个按钮时，它会被填充。当选择同一组中的一个按钮时，同一组的按钮会为空。

### **使用Microsoft Excel**

要在工作表中放置单选按钮控件，请按照以下步骤操作：

1. 确保**表单**工具栏已显示。
1. 单击**选项按钮**工具。
1. 在工作表中，单击并拖动以定义将容纳选项按钮和选项按钮旁边标签的矩形。
1. 将单选按钮放置在工作表中后，将鼠标光标移动到标签区域并更改标签。
1. 在**单元格链接**字段中，指定应将此单选按钮链接到的单元格地址。
1. 单击**确定**。

### **使用Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton)的方法，用于向工作表添加单选按钮控件。该方法返回一个[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)对象。类[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)表示一个选项按钮。它有一些重要的成员：

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定与单选按钮关联的单元格。
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定与单选按钮相关联的文本字符串。这是单选按钮的标签。
- [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked)属性指定单选按钮是否被选中。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定单选按钮的填充格式。
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性指定选项按钮的线格式样式。

以下示例显示了如何在工作表中添加单选按钮。该示例添加了代表年龄组的三个单选按钮。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **向工作表添加组合框控件**

为了使数据输入更容易，或者限制输入到你定义的某些项目，您可以创建一个下拉列表框，或从工作表的其他位置编译的有效条目的下拉列表。当您为单元格创建一个下拉列表时，它会显示在该单元格旁边的一个箭头符号。要在该单元格输入信息，请单击箭头，然后单击您想要的条目。

### **使用Microsoft Excel**

要在工作表中放置一个组合框控件，请按照以下步骤进行:

1. 确保**表单**工具栏已显示。
1. 单击 **组合框** 工具。
1. 在你的工作表区域，单击并拖动以定义将容纳组合框的矩形。
1. 一旦组合框放置在工作表中，右键单击控件以单击 **格式控制** 并指定输入范围。
1. 在 **单元格链接** 字段中，指定此组合框应链接到的单元格的地址。
1. 单击**确定**。

### **使用Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) 的方法，用于向工作表添加一个组合框控件。该方法返回一个 [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) 对象。类[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)表示一个组合框。它具有一些重要成员:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) 属性指定与组合框链接的单元格。
- [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) 属性指定用于填充组合框的工作表单元格的范围。
- [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) 属性指定要在组合框下拉部分中显示的列表行数。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) 属性指示组合框是否具有3D阴影。

下面的示例展示了如何向工作表添加组合框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **向工作表添加标签控件**

标签是用来向用户提供有关工作表内容的信息的一种手段。Aspose.Cells使得在工作表中添加和操作标签成为可能。[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) 的方法，用于向工作表添加一个标签控件。该方法返回一个 [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) 对象。类 [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) 表示工作表中的一个标签。它有一些重要成员:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) 方法指定标签的标题字符串。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) 方法指定 [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，标签附加到工作表中的单元格的方式。

下面的示例展示了如何向工作表添加标签。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **向工作表添加列表框控件**

列表框控件创建一个允许选择单个或多个项目的列表控件。

### **使用Microsoft Excel**

要在工作表中放置一个列表框控件:

1. 确保**表单**工具栏已显示。
1. 单击 **列表框** 工具。
1. 在你的工作表区域，单击并拖动以定义将容纳列表框的矩形。
1. 一旦列表框放置在工作表中，右键单击控件以单击 **格式控制** 并指定输入范围。
1. 在 **单元格链接** 字段中，指定此列表框应链接到的单元格的地址并设置选择类型 (单选，多选，扩展) 属性
1. 单击**确定**。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) 的方法，用于向工作表添加一个列表框控件。该方法返回一个 [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) 对象。类 [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) 表示列表框。它有一些重要成员:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) 方法指定链接到列表框的单元格。
- [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange)方法指定用于填充列表框的工作表范围。
- [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)方法指定列表框的选择模式。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow)方法指示列表框是否具有3D阴影。

以下示例显示了如何向工作表添加列表框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **在工作表中添加按钮控件**

按钮很有用，可用于执行某些操作。有时，将VBA宏分配给按钮或将超链接分配给打开网页很有用。

### **使用Microsoft Excel**

要在工作表中放置按钮控件：

1. 确保**表单**工具栏已显示。
1. 单击**按钮**工具。
1. 在工作表区域，单击并拖动以定义将容纳按钮的矩形。
1. 将列表框放置在工作表中后，右键单击控件，然后选择**格式控件**，然后指定VBA宏和相关字体、对齐、大小、边距等属性。
1. 单击**确定**。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton)的方法，用于向工作表添加按钮控件。该方法返回一个[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button)对象。类[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button)表示一个按钮。它有一些重要成员：

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定按钮的标题。
- [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font)属性指定按钮控件标签的字体属性。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定[**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，按钮附加到工作表中的方式。
- [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)属性为按钮控件添加超链接。单击按钮将导航到相关网址。

以下示例显示了如何向工作表添加按钮。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **在工作表中添加线控件**

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**自选图形**，指向**线条**，选择要使用的线条样式。
1. 拖动以绘制线条。
1. 进行以下操作中的一项或两项：
   1. 若要约束线条在与其起始点成15度角的方向上绘制，请按住SHIFT并拖动。
   1. 若要从第一端点向相反方向拉长线段，请按住CTRL并拖动。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)的方法，用于向工作表添加线条形状。该方法返回一个[**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)对象。类[**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)表示一条线。它有一些重要成员：

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)方法指定线条的格式。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)方法指定[**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，线条附加到工作表中的方式。

以下示例显示了如何向工作表添加线条。它创建了具有不同样式的三条线。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **向线条添加箭头**

Aspose.Cells还允许您绘制箭头线。可以向线条添加箭头头部，并格式化线条。例如，可以更改线条的颜色，或指定线条的粗细和样式。

以下示例演示如何向一条线条添加箭头。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **向工作表添加矩形控件**

Aspose.Cells允许您在工作表中绘制矩形形状。您可以创建矩形、正方形等形状。您也可以自定义控件的填充颜色和边界线颜色。例如，您可以更改矩形的颜色、设置阴影颜色、指定矩形的粗细和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在“绘图”工具栏中，单击“矩形”。
1. 拖动以绘制矩形。
1. 进行以下操作中的一项或两项：
   1. 从起始点开始，按住SHIFT以约束矩形绘制正方形。
   1. 按住CTRL并拖动以从中心点绘制矩形。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)的方法，用于向工作表添加矩形形状。该方法返回[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)对象。类[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)表示一个矩形。它具有一些重要成员：

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性指定了矩形的线条格式属性。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定了[**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)的格式，即矩形附加到工作表中单元格的方式。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定了矩形的填充格式样式。

以下示例演示如何向工作表添加矩形。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **向工作表添加弧控件**

Aspose.Cells允许您在工作表中绘制弧形状。您可以创建简单的填充弧。您可以自定义控件的填充颜色和边界线颜色。例如，您可以指定/更改弧形的颜色、设置阴影颜色、指定形状的粗细和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在“绘图”工具栏中，单击“自选图形”中的“弧”。
1. 拖动以绘制弧。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc)的方法，用于向工作表添加弧形状。该方法返回一个[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)对象。类[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)表示一个弧。它具有一些重要成员：

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性指定了弧形状的线条格式属性。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定了[**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)的格式，即弧附加到工作表中单元格的方式。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定形状的填充格式样式。
- [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)属性指定右下角行索引。
- [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)属性指定右下角列索引。

以下示例演示如何向工作表添加弧形状。该示例创建了两个弧形状：一个是填充的，另一个是简单的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **向工作表添加椭圆形控件**

Aspose.Cells允许您在工作表中绘制椭圆形状。创建简单的和填充的椭圆形状，并自定义控件的填充颜色和边界线颜色。例如，您可以指定/更改椭圆的颜色、设置阴影颜色、指定形状的粗细和样式。

### **使用Microsoft Excel**

- 在“绘图”工具栏上，单击“椭圆”。
- 拖动以绘制椭圆。
- 进行以下操作中的一项或两项：
- 从起始点开始，按住SHIFT以约束椭圆绘制圆形。
- 在拖动时按住CTRL键，从中心点绘制椭圆。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval)的方法，用于在工作表中添加椭圆形状。该方法返回一个[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)对象。类[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)代表一个椭圆形状。它有一些重要的成员：

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性指定椭圆形状的线条格式属性。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定[**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，椭圆如何连接到工作表中的单元格。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定形状的填充格式样式。
- [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)属性指定右下角行索引。
- [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)属性指定右下角列索引。

以下示例显示如何将椭圆形状添加到工作表。示例创建两个椭圆形状：一个是填充的椭圆，另一个是简单的圆。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **向工作表添加微调控件**

微调框是附加到按钮（称为微调按钮）的文本框，由上箭头和下箭头组成，点击箭头逐步更改文本框中的值。通过使用微调框，您可以看到对财务模型的输入更改如何改变模型输出。您可以将微调按钮附加到特定输入单元格。当您点击微调按钮上的上箭头或下箭头时，目标输入单元格中的整数值会增加或减少。 *Aspose.Cells*允许您在工作表中创建微调器。

### **使用Microsoft Excel**

在工作表中放置微调器控件：

- 确保显示*表单*工具栏。
- 单击*微调器*工具。
- 在工作表区域，单击并拖动定义将包含微调器的矩形。
- 放置微调器在工作表中后，右键单击控件，单击*格式控件*并指定最大、最小和递增值。
- 在*单元格链接*字段中，指定应将此微调框链接到的单元格的地址。
- 单击*确定*。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner)的方法，用于在工作表中添加微调框控件。该方法返回一个[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)对象。类[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)代表一个微调框。它有一些重要的成员：

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定与微调框链接的单元格。
- [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max)属性指定微调框范围的最大值。
- [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min)属性指定微调框范围的最小值。
- [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange)属性指定按行滚动时微调器增加的值数量。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow)属性指示微调框是否具有3D阴影。
- [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue)属性指定微调框的当前值。

以下示例显示如何向工作表添加一个微调框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **向工作表添加滚动条控件**

滚动条控件用于帮助在工作表上选择数据，方式类似于微调框控件。通过将控件添加到工作表并将其链接到单元格，可以返回控件当前位置的数值。

### **使用Microsoft Excel**

- 要在Excel 2003及更早版本中添加滚动条，单击*表单*工具栏上的*滚动条*按钮，然后创建一个高度覆盖单元格B2:B6且宽度为列宽四分之一的滚动条。
- 要在Excel 2007中添加滚动条，单击*开发人员*选项卡，单击*插入*，然后单击*滚动条*在表单控件部分。
- 右键单击滚动条，然后单击*格式控件*。
- 输入以下信息，并单击 *确定*：
  - 在 *当前值* 栏中输入 1。
  - 在 *最小值* 栏中输入 1。此值将滚动条的顶端限制为列表中的第一项。
  - 在 *最大值* 栏中输入 20。该数字指定列表中的最大条目数。
  - 在 *递增更改* 栏中输入 1。此值控制滚动条控件递增当前值的数量。
  - 在 *页更改* 栏内输入 5。此条目控制点击滚动块两侧滚动条内部时当前值将增加多少。
  - 在 *单元格链接* 栏中输入 G1（取决于列表中选择了哪个项目），
- 单击任意单元格，以取消选定滚动条。

单击滚动条上的向上或向下控件时，单元格 G1 的值将更新为指示滚动条的当前值加上或减去滚动条的递增更改值的数字。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) 的方法，用于向工作表添加滚动条控件。该方法返回一个 [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) 对象。类 [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) 表示滚动条，其中有一些重要成员:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) 属性指定与滚动条关联的单元格。
- [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) 属性指定滚动条范围的最大值。
- [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) 属性指定滚动条范围的最小值。
- [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) 属性指定滚动条递增一行滚动的值量。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) 属性指示滚动条是否具有 3D 阴影。
- [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) 属性指定滚动条的当前值。
- [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) 属性指定如果在滚动条的滚动块两侧内部单击，将增加当前值的量。

下面的示例显示了如何向工作表添加滚动条。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **向工作表中的组控件添加 GroupBox 控件**

有时您需要实现单选按钮或其他属于特定组的控件，可以通过包含组框或矩形控件来实现。其中任何一个对象都将用作组的分隔符。添加其中一个形状后，您便可以添加两个或更多单选按钮或其他组对象。

### **使用Microsoft Excel**

要在工作表中放置组框控件并在其中放置控件:

- 要启动表单，在主菜单中，单击*查看*，然后单击*工具栏*和*表单*。
- 在 *表单* 工具栏上，单击*组框*，然后在工作表上绘制一个矩形。
- 为框输入标题字符串。
- 在 *表单* 工具栏上，单击*选项按钮*，然后单击*组框*中的标题字符串下方。
- 再次从 *表单* 工具栏中，单击*选项按钮*，然后单击*组框*中第一个单选按钮下方。
- 再次在 *表单* 工具栏中，单击*选项按钮*，然后单击*组框*中上一个单选按钮下方。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) 的方法，用于向工作表添加组框控件。该方法返回一个 [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) 对象。另外，[**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) 类的 [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 方法将形状分组，它以 [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) 数组作为参数并返回一个 [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) 对象。类 [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) 表示组框，其中有一些重要成员:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) 属性指定组框的标题字符串。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) 属性指示组框是否具有 3D 阴影。

以下示例显示了如何向工作表中添加分组框并对控件进行分组。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **高级主题**
- [使用Aspose.Cells添加ActiveX控件](/cells/zh/net/add-activex-controls-using-aspose-cells/)
- [移除ActiveX控件](/cells/zh/net/remove-activex-control/)
- [更新 ActiveX ComboBox 控件](/cells/zh/net/update-activex-combobox-control/)
