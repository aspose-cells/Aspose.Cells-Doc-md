---
title: Läser Cell Värden i flera trådar samtidigt
linktitle: Flera trådar
type: docs
weight: 1100
url: /sv/java/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur du använder Aspose.Cells för detta ändamål.

{{% /alert %}}

 För att läsa cellvärden i mer än en tråd samtidigt, ställ in[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) till**Sann**Om du inte gör det kan du få fel cellvärden. Observera att vissa funktioner som formatering av cellvärden inte stöds för flera trådar. Så med MultiThreadReading kan du bara komma åt cellens ursprungliga data. Om du försöker få cellens formaterade värde i en miljö med flera trådar, till exempel med Cell.getStringValue() för numeriska värden, kan du få oväntade resultat eller undantag.

Följande kod:

1. Skapar en arbetsbok.
1. Lägger till ett kalkylblad.
1. Fyller kalkylbladet med strängvärden.
1. Den skapar sedan två trådar som samtidigt läser värden från slumpmässiga celler.
 Om de avlästa värdena är korrekta händer ingenting. Om de avlästa värdena är felaktiga visas ett meddelande.

Om du kommenterar den här raden:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

då visas följande meddelande:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Annars körs programmet utan att visa något meddelande vilket betyder att alla värden som läses från celler är korrekta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
