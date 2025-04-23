---
title: Visa ledande apostrofer i celler
type: docs
weight: 70
url: /sv/net/show-leading-apostrophe-in-cells/
---

I Microsoft Excel är den ledande apostrofen i cellens värde dold. Aspose.Cells tillhandahåller funktionen för att visa apostrofen som standard. För detta erbjuder API:et egenskapen [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle). Denna egenskap indikerar om du vill ställa in egenskapen [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) när du skriver in strängvärdet som börjar med ett enkelt citattecken i cellen. Genom att ställa in [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) till **false** kommer den ledande apostrofen att visas i utmatningsfilen för Excel.

Följande skärmbild visar den resulterande Excelfilen med den synliga apostrofen.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Följande kodsnutt demonstrerar detta genom att lägga till data med Smart Markers i källan för Excel-filen. Käll- och utsprungsfiler för Excel är bifogade för referens.

[Källfil](98107425.xlsx)

[Utmatningsfil](98107426.xlsx)
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

Implementeringen av klassen *DataObject* ges nedan

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
