---
title: 从网址插入链接图片
type: docs
weight: 50
url: /zh/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

有时您需要将来自网络 (http://) 的图片插入到工作表中。为此，请指定图片的 URL，每次在 Microsoft Excel 中打开电子表格时都会下载图片。该图像并未物理嵌入到 Excel 文档中，而是指向 Web 资源。

{{% /alert %}}

## **从网址插入链接图片**

### **使用 Microsoft Excel**

在 Microsoft Excel 中（例如 2007）：

1. 点击**插入**菜单并选择**图片**.

![待办事项：图片_替代_文本](insert-a-linked-picture-from-web-address_1.png)

1. 在“插入图片”对话框中指定图片的网址。

![待办事项：图片_替代_文本](insert-a-linked-picture-from-web-address_2.png)

图像被插入。

![待办事项：图片_替代_文本](insert-a-linked-picture-from-web-address_3.png)

### **使用 Aspose.Cells for Java**

 Aspose.Cells for Java 支持使用方法添加链接图片[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

该方法返回一个[**图片**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)目的。

以下示例显示如何将网址中的链接图片添加到工作表。

运行代码后，生成的 Excel 文件在第一个工作表上包含一个链接图像。

**输出文件** 

![待办事项：图片_替代_文本](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
