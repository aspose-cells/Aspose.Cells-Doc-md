---
title: 用Golang通过C++获取或设置嵌入式OLE对象的类标识符
linktitle: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 200
url: /zh/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: 学习如何用Golang通过C++用Aspose.Cells获取或设置嵌入式OLE对象的类标识符。
---

## **可能的使用场景**
Aspose.Cells提供[OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/)属性，您可以用它获取或设置嵌入式OLE对象的类标识符。OLE对象类标识符实际上是GUID，即全局唯一标识符。GUID始终是16字节长，因此类标识符也是16字节长。它们通常在Windows注册表中找到，并向宿主应用程序提供有关如何打开包含各种嵌入式资源的OLE对象的信息。

## **获取或设置嵌入的OLE对象的类标识符**
下图显示了从[示例Excel文件](5115190.xls)中读取的OLE对象类别标识符（GUID），该文件包含嵌入的PowerPoint OLE对象。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **示例代码**
请参见执行以下示例代码的结果，使用[示例Excel文件](5115190.xls)，其控制台输出显示了OLE对象的类别标识符（即GUID）。打印的GUID与截图中的完全相同。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **控制台输出**
这是上述样本代码执行时与[示例excel文件](5115190.xls)一起的控制台输出。

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
