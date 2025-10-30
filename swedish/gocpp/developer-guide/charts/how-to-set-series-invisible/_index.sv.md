---
title: Hur man gör serie osynlig med Golang via C++
linktitle: Hur man sätter serien osynlig
description: I Excel diagram kan du behöva ställa in serie som osynlig. Denna artikel beskriver hur man använder Aspose.Cells med Golang via C++ för att göra det.
keywords: Excel diagram, Serie, Osynlig, ÄrFiltrerad.
type: docs
weight: 74
url: /sv/go-cpp/how-to-set-series-invisible/
---

## Hur man ställer in serie som osynlig i Excel-diagram

I Excel-diagram kan du högerklicka på ett diagram, klicka på "Välj data" och i pop-up-fönstret kan du ställa in om en serie är synlig genom att markera eller avmarkera den. Du kan ladda ner följande [exempelfil](SeriesFiltered.xlsx) och använda den i Excel enligt figuren för att uppnå denna funktion. Nästa steg är att visa dig hur du uppnår detta med Aspose.Cells-biblioteket.

![todo:image_alt_text](series-invisible.png)

## Hur man ställer in serie som osynlig med Aspose.Cells 

Vi använder följande kod för att göra serie osynlig med Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
Du kan hämta följande [Inmatningsfil](SeriesFiltered.xlsx) och [Utdatafil](output.xlsx).

Som visas i figuren nedan har de två första serierna, som ursprungligen var synliga, blivit osynliga i utdatafilen.  
![todo:image_alt_text](output.png)
