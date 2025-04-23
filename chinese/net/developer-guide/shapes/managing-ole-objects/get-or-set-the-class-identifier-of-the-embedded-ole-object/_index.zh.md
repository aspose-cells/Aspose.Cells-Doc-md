---
title: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 200
url: /zh/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能的使用场景**
Aspose.Cells提供了[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)属性，您可以使用它来获取或设置嵌入ole对象的类标识符。OLE对象类标识符实际上是GUID，即全局唯一标识符。GUID始终是16个字节长，因此类标识符也是16个字节长。它们经常出现在Windows注册表中，并向宿主应用程序提供有关如何在客户端应用程序中打开嵌入的OLE对象的嵌入资源的信息。
## **获取或设置嵌入的OLE对象的类标识符**
以下截图显示了从包含嵌入式PowerPoint OLE对象的[示例Excel文件](5115190.xls)中读取的OLE对象类标识符即GUID。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **示例代码**
请参见以下使用[示例Excel文件](5115190.xls)执行的样本代码和其控制台输出，该输出打印了OLE对象的类标识符即GUID。打印出的GUID与截图中显示的完全相同。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **控制台输出**
这是上述样本代码执行时与[示例excel文件](5115190.xls)一起的控制台输出。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
