---
title: Erstellen eines Open High Low Close (OHLC) Aktiencharts mit Golang über C++
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ ein Open Hoch Tief Schluss Aktienchart erstellen. Unser Leitfaden zeigt, wie Sie Börsendaten, einschließlich Eröffnungs , Hoch , Tief und Schlusskurse, in ein Diagramm plotten, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for C++, Open Hoch Tief Schluss Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 182
url: /de/go-cpp/create-open-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das Open-High-Low-Close (OHLC) Diagramm verwendet fünf Datenkategorien in dieser Reihenfolge: Kategorie, Öffnen, Hoch, Tief und Schlusskurs. Die Preisspanne in jeder Kategorie wird erneut durch eine vertikale Linie angezeigt, während die Spanne zwischen Öffnen und Schließen durch eine breitere, freischwebende Leiste angegeben wird. Wenn der Preis in der Kategorie steigt (Schlusskurs höher als Öffnungspreis), wird die Leiste mit einer Farbe gefüllt, während sie bei sinkenden Preisen mit einer anderen Farbe gefüllt wird. Dieser Diagrammtyp wird oft als Candlestick-Diagramm bezeichnet.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Verbesserungen der Sichtbarkeit im Diagramm**
Wir verwenden oft Farben anstelle von Schwarz-Weiß, um steigende und fallende Kurse anzuzeigen. Im ersten Satz von Kerzencharts unten zeigt Rot steigende und Grün fallende Kurse.

![todo:image_alt_text](sample2.png)

## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Open-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateOpenHighLowCloseChart.go" >}}
