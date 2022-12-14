---
title: Datasortering
type: docs
weight: 90
url: /sv/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

Datasortering är en av Microsoft Excels många användbara funktioner. Det låter användare beställa data för att göra det lättare att skanna.

Aspose.Cells låter dig sortera kalkylbladsdata alfabetiskt eller numeriskt. Det fungerar på samma sätt som Microsoft Excel gör för att sortera data.

{{% /alert %}}

## **Sortera data i Microsoft Excel**

Så här sorterar du data i Microsoft Excel:

1.  Välj**Data** från**Sortera** meny.
 Dialogrutan Sortera visas.
1. Välj ett sorteringsalternativ.

I allmänhet utförs sortering på en lista - definierad som en sammanhängande grupp av data där data visas i kolumner.

**Dialogrutan Sortera i Microsoft Excel**

![todo:image_alt_text](data-sorting_1.png)

## **Sortera data med Aspose.Cells**

 Aspose.Cells tillhandahåller[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) klass som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel metoder som[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) och[**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)Dessa medlemmar används för att definiera sorterade nycklar och specificera nyckelsorteringsordningen.

 Du måste definiera nycklar och ställa in sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller[**sortera**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) metod som används för att utföra datasortering baserat på celldata i ett kalkylblad.

 De[**sortera**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) metod accepterar följande parametrar:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), cellerna i kalkylbladet.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), cellintervallet. Definiera cellområdet innan du tillämpar datasortering.

Det här exemplet visar hur man sorterar data med Aspose.Cells API. Exemplet använder en mallfil "Book1.xls" och sorterar data för dataintervall (A1:B14) i det första kalkylbladet:

Det här exemplet använder mallfilen "Book1.xls" skapad i Microsoft Excel.

**Mall Excel-fil komplett med data**

![todo:image_alt_text](data-sorting_2.png)

Efter att ha kört koden nedan sorteras data på lämpligt sätt som du kan se från utdata Excel-filen.

**Utdata Excel-fil efter sortering av data**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 Att sortera*Vänster till höger* , Använd[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight)attribut.

{{% /alert %}}

## **Sortera data med bakgrundsfärg**

 Excel tillhandahåller funktionen för att sortera data baserat på bakgrundsfärgen. Samma funktion tillhandahålls med hjälp av Aspose.Cells[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) var[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) kan användas i[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) för att sortera data baserat på bakgrundsfärgen. Alla celler som innehåller specificerad färg i[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), placeras funktionen på toppen eller botten enligt SortOrder-inställningen och ordningen på resten av cellerna ändras inte alls.

Följande är exempelfilerna som kan laddas ner för att testa den här funktionen:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Förhandsämnen**
- [Sortera data i kolumn med anpassad sorteringslista](/cells/sv/java/sort-data-in-column-with-custom-sort-list/)
- [Ange sorteringsvarning vid sortering av data](/cells/sv/java/specifying-sort-warning-while-sorting-data/)

