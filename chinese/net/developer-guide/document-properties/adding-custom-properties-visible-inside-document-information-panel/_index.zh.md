---
title: 在文档信息面板中可见的自定义属性
type: docs
weight: 300
url: /zh/net/adding-custom-properties-visible-inside-document-information-panel/
---

## **在文档信息面板中显示的添加自定义属性**

Aspose.Cells可用于在工作簿对象中添加可在文档信息面板中看到的自定义属性。您可以使用Microsoft Excel中的文件 > 信息 > 属性 > 显示文档面板菜单命令打开文档信息面板。

请使用[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)方法添加一个可在文档信息面板中看到的自定义属性。

以下示例代码添加了两个自定义属性。第一个属性没有任何类型，第二个属性的类型为DateTime。一旦您打开此代码生成的输出Excel文件，您将在文档信息面板中看到这两个属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddingCustomPropertiesVisible-1.cs" >}}

### **相关文章**

{{% alert color="primary" %}}

- [在Aspose.Cells中使用自定义XML部件](/cells/zh/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
