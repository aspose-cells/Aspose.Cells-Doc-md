---
title: 在Aspose.Cells中使用自定义XML部件
type: docs
weight: 570
url: /zh/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

自定义XML部件是由SharePoint等不同应用程序存储在Excel文件中的XML数据。这些数据由需要它们的不同应用程序使用。Microsoft Excel不使用此数据，因此没有GUI来添加它。您可以通过将**.xlsx**的扩展名更改为**.zip**，然后再使用**WinRAR**打开它来查看此数据。如此图所示，数据存在于**customXml**文件夹中。

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

您可以通过[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\))方法使用Aspose.Cells添加自定义XML部件。

{{% /alert %}} 
## **在Aspose.Cells中使用自定义XML部件**
以下示例代码使用[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\))方法，添加了**Book Catalog Xml**（其名称为**BookStore**）。以下图片显示了此代码的结果。正如您所见，Book Catalog Xml被添加到了名为BookStore的节点内，这是该属性的名称。

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **相关文章**
{{% alert color="primary" %}} 

- [在文档信息面板中显示的添加自定义属性](/cells/zh/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
