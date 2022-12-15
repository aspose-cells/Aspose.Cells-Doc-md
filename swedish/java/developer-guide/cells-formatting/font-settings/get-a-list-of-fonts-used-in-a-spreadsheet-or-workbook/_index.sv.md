---
title: Få en lista över teckensnitt som används i ett kalkylblad eller en arbetsbok
type: docs
weight: 20
url: /sv/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Möjliga användningsscenarier**

 Det är ofta nödvändigt att känna till typsnitten som används i din arbetsbok för renderingsändamål. När du konverterar din arbetsbok till PDF eller bild, kräver Aspose.Cells att alla nödvändiga teckensnitt är installerade på ditt system eller finns i din**teckensnittskatalog**Om Aspose.Cells inte kan hitta det önskade teckensnittet, försöker den ersätta det med något annat lämpligt teckensnitt som finns på ditt system eller i din teckensnittskatalog och kan ersätta ditt faktiska teckensnitt. Detta resulterar inte bara i oönskad rendering av PDF eller bilder utan tar också bearbetningstid för att hitta lämpliga typsnitt.

För att hantera sådana fall bör du veta vilka typsnitt som används av din arbetsbok och sedan antingen installera dessa typsnitt på ditt system i fallet med Windows-miljön eller placera det i din typsnittskatalog i fall av Windows- eller Linux-miljö.

 Aspose.Cells tillhandahåller[Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()) metod som returnerar listan över alla teckensnitt som används i din arbetsbok eller kalkylblad.

## **Få en lista över teckensnitt som används i ett kalkylblad eller en arbetsbok**

 Följande exempelkod laddar källexcelfilen och hämtar listan över teckensnitt som används i den. Den har ett dummy-arbetsblad som har några dummy-teckensnitt som lagts till i illustrationssyfte. När koden skriver ut alla teckensnitt i arbetsboken, skriver den också ut dessa dummy-teckensnitt. Följande skärmdump visar[exempel på excel-fil](sampleGetFonts.xlsx)och hur dummy-teckensnitten är listade.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Konsolutgång**

 Här är konsolutgången för ovanstående exempelkod när den körs med den givna[exempel på excel-fil](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
