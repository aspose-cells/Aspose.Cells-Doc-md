---
title: 使用 Cells GridWeb
type: docs
weight: 50
url: /zh/java/working-with-cells-gridweb/
---
## **在工作表中访问 Cells**
本主题讨论单元格，着眼于 GridWeb 的最基本功能：访问单元格。

每个工作表都包含一个 GridCells 对象，即 GridCell 对象的集合。 GridCell 对象表示 Aspose.Cells.GridWeb 中的一个单元格。可以使用 GridWeb 访问任何单元格。有两种首选方法：

- [按名称访问单元格](/cells/zh/java/working-with-cells-gridweb/).
- [按行和列索引访问单元格](/cells/zh/java/working-with-cells-gridweb/).

下面，将讨论每种方法。
### **使用 Cell 名称**
所有单元格都有一个唯一的名称。例如，A1、A2、B1、B2 等。 Aspose.Cells.GridWeb 允许开发人员使用单元格名称访问任何所需的单元格。只需将单元格名称（作为索引）传递给 GridWorksheet 的 GridCells 集合。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **使用行和列索引**
单元格也可以通过其在行和列索引方面的位置来识别。只需将单元格的行和列索引传递给 GridWorksheet 的 GridCells 集合。这种方法比上面的方法更快。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **访问和修改 a Cell 的值**
[在工作表中访问 Cells](/cells/zh/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet)讨论了访问单元格。本主题扩展该讨论以显示如何使用 GridWeb API 访问和修改单元格值。
### **访问和修改 Cell 的值**
#### **字符串值**
在访问和修改单元格的值之前，您需要知道如何访问单元格。有关访问单元格的不同方法的详细信息，请参阅[在工作表中访问 Cells](/cells/zh/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

每个单元格都有一个名为 getStringValue() 的属性。访问单元格后，开发人员可以访问 getStringValue() 方法来访问单元格字符串值。

{{% alert color="primary" %}} 

重要提示：五种类型的值（布尔值、整数、双精度值、日期时间和字符串）可以存储在单元格中，但 getValue()/setValue() 方法只能用于访问/修改对象值。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **所有类型的值**
Aspose.Cells.GridWeb 还为每个单元格提供了一个特殊的方法putValue。使用此方法，可以在单元格中插入或修改任何类型的值（Boolean、int、double、DateTime 和 string）。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



还有一个重载版本的 putValue 方法，它可以接受任何类型的字符串格式的值并自动将其转换为适当的数据类型。为此，将布尔值 true 传递给 putValue 方法的另一个参数，如下例所示。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **将公式添加到 Cells**
Aspose.Cells.GridWeb 提供的最有价值的功能是支持公式或函数。 Aspose.Cells.GridWeb 有自己的公式引擎，可以计算工作表中的公式。 Aspose.Cells.GridWeb 支持内置和用户定义的函数或公式。本主题详细讨论使用 Aspose.Cells.GridWeb API 向单元格添加公式。
### **如何添加和计算公式？**
可以使用单元格的公式属性在单元格中添加、访问和修改公式。 Aspose.Cells.GridWeb支持从简单到复杂的用户自定义公式。但是，Aspose.Cells.GridWeb也提供了大量的内置函数或公式（类似于Microsoft Excel）。要查看内置函数的完整列表，请参阅此[支持的功能列表。](/cells/zh/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

公式语法应与 Microsoft Excel 语法兼容。例如，所有公式都必须以等号 (=) 开头。

要以编程方式添加公式，Aspose.Cells.GridWeb 会将其识别为公式，即使您不使用 **=** 符号，但如果在 GUI 中工作的最终用户必须使用它。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**公式添加到 B3 单元格但未由 GridWeb 计算** 

![待办事项：图片_替代_文本](working-with-cells-gridweb_1.png)

在上面的截图中，可以看到B3中已经添加了一个公式，但是还没有进行计算。要计算所有公式，请在将公式添加到工作表后调用 GridWeb 控件的 GridWorksheetCollection 的 calculateFormula 方法，如下所示。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

用户还可以通过单击计算公式**提交**.

**单击 GridWeb 的提交按钮** 

![待办事项：图片_替代_文本](working-with-cells-gridweb_2.png)

**重要的**：如果用户点击**节省**或者**撤消**按钮或工作表选项卡，所有公式均由 GridWeb 自动计算。

**计算后的公式结果** 

![待办事项：图片_替代_文本](working-with-cells-gridweb_3.png)
### **从其他工作表中引用 Cells**
使用 Aspose.Cells.GridWeb，可以在其公式中引用存储在不同工作表中的值，从而创建复杂的公式。

从不同工作表引用单元格值的语法是 SheetName!CellName。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **在 GridWeb 的 GridCell 中创建数据验证**
Aspose.Cells.GridWeb 允许您添加**数据验证**使用 GridWorksheet.getValidations().add() 方法。使用此方法，您必须指定**Cell 范围**.但是如果你想在单个 GridCell 中创建数据验证，那么你可以直接使用 GridCell.createValidation() 方法来完成。同样，您可以删除**数据验证**从 GridCell 使用 GridCell.removeValidation() 方法。

下面的示例代码创建一个**数据验证**在单元格 B3 中。如果您输入任何不在 20 到 40 之间的值，单元格 B3 将显示**验证错误**形式为**红色 XXXX**如这个屏幕截图所示。

![待办事项：图片_替代_文本](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **创建自定义命令按钮**
Aspose.Cells.GridWeb 包含特殊按钮，如提交、保存和撤消。所有这些按钮都为 Aspose.Cells.GridWeb 执行特定任务。还可以添加执行自定义任务的自定义按钮。本主题说明如何使用此功能。

以下示例代码解释了如何创建自定义命令按钮以及如何处理其单击事件。您可以为自定义命令按钮使用任何图标。出于说明目的，我们使用了这个图像图标。

![待办事项：图片_替代_文本](working-with-cells-gridweb_5.png)

正如您在下面的屏幕截图中看到的，当用户单击自定义命令按钮时，它会在单元格 A1 中添加一个文本说**“单击了我的自定义命令按钮。”**

![待办事项：图片_替代_文本](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **自定义命令按钮的事件处理**
以下示例代码解释了如何执行自定义命令按钮的事件处理。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **为 GridWeb 格式化单元格**
### **可能的使用场景**
GridWeb 现在支持用户以百分比格式输入单元格数据，如 3%，单元格中的数据将自动格式化为 3.00%。但是，您必须将单元格样式设置为百分比格式，即 GridTableItemStyle.NumberType 9 或 10。数字 9 会将 3% 的格式设置为 3%，而数字 10 会将 3% 的格式设置为 3.00%。

{{% alert color="primary" %}} 

如果你没有设置单元格样式为百分比格式，那么输入数据3%会显示为0.03。

{{% /alert %}} 
### **以百分比格式输入 Cell GridWeb 工作表数据**
以下示例代码将单元格 A1 GridTableItemStyle.NumberType 设置为 10，因此输入数据 3% 会自动格式化为 3.00%，如屏幕截图所示。

![待办事项：图片_替代_文本](working-with-cells-gridweb_7.png)
### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
