---
title: Hur man sätter punkt som totalsumma med Golang via C++
linktitle: Hur man ställer in punkt som total
description: I vissa Excel diagram, till exempel vattenfallsdiagram, kan du behöva ställa in punkt som totalsumma. Denna artikel beskriver hur man använder Aspose.Cells med Golang via C++ för att göra det.
keywords: Vattenfallsdiagram, punkt, ställ in som total.
type: docs
weight: 72
url: /sv/go-cpp/how-to-set-point-as-total/
---

## Vad är "Ställ in punkt som total" i Excel-diagram

I vissa Excel-diagram, till exempel vattenfall-diagram, är vissa datapunkter summan av de föregående punkterna, och du kan behöva "ställer in punkten som total". Vi visar exempel på kod och illustration nedan.

## Ett vattenfallsdiagram behöver "Ställa in punkt som total" 

![todo:image_alt_text](set-as-total1.png)

Denna bild visar ett vattenfall-diagram i Excel. Vi kan se att det finns fyra datapunkter som börjar med "Total", och de används för att räkna alla föregående datapunkter.
I denna bild är inställningarna inte helt rätt, när vi väljer en punkt "Total 2024" och kan se att alternativet "Ställ som total" inte är markerat i Excel.
Bifogat nedan finns [exempelfilen Excel](SampleSheet.xlsx) som behöver ändras, och vi kommer att använda Aspose.Cells för att ställa in den korrekt.

## Använd Aspose.Cells för "Ställ in punkten som total" 

Vi använder följande kod för att få filen att ställas in korrekt:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetPointAsTotal.go" >}}
Du kan få följande rätta [utdatafil](output.xlsx)

Som visas i figuren nedan är de fyra "Total"-datapunkterna korrekt inställda, och du kan se skillnaden från föregående diagram.

![todo:image_alt_text](set-as-total2.png)
