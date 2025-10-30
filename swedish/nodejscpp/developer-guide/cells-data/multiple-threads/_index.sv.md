---
title: Läs cellvärden i flera trådar samtidigt
linktitle: Flera trådar
type: docs
weight: 1800
url: /sv/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Lär dig hur du kan läsa cellvärden i flera trådar samtidigt via Aspose.Cells for Node.js via C++ API.
keywords: Läs cellvärden i flera trådar samtidigt Node.js via C++, Aspose.Cells C++ Flera trådar, Läs data i flera trådar
---

{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur man använder Aspose.Cells för detta ändamål.

{{% /alert %}}

För att läsa cellvärden i mer än en tråd samtidigt, sätt [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) till **true**. Om du inte gör det kan du få felaktiga cellvärden.

Följande kod:

1. Skapar en arbetsbok.
1. Lägger till en arbetsblad.
1. Fyller arbetsbladet med strängvärden.
1. Skapar sedan två trådar som samtidigt läser värden från slumpmässiga celler.
   Om de lästa värdena är korrekta händer ingenting. Om de lästa värdena är inkorrekta visas ett meddelande.

Om du kommenterar denna rad:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

visas sedan följande meddelande:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

I annat fall körs programmet utan att visa något meddelande, vilket betyder att alla värden som läses från cellerna är korrekta.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
