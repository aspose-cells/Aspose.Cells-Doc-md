---
title: Få maximal räckvidd i ett arbetsblad
type: docs
weight: 360
url: /sv/net/get-max-range-in-a-worksheet/
description: Den här artikeln beskriver hur du får maxintervallet , maxdataintervallet, maxvisningsintervallet för Excel-filer med Aspose.Cells för .Net-biblioteket.
---
{{% alert color="primary" %}} 

När vi läser data från kalkylbladet måste vi veta den maximala arean.

När vi kopierar all data från ett kalkylblad måste vi veta den maximala ytan.

När vi exporterar ett specificerat område till html och pdf måste vi veta den maximala ytan.

 Aspose.Cells för .Net innehåller olika sätt att hitta maxintervall i ett kalkylblad.


{{% /alert %}} 



##  **Får max räckvidd**
 På Aspose.Cells, om[**rad**](https://reference.aspose.com/cells/net/aspose.cells/row) och[**kolumn**](https://reference.aspose.com/cells/net/aspose.cells/column) objekt initieras, kommer dessa rader och kolumner att räknas till den maximala ytan, även om det inte finns några data i tomma rader eller kolumner.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **Hämtar maximalt dataintervall**
de flesta fall behöver vi bara få alla intervall som innehåller all data, även om de tomma cellerna utanför intervallet är formaterade.
Och inställningarna om former, tabeller och pivottabeller kommer att ignoreras.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **Får maximalt visningsområde**
När vi exporterar all data från kalkylbladet till HTML, PDF eller bilder måste vi få ett område som innehåller alla synliga objekt, inklusive data, stilar, grafik, tabeller och pivottabeller.
Följande koder visar hur man renderar det maximala visningsintervallet till html:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

 Här är[source excel-fil](Book1.xlsx).
