---
title: Infoga och ta bort rader och kolumner
type: docs
weight: 60
url: /sv/java/inserting-and-deleting-rows-and-columns/
description: Lär dig hur man infogar och tar bort rader och kolumner genom Aspose.Cells for Java API er.
keywords: Hur man infogar och tar bort rader och kolumner i Java, Infoga rader och kolumner med Java, Ta bort rader och kolumner i Java, Infoga rader eller kolumner med Java, Ta bort rader eller kolumner via Java.
---

## **Introduktion**
Oavsett om du skapar en ny arbetsbok från grunden eller arbetar med en befintlig arbetsbok kan vi behöva lägga till extra rader eller kolumner för att rymma mer data. Å andra sidan kan det också hända att vi behöver ta bort rader eller kolumner från angivna positioner i arbetsboken.

För att uppfylla dessa krav tillhandahåller Aspose.Cells en mycket enklaste uppsättning klasser och metoder, som diskuteras nedan.
## **Hur man hanterar rader/kolumner**
Aspose.Cells tillhandahåller en [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som ger åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-kollektion som representerar alla celler i arbetsbladet.

Samlingen [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) tillhandahåller flera metoder för att hantera rader och kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}} 

När rader eller kolumner läggs till förflyttas innehållet i arbetsbladet nedåt eller åt höger, men om rader eller kolumner tas bort förflyttas innehållet uppåt eller åt vänster.

{{% /alert %}} 
## **Hur man infogar en rad**
Infoga en rad på vilken plats som helst genom att anropa metoden [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. Metoden [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) tar indexet för den rad där den nya raden ska infogas som första argument, och antalet rader att infoga som andra argument.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Hur man infogar flera rader**
För att infoga flera rader i arbetsbladet, anropa metoden [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. Metoden [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) tar två parametrar:

- Radindex: index för raden där de nya raderna ska sättas in.
- Antal rader: det totala antalet rader som behöver sättas in.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Hur man infogar en rad med formatering**
För att infoga en rad med formateringsalternativ, använd överlastningen [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) som tar [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) som parameter. Ställ in egenskapen [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) av [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) klassen till [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) enum. [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) enum har tre medlemmar som listas nedan.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): Formaterar raden som ovanstående rad.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW): Formaterar raden som nedanstående rad.
- [RENSA](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Rensar formateringen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Hur man tar bort en rad**
För att ta bort en rad på vilken plats som helst, ring [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) metoden i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. Metoden [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) tar två parametrar:

- Radindex: index för raden från vilken raderna kommer att tas bort.
- Antal rader: det totala antalet rader som ska tas bort.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Hur man tar bort flera rader**
För att ta bort flera rader från ett arbetsblad, ring [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) metoden i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Metoden [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) tar två parametrar:

- Radindex: index för raden från vilken raderna kommer att tas bort.
- Antal rader: det totala antalet rader som ska tas bort.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Hur man sätter in en eller flera kolumner**
Utvecklare kan också infoga en kolumn i arbetsbladet på vilken plats som helst genom att anropa metoden [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Metoden [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) tar två parametrar:

- Kolumnindex, index av kolumn där kolumnen ska infogas
- Antal kolumner, det totala antalet kolumner som behöver sättas in

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Hur man tar bort en kolumn**
För att ta bort en kolumn från arbetsbladet på vilken plats som helst, ring [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) metoden i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Metoden [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) tar följande parametrar:

- Kolumnindex: index för kolumnen från vilken kolumnen kommer att tas bort.
- Antal kolumner: det totala antalet kolumner som ska tas bort.
- Uppdatera referens: Boolesk parameter för att ange om referenser i andra arbetsblad ska uppdateras.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
