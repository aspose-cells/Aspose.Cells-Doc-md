---
title: Hur man skriver ut Excel som anpassade sidor breda och höga
type: docs
weight: 200
url: /sv/java/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Denna artikel visar kod som förklarar hur man ställer in FitToPagesWide och FitToPagesTall med Aspose.Cells biblioteket.
keywords: Java Hur man ställer in FitToPagesWide och FitToPagesTall, hur man lägger till FitToPagesWide och FitToPagesTall i Java, hur man ställer in FitToPagesWide och FitToPagesTall i Excel, hur man rensar FitToPagesWide och FitToPagesTall i Excel, hur man skriver ut Excel som passande sidor i bredd och höjd, hur man skriver ut arbetsblad som en sida, hur man skriver ut alla kolumner i arbetsbladet på en sida.
---

## **Introduktion**

FitToPagesWide och FitToPagesTall-inställningarna används i kalkylprogram (som Microsoft Excel) för att styra hur ett kalkylblad skalas när det skrivs ut. Dessa inställningar hjälper till att säkerställa att ditt utskrivna utskriftsresultat passar inom ett specificerat antal sidor, både horisontellt och vertikalt. Här är en översikt av varje inställning:

1. FitToPagesWide: Denna inställning specificerar antalet sidor brett som utskriften ska passa in i. Till exempel, att ställa in FitToPagesWide till 1 innebär att innehållet skalas för att passa inom en enkel sidbredde, oavsett hur brett kalkylbladet är.
1. FitToPagesTall: Denna inställning specificerar antalet sidor högt som utskriften ska passa in i. Till exempel, att ställa in FitToPagesTall till 1 innebär att innehållet skalas för att passa inom en enkel sidhöjd, oavsett antalet rader.

## **Varför använda FitToPagesWide och FitToPagesTall**
Här är några skäl att ställa in FitToPagesWide och FitToPagesTall:
1. Kontroll över utskriftslayout: Genom att specificera antalet sidor brett och högt kan du säkerställa att din utskrivna dokument är lätt att läsa och välorganiserad, utan att kolumner eller rader delas på ett oönskat sätt över sidor.
1. Konsistens: Om du skriver ut flera blad eller rapporter hjälper dessa inställningar till att bibehålla ett konsekvent format, vilket gör det enklare att jämföra och analysera utskrivna dokument.
1. Professionell presentation: Att skala och passa innehållet till ett specificerat antal sidor kan resultera i en mer professionell och polerad presentation av dina data.

## **Hur man skriver ut filen som anpassade sidor breda och höga i Excel**

För att ställa in FitToPagesWide och FitToPagesTall i Microsoft Excel, följ dessa steg:

1. Öppna ditt Excel-arbetsbok och gå till det blad du vill skriva ut.
1. Gå till fliken Sidlayout på bandet.
1. I gruppen Sidinställningar, klicka på den lilla pilen längst ner till höger för att öppna dialogrutan Sidinställningar.
1. I dialogrutan Sidinställningar, gå till fliken Sida.
1. Under Skalning, välj alternativet "Anpassa till" och specificera sedan antalet sidor brett och högt du vill: Ange antalet sidor brett du vill i den första boxen (Anpassa till x sidor brett). Ange antalet sidor högt du vill i den andra boxen (Anpassa till y sidor högt).
<br>
<img src="2.png" width=60% />

1. Klicka på OK för att tillämpa inställningarna.


## **Hur man skriver ut Excel som anpassade sidor brett och högt med Aspose.Cells**

För att ställa in FitToPagesWide och FitToPagesTall i ett angivet blad: Först, ladda [exempelfilen](input.xlsx), och sedan måste du anropa [**Worksheet.PageSetup.setFitToPagesTall(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesTall-int-) och [**Worksheet.PageSetup.setFitToPagesWide(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesWide-int-) metoderna av [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/) objektet för det önskade bladet. Här är ett exempel i Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.java" >}}

Utmatningsresultat:
<br>
<img src="1.png" width=60% />

## **Hur man skriver ut blad som en sida med Aspose.Cells**

För att skriva ut arbetsblad som en sida: Först, ladda [exempelfilen](sample.xlsx), och sedan måste du anropa [**PdfSaveOptions.setOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setOnePagePerSheet-boolean-) metoden av [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/) objektet. Här är ett exempel i Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-OnePagePerSheet.java" >}}

Utmatningsresultat:
<br>
<img src="3.png" width=60% />


## **Hur man skriver ut alla kolumner i ett blad på en sida med Aspose.Cells**

För att skriva ut alla kolumner i ett arbetsblad på en sida: Först, ladda [exempelfilen](sample.xlsx), och sedan måste du anropa [**PdfSaveOptions.setAllColumnsInOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setAllColumnsInOnePagePerSheet-boolean-) metoden av [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/) objektet. Här är ett exempel i Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.java" >}}

Utmatningsresultat:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="java" >}}
