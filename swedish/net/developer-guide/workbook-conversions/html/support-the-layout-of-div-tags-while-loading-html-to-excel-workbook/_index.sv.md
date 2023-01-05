---
title: Stöd layouten för DIV-taggar när du laddar HTML till Excel-arbetsboken
type: docs
weight: 50
url: /sv/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---
{{% alert color="primary" %}} 

Normalt ignoreras layouten för div-taggar när HTML läses in i ett Excel-arbetsboksobjekt. Men om du vill att layouten för div-taggar inte ska ignoreras, ställ in[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) egendom till**Sann** . Standardvärdet för den här egenskapen är**falsk**.

{{% /alert %}} 

 Följande exempelkod illustrerar användningen av[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) fast egendom. Vänligen ladda ner[Aspose Logotyp](5115218.png) används inuti ingången HTML och[output excel-fil](5115220.xlsx) genereras av koden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
