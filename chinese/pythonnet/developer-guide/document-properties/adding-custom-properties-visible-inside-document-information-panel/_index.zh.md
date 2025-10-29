---
title: 在文档信息面板中显示添加的自定义属性
type: docs
weight: 300
url: /zh/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **在文档信息面板中可见的自定义属性**

 Aspose.Cells for Python via .NET 可以在工作簿对象中添加自定义属性，这些属性在文档信息面板中可见。 使用 Microsoft Excel 的 文件 > 信息 > 属性 > 显示文档面板菜单命令即可打开文档信息面板。

请使用 [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add) 方法添加可在文档信息面板中看到的自定义属性

以下示例代码添加了两个自定义属性。第一个属性没有任何类型，并且第二个属性是DateTime类型。一旦您打开此代码生成的输出Excel文件，您将在文档信息面板中看到这两个属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **相关文章**

{{% alert color="primary" %}}

- [在Aspose.Cells中使用自定义XML部分](/cells/zh/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
