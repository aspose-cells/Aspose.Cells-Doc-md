---
title: 用Golang通过C++从网页地址插入链接图片
linktitle: 从Web地址插入链接图片
type: docs
weight: 450
url: /zh/go-cpp/insert-a-linked-picture-from-web-address/
description: 学习如何使用Aspose.Cells for C++从Web地址在工作表中插入链接图片。
---

{{% alert color="primary" %}}

有时您需要从Web（http://）将图片插入工作表中。为此，指定图片的URL，每次在Microsoft Excel中打开电子表格时都会下载图片。该图像并没有实际嵌入到Excel文档中，而是指向Web资源。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中（例如2007）：

1. 单击**插入**菜单，然后选择**图片**。
1. 在插入图片对话框中指定图片的Web地址。

## **使用Aspose.Cells for C++**

Aspose.Cells for C++支持使用[**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/)方法添加链接图片。该方法返回一个[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)对象。

以下示例展示了如何将来自Web地址的链接图片添加到工作表中。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
