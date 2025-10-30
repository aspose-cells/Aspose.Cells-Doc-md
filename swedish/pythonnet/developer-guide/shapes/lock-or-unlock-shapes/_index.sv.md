---
title: Lås eller lås upp figurer
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade arbetsblad, i vilket fall måste du låsa upp dessa figurer.

Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

{{% /alert %}}

## **Skydda alla figurer i ett angivet arbetsblad**

För att skydda alla former i ett angivet arbetsblad, använd [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType) metoden, enligt följande exempelkod.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Lås upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en angiven form i ett skyddat arbetsblad, använd [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/), enligt följande exempelkod.

Observera: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) är meningsfull endast när arbetsbladet är låst.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}
