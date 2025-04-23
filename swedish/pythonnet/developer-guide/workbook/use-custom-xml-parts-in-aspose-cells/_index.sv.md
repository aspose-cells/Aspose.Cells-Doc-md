---
title: Använd anpassade XML delar i Aspose.Cells
type: docs
weight: 390
url: /sv/python-net/use-custom-xml-parts-in-aspose-cells/
---

## Använda anpassade XML-delar i Aspose.Cells för Python via .NET

Anpassade XML-delar är XML-data som lagras av olika program som SharePoint etc. inuti excelfilen. Denna data konsumeras av olika applikationer som behöver den. Microsoft Excel använder inte den här datan så det finns ingen GUI för att lägga till den. Du kan se denna data genom att ändra förlängningen **.xlsx** till **.zip** och sedan genom att öppna den med **WinZip**. Du kan också öppna ZIP-filen med hjälp av valfri 3: e parts Windows zip-verktyg som WinRAR eller WinZip etc. Datan finns inuti mappen **customXml**.

Du kan lägga till anpassade XML-delar med hjälp av Aspose.Cells via [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str) metoden.

Följande exempelkod använder [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str) metoden och lägger till **Book Catalog XML** och dess namn är **BookStore**. Följande bild visar resultatet av denna kod. Som du kan se läggs Book Catalog XML till inuti BookStore noden som är namnet på den här egenskapen.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C# kod för att använda anpassade XML-delar

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-UsingCustomXmlParts.py" >}}



