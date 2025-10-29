---
title: 用Golang通过C++基于单元引用插入图片
linktitle: 基于单元格引用插入图片
type: docs
weight: 150
url: /zh/go-cpp/insert-a-picture-based-on-cell-reference/
description: 学习如何使用Aspose.Cells for C++根据单元格引用插入图片。
---

{{% alert color="primary" %}}

有时您会有一张空白图片，并且需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。Aspose.Cells支持此功能（Microsoft Excel 2010）。

{{% /alert %}}

## 根据单元格引用插入图片

Aspose.Cells支持将工作表单元格的内容显示在图像形状中。您可以将图片链接到包含要显示的数据的单元格。由于单元格或单元格范围与图形对象相关联，因此对该单元格或单元格范围中数据的更改会自动出现在图形对象中。通过调用[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)集合（封装在[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)对象中）的[**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/)方法向工作表中添加图片。使用[**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/)对象的属性指定单元格范围。

### 代码示例

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
