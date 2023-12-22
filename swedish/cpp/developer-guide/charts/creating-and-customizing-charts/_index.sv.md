---
title: Skapa och anpassa diagram
type: docs
weight: 10
url: /sv/cpp/creating-and-customizing-charts/
---
##  **Möjliga användningsscenarier**

Ett diagram är en visuell visning av information. Aspose.Cells tillåter utvecklare att visualisera information i diagram precis som Microsoft Excel gör. Att presentera information i diagram är alltid till hjälp för beslutsfattare för att fatta snabba och snabba beslut. Det är lättare att snabbt se jämförelser, mönster och trender i data med diagram snarare än råa siffror. Att skapa diagram vid körning, baserat på data i ett kalkylblad, är en av Aspose.Cells' användbara funktioner. Aspose.Cells stöder att skapa både standard- och anpassade diagram. Nedan kommer vi att visa några exempel med exempelfiler på hur man skapar några vanliga MS-Excel-diagramtyper med Aspose.Cells API.

##  **Pyramiddiagram**

 När exempelkoden exekveras läggs ett pyramiddiagram till i kalkylbladet. Vänligen se[utdata Excel-fil](66519068.xlsx) av följande exempelkod.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **Linjediagram**

I exemplet ovan ändrar du helt enkelt[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)till**`ChartType::Line`**skapar ett linjediagram. Den fullständiga källan finns nedan. när koden exekveras läggs ett linjediagram till i kalkylbladet. Vänligen se[utdata Excel-fil](66519069.xlsx) av följande exempelkod.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **Bubbeldiagram**

För att skapa ett bubbeldiagram,[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) måste ställas in på**`ChartType_Bubble`** och få extra fastigheter som t.ex[**Ange BubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) måste ställas in därefter. När följande kod körs läggs ett bubbeldiagram till i kalkylbladet. Vänligen se[utdata Excel-fil](66519070.xlsx) av följande exempelkod.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **Skapa anpassade diagram**

Hittills, när vi har diskuterat diagram, har vi tittat på standarddiagram som har sina egna standardformateringsinställningar. Vi definierar bara datakällan, ställer in några få egenskaper och diagrammet skapas med dess standardformatinställningar. Men Aspose.Cells API:er stöder också att skapa anpassade diagram som gör det möjligt för utvecklare att skapa diagram med sina egna formatinställningar. Utvecklare kan skapa anpassade diagram under körning med Aspose.Cells.

Ett diagram är sammansatt av en dataserie. När du skapar ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier.

 Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett kolumndiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett kolumndiagram, kombinerat med ett linjediagram, till kalkylbladet. Vänligen se[utdata Excel-fil](66519071.xlsx) av följande exempelkod.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
