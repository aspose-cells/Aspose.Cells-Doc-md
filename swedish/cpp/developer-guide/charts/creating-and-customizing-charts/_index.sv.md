---
title: Skapa och anpassa diagram
type: docs
weight: 10
url: /sv/cpp/creating-and-customizing-charts/
---

## **Möjliga användningsscenario**

Ett diagram är en visuell presentation av information. Aspose.Cells tillåter utvecklare att visualisera information i diagram precis som Microsoft Excel gör. Att presentera information i diagram är alltid till hjälp för beslutsfattare att fatta snabba och rättidiga beslut. Det är lättare att snabbt se jämförelser, mönster och trender i data med diagram snarare än råa siffror. Att skapa diagram vid körning, baserat på datan i ett kalkylblad, är en av Aspose.Cells användbara funktioner. Aspose.Cells stödjer skapandet av både standard- och anpassade diagram. Nedan kommer vi att visa några exempel med exempelfiler om hur man skapar några vanliga MS-Excel-diagram med hjälp av Aspose.Cells API.

## **Pyramiddiagram**

När exempelkoden körs läggs ett pyramid-diagram till arbetsbladet. Vänligen se den [utdata Excel-filen](66519068.xlsx) från följande kodexempel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **Linjediagram**

I det ovanstående exemplet skapar en enkel ändring av [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) till **`ChartType::Line`** ett linjediagram. Den kompletta källkoden ges nedan. När koden körs läggs ett linjediagram till arbetsbladet. Vänligen se den [utdata Excel-filen](66519069.xlsx) från följande kodexempel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **Bubbel-diagram**

För att skapa ett bubbel-diagram måste [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) sättas till **`ChartType_Bubble`** och några extra egenskaper såsom [**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) måste ställas in därefter. När följande kod exekveras läggs ett bubbel-diagram till arbetsbladet. Vänligen se den [utdata Excel-filen](66519070.xlsx) från följande kodexempel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **Skapa Anpassade Diagram**

Hittills, när vi har diskuterat diagram, har vi tittat på standarddiagram som har sina egna standardformateringsinställningar. Vi definierar bara datakällan, ställer in några egenskaper och diagrammet skapas med sina standardformateringsinställningar. Men Aspose.Cells API:er stödjer också skapandet av anpassade diagram som tillåter utvecklare att skapa diagram med sina egna formateringsinställningar. Utvecklare kan skapa anpassade diagram vid körning med hjälp av Aspose.Cells.

Ett diagram består av en dataserie. När man skapar ett anpassat diagram har utvecklare friheten att använda olika diagramtyper för olika dataserier.

Följande kodexempel visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, i kombination med ett linjediagram, till arbetsbladet. Vänligen se den [utdata Excel-filen](66519071.xlsx) från följande kodexempel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
