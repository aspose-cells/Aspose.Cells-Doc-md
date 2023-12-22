---
title: Infoga och ta bort rader och kolumner
type: docs
weight: 60
url: /sv/java/inserting-and-deleting-rows-and-columns/
description: "Lär dig hur du infogar och tar bort rader och kolumner via API:erna Aspose.Cells for Java."
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **Introduktion**
Oavsett om vi skapar ett nytt kalkylblad från början eller arbetar med ett befintligt kalkylblad, kan vi behöva lägga till extra rader eller kolumner för att ta emot mer data. Omvänt kan vi också behöva ta bort rader eller kolumner från angivna positioner i kalkylbladet.

För att uppfylla dessa krav tillhandahåller Aspose.Cells en mycket enklaste uppsättning klasser och metoder, som diskuteras nedan.
##  **Hur man hanterar rader/kolumner**
 Aspose.Cells tillhandahåller en[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)samling som representerar alla celler i kalkylbladet.

 De[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)samling innehåller flera metoder för att hantera rader och kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}} 

När rader eller kolumner läggs till flyttas innehållet i kalkylbladet nedåt eller åt höger, men om rader eller kolumner tas bort flyttas innehållet uppåt eller åt vänster.

{{% /alert %}} 
##  **Hur man infogar en rad**
 Infoga en rad på valfri plats genom att anropa[infoga rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. De[infoga rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))-metoden tar indexet för raden där den nya raden kommer att infogas som det första argumentet, och antalet rader som ska infogas som det andra argumentet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **Hur man infogar flera rader**
 För att infoga flera rader i kalkylbladet, anropa[infoga rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. De[infoga rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) metod tar två parametrar:

- Radindex: indexet för raden varifrån de nya raderna kommer att infogas.
- Antal rader: det totala antalet rader som behöver infogas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **Hur man infogar en rad med formatering**
För att infoga en rad med formateringsalternativ, använd[infoga rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)överbelastning som tar[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)som en parameter. Ställ in[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)egendom av[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)klass med[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Uppräkning. De[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Enumeration har tre medlemmar enligt nedan.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Formaterar raden på samma sätt som raden ovan.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): Formaterar raden på samma sätt som under raden.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Rensar formateringen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **Hur man tar bort en rad**
 Om du vill ta bort en rad på valfri plats ringer du[ta bort rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. De[ta bort rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metod tar två parametrar:

- Radindex: indexet för raden där raderna kommer att tas bort.
- Antal rader: det totala antalet rader som måste raderas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **Hur man tar bort flera rader**
 För att ta bort flera rader från ett kalkylblad, anropa[ta bort rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. De[ta bort rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metod tar två parametrar:

- Radindex: indexet för raden där raderna kommer att tas bort.
- Antal rader: det totala antalet rader som måste raderas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **Hur man infogar en eller flera kolumner**
 Utvecklare kan också infoga en kolumn i kalkylbladet var som helst genom att anropa[infoga kolumner](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling. De[infoga kolumner](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) metod tar två parametrar:

- Kolumnindex, indexet för den kolumn varifrån kolumnen kommer att infogas
- Antal kolumner, det totala antalet kolumner som behöver infogas

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **Hur man tar bort en kolumn**
 För att ta bort en kolumn från kalkylbladet på valfri plats, ring till[radera kolumner](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. De[radera kolumner](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) metod tar följande parametrar:

- Kolumnindex: indexet för den kolumn där kolumnen kommer att tas bort.
- Antal kolumner: det totala antalet kolumner som måste raderas.
- Uppdatera referens: Boolesk parameter för att indikera om referenser i andra kalkylblad ska uppdateras.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

