---
title: Lägg till anpassade XML delar och välj dem efter ID
type: docs
weight: 70
url: /sv/net/add-custom-xml-parts-and-select-them-by-id/
---

## **Möjliga användningsscenario**

Anpassade XML-delar är XML-data som lagras inne i Microsoft Excel-dokument och används av de applikationer som hanterar dem. Det finns för närvarande inget direkt sätt att lägga till dem med Microsoft Excel UI. Du kan dock lägga till dem programmatiskt på olika sätt t.ex. med VSTO, med Aspose.Cells osv. Använd [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) metoden om du vill lägga till anpassade XML-delar med Aspose.Cells API. Du kan också ställa in dess ID med hjälp av [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) egenskapen. På samma sätt, om du vill välja anpassad XML-del efter ID, kan du använda [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) metoden.

## **Lägg till anpassade XML-delar och välj dem efter ID**

Följande exempelkod lägger först till fyra anpassade XML-delar med [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) metoden. Den ställer sedan in deras ID:er med [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) egenskapen. Slutligen hittar eller väljer den ena av de tillagda anpassade XML-delarna med [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) metoden. Se även konsoloutputen för koden nedan som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
