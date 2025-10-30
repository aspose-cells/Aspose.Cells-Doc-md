---
title: Använd anpassade XML delar i Aspose.Cells med Golang via C++
linktitle: Använd anpassade XML delar
type: docs
weight: 390
url: /sv/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Lär dig hur du använder anpassade XML delar i Excel filer programmässigt med Aspose.Cells med Golang via C++.
---

## Användning av anpassade XML-delar i Aspose.Cells

Anpassade XML-delar är XML-data som lagras av olika applikationer som SharePoint innanför en Excel-fil. Denna data används av olika applikationer som behöver den. Microsoft Excel använder inte denna data, så det finns ingen GUI för att lägga till den. Du kan se denna data genom att byta filändelsen på **.xlsx** till **.zip** och öppna den med **WinZip**. Du kan även öppna ZIP-filen med vilken third-party Windows-zip-arkivhanterare som helst, exempelvis WinRAR eller WinZip. Data finns i mappen **customXml**.

Du kan lägga till anpassade XML-delar med Aspose.Cells via [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) metoden.

Följande exempel använder metoden [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) för att lägga till **Book Catalog XML**, som heter **BookStore**. Bilden nedan visar resultatet av denna kod. Som du kan se är Book Catalog XML tillagt inuti BookStore-noden, vilket är namnet på denna egenskap.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++-kod för att använda anpassade XML-delar

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## Relaterad artikel

- [Lägga till synliga anpassade egenskaper inuti dokumentinformationen](/cells/sv/cpp/adding-custom-properties-visible-inside-document-information-panel/)
