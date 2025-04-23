---
title: Ange intervallsram
type: docs
weight: 600
url: /sv/java/set-range-border/
---

## **Möjliga användningsscenario**
När du vill ange en ram för ett intervall behöver du inte ange varje cell individuellt. Du kan ange ramen för intervallet. Aspose.Cells erbjuder denna funktion.
Denna artikel ger en kodexempel som använder Aspose.Cells för att ange intervallsramen.

## **Ange intervallsram i Excel**
För att ställa in gränsen för en serie i Excel kan du följa dessa steg:
1. Välj det cellområde där du vill tillämpa gränsen.
2. I fliken "Start" på menyfliksområdet, leta upp gruppen "Teckenformat".
3. Inom gruppen "Teckenformat", klicka på knappen "Gränser".
<br>
<img src="border.png" />
4. Välj den typ av gräns som du vill använda från alternativen i rullgardinsmenyn. Du kan välja mellan förinställda gränstyper eller anpassa din egen gräns.
5. När du har valt önskad gränstil kommer gränsen att appliceras på det valda cellområdet.

## **Ställ in gränslinje med hjälp av Aspose.Cells**
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Skapa en [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/range/).
1. Ange den inre gränsen för området.
1. Ange den yttre gränsen för området.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Range-set-border.java" >}}
{{< app/cells/assistant language="java" >}}
