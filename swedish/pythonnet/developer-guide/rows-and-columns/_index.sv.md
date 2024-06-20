---
title: Formatera rader och kolumner
linktitle: Rader och kolumner
type: docs
weight: 100
url: /sv/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells för Python via .NET kan stödja ändring av radhöjd eller kolumnbredd, samt tillämpa formatering på rader eller kolumner.
keywords: Python Excel Library, Python Adjust row height and column width, Python Set row height and column width, Python ändra radhöjden eller kolumbredden, Python formatera rader och kolumner, Python hur man ställer in radhöjd och kolumnbredd.
---


{{% alert color="primary" %}}

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på rader eller bredden på kolumner. Ibland innebär att tillämpa formatering på rader eller kolumner att den aktuella höjden eller bredden behöver ändras för att visa datan. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med Microsoft Excel. Men med Aspose.Cells för Python via .NET kan utvecklare utföra dessa operationer under körning.

{{% /alert %}}

## **Arbeta med rader**

### **Hur man justerar radhöjden**

Aspose.Cells for Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) som representerar alla celler i kalkylbladet.

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan mer detaljerat.

### **Hur man ställer in höjden på en rad**

Det är möjligt att ställa in höjden på en enskild rad genom att anropa [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) metoden på [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) samlingen. Metoden [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) tar följande parametrar som följer:

- **rad**, indexet för den rad du ändrar höjden på.
- **höjd**, radhöjden att tillämpa på raden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **Hur man ställer in höjden på alla rader i ett kalkylblad**

Om utvecklare behöver ange samma radhöjd för alla rader i kalkylbladet kan de göra det genom att använda [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) egenskapen för [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) samlingen.

**Exempel:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **Arbeta med kolumner**

### **Hur man ställer in bredden på en kolumn**

Ställ in bredden på en kolumn genom att anropa [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) metoden på [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) samlingen. Metoden [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) tar följande parametrar:

- **kolumn**, index för den kolumn som du ändrar bredden på.
- **bredd**, önskad kolumnbredd.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **Hur man ställer in kolumnbredd i pixlar**

Ange kolumnbredden genom att ringa in samlingens [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) metoden [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int). Metoden [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) tar följande parametrar:

- **kolumn**, index för den kolumn som du ändrar bredden på.
- **pixlar**, önskad kolumnbredd i pixlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **Hur man ställer in bredden på alla kolumner i en arbetsbok**

För att ställa in samma kolumnbredd för alla kolumner i arbetsboken, använd samlingens [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) egenskap [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **Fortsatta ämnen**
- [AutoAnpassa rader och kolumner](/cells/sv/python-net/autofit-rows-and-columns/)
- [Konvertera Text till Kolumner med Aspose.Cells](/cells/sv/python-net/convert-text-to-columns-using-aspose-cells/)
- [Kopiera rader och kolumner](/cells/sv/python-net/copying-rows-and-columns/)
- [Ta bort tomma rader och kolumner i en arbetsbok](/cells/sv/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppering och avgruppering av rader och kolumner](/cells/sv/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Dölja och visa rader och kolumner](/cells/sv/python-net/hiding-and-showing-rows-and-columns/)
- [Infoga eller ta bort rader i en Excel-arbetsbok](/cells/sv/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Infoga och ta bort rader och kolumner i Excel-fil](/cells/sv/python-net/inserting-and-deleting-rows-and-columns/)
- [Ta bort dubblettrader i ett kalkylblad](/cells/sv/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad](/cells/sv/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
