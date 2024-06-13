---
title: 在文档信息面板中显示添加的自定义属性
type: docs
weight: 500
url: /zh/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells可以用于向工作簿对象中添加可在文档信息面板中看到的自定义属性。您可以使用Microsoft Excel中的文件 > 信息 > 属性 > 显示文档面板菜单命令打开文档信息面板。

请使用[**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object))方法添加可在文档信息窗格中看到的自定义属性。

{{% /alert %}}

## **示例**

以下示例代码添加了两个自定义属性。第一个属性没有任何类型，并且第二个属性是DateTime类型。一旦您打开此代码生成的输出Excel文件，您将在文档信息面板中看到这两个属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **相关文章**

{{% alert color="primary" %}}

- [在Aspose.Cells中使用自定义XML部件](/cells/zh/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
