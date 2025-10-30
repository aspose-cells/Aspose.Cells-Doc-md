---
title: Hämta det största området i ett blad med Golang via C++
linktitle: Få maxintervall i ett arbetsblad
type: docs
weight: 360
url: /sv/go-cpp/get-max-range-in-a-worksheet/
description: Denna artikel beskriver hur man får det maximala området, max dataintervall, max visningsintervall av Excel filer med Aspose.Cells for C++ biblioteket.
---

{{% alert color="primary" %}} 

När vi läser data från arket behöver vi känna till det maximala området.

När vi kopierar all data från ett ark behöver vi känna till det maximala området.

När du exporterar ett specificerat område till HTML och PDF behöver vi känna till det maximala området.

Aspose.Cells for C++ innehåller olika sätt att hitta det maximala området i ett kalkylblad. 

{{% /alert %}} 

## **Får maximalt intervall**
I Aspose.Cells, om objekten [**Row**](https://reference.aspose.com/cells/go-cpp/row/) och [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) är initialiserade, kommer dessa rader och kolumner att räknas till det maximala området, även om det inte finns någon data i tomma rader eller kolumner.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **Får maximalt datointervall**
I de flesta fall behöver vi bara få alla intervall som innehåller all data, även om de tomma cellerna utanför intervallet är formaterade.
Och inställningarna för former, tabeller och pivottabeller kommer att ignoreras.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **Får maximalt visningsintervall**
När vi exporterar all data från arket till HTML, PDF eller bilder behöver vi få ett område som innehåller alla synliga objekt, inklusive data, stilar, grafik, tabeller och pivottabeller.
Följande kodexempel visar hur man renderar det maximala visningsområdet till HTML:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
Här är [källa excel-fil](Book1.xlsx).
