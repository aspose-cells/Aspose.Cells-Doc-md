---
title: Läs av axeletiketter efter att ha beräknat diagrammet
description: Lär dig hur du läser av axeletiketterna i Aspose.Cells for .NET efter att ha beräknat diagrammet. Vår guide kommer att visa dig hur du får åtkomst till och hämtar axeletiketter, inklusive deras formatering och positionering.
keywords: Aspose.Cells for .NET, diagram, axeletiketter, beräkning, läsning, åtkomst, hämtning, formatering, positionering.
type: docs
weight: 90
url: /sv/net/read-axis-labels-after-calculating-the-chart/
---

## **Möjliga användningsscenario**

Du kan läsa av axeletiketterna för ditt diagram efter att ha beräknat dess värden med hjälp av [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)-metoden. Använd [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/)-metoden för detta ändamål som kommer att returnera listan över axeletiketter.

## **Läs av axeletiketter efter att ha beräknat diagrammet**

Vänligen se följande kodexempel som laddar in den [exempel Excel-filen](ReadAxisLabels.xlsx) och läser kategoriaxlarna i diagrammet på den första arbetsbladet. Den skriver sedan ut värdena för axelmärkena på konsolen. Se konsolresultatet för kodexemplet nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

## **Konsoloutput**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
