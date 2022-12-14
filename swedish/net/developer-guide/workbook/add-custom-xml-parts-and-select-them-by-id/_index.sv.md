---
title: Lägg till anpassade XML-delar och välj dem efter ID
type: docs
weight: 70
url: /sv/net/add-custom-xml-parts-and-select-them-by-id/
---
## **Möjliga användningsscenarier**

Anpassade XML-delar är XML-data som lagras i Microsoft Excel-dokumenten och används av de applikationer som hanterar dem. Det finns inget direkt sätt att lägga till dem med hjälp av Microsoft Excel UI för tillfället. Du kan dock lägga till dem programmatiskt på olika sätt, t.ex. med VSTO, med Aspose.Cells etc. Använd[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) metod om du vill lägga till anpassad XML-del med Aspose.Cells API. Du kan också ställa in dess ID med hjälp av[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)fast egendom. På samma sätt, om du vill välja anpassad XML-del efter ID, kan du använda[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)metod.

## **Lägg till anpassade XML-delar och välj dem efter ID**

Följande exempelkod lägger först till fyra anpassade XML-delar med hjälp av[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)metod. Den ställer sedan in deras ID med hjälp av[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) fast egendom. Slutligen hittar eller väljer den en av de tillagda anpassade XML-delarna med hjälp av[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)metod. Se även konsolutgången för koden nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
