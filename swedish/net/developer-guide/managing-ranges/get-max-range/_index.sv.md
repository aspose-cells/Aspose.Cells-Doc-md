---
title: Få maxintervall i ett arbetsblad
type: docs
weight: 360
url: /sv/net/get-max-range-in-a-worksheet/
description: Den här artikeln beskriver hur man får det maximala intervallet, maximala dataintervallet, maximala visningsintervallet för Excel filer med Aspose.Cells för .Net bibliotek.
---

{{% alert color="primary" %}} 

När vi läser data från arket behöver vi känna till det maximala området.

När vi kopierar all data från ett ark behöver vi känna till det maximala området.

När vi exporterar ett angivet område till html och pdf behöver vi känna till det maximala området.

Aspose.Cells för .Net innehåller olika sätt att hitta det maximala intervallet i ett arbetsblad. 


{{% /alert %}} 



## **Får maximalt intervall**
I Aspose.Cells, om [**row**](https://reference.aspose.com/cells/net/aspose.cells/row) och [**column**](https://reference.aspose.com/cells/net/aspose.cells/column) objekten är initialiserade, kommer dessa rader och kolumner räknas till det maximala området, även om det inte finns några data i tomma rader eller kolumner.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Får maximalt datointervall**
I de flesta fall behöver vi bara få alla intervall som innehåller all data, även om de tomma cellerna utanför intervallet är formaterade.
Och inställningarna om former, tabeller och pivottabeller kommer att ignoreras.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Får maximalt visningsintervall**
När vi exporterar all data från arket till HTML, PDF eller bilder behöver vi få ett område som innehåller alla synliga objekt, inklusive data, stilar, grafik, tabeller och pivottabeller.
Följande koder visar hur man renderar det maximala visningsintervallet till html:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

Här är [källa excel-fil](Book1.xlsx).
