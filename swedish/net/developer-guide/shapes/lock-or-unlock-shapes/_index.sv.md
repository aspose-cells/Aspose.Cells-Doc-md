---
title: Lås eller lås upp figurer
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade arbetsblad, i vilket fall måste du låsa upp dessa figurer.

Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

{{% /alert %}}

## **Skydda alla figurer i ett angivet arbetsblad**

För att skydda alla former i ett angivet arbetsblad, använd [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) metoden, som visas i följande exempelkod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Lås upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en angiven form i ett skyddat arbetsblad, använd [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), som visas i följande exempelkod.

Observera: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) är meningsfull endast när arbetsbladet är skyddat.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

