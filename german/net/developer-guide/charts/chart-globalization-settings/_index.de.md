---
title:  Verwenden der ChartGlobalizationSettings-Klasse zum Festlegen einer anderen Sprache für die Diagrammkomponente
type: docs
weight: 2200
url: /de/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Mögliche Nutzungsszenarien**

 Aspose.Cells APIs haben das offengelegt[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) Klasse, um mit Szenarien umzugehen, in denen der Benutzer die Diagrammkomponente auf eine andere Sprache einstellen möchte. benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle.

##  **Einführung in die ChartGlobalizationSettings-Klasse**

 Der[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)Die Klasse bietet derzeit die folgenden 8 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um z. B. AxisTitle-Name, AxisUnit-Name, ChartTitle-Name usw. in eine andere Sprache zu übersetzen.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Ruft den Namen des Titels für die Achse ab.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Ruft den Namen der Achseneinheit ab.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Ruft den Namen des Diagrammtitels ab.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Ruft den Namen Decrease für die Legende ab.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Ruft den Namen der Erhöhung für die Legende ab.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Ruft den Namen „Total“ für die Legende ab.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Ruft den Namen der „Anderen“ Beschriftungen für das Diagramm ab.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Ruft den Namen der Serie im Diagramm ab.

###  **Benutzerdefinierte Sprachübersetzung**
Hier erstellen wir ein Wasserfalldiagramm basierend auf den folgenden Daten. Die Namen der Diagrammkomponenten werden im Diagramm auf Englisch angezeigt. Wir werden anhand eines Beispiels in türkischer Sprache zeigen, wie der Diagrammtitel, die Legenden-Erhöhungs-/Verringerungsnamen, der Gesamtname und der Achsentitel auf Türkisch angezeigt werden.

![todo:image_alt_text](sample.png)

##  **Beispielcode**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Vom Beispielcode generierte Ausgabe

Dies ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
