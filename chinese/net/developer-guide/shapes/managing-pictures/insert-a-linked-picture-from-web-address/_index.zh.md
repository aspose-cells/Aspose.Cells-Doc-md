---
title: 插入来自Web地址的链接图片
type: docs
weight: 450
url: /zh/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

有时候，您需要在工作表中插入来自Web（http://）的图片。为此，请指定图片的URL，并且每次在Microsoft Excel中打开电子表格时都会下载该图片。该图片没有被物理嵌入到Excel文档中，而是指向一个Web资源。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中（例如2007年）:

1. 单击**插入**菜单，然后选择**图片**。
1. 在插入图片对话框中指定图片的Web地址。

## **使用Aspose.Cells for .NET**

Aspose.Cells for .NET支持使用[**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture)添加一个链接的图像。 该方法返回一个[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)对象。

以下示例展示了如何从Web地址添加链接图片到工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
