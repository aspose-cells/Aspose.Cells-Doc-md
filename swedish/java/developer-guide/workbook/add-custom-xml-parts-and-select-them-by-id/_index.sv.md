---
title: Lägg till anpassade XML delar och välj dem efter ID
type: docs
weight: 10
url: /sv/java/add-custom-xml-parts-and-select-them-by-id/
---

## **Möjliga användningsscenario**

Anpassade XML-delar är XML-data som lagras i Microsoft Excel-dokument och används av de applikationer som hanterar dem. Det finns för närvarande inget direkt sätt att lägga till dem med hjälp av Microsoft Excel UI. Du kan dock lägga till dem programmatiskt på olika sätt t.ex. med *VSTO*, med *Aspose.Cells* osv. Använd gärna [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-) om du vill lägga till anpassad XML-del med Aspose.Cells API. Du kan även ställa in dess ID med hjälp av [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID) egenskapen. På samma sätt, om du vill välja anpassad XML-del efter ID, kan du använda [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-) metoden.

## **Lägg till anpassade XML-delar och välj dem efter ID**

Den följande provkoden lägger först till fyra anpassade XML-delsar med [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-) metoden. Därefter ställer den in deras ID:n med [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID) egenskapen. Slutligen hittar eller väljer den ena av de tillagda anpassade XML-delarna med [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-) metoden. Se även konsolens utmatning av koden nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
