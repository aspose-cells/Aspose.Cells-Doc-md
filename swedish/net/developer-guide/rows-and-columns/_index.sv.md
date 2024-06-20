---
title: Formatera rader och kolumner
linktitle: Rader och kolumner
type: docs
weight: 100
url: /sv/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET kan stödja ändra radhöjd eller kolumnbredd, samt tillämpa formatering på rader eller kolumner.
keywords: Ange radhöjd och kolumnbredd, Justera radhöjd och kolumnbredd, ändra radhöjd eller kolumnbredd, formatera rader och kolumner, hur man anger radhöjd och kolumnbredd.
---


{{% alert color="primary" %}}

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på rader eller bredden på kolumner. Ibland innebär tillämpning av formatering på rader eller kolumner att den aktuella höjden eller bredden behöver ändras för att visa datan. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med Microsoft Excel. Med Aspose.Cells kan utvecklare dock utföra dessa operationer vid körningstid.

{{% /alert %}}

## **Arbeta med rader**

### **Hur man justerar radhöjden**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling som representerar alla celler i kalkylbladet.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan mer detaljerat.

### **Hur man ställer in höjden på en rad**

Det är möjligt att ställa in höjden på en enskild rad genom att anropa [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) metoden på [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingen. Metoden [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) tar följande parametrar som följer:

- **Radindex**, index för den rad vars höjd du ändrar.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Hur man ställer in höjden på alla rader i ett kalkylblad**

Om utvecklare behöver ange samma radhöjd för alla rader i kalkylbladet kan de göra det genom att använda [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) egenskapen för [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) samlingen.

**Exempel:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Arbeta med kolumner**

### **Hur man ställer in bredden på en kolumn**

Ställ in bredden på en kolumn genom att anropa [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) metoden på [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingen. Metoden [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) tar följande parametrar:

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Hur man ställer in kolumnbredd i pixlar**

Ange kolumnbredden genom att ringa in samlingens [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) metoden [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel). Metoden [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) tar följande parametrar:

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd i pixlar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Hur man ställer in bredden på alla kolumner i en arbetsbok**

För att ställa in samma kolumnbredd för alla kolumner i arbetsboken, använd samlingens [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) egenskap [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Fortsatta ämnen**
- [AutoAnpassa rader och kolumner](/cells/sv/net/autofit-rows-and-columns/)
- [Konvertera Text till Kolumner med Aspose.Cells](/cells/sv/net/convert-text-to-columns-using-aspose-cells/)
- [Kopiera rader och kolumner](/cells/sv/net/copying-rows-and-columns/)
- [Ta bort tomma rader och kolumner i en arbetsbok](/cells/sv/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppering och avgruppering av rader och kolumner](/cells/sv/net/grouping-and-ungrouping-rows-and-columns/)
- [Dölja och visa rader och kolumner](/cells/sv/net/hiding-and-showing-rows-and-columns/)
- [Infoga eller ta bort rader i en Excel-arbetsbok](/cells/sv/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Infoga och ta bort rader och kolumner i Excel-fil](/cells/sv/net/inserting-and-deleting-rows-and-columns/)
- [Ta bort dubblettrader i ett kalkylblad](/cells/sv/net/remove-duplicate-rows-in-a-worksheet/)
- [Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad](/cells/sv/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
