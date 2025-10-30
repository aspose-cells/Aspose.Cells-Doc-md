---
title: Ange kantlinje för område med Golang via C++
type: docs
weight: 600
url: /sv/go-cpp/set-range-border/
description: Lär dig hur du ställer in kantlinjer för områden med Aspose.Cells och Golang via C++.
---

## **Möjliga användningsscenario**
När du vill sätta gränsen för ett område behöver du inte ange varje cell individuellt. Du kan ställa in gränsen på hela området. Aspose.Cells erbjuder denna funktion. Denna artikel ger ett exempel på hur man använder Aspose.Cells för att sätta områdegräns.

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
2. Lägg till data i celler i första kalkylbladet.
3. Skapa en [**Range**](https://reference.aspose.com/cells/go-cpp/range).
4. Sätt inre gräns för område.
5. Sätt yttergräns för område.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetBorder.go" >}}
