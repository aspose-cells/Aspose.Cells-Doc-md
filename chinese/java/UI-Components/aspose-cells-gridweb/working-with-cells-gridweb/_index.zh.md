---
title: 与Cells GridWeb工作
type: docs
weight: 50
url: /zh/java/working-with-cells-gridweb/
---

## **访问工作表中的单元格**
本主题讨论了单元格，查看GridWeb的最基本功能：访问单元格。

每个工作表都包含一个GridCells对象，一个GridCell对象的集合。GridCell对象代表Aspose.Cells.GridWeb中的单元格。可以使用GridWeb访问任何单元格。有两种首选方法：

- [通过名称访问单元格](/cells/zh/java/working-with-cells-gridweb/)。
- [通过行和列索引访问单元格](/cells/zh/java/working-with-cells-gridweb/)。

下面讨论了每种方法。
### **使用单元格名称**
所有单元格都有唯一的名称。例如，A1、A2、B1、B2等。Aspose.Cells.GridWeb允许开发人员通过使用单元格名称来访问任何所需的单元格。只需将单元格名称（作为索引）传递给GridWorksheet的GridCells集合即可。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **使用行和列索引**
单元格也可以通过其行和列索引的位置来识别。只需将单元格的行和列索引传递给GridWorksheet的GridCells集合即可。这种方法比上面的方法更快。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **访问和修改单元格的值**
[访问工作表中的单元格](/cells/zh/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet)讨论了访问单元格。本主题将扩展该讨论，展示如何使用GridWeb API来访问和修改单元格值。
### **访问和修改单元格的值**
#### **字符串值**
在访问和修改单元格的值之前，需要知道如何访问单元格。有关访问单元格的不同方法的详细信息，请参阅[访问工作表中的单元格](/cells/zh/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet)。

每个单元格都有一个名为getStringValue()的属性。一旦访问一个单元格，开发人员可以访问getStringValue()方法来访问单元格的字符串值。

{{% alert color="primary" %}} 

重要提示：单元格中可以存储五种类型的值（布尔值、整数、双精度、日期时间和字符串），但getValue()/setValue()方法只能用于访问/修改对象值。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **所有类型的值**
Aspose.Cells.GridWeb还为每个单元格提供了一个特殊的方法putValue。使用该方法，可以在单元格中插入或修改任何类型的值（布尔、整数、双精度、日期时间和字符串）。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



putValue方法还有一个重载版本，可以接受以字符串格式表示的任何类型的值，并自动将其转换为适当的数据类型。要实现这一点，将Boolean值true传递给putValue方法的另一个参数，如下例所示。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **向单元格添加公式**
Aspose.Cells.GridWeb提供的最有价值的功能是支持公式或函数。 Aspose.Cells.GridWeb拥有自己的公式引擎，用于计算工作表中的公式。 Aspose.Cells.GridWeb支持内置和用户定义的函数或公式。 本主题详细讨论了使用Aspose.Cells.GridWeb API向单元格添加公式。
### **如何添加和计算公式？**
可以通过使用单元格的公式属性向单元格中添加、访问和修改公式。Aspose.Cells.GridWeb支持简单到复杂的用户定义公式。然而，Aspose.Cells.GridWeb还提供了大量的内置函数或公式（类似于Microsoft Excel）。要查看完整的内置函数列表，请参考这个[支持的功能列表。](/cells/zh/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

公式语法应与Microsoft Excel语法兼容。例如，所有公式必须以等号（=）开头。

要以编程方式添加公式，Aspose.Cells.GridWeb将识别它为公式，即使您不使用**=**符号，但在GUI中工作的最终用户必须使用它。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**向B3单元格添加但未由GridWeb计算的公式** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

在上述屏幕截图中，您可以看到已向B3添加了一个公式，但尚未计算。要计算所有公式，请在向工作表添加公式之后调用GridWeb控件的GridWorksheetCollection的calculateFormula方法，如下所示。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

用户还可以通过单击**提交**来计算公式。

**单击GridWeb的提交按钮** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**重要**：如果用户单击**保存** 或 **撤销** 按钮，或者工作表选项卡，GridWeb会自动计算所有公式。

**计算后的公式结果** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **其他工作表中引用单元格**
使用Aspose.Cells.GridWeb，可以在公式中引用存储在不同工作表中的值，创建复杂的公式。

从不同工作表引用单元格值的语法是工作表名称！单元格名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **在GridWeb的GridCell中创建数据验证**
Aspose.Cells.GridWeb允许您使用GridWorksheet.getValidations().add()方法添加**数据验证**。使用此方法，您必须指定**单元格范围**。但是，如果要在单个GridCell中创建数据验证，则可以直接使用GridCell.createValidation()方法。类似地，您可以使用GridCell.removeValidation()方法从GridCell中删除**数据验证**。

以下示例代码在单元格B3中创建了一个**数据验证**。 如果您输入任何不在20和40之间的值，单元格B3将以**红色XXXX**形式显示**验证错误**，如此截屏所示。

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **创建自定义命令按钮**
Aspose.Cells.GridWeb包含特殊按钮，如提交、保存和撤销。所有这些按钮为Aspose.Cells.GridWeb执行特定任务。还可以添加执行自定义任务的自定义按钮。本主题解释了如何使用此功能。

以下示例代码解释了如何创建自定义命令按钮以及如何处理其单击事件。您可以为自定义命令按钮使用任何图标。为了说明目的，我们使用了此图像图标。

![todo:image_alt_text](working-with-cells-gridweb_5.png)

如您在以下屏幕截图中所见，用户单击自定义命令按钮时，将在单元格A1中添加一条消息**“我的自定义命令按钮已被点击。”**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **自定义命令按钮的事件处理**
以下示例代码解释了如何执行自定义命令按钮的事件处理。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **为GridWeb格式化单元格**
### **可能的使用场景**
GridWeb现在支持用户以百分比格式输入单元格数据，如3%，单元格中的数据将自动格式化为3.00%。但是，您必须将单元格样式设置为百分比格式，即GridTableItemStyle.NumberType为9或10。数字9将3%格式化为3%，但数字10将3%格式化为3.00%。

{{% alert color="primary" %}} 

如果未将单元格样式设置为百分比格式，则输入数据3%将显示为0.03。

{{% /alert %}} 
### **以百分比格式输入GridWeb工作表的单元格数据**
以下示例代码将单元格A1 GridTableItemStyle.NumberType设为10，因此输入的数据3%将自动格式化为3.00%，如屏幕截图所示。

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
