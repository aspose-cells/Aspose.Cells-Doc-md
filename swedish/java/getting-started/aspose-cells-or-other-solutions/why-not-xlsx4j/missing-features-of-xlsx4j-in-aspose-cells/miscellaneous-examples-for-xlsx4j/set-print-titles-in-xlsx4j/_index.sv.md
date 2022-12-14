---
title: Ställ in Skriv ut titlar i xlsx4j
type: docs
weight: 40
url: /sv/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - Ställ in trycktitlar**
Aspose.Cells låter dig ange rad- och kolumnrubriker som ska upprepas på alla sidor i ett utskrivet kalkylblad. För att göra det, använd[Utskriftsformat](/java/PageSetup)class'setPrintTitleColumns och setPrintTitleRows egenskaper.

Raderna eller kolumnerna som kommer att upprepas definieras genom att skicka deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

 För mer information, besök[Ställa in utskriftsalternativ](/cells/sv/java/page-setup-features/#setting-print-options).

{{% /alert %}}
