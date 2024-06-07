---
title: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 200
url: /zh/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能的使用场景**
Aspose.Cells提供了[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier) 属性，你可以用它来获取或设置嵌入ole对象的类标识符。OLE对象类标识符实际上是GUID，即全局唯一标识符。 GUID总是16字节长，因此类标识符也是16字节长。 通常在Windows注册表中找到，并向主机应用程序提供关于如何打开包含各种嵌入资源的嵌入ole对象的信息。
## **获取或设置嵌入式OLE对象的类标识符**
下面的屏幕截图显示了从包含嵌入PowerPoint ole对象的 [示例 Excel 文件](5115190.xls) 中读取的 Ole 对象类标识符即GUID。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **示例代码**
请查看执行 [示例 Excel 文件](5115190.xls) 和其控制台输出的以下示例代码，打印 Ole 对象即GUID 的类标识符。 打印的GUID与屏幕截图中显示的GUID完全相同。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **控制台输出**
这是上述示例代码在 [示例 Excel 文件](5115190.xls) 上执行时的控制台输出。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
