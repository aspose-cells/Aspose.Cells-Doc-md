---
title: 用Golang通过C++将形状置于工作表前端或后端
linktitle: 在工作表内部发送形状到前面或后面
type: docs
weight: 3400
url: /zh/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: 学习如何使用 Aspose.Cells for C++ 改变工作表中形状的z次序位置。
---

## **可能的使用场景**

当多个形状位于同一位置时，它们的可见性由z次序位置决定。Aspose.Cells 提供了 [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/) 方法，可以改变形状的z次序。如果要将形状送到最底层，可以使用负数如-1、-2、-3等；如果要将形状带到最前面，使用正数如1、2、3等。

## **在工作表内发送形状到最前或最后**

以下示例代码演示了 [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/) 方法的用法。请查看用于此代码的 [示例Excel文件](50528330.xlsx) 和由它生成的 [输出Excel文件](50528331.xlsx)。截图展示了代码执行后对示例Excel文件的效果。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
