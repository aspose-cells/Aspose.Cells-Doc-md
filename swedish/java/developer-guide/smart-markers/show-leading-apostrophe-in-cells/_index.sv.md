---
title: Visa ledande apostrofer i celler
type: docs
weight: 20
url: /sv/java/show-leading-apostrophe-in-cells/
---

## **Visa ledande apostrofer i celler**

I Microsoft Excel är den ledande apostrofen i cellens värde dold. Aspose.Cells erbjuder funktionen att visa apostrofen som standard. För detta tillhandahåller API:et egenskapen [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle). Denna egenskap indikerar om man ska ställa in [**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix) egenskapen när man anger en textvärde som börjar med en enkel citation till cellen. Inställning av [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle) egenskapen till **falskt** kommer att visa den ledande apostrofen i den resulterande Excelfilen.

Följande skärmbild visar den resulterande Excelfilen med den synliga apostrofen.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Följande kodsnutt demonstrerar detta genom att lägga till data med Smart Markers i källan för Excel-filen. Käll- och utsprungsfiler för Excel är bifogade för referens.

[Källfil](AllowLeadingApostropheSample.xlsx)

[Utskriftsfiltyp](AllowLeadingApostropheSample_out.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

Implementeringen av klassen *DataObject* ges nedan

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
{{< app/cells/assistant language="java" >}}
