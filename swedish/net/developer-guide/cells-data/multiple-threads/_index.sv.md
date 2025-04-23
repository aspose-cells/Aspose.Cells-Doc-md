---
title: Läs cellvärden i flera trådar samtidigt
linktitle: Flera trådar
type: docs
weight: 1800
url: /sv/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Lär dig hur man läser cellvärden i flera trådar samtidigt genom Aspose.Cells for .NET API.
keywords: Läs cellvärden i flera trådar samtidigt, Aspose.Cells C# Flertalet trådar, Läs data i flera trådar
---

{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur man använder Aspose.Cells för detta ändamål.

{{% /alert %}}

För att läsa cellvärden i mer än en tråd samtidigt, ange [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) till **true**. Om du inte gör det kan du få felaktiga cellvärden.

Följande kod:

1. Skapar en arbetsbok.
1. Lägger till en arbetsblad.
1. Fyller arbetsbladet med strängvärden.
1. Skapar sedan två trådar som samtidigt läser värden från slumpmässiga celler.
   Om de lästa värdena är korrekta händer ingenting. Om de lästa värdena är inkorrekta visas ett meddelande.

Om du kommenterar denna rad:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

visas sedan följande meddelande:

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

I annat fall körs programmet utan att visa något meddelande, vilket betyder att alla värden som läses från cellerna är korrekta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
