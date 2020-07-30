---
title : "Using Custom XML Parts in Aspose.Cells" 
description : "" 
weight : 12524 
toc : false
type: docs
url: /java/developerguide/technicalarticles/using+custom+xml+parts+in+aspose.cells/
---

# Aspose.Cells for Java : Using Custom XML Parts in Aspose.Cells


Custom XML Parts are the XML data which is stored by different applications like SharePoint etc inside the excel file. This data is consumed by different applications that need it. Microsoft Excel does not make use of this data so there is no GUI to add it. You can view this data by changing the extension of **.xlsx** into **.zip** and then by opening it using **WinRAR**. The data is present inside the **customXml** folder as shown in this image.

![](https://docs2.aspose.com/cells/java/attachments/5276110/5472481.png)

You can add custom XML parts using Aspose.Cells via the [Workbook.getContentTypeProperties().add()](https://apireference.aspose.com/java/cells/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) method.

#### Using Custom Xml Parts in Aspose.Cells

The following sample code makes use of [Workbook.getContentTypeProperties().add()](https://apireference.aspose.com/java/cells/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) method and adds the **Book Catalog Xml** and its name is **BookStore**. The following image shows the result of this code. As you can see Book Catalog Xml is added inside the BookStore node which is the name of this property.

![](https://docs2.aspose.com/cells/java/attachments/5276110/5472480.png)


#### Related Article

*   [Adding Custom Properties visible inside Document Information Panel](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/mngworkbooksandworksheets/adding+custom+properties+visible+inside+document+information+panel)

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [BookStore-XML-Part.png](https://docs2.aspose.com/cells/java/attachments/5276110/5472480.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [custom-xml-parts-location.png](https://docs2.aspose.com/cells/java/attachments/5276110/5472481.png) (image/png)  

