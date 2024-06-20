---
title: Läs cellvärden i flera trådar samtidigt
linktitle: Flera trådar
type: docs
weight: 1100
url: /sv/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Lär dig hur man läser cellvärden i flera trådar samtidigt med Aspose.Cells for Java API er.
keywords: Java Läs cellvärden i flera trådar samtidigt, Flera trådar för Aspose.Cells for Java API er.
---

{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur man använder Aspose.Cells för detta ändamål.

{{% /alert %}}

## **Hur man läser cellvärden i flera trådar samtidigt med Aspose.Cells for Java**

För att läsa cellvärden i flera trådar samtidigt, sätt [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) till **true**. Om du inte gör det kan du få felaktiga cellvärden. Observera att vissa funktioner, såsom formatering av cellvärden, inte stöds för flera trådar. Så MultiThreadReading gör det bara möjligt att komma åt cellens ursprungliga data. I en flera-trådar-miljö om du försöker hämta cellens formaterade värde, till exempel med Cell.getStringValue() för numeriska värden, kan du få oväntat resultat eller undantag.

Följande kod:

1. Skapar en arbetsbok.
1. Lägger till en arbetsblad.
1. Fyller arbetsbladet med strängvärden.
1. Skapar sedan två trådar som samtidigt läser värden från slumpmässiga celler.
   Om de lästa värdena är korrekta händer ingenting. Om de lästa värdena är inkorrekta visas ett meddelande.

Om du kommenterar denna rad:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

visas sedan följande meddelande:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

I annat fall körs programmet utan att visa något meddelande, vilket betyder att alla värden som läses från cellerna är korrekta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
