---
title: Stöd layouten för DIV-taggar när du laddar HTML till Excel-arbetsbok
type: docs
weight: 770
url: /sv/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---
{{% alert color="primary" %}} 

 Normalt ignoreras layouten för div-taggar när HTML läses in i ett Excel-arbetsboksobjekt. Men om du vill att layouten för div-taggar inte ska ignoreras, ställ in[HtmlLoadOptions.SupportDivTag](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#SupportDivTag) egendom till**Sann** . Standardvärdet för den här egenskapen är**falsk**.

{{% /alert %}} 
## **Stöd layouten för DIV-taggar när du laddar HTML till Excel-arbetsbok**
 Följande exempelkod illustrerar användningen av[HtmlLoadOptions.SupportDivTag](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#SupportDivTag) fast egendom. Vänligen ladda ner[Aspose Logotyp](5473442.png) används i HTML-inmatningen och[output excel-fil](5473439.xlsx) genereras av koden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-SupportthelayoutofDIVtags-1.java" >}}
