---
title: 根据单元格引用插入图片
type: docs
weight: 150
url: /zh/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

有时候您有一个空图片，并且需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。Aspose.Cells支持此功能（Microsoft Excel 2010）。

{{% /alert %}}

## 基于单元格引用插入图片

Aspose.Cells支持在图像形状中显示工作表单元格的内容。您可以将图片链接到包含要显示数据的单元格。由于单元格或单元格范围与图形对象相连，因此对该单元格或单元格范围中数据的更改会自动显示在图形对象中。通过调用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)对象中封装的[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)集合的[**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)方法将图片添加到工作表中。使用[**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)对象的[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)属性指定单元格范围。

### 代码示例

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
