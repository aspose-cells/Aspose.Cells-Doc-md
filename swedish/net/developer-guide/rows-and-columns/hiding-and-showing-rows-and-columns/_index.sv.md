---
title: Dölja och visa rader och kolumner
type: docs
weight: 60
url: /sv/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

Ibland är det meningsfullt att dölja vissa rader eller kolumner i en arbetsbok och sedan visa dem senare. Microsoft Excel tillhandahåller den här funktionen och så gör även Aspose.Cells.

{{% /alert %}}

## **Kontrollera synligheten av rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som gör det möjligt för utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av  [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen.  [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen tillhandahåller en  [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling som representerar alla celler i arbetsbladet.  [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingen tillhandahåller flera metoder för hantering av rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

### **Dölja rader och kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa  [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) och  [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metoderna i respektive samling. Båda metoderna tar rad- och kolumnindex som parameter för att gömma den specifika raden eller kolumnen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Visa rader och kolumner**

Utvecklare kan visa vilken som helst dold rad eller kolumn genom att anropa  [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) och [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) orden samling respektive metoder. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, om du behöver återställa den till tidigare tilldelad bredd eller till dess originalbredd, vänligen avdölj kolumnen med negativ bredd. Till exempel: arbetsblad.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Dölja flera rader och kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa  [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) och [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) orden i respektive samling. Båda metoderna tar startindex för rad eller kolumn och antalet rader eller kolumner som ska döljas som parametrar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Det är också möjligt att använda  {1} klassens  {2} och {3} metoder för att göra flera rader och kolumner synliga.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
