---
title: Lås eller lås upp figurer
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade arbetsblad, i vilket fall måste du låsa upp dessa figurer.

Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

{{% /alert %}}

## **Skydda alla figurer i ett angivet arbetsblad**

För att skydda alla figurer i ett angivet arbetsblad, använd [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)) metoden, enligt visat i följande exempelkod.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Lås upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en angiven figur i ett skyddat arbetsblad, använd [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked), enligt visad i följande exempelkod.

Observera: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) är meningsfull endast när arbetsbladet är skyddat.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

