---
title: Lås eller lås upp figurer
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade arbetsblad, i vilket fall måste du låsa upp dessa figurer.

Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

{{% /alert %}}

## **Skydda alla figurer i ett angivet arbetsblad**

För att skydda alla former i ett angivet kalkylblad, använd metoden [Worksheet.protect(int type)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-), som visas i följande exempelkod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **Lås upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en angiven form i ett skyddat kalkylblad, använd [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) och [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-), som visas i följande exempelkod.

Observera: [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) och [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) är meningsfulla endast när kalkylbladet är skyddat.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

