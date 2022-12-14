---
title: Visa ledande apostrof i celler
type: docs
weight: 70
url: /sv/net/show-leading-apostrophe-in-cells/
---
 I Microsoft Excel är den ledande apostrof i cellens värde dold. Aspose.Cells tillhandahåller funktionen för att visa apostrof som standard. För detta tillhandahåller API[Arbetsbok.Inställningar.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) fast egendom. Den här egenskapen anger om du ska ställa in[CitatPrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)egenskap när du anger ett strängvärde som börjar med ett enda citattecken i cellen. Ställa in[Arbetsbok.Inställningar.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) egendom till**falsk**kommer att visa den inledande apostrof i excel-filen.

Följande skärmdump visar utdata excel-filen med den synliga apostrof.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Följande kodavsnitt visar detta genom att lägga till data med Smart Markers i källexcelfilen. Käll- och utdata Excel-filerna bifogas som referens.

[Källfilen](98107425.xlsx)

[Utdatafil](98107426.xlsx)
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

Genomförandet av*DataObject*klass ges nedan

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
