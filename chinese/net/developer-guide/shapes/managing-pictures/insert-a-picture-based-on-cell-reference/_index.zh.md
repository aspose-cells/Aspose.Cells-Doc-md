---
title: 根据Cell参考插入图片
type: docs
weight: 150
url: /zh/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

有时您有一张空白图片，需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。 Aspose.Cells 支持此功能 (Microsoft Excel 2010)。

{{% /alert %}}

## 根据Cell参考插入图片

Aspose.Cells 支持以图像形状显示工作表单元格的内容。您可以将图片链接到包含要显示的数据的单元格。由于单元格或单元格区域链接到图形对象，因此您对该单元格或单元格区域中的数据所做的更改会自动出现在图形对象中。通过调用将图片添加到工作表[**添加图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)的方法[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)集合（封装在[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的）。使用指定单元格范围[**公式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)的属性[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)目的。

### 代码示例

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
