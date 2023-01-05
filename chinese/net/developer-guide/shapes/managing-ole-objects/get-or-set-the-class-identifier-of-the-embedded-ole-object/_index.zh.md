---
title: 获取或设置嵌入式 OLE 对象的类标识符
type: docs
weight: 200
url: /zh/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **可能的使用场景**
Aspose.Cells 提供了[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)可用于获取或设置嵌入的 ole 对象的类标识符的属性。 Ole 对象类标识符实际上是 GUID，即全局唯一标识符。 GUID 始终为 16 字节长，因此类标识符也为 16 字节长。它们通常位于 Windows 注册表中，并向主机应用程序提供有关如何打开包含客户端应用程序中各种嵌入式资源的嵌入式 ole 对象的信息。
## **获取或设置嵌入式 OLE 对象的类标识符**
以下屏幕截图显示了 Ole 对象类标识符，即从中读取的 GUID[示例 excel 文件](5115190.xls)包含嵌入的 PowerPoint ole 对象。

![待办事项：图片_替代_文本](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **示例代码**
请参阅以下示例代码执行[示例 excel 文件](5115190.xls)及其控制台输出打印 Ole 对象的类标识符，即 GUID。打印的 GUID 与屏幕截图中显示的完全相同。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **控制台输出**
这是上面示例代码执行时的控制台输出[示例 excel 文件](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
