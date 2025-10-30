---
title: Lägg till anpassade XML delar och välj dem med hjälp av ID med Golang via C++
linktitle: Lägg till anpassade XML delar och välj dem efter ID
type: docs
weight: 70
url: /sv/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Lär dig hur man lägger till och väljer anpassade XML delar i Excel filer med Aspose.Cells med Golang via C++.
---

## **Möjliga användningsscenario**

Anpassade XML-delar är XML-data som lagras inuti Microsoft Excel-dokument och används av applikationer som interagerar med dem. Det finns för närvarande ingen direkt metod att lägga till dem via Microsoft Excel UI. Du kan dock lägga till dem programmatiskt på olika sätt, exempelvis med VSTO eller Aspose.Cells. Använd [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)-metoden för att lägga till en anpassad XML-del med Aspose.Cells API. Du kan även ställa in dess ID med [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-egenskapen. På samma sätt, om du vill välja en anpassad XML-del efter ID, kan du använda [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-metoden.

## **Lägg till anpassade XML-delar och välj dem efter ID**

Följande exempel lägger först till fyra anpassade XML-delar med [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)-metoden. Den ställer sedan in deras ID med [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-egenskapen. Slutligen hittar eller väljer den en av de tillagda XML-delarna med [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-metoden. Se också kodens konsolutdata nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Konsoloutput**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
