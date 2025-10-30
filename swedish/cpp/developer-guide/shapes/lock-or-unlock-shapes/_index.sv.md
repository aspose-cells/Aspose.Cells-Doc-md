---
title: Lås eller lås upp figurer
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade arbetsblad, i vilket fall måste du låsa upp dessa figurer.

Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

{{% /alert %}}

## **Skydda alla figurer i ett angivet arbetsblad**

För att skydda alla former i ett angivet kalkylblad, använd metoden [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) enligt följande exempelkod.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **Lås upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en angiven form i ett skyddat kalkylblad, använd [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) och [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) enligt följande exempelkod.

Observera: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) och [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) har endast betydelse när kalkylarket är skyddat.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
