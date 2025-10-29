---
title: 用Golang通过C++访问并修改链接的Ole对象显示标签
linktitle: 访问和修改链接的OLE对象的显示标签
type: docs
weight: 100
url: /zh/go-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: 学习如何使用 Aspose.Cells for C++ 访问和修改 Excel 文件中链接的 Ole 对象的显示标签。
---

## **可能的使用场景**

Microsoft Excel 允许您更改 Ole 对象的显示标签，如以下截图所示。您还可以使用 Aspose.Cells API 结合 [**GetLabel()**](https://reference.aspose.com/cells/go-cpp/oleobject/getlabel/) 和 [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) 方法访问或修改 Ole 对象的显示标签。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **访问和修改链接的OLE对象的显示标签**

请参见以下样本代码，它加载包含Ole对象的 [样本Excel文件](64716810.xlsx)。该代码访问Ole对象并将其标签从Sample APIs更改为Aspose APIs。请参见下面给出的控制台输出，以了解样本代码对样本Excel文件的效果。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessAndModifyTheDisplayLabelOfTheLinkedOleObject.go" >}}
## **控制台输出**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
