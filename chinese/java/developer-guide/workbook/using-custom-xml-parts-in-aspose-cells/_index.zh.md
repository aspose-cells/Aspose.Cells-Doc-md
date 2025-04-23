---
title: 在Aspose.Cells中使用自定义XML部件
type: docs
weight: 570
url: /zh/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

自定义XML部件是由不同应用程序（如SharePoint等）存储在Excel文件中的XML数据。这些数据被需要的不同应用程序消耗。Microsoft Excel不使用此数据，因此没有GUI添加它。您可以通过将**.xlsx**的扩展名更改为**.zip**，然后使用**WinRAR**打开来查看这些数据。数据位于**customXml**文件夹中，如此图所示。

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

可以通过 Aspose.Cells 使用 [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) 方法添加自定义 XML 部件。

{{% /alert %}} 
## **在Aspose.Cells中使用自定义XML部件**
以下示例代码使用 [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) 方法添加了书籍目录 Xml，名称为 BookStore。结果显示，Book Catalog Xml 被添加到名为 BookStore 的节点内，如图所示。

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **相关文章**
{{% alert color="primary" %}} 

- [在文档信息面板中可见的自定义属性](/cells/zh/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
