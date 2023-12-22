---
title:  Använda ChartGlobalizationSettings Class för att ställa in annat språk för diagramkomponent
description: Lär dig hur du använder klassen ChartGlobalizationSettings i Aspose.Cells for .NET för att ställa in olika språk för diagramkomponenter. Vår guide hjälper dig att förstå hur du lokaliserar diagramelement, etiketter och legender till olika språk, så att du kan presentera dina data på ett kulturellt lämpligt sätt.
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /sv/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Möjliga användningsscenarier**

 Aspose.Cells API:er har avslöjat[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) klass för att hantera de scenarier där användaren vill ställa in diagramkomponenten till ett annat språk. anpassade etiketter för delsummor i ett kalkylblad.

##  **Introduktion till ChartGlobalizationSettings Class**

 De[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)class erbjuder för närvarande följande 8 metoder som kan åsidosättas i en anpassad klass för att översätta som AxisTitle name, AxisUnit name, ChartTitle name och så vidare till ett annat språk.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Får namnet på titel för Axis.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Hämtar namnet på axelenheten.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Hämtar namnet på diagramtitel.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Får namnet Decrease for Legend.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Får namnet på ökningen för Legend.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Får namnet Total for Legend.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Hämtar namnet på "Andra"-etiketter för diagram.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Hämtar namnet på serien i diagrammet.

###  **Anpassad språköversättning**
Här kommer vi att skapa ett vattenfallsdiagram baserat på följande data. Namnen på diagramkomponenterna kommer att visas på engelska i diagrammet. Vi kommer att använda ett turkiskt språkexempel för att visa hur man visar diagramtitel, förklaring Öka/minska namn, totalt namn och axeltitel på turkiska.

![todo:image_alt_text](sample.png)

##  **Exempelkod**
 Följande exempelkod laddar[exempel på Excel-fil](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Utdata genererad av exempelkoden

Detta är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
