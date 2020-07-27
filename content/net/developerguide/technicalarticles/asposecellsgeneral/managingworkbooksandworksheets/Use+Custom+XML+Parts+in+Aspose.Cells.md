+++
title = "Use Custom XML Parts in Aspose.Cells" 
description = "" 
weight = 20460 
+++

Aspose.Cells for .NET : Use Custom XML Parts in Aspose.Cells  

# Aspose.Cells for .NET : Use Custom XML Parts in Aspose.Cells


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Using Custom XML Parts in Aspose.Cells](#UseCustomXMLPartsinAspose.Cells-UsingCustomXMLPartsinAspose.Cells)
    *   1.1 [Related Article](#UseCustomXMLPartsinAspose.Cells-RelatedArticle)
{{< /panel >}}
 

 

## Using Custom XML Parts in Aspose.Cells

Custom XML Parts are the XML data that is stored by different applications like SharePoint etc inside the excel file. This data is consumed by different applications that need it. Microsoft Excel does not make use of this data so there is no GUI to add it. You can view this data by changing the extension of **.xlsx** into **.zip** and then by opening it using **WinZip**. You can also open the ZIP file using any 3rd part Windows zip utility such as WinRAR or WinZip etc. The data is present inside the **customXml** folder.

You can add custom XML parts using Aspose.Cells via the [Workbook.ContentTypeProperties.Add()](https://apireference.aspose.com/net/cells/aspose.cells.properties/contenttypepropertycollection/methods/add/index) method.

The following sample code makes use of [Workbook.ContentTypeProperties.Add()](https://apireference.aspose.com/net/cells/aspose.cells.properties/contenttypepropertycollection/methods/add/index) method and adds the **Book Catalog XML** and its name is **BookStore**. The following image shows the result of this code. As you can see Book Catalog XML is added inside the BookStore node which is the name of this property.

  
![](https://docs2.aspose.com/cells/net/attachments/5018956/5115249.png)![](https://docs2.aspose.com/cells/net/attachments/5018956/5115250.png)

### Related Article

*   [Adding Custom Properties visible inside Document Information Panel](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/asposecellsgeneral/managingworkbooksandworksheets/adding+custom+properties+visible+inside+document+information+panel)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [custom-xml-parts-location.png](https://docs2.aspose.com/cells/net/attachments/5018956/5115249.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [BookStore-XML-Part.png](https://docs2.aspose.com/cells/net/attachments/5018956/5115250.png) (image/png)  

