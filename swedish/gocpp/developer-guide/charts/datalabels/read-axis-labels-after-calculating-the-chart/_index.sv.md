---
title: Läs axelrubriker efter att ha beräknat diagrammet med Golang via C++
linktitle: Läs av axeletiketter efter att ha beräknat diagrammet
description: Lär dig hur du läser av axel etiketter i Aspose.Cells for C++ efter att ha beräknat diagrammet. Vår guide visar hur du får åtkomst och hämtar axel etiketter, inklusive deras formatering och positionering.
keywords: Aspose.Cells for C++, diagram, axel etiketter, beräkning, läsning, åtkomst, hämtning, formatering, positionering.
type: docs
weight: 90
url: /sv/go-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Möjliga användningsscenario**

Du kan läsa av axeletiketterna för ditt diagram efter att ha beräknat dess värden med hjälp av [**Chart.Calculate()**](https://reference.aspose.com/cells/go-cpp/chart/calculate/)-metoden. Använd [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/)-metoden för detta ändamål som kommer att returnera listan över axeletiketter.

## **Läs av axeletiketter efter att ha beräknat diagrammet**

Vänligen se följande kodexempel som laddar in den [exempel Excel-filen](ReadAxisLabels.xlsx) och läser kategoriaxlarna i diagrammet på den första arbetsbladet. Den skriver sedan ut värdena för axelmärkena på konsolen. Se konsolresultatet för kodexemplet nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAxisLabelsAfterCalculatingTheChart.go" >}}
## **Konsoloutput**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
