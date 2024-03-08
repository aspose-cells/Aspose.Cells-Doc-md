---
title: Läs axeletiketter efter att ha beräknat diagrammet
description: Lär dig hur du läser axeletiketter i Aspose.Cells for .NET efter att ha beräknat diagrammet. Vår guide visar dig hur du kommer åt och hämtar axeletiketter, inklusive deras formatering och placering.
keywords: Aspose.Cells for .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /sv/net/read-axis-labels-after-calculating-the-chart/
---
##  **Möjliga användningsscenarier**

Du kan läsa axeletiketter för ditt diagram efter att ha beräknat dess värden med hjälp av[**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)metod. Vänligen använd[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) metod för detta ändamål som kommer att returnera listan med axeletiketter.

##  **Läs axeletiketter efter att ha beräknat diagrammet**

Se följande exempelkod som laddar[exempel på Excel-fil](ReadAxisLabels.xlsx)och läser kategoriaxeletiketterna i diagrammet i det första kalkylbladet. Den skriver sedan ut värdena för axeletiketterna på konsolen. Se konsolutgången för exempelkoden nedan för en referens.

##  **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

##  **Konsolutgång**

{{< highlight "csharp" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
