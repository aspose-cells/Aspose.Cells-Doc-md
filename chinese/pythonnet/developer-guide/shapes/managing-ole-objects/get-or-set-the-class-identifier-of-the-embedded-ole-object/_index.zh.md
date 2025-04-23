---
title: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 200
url: /zh/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能的使用场景**
Aspose.Cells for Python via .NET 提供了 [OleObject.class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier) 属性，可以用来获取或设置嵌入的 Ole 对象的类标识符。Ole 对象类标识符实际上是 GUID，也就是全局唯一标识符。GUID 长度始终为 16 字节，因此类标识符也是 16 字节。它们通常在 Windows 注册表内可找到，为宿主应用提供关于如何打开包含各种嵌入资源的嵌入式 Ole 对象的信息。

## **获取或设置嵌入的OLE对象的类标识符**
以下截图显示了从包含嵌入式PowerPoint OLE对象的[示例Excel文件](5115190.xls)中读取的OLE对象类标识符即GUID。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **示例代码**
请参见以下使用[示例Excel文件](5115190.xls)执行的样本代码和其控制台输出，该输出打印了OLE对象的类标识符即GUID。打印出的GUID与截图中显示的完全相同。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **控制台输出**
这是上述样本代码执行时与[示例excel文件](5115190.xls)一起的控制台输出。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
