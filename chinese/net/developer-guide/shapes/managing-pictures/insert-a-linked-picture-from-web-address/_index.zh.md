---
title: 从网址插入链接图片
type: docs
weight: 450
url: /zh/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

有时您需要将来自网络 (http://) 的图片插入到工作表中。为此，请指定图片的 URL，每次在 Microsoft Excel 中打开电子表格时都会下载图片。该图像并未物理嵌入到 Excel 文档中，而是指向 Web 资源。

{{% /alert %}}

## **使用 Microsoft Excel**

在 Microsoft Excel 中（例如 2007）：

1. 点击**插入**菜单并选择**图片**.
1. 在“插入图片”对话框中指定图片的网址。

## **使用 Aspose.Cells for .NET**

 Aspose.Cells for .NET 支持使用添加链接图像[**ShapeCollection.AddLinkedPicture（int upperLeftRow，int upperLeftColumn，int heightPixels，int widthPixels，字符串 sourceFullName）**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) .该方法返回一个[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)目的。

以下示例显示如何将网址中的链接图片添加到工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
