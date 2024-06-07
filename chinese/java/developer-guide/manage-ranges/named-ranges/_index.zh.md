---
title: 命名范围
type: docs
weight: 40
url: /zh/java/named-ranges/
---

{{% alert color="primary" %}} 

通常，列和行标签用于引用单个单元格。可以创建描述性名称来表示单元格、单元格范围、公式或固定值。单词**名称**可以指代代表单元格、单元格范围、公式或固定值的字符串。为一段区域指定名称意味着该单元格范围可以按其名称引用。使用易于理解的名称，例如Products，来引用难以理解的范围，例如Sales!C20:C30。标签可用于引用同一工作表上的数据的公式；如果要表示另一个工作表上的范围，可以使用名称。* 命名范围是Microsoft Excel中最强大的功能之一，特别是当用作列表控件、数据透视表、图表等的源范围时。

{{% /alert %}} 
## **创建命名范围**
### **使用Microsoft Excel**
以下步骤描述了如何使用Microsoft Excel为单元格或单元格范围命名。该方法适用于Microsoft Office Excel 2003、Microsoft Excel 97、2000和2002。

1. 选择要命名的单元格、单元格范围。
1. 在公式栏的左端点击名称框。
1. 为单元格键入名称。
1. 按 ENTER 键。

{{% alert color="primary" %}} 

更改单元格内容时无法为单元格命名。

{{% /alert %}} 
### **使用Aspose.Cells**
在这里，我们使用Aspose.Cells API来完成任务。

Aspose.Cells提供一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个Microsoft Excel文件。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。

通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的重载的[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\))方法，可以创建一个命名范围。 [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\))方法的典型版本需要以下参数：

- 左上角单元格的名称，范围中左上角单元格的名称。
- 右下角单元格的名称，范围中右下角单元格的名称。

调用[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\))方法时，它将以[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)类的实例形式返回新创建的命名范围。

下面的示例显示如何创建一个命名范围，该范围扩展到B4:G14。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **访问电子表格中的所有命名范围**
调用[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)集合的[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\))方法，以获取电子表格中的所有命名范围。 [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcolle...

以下示例显示了如何访问工作簿中的所有命名范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **访问特定的命名范围**
调用[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)集合的[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\))方法来按名称获取指定范围。典型的[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\))方法选择名称范围并将指定的命名范围作为[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)类的实例...

下面的示例显示如何按名称访问指定范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **识别命名范围中的单元格**
使用Aspose.Cells，可以将数据插入到命名范围中的各个单元格中。假设您有一个名为的单元格范围.i.e. A1:C4。因此，矩阵将生成4 * 3 = 12个单元格，并且单个范围单元按顺序排列。Aspose.Cells为[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)类提供一些有用的属性，以访问范围内的单个单元格。您可以使用以下方法来识别范围中的单元格：

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) 返回命名范围中第一行的索引。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) 返回命名范围中第一列的索引。

以下示例显示了如何将一些值输入到指定范围的单元格中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **向所命名范围中的单元格输入数据**
使用Aspose.Cells，您可以将数据插入到命名范围中的各个单元格中。假设您有一个名为的单元格范围，例如H1:J4。因此，该矩阵会生成4 * 3 = 12个单元格，并且单个范围单元按顺序排列。Aspose.Cells为[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)类提供一些有用的属性来访问范围内的单个单元格。您可以使用以下属性来识别范围中的单元格：

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) 返回命名范围中第一行的索引。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) 返回命名范围中第一列的索引。

以下示例显示了如何将一些值输入到指定范围的单元格中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **格式化范围...将背景颜色和字体属性设置为命名范围**
要应用格式，定义一个[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象以指定样式设置，并将其应用于[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)对象。

下面的示例显示如何为范围设置实体填充颜色（着色颜色）和字体设置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **格式化范围...向命名范围添加边框**
可以向一组单元格添加边框，而不仅仅是单个单元格。 [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)对象提供了一个[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\))方法，该方法需要以下参数来向单元格范围添加边框：

- borderStyle: 边框类型，从[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举中选择。
- borderColor: 边框线颜色，从[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举中选择。

以下示例显示如何将轮廓边框设置为区域。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


执行以上代码后，将生成以下输出： 

![todo:image_alt_text](named-ranges_1.png)
#### **在范围中应用样式到单元格**
有时，您希望为[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)中的单元格应用样式。为此，可以迭代范围中的单元格并使用[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspo...

下面的示例显示如何将样式应用于范围中的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **删除命名范围**
Aspose.Cells提供[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\))方法来删除范围的名称。要清除范围的内容，请使用[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\))方法。
下面的示例显示如何删除具有其内容的命名范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
