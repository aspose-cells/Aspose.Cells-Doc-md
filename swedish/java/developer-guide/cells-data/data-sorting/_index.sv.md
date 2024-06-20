---
title: Data Sortering
type: docs
weight: 90
url: /sv/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

Data sortering är en av Microsoft Excels många användbara funktioner. Den gör det möjligt för användare att ordna data för att göra det enklare att skanna.

Aspose.Cells tillåter dig att sortera kalkylbladsdata i alfabetisk eller numerisk ordning. Det fungerar på samma sätt som Microsoft Excel gör för att sortera data.

{{% /alert %}}

## **Sortering av data i Microsoft Excel**

För att sortera data i Microsoft Excel:

1. Välj **Data** från **Sortera**-menyn.
   Sorteringsdialogrutan visas.
1. Välj ett sorteringsalternativ.

I allmänhet utförs sortering på en lista - definierad som en sammanhängande grupp data där data visas i kolumner.

Sorteringsdialogrutan i Microsoft Excel

![todo:image_alt_text](data-sorting_1.png)

## **Sortera data med Aspose.Cells**

Aspose.Cells tillhandahåller [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)-klassen som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel metoder som [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1)...[**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) och [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1)...[**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). Dessa medlemmar används för att definiera sorterade nycklar och ange sorteringsordning för nyckeln.

Du måste definiera nycklar och ange sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller metoden [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) som används för att utföra datasortering baserat på celldata i ett arbetsblad.

Metoden [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) accepterar följande parametrar:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), arbetsbladets celler.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), cellområdet. Definiera cellområdet innan du tillämpar datasortering.

Detta exempel visar hur man sorterar data med hjälp av Aspose.Cells API. Exemplet använder en mallfil "Book1.xls" och sorterar data för dataraden (A1:B14) på det första arket:

Detta exempel använder mallfilen "Book1.xls" skapad i Microsoft Excel.

Mall för Excel-fil komplett med data

![todo:image_alt_text](data-sorting_2.png)

Efter att koden nedan har körts är data sorterad korrekt som du kan se från den utdata Excel-filen.

Utdata Excel-fil efter sorteringsdata

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

För att sortera *VänsterTillHöger*, använd [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight)-attributen.

{{% /alert %}}

## **Sortera data med bakgrundsfärg**

Excel tillhandahåller funktionen att sortera data baserat på bakgrundsfärg. Samma funktion tillhandahålls med hjälp av Aspose.Cells med [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter), där [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) kan användas i [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) för att sortera data baserat på bakgrundsfärg. Alla celler som innehåller angiven färg i [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int))-funktionen placeras överst eller längst ned enligt SortOrder-inställningen och ordningen för resten av cellerna ändras inte alls.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Fortsatta ämnen**
- [Sortera Data i Kolumn med Anpassad Sorteringslista](/cells/sv/java/sort-data-in-column-with-custom-sort-list/)
- [Angivande av sorteringsvarning vid sortering av data](/cells/sv/java/specifying-sort-warning-while-sorting-data/)

