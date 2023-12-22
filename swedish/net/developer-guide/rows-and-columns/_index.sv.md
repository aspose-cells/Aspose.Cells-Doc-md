---
title: Formatera rader och kolumner
linktitle: Rader och kolumner
type: docs
weight: 100
url: /sv/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET kan stödja ändra radhöjd eller kolumnbredd, samt tillämpa formatering på rader eller kolumner.
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på raderna eller bredden på kolumner. Ibland innebär formatering på rader eller kolumner att den aktuella höjden eller bredden måste ändras för att visa data. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med hjälp av Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer under körning.

{{% /alert %}}

##  **Arbeta med rader**

###  **Hur man justerar radhöjden**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling som representerar alla celler i kalkylbladet.

 De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras mer i detalj nedan.

###  **Hur man ställer in höjden på en rad**

 Det är möjligt att ställa in höjden på en enstaka rad genom att anropa[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingens[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) metod. De[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)metoden tar följande parametrar enligt följande:

- *Radindex**, indexet för raden som du ändrar höjden på.
- *Radhöjd**, radhöjden som ska tillämpas på raden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **Hur man ställer in höjden på alla rader i ett kalkylblad**

 Om utvecklare behöver ställa in samma radhöjd för alla rader i kalkylbladet kan de göra det genom att använda[**Standardhöjd**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) egendom av[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling.

**Exempel:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **Arbeta med kolumner**

###  **Hur man ställer in bredden på en kolumn**

 Ställ in bredden på en kolumn genom att anropa[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingens[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) metod. De[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)metoden tar följande parametrar:

- *Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- *Kolumnbredd**, önskad kolumnbredd.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **Hur man ställer in kolumnbredd i pixlar**

Ställ in bredden på en kolumn genom att anropa[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samlingens[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)metod. De[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)metoden tar följande parametrar:

- *Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- *Kolumnbredd**, önskad kolumnbredd i pixlar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **Hur man ställer in bredden på alla kolumner i ett kalkylblad**

 För att ställa in samma kolumnbredd för alla kolumner i kalkylbladet, använd[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingens[**Standardbredd**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **Förhandsämnen**
- [Autopassa rader och kolumner](/cells/sv/net/autofit-rows-and-columns/)
- [Konvertera text till kolumner med Aspose.Cells](/cells/sv/net/convert-text-to-columns-using-aspose-cells/)
- [Kopiera rader och kolumner](/cells/sv/net/copying-rows-and-columns/)
- [Ta bort tomma rader och kolumner i ett kalkylblad](/cells/sv/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppera och dela upp rader och kolumner](/cells/sv/net/grouping-and-ungrouping-rows-and-columns/)
- [Dölja och visa rader och kolumner](/cells/sv/net/hiding-and-showing-rows-and-columns/)
- [Infoga eller ta bort rader i ett Excel-kalkylblad](/cells/sv/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Infoga och ta bort rader och kolumner i Excel-fil](/cells/sv/net/inserting-and-deleting-rows-and-columns/)
- [Ta bort dubbletter av rader i ett kalkylblad](/cells/sv/net/remove-duplicate-rows-in-a-worksheet/)
- [Uppdatera referenser i andra kalkylblad samtidigt som du tar bort tomma kolumner och rader i ett kalkylblad](/cells/sv/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
