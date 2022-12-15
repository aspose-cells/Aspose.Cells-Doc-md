---
title: 命名范围
type: docs
weight: 40
url: /zh/java/named-ranges/
---
{{% alert color="primary" %}} 

通常，列和行标签用于引用单个单元格。可以创建描述性名称来表示单元格、单元格区域、公式或常量值。这个单词**姓名**可以指表示单元格、单元格区域、公式或常量值的字符串。为范围指定名称意味着可以通过其名称引用该单元格范围。使用易于理解的名称（例如 Products）来指代难以理解的范围，例如 Sales!C20:C30。标签可用于引用同一工作表上数据的公式中；如果你想在另一个工作表上表示一个范围，你可以使用一个名称。 *命名区域是 Microsoft Excel 最强大的功能之一，尤其是用作列表控件、数据透视表、图表等的源区域时。

{{% /alert %}} 
## **创建命名范围**
### **使用 Microsoft Excel**
以下步骤描述了如何使用 Microsoft Excel 命名一个单元格或单元格区域。此方法适用于Microsoft Office Excel 2003、Microsoft Excel 97、2000、2002。

1. 选择要命名的单元格、单元格区域。
1. 单击编辑栏左端的名称框。
1. 键入单元格的名称。
1. 按 ENTER。

{{% alert color="primary" %}} 

在更改单元格的内容时不能命名单元格。

{{% /alert %}} 
### **使用 Aspose.Cells**
在这里，我们使用 Aspose.Cells API 来完成任务。

Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。

可以通过调用重载来创建命名范围[创建范围](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。一个典型的版本[创建范围](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)方法采用以下参数：

- 左上角单元格的名称，区域中左上角单元格的名称。
- 右下角单元格的名称，范围内右下角单元格的名称。

当。。。的时候[创建范围](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) 方法被调用，它返回新创建的命名范围作为实例[范围](https://reference.aspose.com/cells/java/com.aspose.cells/range)班级。

下面的示例演示如何创建扩展到 B4:G14 的命名单元格区域。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **访问电子表格中的所有命名范围**
打电话给[获取命名范围](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) 的方法[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)获取电子表格中的所有命名范围。这[获取命名范围](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) 方法返回一个包含所有命名范围的数组[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

下面的示例演示如何访问工作簿中的所有命名范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **访问特定的命名范围**
打电话给[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)收藏的[获取范围名称](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) 方法按名称获取指定范围。一个典型的[获取范围名称](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) 方法采用命名范围的名称，并将指定的命名范围作为[范围](https://reference.aspose.com/cells/java/com.aspose.cells/range)班级。

以下示例显示如何通过名称访问指定范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **在命名范围内识别 Cells**
使用 Aspose.Cells，您可以将数据插入范围的各个单元格中。假设您有一个命名的单元格区域，即 A1:C4。因此矩阵将生成 4 * 3 = 12 个单元格，并且各个范围单元格按顺序排列。 Aspose.Cells 为您提供了 [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) 类的一些有用属性，用于访问范围内的各个单元格。您可以使用以下方法来识别区域中的单元格：

- [获取第一行](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)返回命名范围中第一行的索引。
- [获取第一列](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)返回命名范围中第一列的索引。

下面的示例演示如何将一些值输入到指定区域的单元格中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **在命名范围内输入数据到 Cells**
使用 Aspose.Cells，您可以将数据插入范围的各个单元格中。假设您有一个命名的单元格区域，即 H1:J4。因此矩阵将生成 4 * 3 = 12 个单元格，并且各个范围单元格按顺序排列。 Aspose.Cells 为您提供了 [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) 类的一些有用属性，用于访问范围内的各个单元格。您可以使用以下属性来识别范围内的单元格：

- [获取第一行](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)返回命名范围中第一行的索引。
- [获取第一列](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)返回命名范围中第一列的索引。

下面的示例演示如何将一些值输入到指定区域的单元格中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **格式化范围...将背景颜色和字体属性设置为命名范围**
要应用格式，定义一个[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象指定样式设置并将其应用于[范围](https://reference.aspose.com/cells/java/com.aspose.cells/range)目的。

以下示例显示如何使用字体设置将纯色填充颜色（底纹颜色）设置为一个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **格式化范围...向命名范围添加边框**
可以为一系列单元格而不是单个单元格添加边框。这[范围](https://reference.aspose.com/cells/java/com.aspose.cells/range)对象提供了一个[设置轮廓边框](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)方法，它采用以下参数为单元格区域添加边框：

-  borderStyle：边框的类型，从[单元格边框类型](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举。
- borderColor：边框的线条颜色，从[颜色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举。

下面的示例演示如何将轮廓边框设置为范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


执行上述代码后会产生如下输出：

![待办事项：图像_替代_文本](named-ranges_1.png)
#### **将样式应用于范围内的单元格**
有时，您想要创建将样式应用于[范围](https://reference.aspose.com/cells/java/com.aspose.cells/range).为此，您可以遍历范围内的单元格并使用[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)方法将样式应用于单元格。

下面的示例演示如何将样式应用于范围中的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **删除命名范围**
Aspose.Cells 提供了[名称集合.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) 方法来擦除范围的名称。要清除范围的内容，请使用[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)） 方法。
以下示例显示如何删除命名范围及其内容。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


边框颜色
