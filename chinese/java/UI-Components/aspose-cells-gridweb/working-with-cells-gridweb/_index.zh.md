---
title: 与GridWeb中的单元格一起工作
type: docs
weight: 50
url: /zh/java/working-with-cells-gridweb/
---

## **访问工作表中的单元格**
此主题讨论单元格，查看GridWeb的最基本功能：访问单元格。

每个工作表包含 GridCells 对象，即 GridCell 对象的集合。GridCell 对象代表 Aspose.Cells.GridWeb 中的一个单元格。可以使用 GridWeb 访问任何单元格。有两种首选方法：

- [按名称访问单元格](/cells/zh/java/working-with-cells-gridweb/)
- [按行和列索引访问单元格](/cells/zh/java/working-with-cells-gridweb/)

下面讨论了每种方法。
### **使用单元格名称**
所有单元格都有唯一的名称。例如，A1、A2、B1、B2 等。Aspose.Cells.GridWeb 允许开发人员使用单元格名称访问任何所需的单元格。只需将单元格名（作为索引）传递给 GridCells 集合的 GridWorksheet。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **使用行和列索引**
也可以通过行和列索引的位置来识别单元格。只需将单元格的行和列索引传递给 GridCells 集合的 GridWorksheet。这种方法比上面的方法更快。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **访问和修改单元格的值**
[访问工作表中的单元格](/cells/zh/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) 中讨论了访问单元格。本主题将扩展该讨论，以显示如何使用 GridWeb API 访问和修改单元格的值。
### **访问和修改单元格的值**
#### **字符串值**
在访问和修改单元格的值之前，需要知道如何访问单元格。有关访问单元格的不同方法的详细信息，请参阅[访问工作表中的单元格](/cells/zh/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet)。

每个单元格都有一个名为 getStringValue() 的属性。一旦访问了单元格，开发人员可以访问 getStringValue() 方法以访问单元格的字符串值。

{{% alert color="primary" %}} 

重要提示：单元格中可以存储五种类型的值（布尔值、整数、双精度浮点数、日期时间和字符串），但 getValue()/setValue() 方法仅用于访问/修改对象的值。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **所有类型的值**
Aspose.Cells.GridWeb 还为每个单元格提供了一个特殊的方法 putValue。使用该方法可以在单元格中插入或修改任何类型的值（布尔值、整数、双精度浮点数、日期时间和字符串）。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



putValue 方法还有一个重载版本，可以接受字符串格式的任何类型的值并自动将其转换为适当的数据类型。要实现这一点，请将布尔值 true 传递给 putValue 方法的另一个参数，如下面的示例所示。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **将公式添加到单元格**
Aspose.Cells.GridWeb 提供的最有价值的功能是支持公式或函数。Aspose.Cells.GridWeb 有自己的公式引擎，用于计算工作表中的公式。Aspose.Cells.GridWeb 支持内置和用户定义的函数或公式。本主题详细讨论了使用 Aspose.Cells.GridWeb API 向单元格添加公式。
### **如何添加和计算公式？**
可以通过使用单元格的 Formula 属性来添加、访问和修改公式。Aspose.Cells.GridWeb 支持从简单到复杂的用户定义公式。但是，Aspose.Cells.GridWeb 也提供了大量与 Microsoft Excel 类似的内置功能或公式。要查看完整的内置函数列表，请参阅此[受支持功能列表](/cells/zh/net/list-of-supported-functions/)。

{{% alert color="primary" %}} 

公式语法应与 Microsoft Excel 语法兼容。例如，所有公式必须以等号（=）开头。

要以编程方式添加公式，Aspose.Cells.GridWeb 将会识别它作为公式，即使您不使用 **=** 符号，但如果最终用户在 GUI 中使用必须使用它。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**将公式添加到 B3 单元格，但未由 GridWeb 计算** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

在上面的屏幕截图中，您可以看到已将公式添加到 B3，但尚未计算。要计算所有公式，请在将公式添加到工作表后调用 GridWeb 控件的 GridWorksheetCollection 的 calculateFormula 方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

用户还可以通过单击 **提交** 来计算公式。

**单击 GridWeb 的提交按钮** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**重要**：如果用户单击 **保存** 或 **撤销** 按钮，或者工作表标签，则所有公式将由 GridWeb 自动计算。

**计算后的公式结果** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **引用其他工作表中的单元格**
使用 Aspose.Cells.GridWeb，可以在其公式中引用存储在不同工作表中的值，从而创建复杂的公式。

从不同工作表引用单元格值的语法是 SheetName!CellName。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **在 GridWeb 的 GridCell 中创建数据验证**
Aspose.Cells.GridWeb 允许使用 GridWorksheet.getValidations().add() 方法添加 **数据验证**。使用这个方法，您必须指定**单元格范围**。但如果您想在单个 GridCell 中创建数据验证，那么可以直接使用 GridCell.createValidation() 方法。同样，您可以使用 GridCell.removeValidation() 方法从 GridCell 中删除**数据验证**。

下面的示例代码在 B3 单元格中创建了**数据验证**。如果输入任何不在 20 到 40 之间的值，B3 单元格将以**红色 XXXX**的形式显示**验证错误**，如屏幕截图所示。

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **创建自定义命令按钮**
Aspose.Cells.GridWeb 包含特殊按钮，如提交、保存和撤消。所有这些按钮都执行特定的任务。还可以添加执行自定义任务的自定义按钮。本主题解释了如何使用此功能。

下面的示例代码说明了如何创建自定义命令按钮以及如何处理其单击事件。您可以为自定义命令按钮使用任何图标。为说明目的，我们使用了这个图标。

![todo:image_alt_text](working-with-cells-gridweb_5.png)

如您在下面的屏幕截图中所见，当用户点击自定义命令按钮时，它将在 A1 单元格中添加一段文本，内容为**"My Custom Command Button is Clicked."**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **自定义命令按钮的事件处理**
以下示例代码说明了如何执行自定义命令按钮的事件处理。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **为 GridWeb 格式化单元格**
### **可能的使用场景**
GridWeb现在支持用户以百分比格式（如3%）输入单元格数据，并且单元格中的数据将自动格式为3.00%。但是，您必须将单元格样式设置为百分比格式，即GridTableItemStyle.NumberType为9或10。数字9将以3%的格式显示，但数字10将以3.00%的格式显示。

{{% alert color="primary" %}} 

如果未将单元格样式设置为百分比格式，则输入数据3%将显示为0.03。

{{% /alert %}} 
### **在GridWeb工作表的单元格中输入百分比格式的数据**
以下示例代码将单元格A1的GridTableItemStyle.NumberType设置为10，因此输入的3%数据将自动格式为3.00%，如屏幕截图所示。

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
