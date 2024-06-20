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
Sätt in en rad på vilken plats som helst genom att ringa [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) metoden från [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. [insertRows ](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) metoden tar indexet för raden där den nya raden ska sättas in som det första argumentet och antalet rader som ska sättas in som det andra argumentet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Hur man infogar flera rader**
För att sätta in flera rader i arbetsbladet, ring [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) metoden från [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) metoden tar två parametrar:

- Radindex: index för raden där de nya raderna ska sättas in.
- Antal rader: det totala antalet rader som behöver sättas in.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Hur man infogar en rad med formatering**
För att sätta in en rad med formateringsalternativ, använd [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) överbelastningen som tar [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) som ett parameter. Ställ in [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) egenskapen i [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) klassen med [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Uppräkning. [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Uppräkningen har tre medlemmar som listas nedan.

- [SAMA_SOM_NÄMND](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Formaterar raden likadan som ovanstående rad.
- [SAMA_SOM_NEDAN](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): Formaterar raden likadan som nedanstående rad.
- [RENSA](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Rensar formateringen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Hur man tar bort en rad**
För att ta bort en rad på vilken plats som helst, ring [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metoden från [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metoden tar två parametrar:

- Radindex: index för raden från vilken raderna kommer att tas bort.
- Antal rader: det totala antalet rader som ska tas bort.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Hur man tar bort flera rader**
För att ta bort flera rader från ett arbetsblad, ring [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metoden från [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metoden tar två parametrar:

- Radindex: index för raden från vilken raderna kommer att tas bort.
- Antal rader: det totala antalet rader som ska tas bort.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Hur man sätter in en eller flera kolumner**
Utvecklare kan också sätta in en kolumn i arbetsbladet på vilken plats som helst genom att ringa [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) metoden från [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) metoden tar två parametrar:

- Kolumnindex, index av kolumn där kolumnen ska infogas
- Antal kolumner, det totala antalet kolumner som behöver sättas in

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Hur man tar bort en kolumn**
För att ta bort en kolumn från arbetsbladet på vilken plats som helst, ring [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) metoden från [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) metoden tar följande parametrar:

- Kolumnindex: index för kolumnen från vilken kolumnen kommer att tas bort.
- Antal kolumner: det totala antalet kolumner som ska tas bort.
- Uppdatera referens: Boolesk parameter för att ange om referenser i andra arbetsblad ska uppdateras.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

