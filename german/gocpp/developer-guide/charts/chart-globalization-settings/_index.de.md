---
title: Verwendung der ChartGlobalizationSettings Klasse zum Einstellen verschiedener Sprachen für das Diagramm mit Golang über C++
linktitle: Verwendung der ChartGlobalizationSettings Klasse
description: Lernen Sie, wie man die ChartGlobalizationSettings Klasse in Aspose.Cells for C++ nutzt, um verschiedene Sprachen für Diagrammkomponenten einzustellen. Unser Leitfaden hilft Ihnen zu verstehen, wie man Diagrammelemente, Beschriftungen und Legenden in verschiedene Sprachen lokalisiert, sodass Sie Ihre Daten kulturell angemessen präsentieren können.
keywords: Aspose.Cells for C++, Diagramm, Chart Globalisierung, Sprachen, Lokalisierung, ChartGlobalizationSettings, Elemente, Beschriftungen, Legenden
type: docs
weight: 2200
url: /de/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells-APIs haben die Klasse [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) freigelegt, um mit Szenarien umzugehen, in denen der Benutzer die Diagrammkomponente auf eine andere Sprache einstellen möchte. Benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle. 

## **Einführung in die ChartGlobalizationSettings-Klasse**

Die [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) Klasse bietet derzeit die folgenden 8 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um solche Übersetzungen wie AxisTitle Name, AxisUnit Name, ChartTitle Name und so weiter in eine andere Sprache vorzunehmen.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/): Gibt den Titel für die Achse zurück.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/): Gibt den Namen der Achseneinheit zurück.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/): Gibt den Titel des Diagramms zurück.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/): Gibt den Namen der Abnahme für die Legende zurück.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/): Gibt den Namen des Anstiegs für die Legende zurück.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/): Gibt den Namen des Gesamtwerts für die Legende zurück.
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/): Gibt den Namen der "Andere"-Beschriftungen für das Diagramm zurück.
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/): Gibt den Namen der Serie im Diagramm zurück.

### **Benutzerdefinierte Sprachübersetzung**
Hier erstellen wir ein Wasserfalldiagramm basierend auf den folgenden Daten. Die Namen der Diagrammkomponenten werden im Diagramm auf Englisch angezeigt. Wir verwenden ein Beispiel für die türkische Sprache, um zu zeigen, wie der Diagrammtitel, die Legenden-Abnahme/Zunahme-Namen, der Gesamtwert und der Achsentitel auf Türkisch angezeigt werden.

![todo:image_alt_text](sample.png)

## **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
