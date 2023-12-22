---
title: Läser Cell Värden i flera trådar samtidigt
linktitle: Flera trådar
type: docs
weight: 1800
url: /sv/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Lär dig hur du läser Cell-värden i flera trådar samtidigt genom Aspose.Cells for .NET API.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur du använder Aspose.Cells för detta ändamål.

{{% /alert %}}

 För att läsa cellvärden i mer än en tråd samtidigt, ställ in[**Arbetsblad.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)till *sant**. Om du inte gör det kan du få fel cellvärden.

Följande kod:

1. Skapar en arbetsbok.
1. Lägger till ett kalkylblad.
1. Fyller kalkylbladet med strängvärden.
1. Den skapar sedan två trådar som samtidigt läser värden från slumpmässiga celler.
 Om de avlästa värdena är korrekta händer ingenting. Om de avlästa värdena är felaktiga visas ett meddelande.

Om du kommenterar den här raden:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

då visas följande meddelande:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Annars körs programmet utan att visa något meddelande vilket betyder att alla värden som läses från celler är korrekta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
