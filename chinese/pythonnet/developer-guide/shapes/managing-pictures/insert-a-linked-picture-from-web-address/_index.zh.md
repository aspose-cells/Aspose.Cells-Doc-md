---
title: 从Web地址插入链接图片
type: docs
weight: 450
url: /zh/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

有时您需要从Web（http://）将图片插入工作表中。为此，指定图片的URL，每次在Microsoft Excel中打开电子表格时都会下载图片。该图像并没有实际嵌入到Excel文档中，而是指向Web资源。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中（例如2007）：

1. 单击**插入**菜单，然后选择**图片**。
1. 在插入图片对话框中指定图片的Web地址。

## **使用Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET 支持使用 [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture) 添加链接图片。该方法返回一个 [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) 对象。

下面的示例显示了如何将来自Web地址的链接图片添加到工作表中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
