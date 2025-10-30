---
title: Använder ChartGlobalizationSettings klass för att ställa in olika språk för diagramkomponenten med Golang via C++
linktitle: Använd Class ChartGlobalizationSettings
description: Lär dig hur du använder klassen ChartGlobalizationSettings i Aspose.Cells for C++ för att ställa in olika språk för diagramkomponenter. Vår guide hjälper dig att förstå hur du lokaliserar diagramdelar, etiketter och legender till olika språk, så att du kan presentera dina data på ett kulturellt lämpligt sätt.
keywords: Aspose.Cells for C++, diagram, diagramglobalisering, språk, lokalisation, ChartGlobalizationSettings, element, etiketter, legender.
type: docs
weight: 2200
url: /sv/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Möjliga användningsscenario**

Aspose.Cells API har exponerat [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/)-klassen för att hantera scenarier där användaren vill ställa in diagramkomponent till olika språk. Anpassade etiketter för delsummer i en kalkyl. 

## **Introduktion till ChartGlobalizationSettings-klassen**

Klassen [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) erbjuder för närvarande de följande 8 metoder som kan åsidosättas i en anpassad klass för att översätta såsom AxisTitle-namn, AxisUnit-namn, ChartTitle-namn och så vidare till ett annat språk.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/): Hämtar namnet på titeln för axeln.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/): Hämtar namnet på axelenhet.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/): Hämtar namnet på diagramtiteln.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/): Hämtar namnet på minskningen för förklaringen.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/): Hämtar namnet på ökningen för förklaringen.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/): Hämtar namnet på totalen för förklaringen.
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/): Hämtar namnet på "Annan" etiketter för diagrammet.
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/): Hämtar namnet på serier i diagrammet.

### **Anpassad språköversättning**
Här kommer vi att skapa en stapeldiagram baserat på följande data. Namnen på diagramkomponenterna kommer att visas på engelska i diagrammet. Vi kommer att använda ett turkiskt språkexempel för att visa hur man visar diagramtitel, förklarings-ökning/minskning, totalt namn och axelns titel på turkiska.

![todo:image_alt_text](sample.png)

## **Exempelkod**
Följande exempelkod laddar [prov Excel-filen](vattenfall.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
