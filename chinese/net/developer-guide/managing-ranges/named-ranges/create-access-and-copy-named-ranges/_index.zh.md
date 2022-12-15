---
title: 创建访问和复制命名范围
type: docs
weight: 200
url: /zh/net/create-access-and-copy-named-ranges/
---
## **介绍**

通常，列和行标签用于指代单个单元格。可以创建描述性名称来表示单元格、单元格区域、公式或常量值。这个单词**姓名**可以指表示单元格、单元格范围、公式或常量值的字符串。为范围指定名称意味着可以通过其名称引用该单元格范围。使用易于理解的名称（例如 Products）来指代难以理解的范围，例如 Sales!C20:C30。标签可用于引用同一工作表上数据的公式中；如果你想在另一个工作表上表示一个范围，你可以使用一个名称。 *命名区域是 Microsoft Excel 最强大的功能之一，尤其是用作列表控件、数据透视表、图表等的源区域时。

## **使用 Microsoft Excel 处理命名范围**

### **创建命名范围**

以下步骤描述了如何使用命名单元格或单元格区域**微软Excel** .此方法适用于**Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**和**2002**.

1. 选择要命名的单元格、单元格区域。
1. 点击**姓名框**在公式栏的左端。
1. 键入单元格的名称。
1. 按 ENTER。

{{% alert color="primary" %}}

在更改单元格的内容时不能命名单元格。

{{% /alert %}}

## **使用 Aspose.Cells 处理命名范围**

在这里，我们使用 Aspose.Cells API 来完成任务。
Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。

### **创建命名范围**

可以通过调用重载来创建命名范围[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。一个典型的版本[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)方法采用以下参数：

- 左上角单元格的名称，区域中左上角单元格的名称。
- 右下角单元格的名称，范围内右下角单元格的名称。

当。。。的时候[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)方法被调用时，它返回新创建的范围作为[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)班级。用这个[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)对象来配置命名范围。例如，使用[**姓名**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name)财产。下面的示例演示如何创建扩展到 B4:G14 的命名单元格区域。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **在命名范围内输入数据到 Cells**

您可以按照模式将数据插入到范围的各个单元格中

- **C#**：范围[行，列]
- **虚拟机**：范围（行，列）

假设您有一个跨 A1:C4 的命名单元格区域。该矩阵有 4 * 3 = 12 个单元格。各个范围单元格按顺序排列：Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、范围[2,0]、范围[2,1]、范围[2,2]、范围[3,0]、范围[3,1]、范围[3,2]。

使用以下属性来识别区域中的单元格：

- FirstRow 返回命名范围中第一行的索引。
- FirstColumn 返回命名范围中第一列的索引。
- RowCount 返回指定范围内的总行数。
- ColumnCount 返回指定区域中的总列数。

下面的示例演示如何将一些值输入到指定区域的单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **在命名范围内识别 Cells**

您可以按照以下模式将数据插入范围的各个单元格中：

- **C#**：范围[行，列]
- **虚拟机**：范围（行，列）

如果您有一个跨越 A1:C4 的命名范围。该矩阵有 4 * 3 = 12 个单元格。各个范围单元格按顺序排列：范围[0,0]、范围[0,1]、范围[0,2]、范围[1,0]、范围[1,1]、范围[1,2]、范围[2,0]、范围[2,1]、范围[2,2]、范围[3,0]、范围[3,1]、范围[3,2]。

使用以下属性来识别区域中的单元格：

- FirstRow 返回命名范围中第一行的索引。
- FirstColumn 返回命名范围中第一列的索引。
- RowCount 返回指定范围内的总行数。
- ColumnCount 返回指定区域中的总列数。

下面的示例演示如何将一些值输入到指定区域的单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **访问命名范围**

#### **访问特定的命名范围**

打电话给[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)收藏的[**按名称获取范围**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)通过指定名称获取范围的方法。一个典型的[**按名称获取范围**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)方法采用命名范围的名称，并将指定的命名范围作为[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)班级。以下示例显示如何通过名称访问指定范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **访问电子表格中的所有命名范围**

打电话给[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)收藏的[**获取命名范围**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)获取电子表格中所有命名范围的方法。这[**获取命名范围**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)方法返回一个包含所有名称范围的数组[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)收藏。

下面的示例演示如何访问工作簿中的所有命名范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **复制命名范围**

Aspose.Cells提供[**范围.复制()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)将具有格式的单元格区域复制到另一个区域的方法。

下面的示例演示如何将单元格的源区域复制到另一个命名区域。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
