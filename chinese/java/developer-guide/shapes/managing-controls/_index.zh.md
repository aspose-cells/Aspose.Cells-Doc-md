---
title: 管理控制
type: docs
weight: 120
url: /zh/java/managing-controls/
---
## **介绍**

开发人员可以添加不同的绘图对象，例如文本框、复选框、单选按钮、组合框、标签、按钮、线条、矩形、圆弧、椭圆、旋转器、滚动条、组框等。Aspose.Cells 提供 Aspose.Cells.Drawing 命名空间，其中包含所有绘图对象。但是，尚不支持一些绘图对象或形状。使用 Microsoft Excel 在设计器电子表格中创建这些绘图对象，然后将设计器电子表格导入 Aspose.Cells。Aspose.Cells 允许您从设计器电子表格加载这些绘图对象并将它们写入生成的文件。

## **将 TextBox 控件添加到工作表**

在报告中强调重要信息的一种方法是使用文本框。例如，添加文本以突出显示公司名称或指示销售额最高的地理区域等。 Aspose.Cells 提供了 TextBoxes 类，用于向集合中添加新的文本框。还有一个类，[**文本框**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), 表示用于定义所有类型设置的文本框。它有一些重要的成员：

- 这[**获取文本框**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame)方法返回一个[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame)用于调整文本框内容的对象。
- 这[**设置位置**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement)方法指定放置类型。
- 这[**设置字体**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font)方法指定字体属性。
- 这[**添加超链接**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)方法为文本框添加超链接。
- 这[**填充格式**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat)财产回报[**MsoFill格式**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat)用于设置文本框填充格式的对象。
- 这[**行格式**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat)属性返回[**MsoLine格式**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat)对象通常用于文本框线的样式和粗细。
- 这[**设置文本**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text)方法指定文本框的输入文本。

下面的示例在工作簿的第一个工作表中创建两个文本框。第一个文本框配备了不同的格式设置。第二个是简单的。

通过执行代码生成以下输出：

**在工作表中创建了两个文本框** 

![待办事项：图像_替代_文本](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **在 Designer 电子表格中操作文本框控件**

Aspose.Cells 还允许您访问设计器工作表中的文本框并对其进行操作。使用[**工作表.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes)属性以获取工作表中的文本框集合。

以下示例使用我们在上例中创建的 Microsoft Excel 文件 – tsttextboxes.xls。它获取两个文本框的文本字符串并更改第二个文本框的文本以保存文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **将 CheckBox 控件添加到工作表**

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

Aspose.Cells 提供了[**复选框集合**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection)类，用于向集合中添加新的复选框。还有一个类，[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox)，代表一个复选框。它有一些重要的成员：

- 这[**设置链接单元格**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell)方法指定链接到复选框的单元格。
- 这[**设置文本**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text)方法指定与复选框关联的文本字符串。它是复选框的标签。
- 这[**设定值**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value)方法指定复选框是否被选中。

以下示例显示如何向工作表添加复选框。下面的输出是在执行代码后生成的。

**工作表中添加了一个 CheckBox** 

![待办事项：图像_替代_文本](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **将 RadioButton 控件添加到工作表**

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

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为 addShape 的方法，可用于将单选按钮控件添加到工作表。该方法可能会返回一个 RadioButton 对象。 RadioButton 类表示一个选项按钮。它有一些重要的成员：

- setLinkedCell 方法指定链接到单选按钮的单元格。
- setText 方法指定与单选按钮关联的文本字符串。它是单选按钮的标签。
- Checked 属性指定单选按钮是否被选中。
- setFillFormat 方法指定单选按钮的填充格式。
- setLineFormat 方法指定选项按钮的行格式样式。

以下示例显示如何将单选按钮添加到工作表。该示例添加了三个代表年龄组的单选按钮。执行代码后将生成以下输出。

**工作表中添加了一些单选按钮** 

![待办事项：图像_替代_文本](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为 addShape 的方法，可用于将组合框控件添加到工作表中。该方法可以返回 ComboBox 对象。 ComboBox 类代表一个组合框。它有一些重要的成员：

- setLinkedCell 方法指定链接到组合框的单元格。
- setInputRange 方法指定用于填充组合框的工作表单元格范围。
- setDropDownLines 方法指定组合框下拉部分中显示的列表行数。
- setShadow 方法指示组合框是否具有 3D 阴影。

以下示例显示如何将组合框添加到工作表。执行代码时会生成以下输出。

**工作表中添加了一个组合框** 

![待办事项：图像_替代_文本](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **向工作表添加标签控件**

标签是向用户提供有关电子表格内容的信息的一种方式。 Aspose.Cells 可以在工作表中添加和操作标签。这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape 的方法，用于向工作表添加标签控件。该方法返回一个标签对象。 Label 类表示工作表中的标签。它有一些重要的成员：

- setText 方法指定标签的标题字符串。
- setPlacement 方法指定 PlacementType，即标签附加到工作表中单元格的方式。

以下示例显示如何向工作表添加标签。执行代码时会生成以下输出。

**工作表中添加了标签**

![待办事项：图像_替代_文本](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为 addShape 的方法，用于将列表框控件添加到工作表中。该方法返回一个 ListBox 对象。类 ListBox 代表一个列表框。它有一些重要的成员：

- setLinkedCell 方法指定链接到列表框的单元格。
- setInputRange 方法指定用于填充列表框的工作表单元格范围。
- setSelectionType 方法指定列表框的选择模式。
- setShadow 方法指示列表框是否具有 3D 阴影。

下面的示例演示如何将列表框添加到工作表。执行代码时会生成以下输出。

**工作表中添加了一个列表框** 

![待办事项：图像_替代_文本](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

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

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape 的方法，用于向工作表中添加一个按钮控件。该方法可能会返回一个 Button 对象。 Button 类代表一个按钮。它有一些重要的成员：

- setText 方法指定按钮的标题。
- setPlacement 方法指定 PlacementType，即按钮附加到工作表中单元格的方式。
- addHyperlink 方法为按钮控件添加超链接。单击该按钮将导航至相关 URL。

以下示例显示如何向工作表添加按钮。执行代码时产生如下输出

**工作表中添加了一个按钮**

![待办事项：图像_替代_文本](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **向工作表添加线条控件**

Aspose.Cells 允许您在工作表中绘制自选图形。您可以轻松创建一条线。您还可以格式化该行。例如，您可以更改线条的颜色，根据需要指定线条的粗细和样式。

### **使用 Microsoft Excel**

1. 在**绘画**工具栏，单击**自选图形**， 指向**线条**然后选择所需的线条样式。
1. 拖动以绘制线条。
1. 执行以下一项或两项操作：
 1. 要限制线条以与其起点成 15 度角绘制，请在拖动时按住 SHIFT。
 1. 要从第一个端点沿相反方向延长线，请在拖动时按住 CTRL。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为 addShape 的方法，用于向工作表添加线条形状。该方法可能会返回一个 LineShape 对象。 LineShape 类表示一条线。它有一些重要的成员：

- setDashStyle 方法指定行的格式。
- setPlacement 方法指定 PlacementType，即线条附加到工作表中的单元格的方式。

以下示例显示如何向工作表添加行。它创建了具有不同样式的三行。执行代码后生成如下输出

**在工作表中添加几行** 

![待办事项：图像_替代_文本](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **向直线添加箭头**

Aspose.Cells 还允许您绘制箭头线。可以将箭头添加到一行，并格式化该行。例如，您可以更改线条的颜色，或指定线条的粗细和样式。

以下示例显示如何向线条添加箭头。执行代码时会生成以下输出。

**工作表中添加了带箭头的线** 

![待办事项：图像_替代_文本](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **向工作表添加矩形控件**

Aspose.Cells 允许您在工作表中绘制矩形。您可以创建一个矩形、正方形等。您还可以设置控件的填充颜色和边框线颜色的格式。例如，您可以根据需要更改矩形的颜色、设置阴影颜色、指定矩形的粗细和样式。

### **使用 Microsoft Excel**

1. 在**绘画**工具栏，单击**长方形**.
1. 拖动以绘制矩形。
1. 执行以下一项或两项操作：
 1. 要限制矩形从其起点绘制正方形，请在拖动时按住 SHIFT。
 1. 要从中心点绘制矩形，请在拖动时按住 CTRL。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为 addShape 的方法，用于向工作表中添加一个矩形形状。该方法可以返回一个 RectangleShape 对象。 RectangleShape 类代表一个矩形。它有一些重要的成员：

- setLineFormat 方法指定矩形的线条格式属性。
- setPlacement 方法指定 PlacementType，即矩形附加到工作表中单元格的方式。
- FillFormat 属性指定矩形的填充格式样式。

下面的示例演示如何将矩形添加到工作表。执行代码时会生成以下输出。

**工作表中添加了一个矩形** 

![待办事项：图像_替代_文本](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **将圆弧控制添加到工作表**

Aspose.Cells 允许您在工作表中绘制弧形。您可以创建简单的填充弧。您可以设置控件的填充颜色和边框线颜色的格式。例如，您可以指定/更改圆弧的颜色、设置阴影颜色、根据需要指定形状的权重和样式。

### **使用 Microsoft Excel**

1. 在**绘画**工具栏，单击**弧**在里面**自选图形**.
1. 拖动以绘制圆弧。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape的方法，用于在工作表中添加一个圆弧形状。该方法可以返回 ArcShape 对象。 ArcShape 类表示弧。它有一些重要的成员：

- setLineFormat 方法指定弧形的线条格式属性。
- setPlacement 方法指定 PlacementType，即弧附加到工作表中单元格的方式。
- FillFormat 属性指定形状的填充格式样式。

以下示例显示如何将圆弧形状添加到工作表。该示例创建了两个弧形：一个是填充的，另一个是简单的。执行代码时产生如下输出

**工作表中添加了两个弧形** 

![待办事项：图像_替代_文本](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **向工作表添加椭圆形控件**

Aspose.Cells 允许您在工作表中绘制椭圆形。创建简单且填充的椭圆形并设置控件的填充颜色和边框线颜色的格式。例如，您可以指定/更改椭圆的颜色、设置阴影颜色、指定形状的权重和样式。

### **使用 Microsoft Excel**

1. 在**绘画**工具栏，单击**椭圆形** .
1. 拖动以绘制椭圆。
1. 执行以下一项或两项操作：
 1. 要限制椭圆从其起点绘制圆，请在拖动时按住 SHIFT。
1. 要从中心点绘制椭圆，请在拖动时按住 CTRL。

### **使用 Aspose.Cells**

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为 addShape 的方法，用于向工作表添加椭圆形。该方法可能会返回一个 Oval 对象。 Oval 类表示椭圆形。它有一些重要的成员：

- setLineFormat 方法指定椭圆形的线条格式属性。
-  setPlacement 方法指定**放置类型**，椭圆附加到工作表中的单元格的方式。
- FillFormat 属性指定形状的填充格式样式。

以下示例显示如何将椭圆形添加到工作表。该示例创建了两个椭圆形：一个是实心椭圆，另一个是简单的圆形。执行代码时会生成以下输出。

**工作表中添加了两个椭圆形** 

![待办事项：图像_替代_文本](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **推进主题**
- [使用 Aspose.Cells 添加 ActiveX 控件](/cells/zh/java/add-activex-controls-using-aspose-cells/)
- [删除 ActiveX 控件](/cells/zh/java/remove-activex-control/)
