---
title: Use Custom XML Parts in Aspose.Cells
type: docs
weight: 390
url: /net/use-custom-xml-parts-in-aspose-cells/
---

## Using Custom XML Parts in Aspose.Cells

Custom XML Parts are the XML data that is stored by different applications like SharePoint etc. inside the excel file. This data is consumed by different applications that need it. Microsoft Excel does not make use of this data so there is no GUI to add it. You can view this data by changing the extension of **.xlsx** into **.zip** and then by opening it using **WinZip**. You can also open the ZIP file using any 3rd part Windows zip utility such as WinRAR or WinZip etc. The data is present inside the **customXml** folder.

You can add custom XML parts using Aspose.Cells via the [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) method.

The following sample code makes use of [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) method and adds the **Book Catalog XML** and its name is **BookStore**. The following image shows the result of this code. As you can see Book Catalog XML is added inside the BookStore node which is the name of this property.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C# code to use custom XML parts

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Related Article

- [Adding Custom Properties visible inside Document Information Panel](/cells/net/adding-custom-properties-visible-inside-document-information-panel/)
