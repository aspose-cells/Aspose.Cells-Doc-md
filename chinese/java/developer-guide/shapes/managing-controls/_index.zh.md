---
title: 管理控件
type: docs
weight: 120
url: /zh/java/managing-controls/
---

## **介绍**

开发人员可以添加不同的绘图对象，如文本框、复选框、单选按钮、组合框、标签、按钮、直线、矩形、弧线、椭圆形、微调按钮、滚动条、分组框等。Aspose.Cells提供了包含所有绘图对象的Aspose.Cells.Drawing命名空间。然而，有一些绘图对象或形状目前尚不支持。在Microsoft Excel中的设计表格中创建这些绘图对象，然后导入到Aspose.Cells中。Aspose.Cells允许您从设计表格加载这些绘图对象，然后将它们写入生成的文件中。

## **在工作表中添加文本框控件**

在报告中强调重要信息的一种方法是使用文本框。 例如，添加文本以突出显示公司名称或指示具有最高销售额的地理区域等。 Aspose.Cells提供TextBoxes类，用于将新文本框添加到集合中。 还有另一个类[**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox)，它表示用于定义所有类型设置的文本框。 它有一些重要成员：

- [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame)方法返回一个[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame)对象，用于调整文本框的内容。
- [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement)方法指定放置类型。
- [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font)方法指定字体属性。
- [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String))方法为文本框添加超链接。
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat)属性返回[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat)对象，用于为文本框设置填充格式。
- [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat)属性返回一个[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat)对象，通常用于样式和粗细设置文本框线条。
- [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text)方法指定文本框的输入文本。

以下示例在工作簿的第一个工作表中创建了两个文本框。第一个文本框具有不同的格式设置。第二个是一个简单的文本框。

通过执行以下代码生成以下输出：

**在工作表中创建了两个文本框** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **在设计器工作表中操作文本框控件**

Aspose.Cells还允许您访问设计工作表中的文本框并对其进行操作。使用[**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes)属性获取工作表中的文本框集合。

以下示例使用我们在上面示例中创建的Microsoft Excel文件 - tsttextboxes.xls。它获取两个文本框的文本字符串并更改第二个文本框的文本以保存文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

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

Aspose.Cells提供了[**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection)类，用于向集合中添加新的复选框。还有另一个类[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox)，它代表一个复选框。它有一些重要的成员：

- [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) 方法指定与复选框关联的单元格。
- [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) 方法指定与复选框关联的文本字符串。这是复选框的标签。
- [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) 方法指定复选框是否被选中。

以下示例显示如何向工作表添加复选框。在执行代码后生成以下输出。

**在工作表中添加了一个复选框** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **在工作表中添加单选按钮控件**

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供一个名为addShape的方法，可以用于向工作表中添加单选按钮控件。该方法可能返回RadioButton对象。RadioButton类表示选项按钮。它有一些重要成员：

- setLinkedCell方法指定与单选按钮关联的单元格。
- setText方法指定与单选按钮关联的文本字符串。这是单选按钮的标签。
- Checked属性指定单选按钮是否被选中。
- setFillFormat方法指定单选按钮的填充格式。
- setLineFormat方法指定选项按钮的线条格式样式。

以下示例显示如何向工作表添加单选按钮。示例添加了三个代表年龄组的单选按钮。在执行代码后将生成以下输出。

**在工作表中添加了一些单选按钮** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供一个名为addShape的方法，可用于向工作表中添加组合框控件。该方法可能返回ComboBox对象。ComboBox类表示组合框。它有一些重要成员：

- setLinkedCell方法指定与组合框关联的单元格。
- setInputRange方法指定用于填充组合框的工作表范围。
- setDropDownLines方法指定在组合框下拉部分中显示的列表行数。
- setShadow方法指示组合框是否具有3D阴影。

以下示例显示如何向工作表添加组合框。在执行代码时将会生成以下输出。

**在工作表中添加了一个组合框** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **向工作表添加标签控件**

标签是向用户提供有关电子表格内容的信息的一种方式。Aspose.Cells使得在工作表中添加和操作标签成为可能。[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供一个名为addShape的方法，用于向工作表中添加标签控件。该方法返回一个Label对象。Label类表示工作表中的标签。它有一些重要成员：

- setText方法指定标签的标题字符串。
- setPlacement方法指定PlacementType，即标签附加到工作表中的单元格的方式。

以下示例显示如何向工作表添加标签。在执行代码时将会生成以下输出。

**工作表中添加了一个标签**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供了一个名为 addShape 的方法，用于在工作表中添加一个列表框控件。该方法返回一个 ListBox 对象。ListBox 类表示一个列表框。它有一些重要的成员：

- setLinkedCell 方法指定与列表框关联的单元格。
- setInputRange 方法指定用于填充列表框的工作表区域。
- setSelectionType 方法指定列表框的选择模式。
- setShadow 方法指示列表框是否具有 3D 阴影。

以下示例演示如何向工作表添加一个列表框。执行代码后生成以下输出。

**工作表中添加了一个列表框** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供了一个名为 addShape 的方法，用于在工作表中添加一个按钮控件。该方法可能返回一个 Button 对象。Button 类表示一个按钮。它有一些重要的成员：

- setText 方法指定按钮的标题。
- setPlacement 方法指定按钮在工作表中与单元格的附着方式。
- addHyperlink 方法为按钮控件添加超链接。单击按钮将导航到相关的 URL。

以下示例演示如何向工作表添加一个按钮。执行代码后生成以下输出。

**工作表中添加了一个按钮**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **向工作表添加线条控件**

Aspose.Cells 允许您在工作表中绘制自动形状。您可以轻松创建一条线。您还可以对线条进行格式设置。例如，您可以更改线条的颜色，指定线条的粗细和样式，以满足您的需求。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**自选图形**，指向**线条**，选择要使用的线条样式。
1. 拖动以绘制线条。
1. 进行以下操作中的一项或两项：
   1. 若要约束线条在与其起始点成15度角的方向上绘制，请按住SHIFT并拖动。
   1. 若要从第一端点向相反方向拉长线段，请按住CTRL并拖动。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供了一个名为 addShape 的方法，用于在工作表中添加一条线条形状。该方法可能返回一个 LineShape 对象。LineShape 类表示一条线条。它有一些重要的成员：

- setDashStyle 方法指定线条的格式。
- setPlacement 方法指定线条在工作表中与单元格的附着方式。

以下示例演示如何向工作表添加线条。它创建了三条具有不同样式的线条。执行代码后生成以下输出。

**工作表中添加了几条线条** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **向线条添加箭头**

Aspose.Cells还允许您绘制箭头线。可以向线条添加箭头头部，并格式化线条。例如，可以更改线条的颜色，或指定线条的粗细和样式。

以下示例演示如何向一条线条添加一个箭头。执行代码后生成以下输出。

**工作表中添加了一条带箭头的线条** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **向工作表添加矩形控件**

Aspose.Cells允许您在工作表中绘制矩形形状。您可以创建矩形、正方形等形状。您也可以自定义控件的填充颜色和边界线颜色。例如，您可以更改矩形的颜色、设置阴影颜色、指定矩形的粗细和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在“绘图”工具栏中，单击“矩形”。
1. 拖动以绘制矩形。
1. 进行以下操作中的一项或两项：
   1. 从起始点开始，按住SHIFT以约束矩形绘制正方形。
   1. 按住CTRL并拖动以从中心点绘制矩形。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供了一个名为 addShape 的方法，用于在工作表中添加一个矩形形状。该方法可以返回一个 RectangleShape 对象。RectangleShape 类表示一个矩形。它有一些重要的成员：

- setLineFormat 方法指定矩形的线条格式属性。
- setPlacement 方法指定矩形在工作表中与单元格的附着方式。
- FillFormat 属性指定矩形的填充格式样式。

以下示例演示如何向工作表添加一个矩形。执行代码后生成以下输出。

**工作表中添加了一个矩形** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **向工作表添加弧控件**

Aspose.Cells允许您在工作表中绘制弧形状。您可以创建简单的填充弧。您可以自定义控件的填充颜色和边界线颜色。例如，您可以指定/更改弧形的颜色、设置阴影颜色、指定形状的粗细和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在“绘图”工具栏中，单击“自选图形”中的“弧”。
1. 拖动以绘制弧。

### **使用Aspose.Cells**

类 [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 提供了一个名为 addShape 的方法，用于向工作表中添加弧形。该方法可以返回 ArcShape 对象。ArcShape 类表示弧形，它具有一些重要的成员：

- setLineFormat 方法指定弧形的线条格式属性。
- setPlacement 方法指定 PlacementType，即弧形附加到工作表中单元格的方式。
- FillFormat 属性指定形状的填充格式样式。

以下示例显示了如何向工作表添加弧形。该示例创建了两个弧形：一个填充，另一个简单。执行代码后生成了以下输出。

**向工作表添加了两个弧形** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **向工作表添加椭圆形控件**

Aspose.Cells允许您在工作表中绘制椭圆形状。创建简单的和填充的椭圆形状，并自定义控件的填充颜色和边界线颜色。例如，您可以指定/更改椭圆的颜色、设置阴影颜色、指定形状的粗细和样式。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**椭圆**。
1. 拖动以绘制椭圆。
1. 进行以下操作中的一项或两项：
   1. 若要限制椭圆从其起点绘制成圆形，按住 SHIFT 键拖动。
   1. 要从中心点绘制椭圆，按住 CTRL 键拖动。

### **使用Aspose.Cells**

类 [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 提供了一个名为 addShape 的方法，用于向工作表中添加椭圆形。该方法可能返回 Oval 对象。Oval 类表示椭圆形状，它具有一些重要的成员：

- setLineFormat 方法指定椭圆形的线条格式属性。
- setPlacement 方法指定**PlacementType**，即椭圆附加到工作表中单元格的方式。
- FillFormat 属性指定形状的填充格式样式。

以下示例显示了如何向工作表添加椭圆形。该示例创建了两个椭圆形：一个为填充椭圆，另一个为简单圆形。执行代码后生成了以下输出。

**工作表中添加了两个椭圆形** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **高级主题**
- [使用Aspose.Cells添加ActiveX控件](/cells/zh/java/add-activex-controls-using-aspose-cells/)
- [移除ActiveX控件](/cells/zh/java/remove-activex-control/)
