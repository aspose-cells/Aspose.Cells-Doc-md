---
title: 命名范围
type: docs
weight: 40
url: /zh/java/named-ranges/
---

{{% alert color="primary" %}} 

通常，列和行标签用于引用单个单元格。可以创建描述性名称来表示单元格、单元格范围、公式或常量值。**名称**可能指代表示单元格、单元格范围、公式或常量值的一系列字符。为范围分配名称意味着可以通过其名称引用该单元格范围。使用易于理解的名称，例如“产品”，来引用难以理解的范围，例如“销售！C20：C30”。标签可在引用同一工作表上的数据的公式中使用；如果要表示另一工作表上的范围，可能会使用名称。*命名范围是Microsoft Excel的最强大功能之一，特别是在作为列表控件、数据透视表、图表等的源范围时。

{{% /alert %}} 
## **创建命名区域**
### **使用Microsoft Excel**
以下步骤描述了如何使用Microsoft Excel为单元格或单元格范围命名。此方法适用于Microsoft Office Excel 2003、Microsoft Excel 97、2000和2002。

1. 选择要命名的单元格或单元格范围。
1. 单击公式栏左端的名称框。
1. 输入单元格的名称。
1. 按ENTER。

{{% alert color="primary" %}} 

在更改单元格内容时，不能为单元格命名。

{{% /alert %}} 
### **使用Aspose.Cells**
在这里，我们使用Aspose.Cells API来完成任务。

Aspose.Cells提供了一个表示Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。

可以调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的重载 [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) 方法创建命名范围。通常的 [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) 方法参数如下：

- 左上角单元格的名称，范围中左上角单元格的名称。
- 右下角单元格的名称，范围中右下角单元格的名称。

调用 [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) 方法后，会返回一个新创建的命名范围，是 [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) 类的实例。

以下示例显示了如何创建一个跨越B4:G14的单元格命名范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **访问电子表格中的所有命名范围**
调用 [WorksheetCollection.getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) 方法获取工作表中的所有命名范围。该方法返回一个包含所有命名范围的数组。

以下示例显示如何访问工作簿中的所有命名范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **访问特定的命名范围**
调用 [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) 集合的 [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) 方法通过名称获取指定范围。一个典型的 [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) 方法接收命名范围的名称并以 [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) 类的实例返回指定的命名范围。

使用Aspose.Cells，您可以将数据插入到范围的各个单元格中。假设您有一个名为A1:C4的单元格命名范围。因此，该矩阵将生成4*3=12个单元格，并且各个范围单元格是按顺序排列的。Aspose.Cells为您提供了[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)类的一些实用属性以访问范围内的各个单元格。您可以使用以下方法来识别范围内的单元格：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **识别命名范围中的单元格**
- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)返回命名范围中第一行的索引。

- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)返回命名范围中第一列的索引。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)返回命名范围中第一列的索引。

以下示例显示如何向指定范围的单元格输入一些值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **将数据输入到命名范围内的单元格**
使用Aspose.Cells，您可以将数据插入到范围的各个单元格中。假设您有一个名为H1:J4的单元格命名范围。因此，该矩阵将生成4*3=12个单元格，并且各个范围单元格是按顺序排列的。Aspose.Cells为您提供了[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)类的一些实用属性以访问范围内的各个单元格。您可以使用以下属性来识别范围内的单元格：

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)返回命名范围中第一行的索引。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)返回命名范围中第一列的索引。

以下示例显示如何向指定范围的单元格输入一些值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **格式化范围...将背景颜色和字体属性设置为命名范围**
要应用格式化，定义一个[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象来指定样式设置，并将其应用到[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)对象。

以下示例显示了如何设置带有字体设置的实心填充颜色（阴影颜色）到一个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **格式化范围...向命名范围添加边框**
可以为一组单元格添加边框，而不仅仅是单个单元格。 [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) 对象提供了 [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) 方法，该方法采用以下参数为单元格范围添加边框：

- borderStyle：边框类型，从[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举中选择。
- borderColor：边框的线颜色，从[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举中选择。

以下示例显示如何将范围设置为轮廓边框。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


执行以上代码后将生成以下输出: 

![todo:image_alt_text](named-ranges_1.png)
#### **在Range中为单元格应用样式**
有时，您希望为 [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) 中的单元格应用样式。为此，您可以遍历范围内的单元格，并使用 [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) 方法将样式应用到单元格。

以下示例展示了如何在Range中为单元格应用样式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **移除命名范围**
Aspose.Cells 提供 [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt-int-) 方法以删除范围的名称。要清除范围内容，请使用 [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange-com.aspose.cells.CellArea-) 方法。
以下示例展示了如何移除命名范围及其内容。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
{{< app/cells/assistant language="java" >}}
