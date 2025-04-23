---
title: Använd anpassade XML delar i Aspose.Cells
type: docs
weight: 390
url: /sv/net/use-custom-xml-parts-in-aspose-cells/
---

## Användning av anpassade XML-delar i Aspose.Cells

Anpassade XML-delar är XML-data som lagras av olika program som SharePoint etc. inuti excelfilen. Denna data konsumeras av olika applikationer som behöver den. Microsoft Excel använder inte den här datan så det finns ingen GUI för att lägga till den. Du kan se denna data genom att ändra förlängningen **.xlsx** till **.zip** och sedan genom att öppna den med **WinZip**. Du kan också öppna ZIP-filen med hjälp av valfri 3: e parts Windows zip-verktyg som WinRAR eller WinZip etc. Datan finns inuti mappen **customXml**.

Du kan lägga till anpassade XML-delar med hjälp av Aspose.Cells via [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) metoden.

Följande exempelkod använder [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) metoden och lägger till **Book Catalog XML** och dess namn är **BookStore**. Följande bild visar resultatet av denna kod. Som du kan se läggs Book Catalog XML till inuti BookStore noden som är namnet på den här egenskapen.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C# kod för att använda anpassade XML-delar

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Relaterad artikel

- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/net/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="csharp" >}}
