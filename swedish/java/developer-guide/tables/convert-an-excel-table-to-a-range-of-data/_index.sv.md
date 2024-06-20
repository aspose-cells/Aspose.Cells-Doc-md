---
title: Konvertera en Excel tabell till en datamängd.
type: docs
weight: 10
url: /sv/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten den kommer med. Istället vill du ha något som ser ut som en tabell. För att behålla data i en tabell utan att förlora formateringen, konvertera tabellen till en vanlig datamängd.

Aspose.Cells stödjer denna funktion i Microsoft Excels tabeller och listobjekt.

{{% /alert %}}

## **Använda Microsoft Excel**

Använd **Konvertera till område**-funktionen för att snabbt konvertera en tabell till en mängd utan att förlora formateringen. I Microsoft Excel 2007/2010:

1. Klicka var som helst i tabellen för att se till att den aktiva cellen är i en tabellkolumn.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. På fliken **Utformning**, i gruppen **Verktyg**, klicka på **Konvertera till område**.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till en mängd. Till exempel inkluderar radrubrikerna inte längre sorterings- och filterpilar, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler omvandlas till vanliga cellreferenser.

{{% /alert %}}

## **Använda Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Konvertera tabell till område med alternativ.**

Aspose.Cells tillhandahåller ytterligare alternativ vid konvertering av tabell till område genom klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions). Klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) tillhandahåller egenskapen [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow) som möjliggör att du anger den sista indexeringen av tabellraden. Tabellformateringen behålls upp till den angivna radindexeringen och resten av formateringen tas bort.

Den angivna provkoden nedan visar användningen av klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
