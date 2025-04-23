---
title: Läs av axeletiketter efter att ha beräknat diagrammet
description: Lär dig hur man läser axelmärken i Aspose.Cells for Java efter att ha beräknat diagrammet. Vår guide visar hur du får åtkomst till och hämtar axelmärken, inklusive deras formatering och positionering.
keywords: Aspose.Cells for Java, diagram, axelmärken, beräkning, läsning, åtkomst, hämtning, formatering, positionering.
type: docs
weight: 90
url: /sv/java/read-axis-labels-after-calculating-the-chart/
---

## **Möjliga användningsscenario**

Du kan läsa diagrammets axelmärken efter att ha beräknat dess värden med [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--) metoden. Använd [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--) metoden för detta ändamål som returnerar listan över axelmärken.

## **Läs av axeletiketter efter att ha beräknat diagrammet**

Se följande exempelkod som laddar in [sample Excel file](64716829.xlsx) och läser kategoriansläggningsetiketterna för diagrammet i det första kalkylbladet. Sedan skrivs värdena på axelmärkena ut i konsolen. Se konsolens utgivning för exempelkoden nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

## **Konsoloutput**

{{< highlight java >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
