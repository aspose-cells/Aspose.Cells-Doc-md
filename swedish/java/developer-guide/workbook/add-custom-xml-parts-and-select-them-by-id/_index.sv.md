---
title: Lägg till anpassade XML-delar och välj dem efter ID
type: docs
weight: 10
url: /sv/java/add-custom-xml-parts-and-select-them-by-id/
---
## **Möjliga användningsscenarier**

Anpassade XML-delar är XML-data som lagras i Microsoft Excel-dokumenten och används av de applikationer som hanterar dem. Det finns inget direkt sätt att lägga till dem med hjälp av Microsoft Excel UI för tillfället. Du kan dock lägga till dem programmatiskt på olika sätt, t.ex*VSTO*, använder sig av*Aspose.Cells*etc. Använd gärna[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) om du vill lägga till anpassad XML-del med Aspose.Cells API. Du kan också ställa in dess ID med hjälp av[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)fast egendom. På samma sätt, om du vill välja anpassad XML-del efter ID, kan du använda[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) metod.

## **Lägg till anpassade XML-delar och välj dem efter ID**

Följande exempelkod lägger först till fyra anpassade XML-delar med hjälp av[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) metod. Det ställer sedan in deras ID med hjälp av[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)fast egendom. Slutligen hittar eller väljer den en av de tillagda anpassade XML-delarna med hjälp av[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) metod. Se även konsolutgången för koden nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
