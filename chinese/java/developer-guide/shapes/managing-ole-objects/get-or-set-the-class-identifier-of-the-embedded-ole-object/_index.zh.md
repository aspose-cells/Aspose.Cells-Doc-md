---
title: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 920
url: /zh/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能的使用场景**
Aspose.Cells提供了[OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier)属性，可用于获取或设置嵌入OLE对象的类标识符。OLE对象类标识符实际上是GUID，即全局唯一标识符。GUID始终是16字节长，因此类标识符也是16字节长。它们经常出现在Windows注册表中，并为主机应用程序提供关于如何在客户应用程序中打开包含各种嵌入资源的嵌入式OLE对象的信息。
## **获取或设置嵌入式OLE对象的类标识符**
下面的截图显示了从包含嵌入式PowerPoint ole对象的[样本Excel文件](5473378.xls)中读取的Ole对象类标识符，即GUID。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **示例代码**
请查看执行了[样本Excel文件](5473378.xls)及其控制台输出的以下示例代码，该输出打印了Ole对象即GUID的*Class Identifier*。打印的GUID与截图中显示的完全相同。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **控制台输出**
这是上述示例代码在使用[样本Excel文件](5473378.xls)时的控制台输出。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
