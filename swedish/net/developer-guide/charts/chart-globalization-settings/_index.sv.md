---
title: Utvecklare kan inte bara kontrollera synligheten av stora rutnätlinjer utan också andra egenskaper inklusive dess färg osv. 
description: Lär dig hur man använder ChartGlobalizationSettings klassen i Aspose.Cells for .NET för att ställa in olika språk för diagramkomponenter. Vår guide hjälper dig att förstå hur man lokaliserar diagramelement, etiketter och legender till olika språk, vilket gör det möjligt att presentera dina data på ett kulturellt lämpligt sätt.
keywords: Aspose.Cells for .NET, diagramskapande, diagramglobalisering, språk, lokaliseringsinställningar, ChartGlobalizationSettings, element, etiketter, legender.
type: docs
weight: 2200
url: /sv/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Möjliga användningsscenario**

Aspose.Cells API har exponerat [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)-klassen för att hantera scenarier där användaren vill ställa in diagramkomponent till olika språk. Anpassade etiketter för delsummer i en kalkyl. 

## **Introduktion till ChartGlobalizationSettings-klassen**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)-klassen erbjuder för närvarande följande 8 metoder som kan åsidosättas i en anpassad klass för att översätta sådana som Axistitelnamn, Axisenhetsnamn, Diagramtitelnamn och så vidare till olika språk.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Hämtar namnet på titeln för axeln.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Hämtar namnet på axelenhet.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Hämtar namnet på diagramtiteln.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Hämtar namnet på minskningen för förklaringen.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Hämtar namnet på ökningen för förklaringen.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Hämtar namnet på totalen för förklaringen.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Hämtar namnet på "Annan" etiketter för diagrammet.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Hämtar namnet på serier i diagrammet.

### **Anpassad språköversättning**
Här kommer vi att skapa en stapeldiagram baserat på följande data. Namnen på diagramkomponenterna kommer att visas på engelska i diagrammet. Vi kommer att använda ett turkiskt språkexempel för att visa hur man visar diagramtitel, förklarings-ökning/minskning, totalt namn och axelns titel på turkiska.

![todo:image_alt_text](sample.png)

## **Exempelkod**
Följande exempelkod laddar [prov Excel-filen](vattenfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
