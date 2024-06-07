---
title: 创建访问和复制命名范围
type: docs
weight: 200
url: /zh/net/create-access-and-copy-named-ranges/
---

## **介绍**

通常，列和行标签用于引用单个单元格。可以创建描述性名称来表示单元格、单元格范围、公式或常量值。名称可能指代代表单元格、单元格范围、公式或常量值的一组字符。为范围分配一个名称意味着可以通过其名称引用该单元格范围。使用易于理解的名称，例如“Products”，表示难以理解的范围，例如“Sales!C20:C30”。标签可以用于引用同一工作表上的数据的公式；如果您想表示另一工作表上的范围，可以使用一个名称。*名称范围是Microsoft Excel最强大的功能之一，特别是在用作列表控件、数据透视表、图表等的源范围时。

## **使用Microsoft Excel处理命名范围**

### **创建命名范围**

以下步骤描述了如何使用 **MS Excel** 为单元格或单元格范围命名。此方法适用于 **Microsoft Office Excel 2003**、**Microsoft Excel 97**、**2000** 和 **2002**。

1. 选择要命名的单元格、单元格范围。
1. 单击公式栏左端的 **名称框**。
1. 为单元格键入名称。
1. 按 ENTER 键。

{{% alert color="primary" %}}

更改单元格内容时无法为单元格命名。

{{% /alert %}}

## **使用Aspose.Cells处理命名范围**

在这里，我们使用Aspose.Cells API来完成任务。
Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 表示Microsoft Excel文件。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了一个 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合。

### **创建命名范围**

可以通过调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合的重载 [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) 方法来创建命名范围。 [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) 方法的典型版本接受以下参数:

- 左上角单元格的名称，范围中左上角单元格的名称。
- 右下角单元格的名称，范围中右下角单元格的名称。

调用 [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) 方法时，它会将新创建的范围作为 [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) 类的实例返回。使用这个 [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) 对象来配置命名范围。例如，使用 [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) 属性设置范围的名称。以下示例显示了如何创建一个单元格命名范围，覆盖 B4:G14。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **向所命名范围中的单元格输入数据**

您可以按照模式将数据插入到范围中的单个单元格中

- **C#**：Range[row,column]
- **VB**：Range(row,column)

假设您有一个跨越A1:C4的命名范围。矩阵包含4 * 3 = 12个单元格。单独的范围单元按顺序排列：Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、 Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

使用以下属性来识别范围中的单元格:

- FirstRow 返回命名范围中第一行的索引。
- FirstColumn 返回命名范围中第一列的索引。
- RowCount 返回命名范围中的总行数。
- ColumnCount 返回命名范围中的总列数。

以下示例显示了如何将一些值输入到指定范围的单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **识别命名范围中的单元格**

您可以按照模式将数据插入到范围中的单个单元格中:

- **C#**：Range[row,column]
- **VB**：Range(row,column)

如果您有一个跨越A1:C4的命名范围。矩阵包含4 * 3 = 12个单元格。单独的范围单元按顺序排列：Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0] 、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

使用以下属性来识别范围中的单元格:

- FirstRow 返回命名范围中第一行的索引。
- FirstColumn 返回命名范围中第一列的索引。
- RowCount 返回命名范围中的总行数。
- ColumnCount 返回命名范围中的总列数。

以下示例显示了如何将一些值输入到指定范围的单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **访问命名范围**

#### **访问特定的命名范围**

调用 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) 集合的 [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) 方法，通过指定名称获取一个范围。典型的 [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) 方法需要命名范围的名称，并将指定的命名范围作为 [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) 类的实例返回。以下示例显示了如何通过名称访问指定范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **访问电子表格中的所有命名范围**

调用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) 集合的 [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) 方法，获取电子表格中的所有命名范围。[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) 方法返回 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) 集合中的所有命名范围的数组。

以下示例显示了如何访问工作簿中的所有命名范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **复制命名范围**

Aspose.Cells提供 [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) 方法，将带有格式的单元格范围复制到另一个范围中。

以下示例显示如何将一个来源范围的单元格复制到另一个命名范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
