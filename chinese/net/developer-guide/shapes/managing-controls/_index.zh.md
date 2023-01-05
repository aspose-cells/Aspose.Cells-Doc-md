---
title: 管理控制
type: docs
weight: 150
url: /zh/net/managing-controls/
---
## **介绍**

开发人员可以添加不同的绘图对象，例如文本框、复选框、单选按钮、组合框、标签、按钮、线条、矩形、圆弧、椭圆、旋转器、滚动条、组框等。Aspose.Cells 提供 Aspose.Cells.Drawing 命名空间，其中包含所有绘图对象。但是，尚不支持一些绘图对象或形状。使用 Microsoft Excel 在设计器电子表格中创建这些绘图对象，然后将设计器电子表格导入 Aspose.Cells。Aspose.Cells 允许您从设计器电子表格加载这些绘图对象并将它们写入生成的文件。

## **将文本框控件添加到工作表**

在报告中强调重要信息的一种方法是使用文本框。例如，添加文本以突出显示公司名称或指示销售额最高的地理区域等。Aspose.Cells 提供[**文本框集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection)类，用于向集合中添加新的文本框。还有一个类，[**文本框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)表示用于定义所有类型设置的文本框。它有一些重要的成员：

- 这[**文本框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe)属性返回一个[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe)用于调整文本框内容的对象。
- 这[**放置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定放置类型。
- 这[**字体**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) property 指定字体属性。
- 这[**添加超链接**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)方法为文本框添加超链接。
- 这[**填充格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性返回一个[**MsoFill格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat)用于设置文本框填充格式的对象。
- 这[**行格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性返回[**MsoLine格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat)对象通常用于文本框线的样式和粗细。
- 这[**文本**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定文本框的输入文本。

下面的示例在工作簿的第一个工作表中创建两个文本框。第一个文本框配备了不同的格式设置。第二个是简单的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **在 Designer 电子表格中操作文本框控件**

Aspose.Cells 还允许您访问设计器工作表中的文本框并对其进行操作。使用[**工作表.文本框**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes)属性以获取工作表中的文本框集合。

以下示例使用我们在上例中创建的 Microsoft Excel 文件。它获取两个文本框的文本字符串并更改第二个文本框的文本以保存文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **将复选框控件添加到工作表**

如果您想为用户提供一种在两个选项（例如 true 或 false）之间进行选择的方式，则复选框很方便；是还是不是。 Aspose.Cells 允许您在工作表中使用复选框。例如，您可能已经开发了一个财务预测工作表，您可以在其中考虑或不考虑特定的收购。在这种情况下，您可能希望在工作表顶部放置一个复选框。然后，您可以将此复选框的状态链接到另一个单元格，这样，如果复选框被选中，则该单元格的值为 True；如果未选中，则单元格的值为 False。

### **使用 Microsoft Excel**

要在工作表中放置复选框控件，请执行以下步骤：

1. 确保显示窗体工具栏。
1. 点击**复选框**窗体工具栏上的工具。
1. 在您的工作表区域中，单击并拖动以定义将容纳复选框和复选框旁边标签的矩形。
1. 放置复选框后，将鼠标光标移动到标签区域并更改标签。
1. 在里面**Cell 链接**字段，指定此复选框应链接到的单元格的地址。
1. 点击**好的**.

### **使用 Aspose.Cells**

Aspose.Cells 提供了[**复选框集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection)类，用于向集合中添加新的复选框。还有一个类，[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox)，代表一个复选框。它有一些重要的成员：

- 这[**链接单元格**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定链接到复选框的单元格。
- 这[**文本**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定与复选框关联的文本字符串。它是复选框的标签。
- 这[**价值**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value)属性指定复选框是否被选中。

以下示例显示如何向工作表添加复选框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **将单选按钮控件添加到工作表**

单选按钮或选项按钮是由圆形框组成的控件。用户通过选择圆形框来做出他或她的决定。单选按钮通常（如果不是总是）伴随其他按钮。这样的单选按钮作为一个组出现和运行。用户通过仅选择其中一个按钮来决定哪个按钮有效。当用户单击一个按钮时，它就会被填充。当组中的一个按钮被选中时，同一组按钮为空。

### **使用 Microsoft Excel**

要在工作表中放置单选按钮控件，请按照下列步骤操作：

1. 确保**形式**显示工具栏。
1. 点击**选项按钮**工具。
1. 在工作表中，单击并拖动以定义将容纳选项按钮和选项按钮旁边标签的矩形。
1. 将单选按钮放置在工作表中后，将鼠标光标移动到标签区域并更改标签。
1. 在里面**Cell 链接**字段，指定此单选按钮应链接到的单元格的地址。
1. 点击**好的**.

### **使用 Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加单选按钮**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton)，用于将单选按钮控件添加到工作表。该方法返回一个[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)目的。班级[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)代表一个选项按钮。它有一些重要的成员：

- 这[**链接单元格**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定链接到单选按钮的单元格。
- 这[**文本**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定与单选按钮关联的文本字符串。它是单选按钮的标签。
- 这[**已检查**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked)属性指定单选按钮是否被选中。
- 这[**填充格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定单选按钮的填充格式。
- 这[**行格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性指定选项按钮的行格式样式。

以下示例显示如何将单选按钮添加到工作表。该示例添加了三个代表年龄组的单选按钮。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **将组合框控件添加到工作表**

为了使数据输入更容易，或将条目限制为您定义的某些项目，您可以创建一个组合框，或从工作表其他地方的单元格编译的有效条目的下拉列表。当您为单元格创建下拉列表时，它会在该单元格旁边显示一个箭头。要在该单元格中输入信息，请单击箭头，然后单击所需的条目。

### **使用 Microsoft Excel**

要在工作表中放置组合框控件，请执行以下步骤：

1. 确保**形式**显示工具栏。
1. 点击**组合框**工具。
1. 在您的工作表区域中，单击并拖动以定义将容纳组合框的矩形。
1. 将组合框放入工作表后，右键单击控件以单击**格式控制**并指定输入范围。
1. 在里面**Cell 链接**字段，指定此组合框应链接到的单元格的地址。
1. 点击**好的**.

### **使用 Aspose.Cells**

这[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加组合框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) 用于将组合框控件添加到工作表。该方法返回一个[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)目的。班级[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)代表一个组合框。它有一些重要的成员：

- 这[**链接单元格**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定链接到组合框的单元格。
- 这[**输入范围**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange)属性指定用于填充组合框的工作表单元格范围。
- 这[**下拉线**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines)属性指定组合框下拉部分中显示的列表行数。
- 这[**阴影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow)属性指示组合框是否具有 3D 阴影。

以下示例显示如何将组合框添加到工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **向工作表添加标签控件**

标签是向用户提供有关电子表格内容的信息的一种方式。 Aspose.Cells 可以在工作表中添加和操作标签。这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加标签**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) 用于向工作表添加标签控件。该方法返回一个[**标签**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)目的。班级[**标签**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)代表工作表中的标签。它有一些重要的成员：

- 这[**文本**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)方法指定标签的标题字符串。
- 这[**放置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)方法指定[**放置类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，标签附加到工作表中的单元格的方式。

以下示例显示如何向工作表添加标签。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **将列表框控件添加到工作表**

列表框控件创建一个允许选择单个或多个项目的列表控件。

### **使用 Microsoft Excel**

要在工作表中放置列表框控件：

1. 确保**形式**显示工具栏。
1. 点击**列表框**工具。
1. 在您的工作表区域中，单击并拖动以定义将容纳列表框的矩形。
1. 将列表框放入工作表后，右键单击控件以单击**格式控制**并指定输入范围。
1. 在里面**Cell 链接**字段，指定此列表框应链接到的单元格的地址并设置选择类型（单、多、扩展）属性
1. 点击**好的**.

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加列表框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox)，用于将列表框控件添加到工作表。该方法返回一个[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox)目的。班级[**列表框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox)代表一个列表框。它有一些重要的成员：

- 这[**链接单元格**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)方法指定链接到列表框的单元格。
- 这[**输入范围**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange)方法指定用于填充列表框的工作表单元格区域。
- 这[**选择类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)method 指定列表框的选择模式。
- 这[**阴影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow)方法指示列表框是否具有 3D 阴影。

下面的示例演示如何将列表框添加到工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **将按钮控件添加到工作表**

按钮对于执行某些操作很有用。有时，将 VBA 宏分配给按钮或分配超链接以打开网页很有用。

### **使用 Microsoft Excel**

要在工作表中放置按钮控件：

1. 确保**形式**显示工具栏。
1. 点击**按钮**工具。
1. 在您的工作表区域中，单击并拖动以定义将放置按钮的矩形。
1. 将列表框放入工作表后，右键单击控件并选择**格式控制**，然后指定一个 VBA 宏和属性相关的字体、对齐方式、大小、边距等。
1. 点击**好的**.

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加按钮**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) 用于向工作表添加按钮控件。该方法返回一个[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button)目的。班级[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button)代表一个按钮。它有一些重要的成员：

- 这[**文本**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定按钮的标题。
- 这[**字体**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font)属性指定按钮控件标签的字体属性。
- 这[**放置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定[**放置类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，按钮附加到工作表中单元格的方式。
- 这[**添加超链接**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)属性为按钮控件添加超链接。单击该按钮将导航至相关 URL。

以下示例显示如何向工作表添加按钮。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **向工作表添加行控件**

### **使用 Microsoft Excel**

1. 在**画画**工具栏，单击**自选图形**， 指向**线条**然后选择所需的线条样式。
1. 拖动以绘制线条。
1. 执行以下一项或两项操作：
 1. 要限制线条以与其起点成 15 度角绘制，请在拖动时按住 SHIFT。
 1. 要从第一个端点沿相反方向延长线，请在拖动时按住 CTRL。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加行**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) 用于向工作表添加线条形状。该方法返回一个[**线型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)目的。班级[**线型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)代表一条线。它有一些重要的成员：

- 这[**行格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)方法指定一行的格式。
- 这[**放置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)方法指定[**放置类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，线条连接到工作表中的单元格的方式。

以下示例显示如何向工作表添加行。它创建了具有不同样式的三行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **向直线添加箭头**

Aspose.Cells 还允许您绘制箭头线。可以将箭头添加到一行，并格式化该行。例如，您可以更改线条的颜色，或指定线条的粗细和样式。

以下示例显示如何向线条添加箭头。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **向工作表添加矩形控件**

Aspose.Cells 允许您在工作表中绘制矩形。您可以创建一个矩形、正方形等。您还可以设置控件的填充颜色和边框线颜色的格式。例如，您可以根据需要更改矩形的颜色、设置阴影颜色、指定矩形的粗细和样式。

### **使用 Microsoft Excel**

1. 在**画画**工具栏，单击**矩形**.
1. 拖动以绘制矩形。
1. 执行以下一项或两项操作：
 1. 要限制矩形从其起点绘制正方形，请在拖动时按住 SHIFT。
 1. 要从中心点绘制矩形，请在拖动时按住 CTRL。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加矩形**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) 用于向工作表添加矩形形状。该方法返回[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)目的。班级[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)代表一个矩形。它有一些重要的成员：

- 这[**行格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) property 指定矩形的线条格式属性。
- 这[**放置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定[**放置类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，矩形附加到工作表中的单元格的方式。
- 这[**填充格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定矩形的填充格式样式。

下面的示例演示如何将矩形添加到工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **将圆弧控制添加到工作表**

Aspose.Cells 允许您在工作表中绘制弧形。您可以创建简单的填充弧。您可以设置控件的填充颜色和边框线颜色的格式。例如，您可以指定/更改圆弧的颜色、设置阴影颜色、根据需要指定形状的权重和样式。

### **使用 Microsoft Excel**

1. 在**画画**工具栏，单击**弧**在里面**自选图形**.
1. 拖动以绘制圆弧。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加圆弧**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) 用于向工作表添加弧形。该方法返回一个[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)目的。班级[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)代表弧线。它有一些重要的成员：

- 这[**行格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)属性指定弧形的线格式属性。
- 这[**放置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定[**放置类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，圆弧附加到工作表中单元格的方式。
- 这[**填充格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定形状的填充格式样式。
- 这[**右下行**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)属性指定右下角的行索引。
- 这[**右下栏**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)属性指定右下角的列索引。

以下示例显示如何将圆弧形状添加到工作表。该示例创建了两个弧形：一个是填充的，另一个是简单的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **向工作表添加椭圆形控件**

Aspose.Cells 允许您在工作表中绘制椭圆形。创建简单且填充的椭圆形并设置控件的填充颜色和边框线颜色的格式。例如，您可以指定/更改椭圆的颜色、设置阴影颜色、指定形状的权重和样式。

### **使用 Microsoft Excel**

- 在*画画*工具栏，单击*椭圆形*.
- 拖动以绘制椭圆。
- 执行以下一项或两项操作：
- 要限制椭圆从其起点绘制圆，请在拖动时按住 SHIFT。
- 要从中心点绘制椭圆，请在拖动时按住 CTRL。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加椭圆形**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) 用于向工作表添加椭圆形。该方法返回一个[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)目的。班级[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)代表一个椭圆形。它有一些重要的成员：

- 这[**行格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) property 指定椭圆形的线条格式属性。
- 这[**放置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)属性指定[**放置类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)，椭圆附加到工作表中的单元格的方式。
- 这[**填充格式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)属性指定形状的填充格式样式。
- 这[**右下行**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)属性指定右下角的行索引。
- 这[**右下栏**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)属性指定右下角的列索引。

以下示例显示如何将椭圆形添加到工作表。该示例创建了两个椭圆形：一个是实心椭圆，另一个是简单的圆形。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **将微调器控件添加到工作表**

旋转框是附加到按钮（称为旋转按钮）的文本框，按钮由向上箭头和向下箭头组成，您单击它们可以逐渐更改文本框中的值。通过使用旋转框，您可以看到财务模型的输入变化将如何改变模型输出。您可以将旋转按钮附加到特定的输入单元格。当您单击微调按钮上的向上箭头或向下箭头时，目标输入单元格中的整数值会增加或减少。*Aspose.Cells*允许您在工作表中创建微调器。

### **使用 Microsoft Excel**

要在工作表中放置旋转框控件：

- 确保*形式*显示工具栏。
- 点击*微调器*工具。
- 在您的工作表区域中，单击并拖动以定义将容纳微调器的矩形。
- 将微调器放置在工作表中后，右键单击控件并单击*格式控制*并指定最大值、最小值和增量值。
- 在里面*Cell 链接*字段，指定此旋转框应链接到的单元格的地址。
- 点击*好的*.

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加微调器**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) 用于将旋转框控件添加到工作表。该方法返回一个[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)目的。班级[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)表示旋转框。它有一些重要的成员：

- 这[**链接单元格**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定链接到旋转框的单元格。
- 这[**最大限度**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max)属性指定旋转框范围的最大值。
- 这[**最小值**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min)属性指定旋转框范围的最小值。
- 这[**增量变化**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange)属性指定微调器增加一行滚动的值量。
- 这[**阴影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow)属性指示微调框是否具有 3D 阴影。
- 这[**当前值**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue)属性指定旋转框的当前值。

以下示例显示如何向工作表添加旋转框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **将滚动条控件添加到工作表**

滚动条控件用于以类似于旋转框控件的方式帮助选择工作表上的数据。通过将控件添加到工作表并将其链接到单元格，可以返回控件当前位置的数值。

### **使用 Microsoft Excel**

- 若要在 Excel 2003 和早期版本中添加滚动条，请单击*滚动条*上的按钮*形式*工具栏，然后创建一个滚动条，其高度覆盖单元格 B2:B6，并且约为列宽的四分之一。
- 要在 Excel 2007 中添加滚动条，请单击*开发商*选项卡，单击*插入* 然后点击*滚动条*在表单控件部分。
- 右键单击滚动条，然后单击*格式控制*.
- 键入以下信息，然后单击*好的*:
 在里面*当前值*框，类型 1。
 在里面*最小值*框，键入 1。此值将滚动条的顶部限制为列表中的第一项。
 在里面*最大值*框，键入 20。此数字指定列表中的最大条目数。
 在里面*增量变化*框，键入 1。此值控制滚动条控件将当前值递增的数量。
 在里面*换页*框，键入 5。如果您在滚动框任一侧的滚动条内单击，则此条目控制当前值将增加多少。
 要将数字值放入单元格 G1（取决于列表中选择的项目），请在*Cell 链接*盒子。
- 单击任何单元格，以便不选择滚动条。

单击滚动条上的向上或向下控件时，单元格 G1 将更新为一个数字，该数字指示滚动条的当前值加上或减去滚动条的增量变化。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加滚动条**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar)，用于向工作表添加滚动条控件。该方法返回一个[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar)目的。班级[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar)代表一个滚动条。它有一些重要的成员：

- 这[**链接单元格**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)属性指定链接到滚动条的单元格。
- 这[**最大限度**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max)属性指定滚动条范围的最大值。
- 这[**最小值**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min)属性指定滚动条范围的最小值。
- 这[**增量变化**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange)属性指定滚动条增加一行滚动的值量。
- 这[**阴影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow)属性表示滚动条是否有 3D 底纹。
- 这[**当前值**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue)属性指定滚动条的当前值。
- 这[**换页**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)属性指定如果您在滚动框任一侧的滚动条内单击，当前值将增加多少。

以下示例显示如何向工作表添加滚动条。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **将 GroupBox 控件添加到工作表中的组控件**

有时您确实需要实现属于某个组的单选按钮或其他控件，您可以通过包含组框或矩形控件来实现。这两个对象中的任何一个都将作为组的分隔符。添加这些形状之一后，您可以添加两个或更多单选按钮或其他组对象。

### **使用 Microsoft Excel**

要在工作表中放置组框控件并在其中放置控件：

- 要启动表单，请在主菜单上单击*看法*， 其次是*工具栏*和*形式*.
- 在*形式*工具栏，单击*组框*并在工作表上绘制一个矩形。
- 为框键入标题字符串。
- 在*形式*工具栏，单击*选项按钮*然后点击*组框*就在标题字符串下面。
- 来自*形式*工具栏再次单击*选项按钮*然后点击*组框*在第一个单选按钮下。
- 再次上*形式*工具栏，单击*选项按钮*然后点击*组框*在上一个单选按钮下。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**添加组框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) 用于向工作表添加分组框控件。该方法返回一个[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox)目的。此外，[**团体**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group)的方法[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类对形状进行分组，需要一个[**形状**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)数组作为参数并返回一个[**组形**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape)目的。班级[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox)代表一个分组框。它有一些重要的成员：

- 这[**文本**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性指定组框的标题字符串。
- 这[**阴影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow)属性指示组框是否具有 3D 阴影。

下面的示例演示如何添加组合框并对工作表中的控件进行分组。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **推进主题**
- [使用 Aspose.Cells 添加 ActiveX 控件](/cells/zh/net/add-activex-controls-using-aspose-cells/)
- [删除 ActiveX 控件](/cells/zh/net/remove-activex-control/)
- [更新 ActiveX ComboBox 控件](/cells/zh/net/update-activex-combobox-control/)
