---
title: 控件管理
type: docs
weight: 120
url: /zh/java/managing-controls/
---

## **介绍**

开发人员可以添加不同的绘图对象，如文本框、复选框、单选按钮、组合框、标签、按钮、直线、矩形、弧线、椭圆、微调控件、滚动条、分组框等。Aspose.Cells 提供了 Aspose.Cells.Drawing 命名空间，其中包含所有的绘图对象。但是，目前还不支持一些绘图对象或形状。可以在 Microsoft Excel 中创建这些绘图对象，并将设计好的电子表格导入到 Aspose.Cells 中。Aspose.Cells 允许从设计好的电子表格加载这些绘图对象，然后将它们写入生成的文件中。

## **向工作表添加文本框控件**

在报告中强调重要信息的一种方式是使用文本框。例如，添加文本以突出公司名称或指示销售额最高的地理区域等。Aspose.Cells 提供了 TextBoxes 类，用于向集合中添加新的文本框。还有另一个类，[**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox)，表示用于定义各种设置的文本框。它具有一些重要成员：

- [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) 方法返回用于调整文本框内容的 [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) 对象。
- [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) 方法指定放置类型。
- [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) 方法指定字体属性。
- [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) 方法为文本框添加超链接。
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) 属性返回用于设置文本框填充格式的 [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) 对象。
- [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) 属性返回用于设置文本框线条样式和粗细的 [**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) 对象。
- [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) 方法指定文本框的输入文本。

以下示例在工作簿的第一个工作表中创建了两个文本框。第一个文本框配有不同的格式设置。第二个是一个简单的文本框。

执行代码后生成以下输出：

**在工作表中创建了两个文本框** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **在设计器电子表格中操作文本框控件**

Aspose.Cells还允许您访问设计器工作表中的文本框并对其进行操作。使用[**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes)属性获取工作表中的文本框集合。

下面的例子使用我们在上面的例子中创建的Microsoft Excel文件 - tsttextboxes.xls。它获取两个文本框的文本字符串并更改第二个文本框的文本以保存文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **向工作表添加复选框控件**

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

Aspose.Cells提供了[**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection)类，用于添加新的复选框到集合中。还有另一个类[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox)，代表一个复选框。它具有一些重要成员：

- 方法[**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell)指定与复选框关联的单元格。
- 方法[**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text)指定与复选框关联的文本字符串。这是复选框的标签。
- 方法[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value)指定复选框是否被选择。

下面的例子显示了如何向工作表中添加复选框。执行代码后生成下面的输出。

**在工作表中添加了一个复选框** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 类提供了一个名为 addShape 的方法，可以用来向工作表添加单选按钮控件。该方法可能会返回一个 RadioButton 对象。RadioButton 类表示一个选项按钮。它具有一些重要成员：

- setLinkedCell 方法指定与单选按钮关联的单元格。
- setText 方法指定与单选按钮关联的文本字符串。它是单选按钮的标签。
- Checked 属性指定单选按钮是否被选中。
- setFillFormat 方法指定单选按钮的填充格式。
- setLineFormat 方法指定选项按钮的线条格式样式。

下面的示例显示了如何向工作表添加单选按钮。该示例添加了代表年龄组的三个单选按钮。在执行代码后，将生成以下输出。

**工作表中添加了一些单选按钮** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape的方法，该方法可用于向工作表添加组合框控件。该方法可以返回ComboBox对象。类ComboBox表示组合框，它有一些重要成员:

- setLinkedCell方法指定与组合框链接的单元格。
- setInputRange方法指定用于填充组合框的工作表单元范围。
- setDropDownLines方法指定下拉式组合框部分显示的列表行数。
- setShadow方法指示组合框是否具有3D阴影。

以下示例显示了如何向工作表添加组合框。执行代码时生成以下输出。

**在工作表中添加了一个组合框** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **将标签控件添加到工作表**

标签是向用户提供有关电子表格内容的信息的一种方式。Aspose.Cells使得可以在工作表中添加和操作标签。[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape的方法，用于在工作表中添加标签控件。该方法返回一个Label对象。类Label表示工作表中的标签，它有一些重要成员:

- setText方法指定标签的标题字符串。
- setPlacement方法指定PlacementType，即标签连接到工作表中的单元格的方式。

以下示例显示了如何向工作表添加一个标签。执行代码时生成以下输出。

**在工作表中添加了一个标签**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供一个名为addShape的方法，用于向工作表中添加列表框控件。该方法返回一个ListBox对象。ListBox类表示一个列表框。它有一些重要的成员：

- setLinkedCell方法指定与列表框链接的单元格。
- setInputRange方法指定用于填充列表框的工作表单元格范围。
- setSelectionType方法指定列表框的选择模式。
- setShadow方法指示列表框是否具有3D阴影。

以下示例显示了如何向工作表中添加列表框。执行代码时生成以下输出。

**在工作表中添加了一个列表框** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

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

类 [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 提供了一个名为 addShape 的方法，用于将按钮控件添加到工作表中。该方法可能会返回一个 Button 对象。Button 类代表一个按钮。它有一些重要的成员：

- setText 方法指定按钮的标题。
- setPlacement 方法指定了 PlacementType，即按钮附加到工作表单元格的方式。
- addHyperlink 方法为按钮控件添加超链接。单击按钮将导航到相关的 URL。

下面的示例显示了如何向工作表中添加一个按钮。在执行代码时生成以下输出

**在工作表中添加了一个按钮**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **向工作表添加线控件**

Aspose.Cells 允许您在工作表中绘制自选图形。您可以轻松地创建一条线，并允许您格式化该线。例如，您可以更改线的颜色、指定线的粗细和样式。

### **使用Microsoft Excel**

1. 在 **绘图** 工具栏上，单击 **自选图形**，指向 **线条**，然后选择所需的线条样式。
1. 拖动以绘制线条。
1. 执行以下操作中的一个或两个：
   1. 要限制线条以与起点呈15度角的方式绘制，请在拖动时按住 SHIFT 键。
   1. 要使线条从第一个端点向相反方向延伸，请在拖动时按住 CTRL 键。

### **使用Aspose.Cells**

类 [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) 提供了一个名为 addShape 的方法，用于向工作表中添加一条线形状。该方法可能会返回一个 LineShape 对象。LineShape 类代表一条线。它有一些重要的成员：

- setDashStyle 方法指定了线条的格式。
- setPlacement 方法指定了 PlacementType，即线条附加到工作表单元格的方式。

下面的示例显示了如何向工作表中添加线条。它创建了三条不同样式的线。在执行代码后生成以下输出

**工作表中添加了几条线** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **向一条线条中添加箭头**

Aspose.Cells 还允许您绘制箭头线条。您可以向一条线条添加箭头，并格式化该线。例如，您可以更改线条的颜色，或指定线条的粗细和样式。

下面的示例显示了如何向一条线添加箭头。在执行代码时生成以下输出。

**在工作表中添加了带箭头的直线** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **在工作表中添加矩形控件**

Aspose.Cells允许您在工作表中绘制矩形形状。您可以创建矩形、正方形等形状，还可以格式化控件的填充颜色和边框线颜色。例如，您可以更改矩形的颜色，设置阴影颜色，指定矩形的重量和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**矩形**。
1. 拖动绘制矩形。
1. 执行以下操作中的一个或两个：
   1. 若要从起点绘制正方形并约束矩形，请按住SHIFT键并拖动。
   1. 若要从中心点绘制矩形，请按住CTRL键并拖动。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape的方法，用于向工作表添加矩形形状。该方法可以返回一个RectangleShape对象。RectangleShape类表示矩形形状。它具有一些重要成员：

- setLineFormat方法指定矩形的线条格式属性。
- setPlacement方法指定PlacementType，即矩形附加到工作表单元格的方式。
- FillFormat属性指定矩形的填充格式样式。

以下示例展示了如何向工作表添加矩形。执行代码时会生成以下输出。

**工作表中添加了一个矩形** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **向工作表添加弧形控件**

Aspose.Cells允许您在工作表中绘制弧形。您可以创建简单的填充弧形。您可以格式化控件的填充颜色和边框线颜色。例如，您可以指定/更改弧形的颜色，设置阴影颜色，指定形状的重量和样式以满足您的需求。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**AutoShapes**中的**弧形**。
1. 拖动绘制弧形。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape的方法，用于向工作表添加弧形。该方法可以返回一个ArcShape对象。ArcShape类表示弧形。它具有一些重要成员：

- setLineFormat方法指定弧形形状的线条格式属性。
- setPlacement方法指定PlacementType，弧形附加到工作表单元格的方式。
- FillFormat属性指定了形状的填充格式样式。

以下示例展示了如何向工作表添加弧形。示例创建了两个弧形：一个是填充的，另一个是简单的。执行代码时会生成以下输出。

**工作表中添加了两个弧形** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **向工作表添加椭圆控件**

Aspose.Cells允许您在工作表中绘制椭圆形状。创建简单和填充的椭圆形状，并格式化控件的填充颜色和边框线颜色。例如，您可以指定/更改椭圆的颜色，设置阴影颜色，指定形状的宽度和样式。

### **使用Microsoft Excel**

1. 在**绘图**工具栏上，单击**椭圆**。
1. 拖动以绘制椭圆。
1. 执行以下操作中的一个或两个：
   1. 要将椭圆约束为从其起始点绘制圆，请在拖动时按住SHIFT。
   1. 要从中心点绘制椭圆，请在拖动时按住CTRL。

### **使用Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)类提供了一个名为addShape的方法，用于向工作表添加椭圆形状。该方法可能返回一个椭圆对象。椭圆类表示椭圆形状。它具有一些重要成员：

- setLineFormat方法指定椭圆形状的线格式属性。
- setPlacement方法指定了**PlacementType**，即椭圆附加到工作表中的单元格的方式。
- FillFormat属性指定了形状的填充格式样式。

以下示例显示如何向工作表添加椭圆形状。该示例创建了两个椭圆形状：一个是填充的椭圆，另一个是简单的圆。执行代码时生成以下输出。

**工作表中添加了两个椭圆形状** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **高级主题**
- [使用Aspose.Cells添加ActiveX控件](/cells/zh/java/add-activex-controls-using-aspose-cells/)
- [移除ActiveX控件](/cells/zh/java/remove-activex-control/)
