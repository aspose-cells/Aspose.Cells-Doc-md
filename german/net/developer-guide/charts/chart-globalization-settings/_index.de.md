---
title: Verwendung der ChartGlobalizationSettings Klasse zum Einstellen einer anderen Sprache für das Diagrammkomponente 
description: Erfahren Sie, wie Sie die ChartGlobalizationSettings Klasse in Aspose.Cells for .NET verwenden, um verschiedene Sprachen für Diagrammkomponenten festzulegen. Unser Leitfaden wird Ihnen helfen zu verstehen, wie Sie Diagrammelemente, Beschriftungen und Legenden in verschiedene Sprachen lokalisiert und so Ihre Daten auf kulturell angemessene Weise präsentieren.
keywords: Aspose.Cells for .NET, Charting, Diagrammglobalisierung, Sprachen, Lokalisierung, ChartGlobalizationSettings, Elemente, Beschriftungen, Legenden.
type: docs
weight: 2200
url: /de/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells-APIs haben die Klasse [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) freigelegt, um mit Szenarien umzugehen, in denen der Benutzer die Diagrammkomponente auf eine andere Sprache einstellen möchte. Benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle. 

## **Einführung in die ChartGlobalizationSettings-Klasse**

Die Klasse [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) bietet derzeit die folgenden 8 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um beispielsweise Achsentitel, Achsenbeschriftung, Diagrammtitel usw. in verschiedene Sprachen zu übersetzen.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Gibt den Titel für die Achse zurück.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Gibt den Namen der Achseneinheit zurück.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Gibt den Titel des Diagramms zurück.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Gibt den Namen der Abnahme für die Legende zurück.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Gibt den Namen des Anstiegs für die Legende zurück.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Gibt den Namen des Gesamtwerts für die Legende zurück.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Gibt den Namen der "Andere"-Beschriftungen für das Diagramm zurück.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Gibt den Namen der Serie im Diagramm zurück.

### **Benutzerdefinierte Sprachübersetzung**
Hier erstellen wir ein Wasserfalldiagramm basierend auf den folgenden Daten. Die Namen der Diagrammkomponenten werden im Diagramm auf Englisch angezeigt. Wir verwenden ein Beispiel für die türkische Sprache, um zu zeigen, wie der Diagrammtitel, die Legenden-Abnahme/Zunahme-Namen, der Gesamtwert und der Achsentitel auf Türkisch angezeigt werden.

![todo:image_alt_text](sample.png)

## **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
