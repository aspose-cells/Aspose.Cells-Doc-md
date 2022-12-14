---
title: Skriva ut arbetsböcker
type: docs
weight: 20
url: /sv/java/printing-workbooks/
description: Hur du skriver ut kalkylblad och arbetsbok med Java. Den här artikeln innehåller Java-koden för att skriva ut kalkylblad och arbetsbok med Aspose.Cells för Java API.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklarna förståelse (på ett kompakt sätt) om hur man skriver ut kalkylblad.

{{% /alert %}}

## Användningsscenario

När du har skapat ditt kalkylblad vill du antagligen skriva ut en papperskopia av bladet för ditt behov. När du skriver ut antar MS Excel att du vill skriva ut hela kalkylbladet om du inte anger ditt val. Följande skärmdump visar dialogrutan för utskrift av arbetsbok med Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**Figur:** Dialogrutan Skriv ut

## Skriva ut arbetsböcker med Aspose.Cells

 Aspose.Cells för Java tillhandahåller en[**till skrivaren**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) metod för[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) klass. Genom att använda[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String))-metoden kan du ange skrivarnamnet och utskriftsjobbets namn.

## Exempelkod

### Skriv ut valt arbetsblad

Följande kodavsnitt visar användningen av[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) metod för att skriva ut ditt valda kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Skriv ut hela arbetsboken

 Du kan också använda[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) metod för att skriva ut hela arbetsboken. Följande kodavsnitt visar användningen av[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)metod för att skriva ut hela arbetsboken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## relaterade artiklar

- [Ange jobb- eller dokumentnamn vid utskrift med Aspose.Cells](/cells/sv/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
