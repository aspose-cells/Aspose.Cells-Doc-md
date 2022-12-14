---
title: Konvertera en Excel-tabell till en rad data
type: docs
weight: 10
url: /sv/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten som den kommer med. Istället vill du ha något som ser ut som ett bord. Om du vill behålla data i en tabell utan att förlora formatering konverterar du tabellen till ett vanligt dataintervall.

Aspose.Cells stöder den här funktionen i Microsoft Excel för tabeller och listobjekt.

{{% /alert %}}

## **Använder Microsoft Excel**

 Använd**Konvertera till Range** funktion för att snabbt konvertera en tabell till ett intervall utan att förlora formatering. I Microsoft Excel 2007/2010:

1. Klicka var som helst i tabellen för att se till att den aktiva cellen finns i en tabellkolumn.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1.  På**Design** fliken, i**Verktyg** grupp, klicka**Konvertera till Range**.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till ett intervall. Till exempel innehåller radrubriker inte längre sortering- och filterpilarna, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler förvandlas till vanliga cellreferenser.

{{% /alert %}}

## **Använder Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Konvertera tabell till intervall med alternativ**

Aspose.Cells ger ytterligare alternativ när du konverterar tabell till intervall genom[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)klass. De[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)klass ger[**Sista raden**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)egenskap som låter dig ställa in det sista indexet för tabellraden. Tabellformateringen kommer att behållas upp till det angivna radindexet och resten av formateringen kommer att tas bort.

Exempelkoden nedan visar användningen av[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)klass.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
