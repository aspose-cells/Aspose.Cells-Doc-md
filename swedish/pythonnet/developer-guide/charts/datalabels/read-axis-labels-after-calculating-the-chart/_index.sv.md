---
title: Läs av axeletiketter efter att ha beräknat diagrammet
description: Lär dig hur du läser axelrubriker i Aspose.Cells för Python via .NET efter diagramberäkning. Vår guide visar hur du kommer åt och hämtar axelrubriker, inklusive deras formatering och positionering.
keywords: Aspose.Cells för Python via .NET, diagram, axelrubriker, beräkning, läsning, åtkomst, hämtning, formatering, positionering.
type: docs
weight: 90
url: /sv/python-net/read-axis-labels-after-calculating-the-chart/
---

## **Möjliga användningsscenario**

Du kan läsa av axeletiketterna för ditt diagram efter att ha beräknat dess värden med hjälp av [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/)-metoden. Använd [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts)-metoden för detta ändamål som kommer att returnera listan över axeletiketter.

## **Läs av axeletiketter efter att ha beräknat diagrammet**

Vänligen se följande kodexempel som laddar in den [exempel Excel-filen](ReadAxisLabels.xlsx) och läser kategoriaxlarna i diagrammet på den första arbetsbladet. Den skriver sedan ut värdena för axelmärkena på konsolen. Se konsolresultatet för kodexemplet nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

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
