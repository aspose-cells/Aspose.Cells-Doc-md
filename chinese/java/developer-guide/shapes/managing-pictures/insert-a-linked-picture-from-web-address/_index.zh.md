---
title: 插入来自Web地址的链接图片
type: docs
weight: 50
url: /zh/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

有时候，您需要在工作表中插入来自Web（http://）的图片。为此，请指定图片的URL，并且每次在Microsoft Excel中打开电子表格时都会下载该图片。该图片没有被物理嵌入到Excel文档中，而是指向一个Web资源。

{{% /alert %}}

## **插入来自Web地址的链接图片**

### **使用Microsoft Excel**

在Microsoft Excel中（例如2007年）:

1. 单击**插入**菜单，然后选择**图片**。

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. 在插入图片对话框中指定图片的Web地址。 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

插入图片。

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **使用Aspose.Cells for Java**

Aspose.Cells for Java支持使用方法[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)添加链接图片。

该方法返回一个[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)对象。

以下示例展示了如何从Web地址添加链接图片到工作表。

运行代码后，生成的Excel文件中包含第一个工作表上的链接图片。

**输出文件** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
