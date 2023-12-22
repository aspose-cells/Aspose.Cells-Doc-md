---
title: Hur man använder färgpalett
type: docs
weight: 80
url: /sv/net/excel-color-palette/
description: C# kod för att lägga till anpassade färger till paletten och använd excel färgpalett med Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **Färger och palett**

En palett är antalet tillgängliga färger för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa ett konsekvent utseende. Varje Microsoft Excel-fil (97-2003) har en palett med 56 färger som kan appliceras på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i ett diagram.

Med Aspose.Cells är det möjligt att inte bara använda palettens befintliga färger utan även anpassade färger. Innan du använder en anpassad färg, lägg till den i paletten först.

Det här ämnet diskuterar hur man lägger till anpassade färger till paletten.

##  **Lägg till anpassade färger till paletten**

Aspose.Cells stöder Microsoft Excels 56 färgpalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass ger en[**Ändra palett**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

- Custom Color, den anpassade färgen som ska läggas till.
- Index, indexet för färgen i paletten som den anpassade färgen kommer att ersätta. Bör vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) till paletten innan den appliceras på ett teckensnitt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg till paletten ändras paletten och alla element i filen som formaterats med föregående färg ändras. Så var mycket försiktig när du ändrar paletten. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast eftersom det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}