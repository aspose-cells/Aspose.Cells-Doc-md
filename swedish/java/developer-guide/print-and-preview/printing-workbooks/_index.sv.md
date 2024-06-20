---
title: Skriv ut arbetsböcker
type: docs
weight: 20
url: /sv/java/printing-workbooks/
description: Hur man skriver ut kalkylblad och arbetsbok med hjälp av Java. Denna artikel tillhandahåller Javakod för att skriva ut kalkylblad och arbetsbok med Aspose.Cells for Java API.
keywords: skriva ut arbetsböcker, skriva ut kalkylblad, skriva ut kalkylbladssidor, skriv ut en arbetsbok, skriv ut arbetsbok java, skriv ut kalkylblad java, skriv ut excelarbetsbok java, skriv ut excelkalkylblad java, skriv ut arbetsbok, skriv ut kalkylblad
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklare förståelse (på ett kompakt sätt) om hur man skriver ut kalkylblad.

{{% /alert %}}

## Användningsscenarie

När du har skapat din kalkylblad färdigt, vill du förmodligen skriva ut ett pappersutskrift av kalkylbladet för ditt behov. När du skriver ut antar MS Excel att du vill skriva ut hela kalkylbladsområdet om du inte specificerar ditt urval. Följande skärmbild visar dialogrutan för att skriva ut arbetsbok med Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**Figur:** Dialogruta för Utskrift

## Skriv ut arbetsböcker med Aspose.Cells

Aspose.Cells for Java tillhandahåller en [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String))-metod av [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)-klassen. Genom att använda [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String))-metoden kan du ange skrivarnamn samt utskriftsuppgiftsnamn.

## Exempelkod

### Skriv ut markerat kalkylblad

Följande kodsax visar användningen av [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String))-metoden för att skriva ut ditt markerade kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Skriv ut hela arbetsboken

Du kan också använda [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String))-metoden för att skriva ut hela arbetsboken. Följande kodsax visar användningen av [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String))-metoden för att skriva ut hela arbetsboken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Relaterade artiklar

- [Ange jobb- eller dokumentnamn vid utskrift med Aspose.Cells](/cells/sv/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
