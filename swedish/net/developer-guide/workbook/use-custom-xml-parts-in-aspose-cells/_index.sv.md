---
title: Använd anpassade XML-delar i Aspose.Cells
type: docs
weight: 390
url: /sv/net/use-custom-xml-parts-in-aspose-cells/
---
## Använda anpassade XML-delar i Aspose.Cells

 Anpassade XML-delar är XML-data som lagras av olika applikationer som SharePoint etc. inuti excel-filen. Denna data konsumeras av olika applikationer som behöver den. Microsoft Excel använder inte denna data så det finns inget GUI för att lägga till det. Du kan se denna data genom att ändra tillägget av**.xlsx** in i**.blixtlås** och sedan genom att öppna den med hjälp av**WinZip** . Du kan också öppna ZIP-filen med hjälp av valfritt 3:e del Windows zip-verktyg som WinRAR eller WinZip etc. Datan finns i**customXml** mapp.

 Du kan lägga till anpassade XML-delar med Aspose.Cells via[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)metod.

 Följande exempelkod använder sig av[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) metod och lägger till**Bokkatalog XML** och dess namn är**Bokhandel**Följande bild visar resultatet av denna kod. Som du kan se läggs bokkatalog-XML till inuti BookStore-noden som är namnet på den här egenskapen.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C#-kod för att använda anpassade XML-delar

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Relaterad artikel

- [Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen](/cells/sv/net/adding-custom-properties-visible-inside-document-information-panel/)
