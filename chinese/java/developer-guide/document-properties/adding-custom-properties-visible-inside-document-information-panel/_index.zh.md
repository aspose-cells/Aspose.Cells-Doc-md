---
title: 添加在文档信息面板内可见的自定义属性
type: docs
weight: 500
url: /zh/java/adding-custom-properties-visible-inside-document-information-panel/
---
{{% alert color="primary" %}}

Aspose.Cells 可用于在工作簿对象内添加自定义属性，这些属性在文档信息面板内可见。您可以使用文件 > 信息 > 属性 > 显示文档面板菜单命令在 Microsoft Excel 中打开文档信息面板。

请用[**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) 方法添加将在文档信息面板中可见的自定义属性

{{% /alert %}}

## **例子**

以下示例代码添加了两个自定义属性。第一个属性没有任何类型，第二个属性的类型为 DateTime。一次，您将打开此代码生成的输出 Excel 文件，您将在文档信息面板中看到这两个属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **相关文章**

{{% alert color="primary" %}}

- [在 Aspose.Cells 中使用自定义 XML 部件](/cells/zh/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
