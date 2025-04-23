---
title: 控件管理
type: docs
weight: 150
url: /zh/python-net/managing-controls/
---

## **介绍**

开发者可以添加不同的绘图对象，如文本框、复选框、单选按钮、组合框、标签、按钮、线条、矩形、弧、椭圆、旋转器、滚动条、分组框等。Aspose.Cells for Python via .NET提供了Aspose.Cells.Drawing命名空间，其中包含所有绘图对象。然而，仍有一些绘图对象或形状尚未支持。在设计器电子表格中使用Microsoft Excel创建这些绘图对象，然后导入到Aspose.Cells。Aspose.Cells for Python via .NET允许您从设计器电子表格加载这些绘图对象并写入生成的文件。

## **将文本框控件添加到工作表**

强调报告中重要信息的一种方式是使用文本框。例如，添加文本以突出公司名称或指示销售额最高的地区等。Aspose.Cells for Python via .NET提供了 [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection) 类，用于向集合中添加新文本框。还有另一类 [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox)，表示用于定义所有类型设置的文本框。它具有一些重要成员：

- [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) 属性返回一个 [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe) 对象，用于调整文本框的内容。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) 属性指定放置类型。
- [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) 属性指定字体属性。
- [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) 方法为文本框添加超链接。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) 属性返回一个 [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat) 对象，用于设置文本框的填充格式。
- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) 属性返回用于设置文本框线条样式和粗细的 [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat) 对象。
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) 属性指定文本框的输入文本。

以下示例在工作簿的第一个工作表中创建了两个文本框。第一个文本框配有不同的格式设置。第二个是一个简单的文本框。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **在设计器电子表格中操作文本框控件**

Aspose.Cells for Python via .NET还允许您访问设计师工作表中的文本框并进行操作。使用 [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) 属性可获取工作表中的文本框集合。

以下示例使用上面示例中创建的 Microsoft Excel 文件。它获取了两个文本框的文本字符串，并将第二个文本框的文本更改后保存了文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **将复选框控件添加到工作表**

复选框在您希望为用户提供两种选择（如真或假；是或否）时非常方便；Aspose.Cells for Python via .NET 允许您在工作表中使用复选框。例如，您可能开发了一个财务预测工作表，在其中可以考虑某项收购或不考虑。在这种情况下，您可能希望在工作表顶部放置一个复选框。然后，您可以将该复选框的状态链接到另一个单元格，因此如果选中复选框，则单元格的值为 True；如果未选中，则值为 False。

### **使用Microsoft Excel**

要在工作表中放置复选框控件，请按照以下步骤进行：

1. 确保显示“表单”工具栏。
1. 单击“表单”工具栏上的**复选框**工具。
1. 在工作表区域，单击并拖动以定义容纳复选框和复选框旁边标签的矩形。
1. 放置复选框后，将鼠标光标移至标签区域并更改标签。
1. 在**单元格链接**字段中，指定应链接到该复选框的单元格地址。
1. 单击**确定**。

### **使用Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET 提供 [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection) 类，用于向集合中添加新复选框。还有另一个类 [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox)，代表复选框。它具有一些重要成员：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)属性指定与复选框链接的单元格。
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)属性指定与复选框关联的文本字符串。它是复选框的标签。
- [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value)属性指定复选框是否已选中。

以下示例显示如何向工作表添加复选框。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

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

### **使用Aspose.Cells for Python via .NET**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button) 的方法，用于向工作表添加单选按钮控件。该方法返回一个 [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) 对象。类 [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) 表示一个选项按钮。它有一些重要成员：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) 属性指定与单选按钮关联的单元格。
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) 属性指定与单选按钮相关联的文本字符串。它是单选按钮的标签。
- [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) 属性指定单选按钮是否选中。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) 属性指定单选按钮的填充格式。
- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) 属性指定选项按钮的线条格式样式。

以下示例显示了如何向工作表添加单选按钮。该示例添加了代表年龄组的三个单选按钮。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

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

### **使用Aspose.Cells for Python via .NET**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box) 的方法，用于向工作表添加组合框控件。该方法返回一个 [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) 对象。类 [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) 表示一个组合框。它有一些重要成员：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) 属性指定与组合框关联的单元格。
- [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) 属性指定用于填充组合框的工作表单元格范围。
- [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) 属性指定下拉部分中显示的列表行数。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow)属性指示下拉框是否具有3D阴影。

以下示例显示如何向工作表添加下拉框。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **将标签控件添加到工作表**

标签是向用户提供有关电子表格内容信息的手段。Aspose.Cells for Python via .NET 使在工作表中添加和操作标签成为可能。[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供一个名为 [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label) 的方法，用于在工作表中添加标签控件。该方法返回一个 [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) 对象。类 [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) 表示工作表中的标签。它具有一些重要成员：

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)方法指定标签的标题字符串。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement)方法指定[**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)，即标签附加到工作表中的单元格的方式。

以下示例显示如何向工作表添加标签。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

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

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类提供了一个名为[**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box)的方法，用于向工作表添加列表框控件。该方法返回一个[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox)对象。[**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox)类表示列表框。它有一些重要成员：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)方法指定与列表框链接的单元格。
- [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range)方法指定用于填充列表框的工作表单元格范围。
- [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type)方法指定列表框的选择模式。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow)方法指示列表框是否具有3D阴影。

以下示例显示了如何向工作表中添加列表框。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **向工作表添加按钮控件**

按钮对于执行某些操作非常有用。有时，将VBA宏分配给按钮或分配超链接以打开网页非常有用。

### **使用Microsoft Excel**

要在工作表中放置按钮控件：

1. 确保**表单**工具栏已显示。
1. 单击**按钮**工具。
1. 在工作表区域，单击并拖动以定义将容纳按钮的矩形。
1. 将按钮放置在工作表中后，右键单击控件并选择**格式控件**，然后指定VBA宏和相关字体、对齐、大小、边距等属性。
1. 单击**确定**。

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类提供了一个名为[**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button)的方法，用于向工作表中添加按钮控件。该方法返回一个[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button)对象。类[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button)表示按钮，具有一些重要成员：

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)属性指定按钮的标题。
- [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font)属性指定按钮控件标签的字体属性。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement)属性指定[**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)，按钮与工作表中的单元格的连接方式。
- [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink)属性为按钮控件添加超链接。单击按钮将导航到相关的URL。

以下示例显示了如何向工作表中添加按钮。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **向工作表添加线控件**

### **使用Microsoft Excel**

1. 在 **绘图** 工具栏上，单击 **自选图形**，指向 **线条**，然后选择所需的线条样式。
1. 拖动以绘制线条。
1. 执行以下操作中的一个或两个：
   1. 要限制线条以与起点呈15度角的方式绘制，请在拖动时按住 SHIFT 键。
   1. 要使线条从第一个端点向相反方向延伸，请在拖动时按住 CTRL 键。

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line) 的方法，用于向工作表添加线形状。该方法返回一个 [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) 对象。类 [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) 表示一条线。它有一些重要成员:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) 方法指定线的格式。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) 方法指定 [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)，线如何连接到工作表中的单元格。

以下示例展示了如何向工作表添加线条。它创建了三条具有不同样式的线。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **向线条添加箭头**

Aspose.Cells for Python via .NET 还允许您绘制箭头线。可以在线条上添加箭头，并对线条进行格式化。例如，您可以更改线条颜色，或指定线宽和线型。

以下示例展示了如何向线添加箭头。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **在工作表中添加矩形控件**

Aspose.Cells for Python via .NET 允许您在工作表中绘制矩形形状。您可以创建矩形、正方形等，还可以设置填充色和边框线颜色。例如，可以更改矩形的颜色，设置阴影颜色，或根据需要指定矩形的线宽和样式。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**矩形**。
1. 拖动绘制矩形。
1. 执行以下操作中的一个或两个：
   1. 若要从起点绘制正方形并约束矩形，请按住SHIFT键并拖动。
   1. 若要从中心点绘制矩形，请按住CTRL键并拖动。

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle) 的方法，用于向工作表添加矩形形状。该方法返回一个 [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) 对象。类 [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) 表示一个矩形。它有一些重要成员:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) 属性指定矩形的线条格式属性。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) 属性指定 [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)，矩形如何连接到工作表中的单元格。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) 属性指定矩形的填充格式样式。

以下示例展示了如何向工作表添加矩形。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **向工作表添加弧形控件**

Aspose.Cells for Python via .NET 允许您在工作表中绘制弧形。可以创建简单的弧和填充弧。还可以设置填充色和边框线颜色。例如，您可以指定/更改弧的颜色，设置阴影颜色，或根据需要指定形状的线宽和样式。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**AutoShapes**中的**弧形**。
1. 拖动绘制弧形。

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc) 的方法，用于向工作表添加弧形状。该方法返回一个 [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) 对象。类 [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) 表示一条弧。它有一些重要成员:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) 属性指定弧形状的线条格式属性。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) 属性指定 [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)，弧形状如何连接到工作表中的单元格。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) 属性指定了形状的填充格式样式。
- [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) 属性指定右下角行索引。
- [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) 属性指定右下角列索引。

以下示例显示了如何将弧形形状添加到工作表。该示例创建了两个弧形形状：一个填充，另一个是简单的。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **向工作表添加椭圆控件**

Aspose.Cells for Python via .NET 允许您在工作表中绘制椭圆形。创建简单的填充椭圆形，并格式化填充色和边框线颜色。例如，可以指定/更改椭圆的颜色，设置阴影颜色，或根据需要指定形状的线宽和样式。

### **使用Microsoft Excel**

- 在*绘图*工具栏上，单击*椭圆*。
- 拖动以绘制椭圆。
- 可以执行以下操作中的一个或者两个：
- 要使椭圆从起点处绘制成圆形，请按住SHIFT键并拖动。
- 要从中心点绘制椭圆，请按住CTRL键并拖动。

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval) 的方法，该方法用于向工作表添加椭圆形状。该方法返回一个 [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) 对象。类 [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) 表示椭圆形状。它具有一些重要成员：

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) 属性指定椭圆形状的线条格式属性。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) 属性指定了 [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)，即椭圆形状附加到工作表中的单元格的方式。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) 属性指定了形状的填充格式样式。
- [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) 属性指定右下角行索引。
- [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) 属性指定右下角列索引。

以下示例显示了如何将椭圆形状添加到工作表。该示例创建了两个椭圆形状：一个填充的椭圆和一个简单的圆形。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **向工作表添加微调控件**

旋转框是附加在按钮（称为旋钮）上的文本框，包括一个向上箭头和一个向下箭头，点击以逐步更改文本框中的值。通过使用旋转框，可以观察输入变化将如何影响财务模型的输出。可以将旋钮附加到特定的输入单元格。当点击旋钮上的向上或向下箭头时，目标输入单元格中的整数值增加或减少。*Aspose.Cells for Python via .NET* 允许您在工作表中创建旋转器。

### **使用Microsoft Excel**

在工作表中放置微调框控件：

- 确保*表单*工具栏已显示。
- 单击*微调*工具。
- 在工作表区域，单击并拖动以定义将容纳微调器的矩形。
将微调按钮放置在工作表中后，右键单击控件，然后单击*格式控件*，指定最大、最小和递增值。
在*单元格链接*字段中，指定与此微调按钮应链接的单元格的地址。
单击*确定*。

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类提供一个名为[**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner)的方法，用于向工作表添加微调按钮控件。该方法返回一个[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner)对象。[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner)类表示微调按钮，具有一些重要成员：

[**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)属性指定与微调按钮关联的单元格。
[**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max)属性指定微调按钮范围的最大值。
[**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min)属性指定微调按钮范围的最小值。
[**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change)属性指定微调按钮递增一行滚动的值。
[**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow)属性指示微调按钮是否具有3D阴影。
[**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value)属性指定微调按钮的当前值。

以下示例显示了如何向工作表添加微调按钮。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

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

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类提供了一个名为[**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar)的方法，用于在工作表中添加滚动条控件。该方法返回一个[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar)对象。类[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar)表示一个滚动条。它有一些重要成员：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)属性指定与滚动条链接的单元格。
- [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max)属性指定滚动条范围的最大值。
- [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min)属性指定滚动条范围的最小值。
- [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change)属性指定滚动条增量的值。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow)属性指示滚动条是否具有3D阴影。
- [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value)属性指定滚动条的当前值。
- [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change)属性指定如果在滚动条滚动框两侧点击，将要增加多少当前值。

下面的示例展示了如何将滚动条添加到工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

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

### **使用Aspose.Cells for Python via .NET**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类提供了一个名为[**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box)的方法，用于向工作表中添加一个分组框控件。该方法返回一个[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox)对象。此外，[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类的[**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group)方法将形状分组，它以[**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)数组作为参数并返回一个[**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape)对象。[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox)类代表一个分组框。它有一些重要成员:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)属性指定分组框的标题字符串。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow)属性指示分组框是否具有3D阴影。

下面的示例演示了如何在工作表中添加一个分组框和对控件进行分组。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **高级主题**
- [添加ActiveX控件](/cells/zh/python-net/add-activex-controls-using-aspose-cells/)
- [移除ActiveX控件](/cells/zh/python-net/remove-activex-control/)
- [更新ActiveX ComboBox控件](/cells/zh/python-net/update-activex-combobox-control/)
