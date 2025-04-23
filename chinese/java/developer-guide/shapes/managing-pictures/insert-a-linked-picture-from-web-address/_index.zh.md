---
title: 从Web地址插入链接图片
type: docs
weight: 50
url: /zh/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

有时您需要从Web（http://）将图片插入工作表中。为此，指定图片的URL，每次在Microsoft Excel中打开电子表格时都会下载图片。该图像并没有实际嵌入到Excel文档中，而是指向Web资源。

{{% /alert %}}

## **从网址插入链接图片**

### **使用Microsoft Excel**

在Microsoft Excel中（例如2007）：

1. 单击**插入**菜单，然后选择**图片**。

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. 在插入图片对话框中指定图片的Web地址。 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

图片已插入。

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **使用Aspose.Cells for Java**

Aspose.Cells for Java支持使用 [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture-int-int-int-int-java.lang.String-) 方法添加连接的图像。

该方法返回一个[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)对象。

下面的示例显示了如何将来自Web地址的链接图片添加到工作表中。

运行代码后，生成的Excel文件在第一个工作表上包含一个链接图片。

**输出文件** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
{{< app/cells/assistant language="java" >}}
