---
title: Using Custom XML Parts in Aspose.Cells
type: docs
weight: 570
url: /java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Custom XML Parts are the XML data which is stored by different applications like SharePoint etc inside the excel file. This data is consumed by different applications that need it. Microsoft Excel does not make use of this data so there is no GUI to add it. You can view this data by changing the extension of **.xlsx** into **.zip** and then by opening it using **WinRAR**. The data is present inside the **customXml** folder as shown in this image.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

You can add custom XML parts using Aspose.Cells via the [Workbook.getContentTypeProperties().add()](https://apireference.aspose.com/java/cells/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) method.

{{% /alert %}} 
#### **Using Custom Xml Parts in Aspose.Cells**
The following sample code makes use of [Workbook.getContentTypeProperties().add()](https://apireference.aspose.com/java/cells/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) method and adds the **Book Catalog Xml** and its name is **BookStore**. The following image shows the result of this code. As you can see Book Catalog Xml is added inside the BookStore node which is the name of this property.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
#### **Related Article**
{{% alert color="primary" %}} 

- [Adding Custom Properties visible inside Document Information Panel](/cells/java/adding-custom-properties-visible-inside-document-information-panel-html/)

{{% /alert %}}
