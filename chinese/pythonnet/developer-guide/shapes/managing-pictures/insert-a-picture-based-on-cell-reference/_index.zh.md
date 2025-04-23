---
title: 基于单元格引用插入图片
type: docs
weight: 150
url: /zh/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

有时你有一张空图片，需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。Aspose.Cells for Python via .NET 支持此功能（Microsoft Excel 2010）。

{{% /alert %}}

## 根据单元格引用插入图片

Aspose.Cells for Python via .NET 支持在图片形状中显示工作表单元格的内容。你可以将图片链接到包含你想显示的数据的单元格。由于单元格或单元格范围与图形对象关联，任何对该单元格或范围数据的更改会自动反映在图形对象中。通过调用 [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) 方法，指定 [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 集合中的 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 对象的 [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) 属性，向工作表添加图片，并链接到对应的单元格范围。

### 代码示例

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
