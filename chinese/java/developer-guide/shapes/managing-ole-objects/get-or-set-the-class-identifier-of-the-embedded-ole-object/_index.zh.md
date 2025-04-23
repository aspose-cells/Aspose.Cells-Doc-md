---
title: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 920
url: /zh/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能的使用场景**
Aspose.Cells 提供了 [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier) 属性，您可以使用它来获取或设置嵌入式 OLE 对象的类标识符。OLE 对象类标识符实际上是 GUID，即全局唯一标识符。GUID 总是 16 字节长，因此类标识符也是 16 字节长。它们经常出现在 Windows 注册表中，并向主机应用程序提供有关如何在客户端应用程序中打开包含各种嵌入式资源的嵌入式 OLE 对象的信息。
## **获取或设置嵌入的OLE对象的类标识符**
以下屏幕截图显示了从包含嵌入式 PowerPoint OLE 对象的 [示例 Excel 文件](5473378.xls) 中读取的 OLE 对象类标识符，即 GUID。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **示例代码**
请查看使用 [示例 Excel 文件](5473378.xls) 执行的以下示例代码和其控制台输出，其中打印了嵌入式 OLE 对象的 *类标识符*，即 GUID。打印的 GUID 与屏幕截图中显示的完全相同。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **控制台输出**
这是使用 [示例 Excel 文件](5473378.xls) 执行上述示例代码的控制台输出。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
