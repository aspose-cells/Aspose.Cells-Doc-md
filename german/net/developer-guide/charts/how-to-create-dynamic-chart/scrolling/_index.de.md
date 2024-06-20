---
title: Wie man ein dynamisches Bildlaufdiagramm erstellt
description: Erfahren Sie, wie Sie ein dynamisches Bildlaufdiagramm mit Aspose.Cells for .NET erstellen können. Unser Schritt für Schritt Leitfaden zeigt, wie Sie sanfte Datenübergänge und automatisches Scrollen in Ihrem Diagramm implementieren können, um eine kontinuierliche und aktualisierte Anzeige zu erreichen.
keywords: Aspose.Cells for .NET, Dynamische Bildlaufdiagramm, Datenübergänge, Sanftes Scrollen, Kontinuierliche Anzeige, Aktualisierung der Visualisierung.
type: docs
weight: 75
url: /de/net/create-dynamic-scrolling-chart/
---

## **Mögliche Verwendungsszenarien**
Das dynamische Bildlaufdiagramm ist eine Art grafische Darstellung, die verwendet wird, um Daten anzuzeigen, die sich im Laufe der Zeit ändern. Es ist darauf ausgelegt, einen Echtzeit-Blick auf Daten zu bieten, der es Benutzern ermöglicht, kontinuierliche Aktualisierungen und Trends zu verfolgen. Das Diagramm aktualisiert sich kontinuierlich, wenn neue Daten hinzugefügt werden, und scrollt automatisch, um die neuesten Informationen anzuzeigen.

Dynamische Bildlaufdiagramme werden in verschiedenen Branchen wie Finanzen, Börsenanalyse, Wetterverfolgung und sozialen Medienanalysen häufig eingesetzt. Sie ermöglichen es Benutzern, Datenmuster zu visualisieren und zu analysieren und auf Echtzeitinformationen basierende fundierte Entscheidungen zu treffen.

Diese Diagramme sind normalerweise interaktiv und ermöglichen es dem Benutzer, herein- oder herauszuzoomen, durch historische Daten zu scrollen und Zeitintervalle anzupassen. Sie unterstützen oft mehrere Datenreihen, die einen umfassenden Überblick über verschiedene Metriken und ihre Korrelationen bieten.

Insgesamt sind dynamische Bildlaufdiagramme wertvolle Werkzeuge zur Überwachung und Analyse von zeitbezogenen Daten, zur Unterstützung von Echtzeit-Entscheidungsfindung und zur Verbesserung der Datenvisualisierungsfähigkeiten.

## **Verwenden Sie Aspose Cells, um ein dynamisches Bildlaufdiagramm zu erstellen**
In den folgenden Absätzen zeigen wir Ihnen, wie Sie mit Aspose.Cells ein dynamisches Bildlaufdiagramm erstellen können. Wir werden Ihnen den Code für das Beispiel sowie die mit diesem Code erstellte Excel-Datei zeigen.

## **Beispielcode**
Der folgende Beispielcode generiert die [Dynamische Bildlaufdiagramm-Datei](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-scrolling-chart.cs" >}}

## **Anmerkungen**
In der generierten Datei können Sie auf die Bildlaufleiste zugreifen, während das Diagramm dynamisch die neuesten 10 Datensätze zählt. Dies wird mithilfe der "OFFSET"-Formel im Beispielcode durchgeführt:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Sie können versuchen, die Zahl "10" in "15" in der Zelle "Sheet1!$H$20" zu ändern, und das dynamische Diagramm wird die neuesten 15 Datensätze zählen. Jetzt haben wir erfolgreich ein dynamisches Bildlaufdiagramm mit Aspose.Cells erstellt.
