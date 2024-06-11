---
title: 从Web地址插入链接图片
type: docs
weight: 450
url: /zh/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

有时您需要从Web（http://）将图片插入工作表中。为此，指定图片的URL，每次在Microsoft Excel中打开电子表格时都会下载图片。该图像并没有实际嵌入到Excel文档中，而是指向Web资源。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中（例如2007）：

1. 单击**插入**菜单，然后选择**图片**。
1. 在插入图片对话框中指定图片的Web地址。

## **使用 Aspose.Cells for .NET**

Aspose.Cells for .NET 支持使用[**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture)添加链接图像。该方法返回一个[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)对象。

下面的示例显示了如何将来自Web地址的链接图片添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
