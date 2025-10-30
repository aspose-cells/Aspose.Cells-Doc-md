---
title: Få maxintervall i ett arbetsblad
type: docs
weight: 360
url: /sv/python-net/get-max-range-in-a-worksheet/
description: Den här artikeln beskriver hur man får den största serien, största dataserien, största visningsserien av Excel filer med Aspose.Cells for Python via .NET biblioteket.
keywords: Python Excel bibliotek, Python få det maximala området, Python få maximalt datarange, Python få maximalt visningsområde.
---

{{% alert color="primary" %}} 

När vi läser data från arket behöver vi känna till det maximala området.

När vi kopierar all data från ett ark behöver vi känna till det maximala området.

När vi exporterar ett angivet område till html och pdf behöver vi känna till det maximala området.

Aspose.Cells för Python via .NET innehåller olika sätt att hitta maximalt område i ett kalkylblad. 


{{% /alert %}} 



## **Hur man får maxområde**
I Aspose.Cells för Python via .NET, om [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) och [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) objekten initialiseras, räknas dessa rader och kolumner till det maximala området, även om det inte finns data i tomma rader eller kolumner.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **Hur man får max datarange**
I de flesta fall behöver vi bara få alla intervall som innehåller all data, även om de tomma cellerna utanför intervallet är formaterade.
Och inställningarna om former, tabeller och pivottabeller kommer att ignoreras.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **Hur man får max visningsområde**
När vi exporterar all data från arket till HTML, PDF eller bilder behöver vi få ett område som innehåller alla synliga objekt, inklusive data, stilar, grafik, tabeller och pivottabeller.
Följande koder visar hur man renderar det maximala visningsintervallet till html:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

Här är [källa excel-fil](Book1.xlsx).
{{< app/cells/assistant language="python-net" >}}
