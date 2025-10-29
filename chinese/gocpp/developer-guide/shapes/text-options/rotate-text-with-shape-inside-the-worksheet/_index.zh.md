---
title: 使用 Golang 通过 C++ 在工作表中旋转文本与形状
linktitle: 旋转带有形状的文本
type: docs
weight: 1300
url: /zh/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: 学习如何在Excel工作表中使用形状控制文本旋转，使用编号Aspose.Cells for C++。
---

## **可能的使用场景**

你可以在任何形状中添加文本，使用Microsoft Excel。如果你使用非常旧的Microsoft Excel 2003添加形状，文本不会随形状旋转。然而，如果你使用较新版本的Microsoft Excel（如2007、2010、2013或2016）添加形状，文本将随形状旋转。你可以通过[**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)属性控制文本是否随形状旋转。该属性的默认值为**true**，意味着文本会随形状旋转。若将其设置为**false**，文本则不会随形状旋转。

## **在工作表内旋转文本与形状**

以下示例代码加载包含三角形形状的[示例Excel文件](64716896.xlsx)，其文本会随形状旋转。如果在Microsoft Excel中打开示例文件并旋转三角形，文本也会旋转。代码随后将[**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)属性设置为**false**，并将文件保存为[输出Excel文件](64716897.xlsx)。如果用Microsoft Excel打开这个输出文件并旋转三角形，文本则不会随之旋转。请参考以下截图，显示代码对示例Excel文件的效果。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
