---
title: 添加在文档信息面板内可见的自定义属性，使用C++中的Golang
linktitle: 在文档信息面板中显示添加的自定义属性
type: docs
weight: 300
url: /zh/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: 学习如何使用C++中的Golang通过Aspose.Cells添加在文档信息面板中可见的自定义属性
---

## **在文档信息面板中可见的自定义属性**

Aspose.Cells可以用于向工作簿对象中添加可在文档信息面板中看到的自定义属性。您可以使用Microsoft Excel中的文件 > 信息 > 属性 > 显示文档面板菜单命令打开文档信息面板。

请使用 [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) 方法添加自定义属性，这些属性将在文档信息面板中显示。

以下示例代码添加了两个自定义属性，第一个没有设定类型，第二个设为日期时间类型。一旦打开由此代码生成的输出Excel文件，你会在文档信息面板中看到这两个属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **相关文章**

{{% alert color="primary" %}}

- [在Aspose.Cells中使用自定义XML部分](/cells/zh/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
