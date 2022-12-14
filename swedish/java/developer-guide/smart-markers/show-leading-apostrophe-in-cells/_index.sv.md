---
title: Visa ledande apostrof i celler
type: docs
weight: 20
url: /sv/java/show-leading-apostrophe-in-cells/
---
## **Visa ledande apostrof i celler**

I Microsoft Excel är den ledande apostrof i cellens värde dold. Aspose.Cells tillhandahåller funktionen för att visa apostrof som standard. För detta tillhandahåller API[**Arbetsbok.Inställningar.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)fast egendom. Den här egenskapen anger om du ska ställa in[**CitatPrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)egenskap när du anger ett strängvärde som börjar med ett enda citattecken i cellen. Ställa in[**Arbetsbok.Inställningar.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)egendom till**falsk**kommer att visa den inledande apostrof i excel-filen.

Följande skärmdump visar utdata excel-filen med den synliga apostrof.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Följande kodavsnitt visar detta genom att lägga till data med Smart Markers i källexcelfilen. Käll- och utdata Excel-filerna bifogas som referens.

[Källfilen](AllowLeadingApostropheSample.xlsx)

[Utdatafil](AllowLeadingApostropheSample_out.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

Genomförandet av*DataObject*klass ges nedan

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
