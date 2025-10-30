---
title: Ange intervallsram
type: docs
weight: 600
url: /sv/python-net/set-range-border/
description: Den här artikeln visar hur du anger intervallsram med hjälp av Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python ange intervallsram, Python lägg till intervallsram.
---

## **Möjliga användningsscenario**
När du vill ange en ram för intervall behöver du inte ange varje cell individuellt. Du kan ange ramen för intervallet. Aspose.Cells for Python via .NET erbjuder den här funktionen.
Den här artikeln tillhandahåller ett kodexempel som använder Aspose.Cells for Python via .NET för att ange intervallsram.

## **Hur man anger intervallsram i Excel**
För att ställa in gränsen för en serie i Excel kan du följa dessa steg:
1. Välj det cellområde där du vill tillämpa gränsen.
2. I fliken "Start" på menyfliksområdet, leta upp gruppen "Teckenformat".
3. Inom gruppen "Teckenformat", klicka på knappen "Gränser".
<br>
<img src="border.png" />
4. Välj den typ av gräns som du vill använda från alternativen i rullgardinsmenyn. Du kan välja mellan förinställda gränstyper eller anpassa din egen gräns.
5. När du har valt önskad gränstil kommer gränsen att appliceras på det valda cellområdet.

## **Hur man ställer in områdesgräns med Aspose.Cells för Python Excel Library**
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Skapa en [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Ange den inre gränsen för området.
1. Ange den yttre gränsen för området.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-set-border.py" >}}
{{< app/cells/assistant language="python-net" >}}
