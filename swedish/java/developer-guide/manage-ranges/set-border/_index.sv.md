---
title: Ställ in intervallgräns
type: docs
weight: 600
url: /sv/net/set-range-border/
---
##  **Möjliga användningsscenarier**
När du vill ställa in gränsen för Range, behöver du inte ställa in varje cell individuellt. Du kan ställa in gränsen för intervallet. Aspose.Cells erbjuder denna funktion.
Den här artikeln innehåller en exempelkod som använder Aspose.Cells för att ställa in intervallgräns.

##  **Ställ in intervallgräns i Excel**
För att ställa in gränsen för ett intervall i Excel, kan du följa dessa steg:
1. Välj intervallet av celler som du vill använda gränsen på.
2. På fliken "Hem" i menyfliksområdet, leta upp gruppen "Teckensnitt".
3. I gruppen "Teckensnitt", klicka på rullgardinsknappen "Kanter".
<br>
<img src="border.png" />
4. Välj den typ av kantlinje som du vill använda från alternativen i rullgardinsmenyn. Du kan välja mellan förinställda kantstilar eller anpassa din egen kant.
5. När du har valt önskad kantstil kommer kanten att tillämpas på det valda cellområdet.

##  **Ställ in intervallgräns med Aspose.Cells**
Det här exemplet visar hur man:

1. Skapa en arbetsbok.
1. Lägg till data i celler i det första kalkylbladet.
1.  Skapa en[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Ställ in den inre gränsen för Range.
1. Ange den yttre gränsen för Range.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-set-border.cs" >}}