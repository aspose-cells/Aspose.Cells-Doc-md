---
title: Wie man ein dynamisches Bildlaufdiagramm erstellt
description: Erfahren Sie, wie Sie mit Aspose.Cells für Python via .NET ein dynamisches Scroll Diagramm erstellen. Unser Schritt für Schritt Leitfaden zeigt Ihnen, wie Sie sanfte Datenübergänge und automatisches Scrollen in Ihrem Diagramm umsetzen, für eine kontinuierliche und aktualisierte Anzeige.
keywords: Aspose.Cells für Python via .NET, Dynamisches Scroll Diagramm, Datenübergänge, Sanftes Scrollen, Kontinuierliche Anzeige, Aktualisierte Visualisierung.
type: docs
weight: 75
url: /de/python-net/create-dynamic-scrolling-chart/
---

## **Mögliche Verwendungsszenarien**
Das dynamische Bildlaufdiagramm ist eine Art grafische Darstellung, die verwendet wird, um Daten anzuzeigen, die sich im Laufe der Zeit ändern. Es ist darauf ausgelegt, einen Echtzeit-Blick auf Daten zu bieten, der es Benutzern ermöglicht, kontinuierliche Aktualisierungen und Trends zu verfolgen. Das Diagramm aktualisiert sich kontinuierlich, wenn neue Daten hinzugefügt werden, und scrollt automatisch, um die neuesten Informationen anzuzeigen.

Dynamische Bildlaufdiagramme werden in verschiedenen Branchen wie Finanzen, Börsenanalyse, Wetterverfolgung und sozialen Medienanalysen häufig eingesetzt. Sie ermöglichen es Benutzern, Datenmuster zu visualisieren und zu analysieren und auf Echtzeitinformationen basierende fundierte Entscheidungen zu treffen.

Diese Diagramme sind normalerweise interaktiv und ermöglichen es dem Benutzer, herein- oder herauszuzoomen, durch historische Daten zu scrollen und Zeitintervalle anzupassen. Sie unterstützen oft mehrere Datenreihen, die einen umfassenden Überblick über verschiedene Metriken und ihre Korrelationen bieten.

Insgesamt sind dynamische Bildlaufdiagramme wertvolle Werkzeuge zur Überwachung und Analyse von zeitbezogenen Daten, zur Unterstützung von Echtzeit-Entscheidungsfindung und zur Verbesserung der Datenvisualisierungsfähigkeiten.

## **Verwenden Sie Aspose.Cells für Python via .NET, um ein dynamisches Scroll-Diagramm zu erstellen.**
In den nächsten Abschnitten zeigen wir Ihnen, wie Sie mit Aspose.Cells für Python via .NET ein dynamisches Scroll-Diagramm erstellen. Wir zeigen Ihnen den Code für das Beispiel sowie die mit diesem Code erstellte Excel-Datei.

## **Beispielcode**
Der folgende Beispielcode generiert die [Dynamische Bildlaufdiagramm-Datei](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-scrolling-chart.py" >}}

## **Anmerkungen**
In der generierten Datei können Sie auf die Bildlaufleiste zugreifen, während das Diagramm dynamisch die neuesten 10 Datensätze zählt. Dies wird mithilfe der "OFFSET"-Formel im Beispielcode durchgeführt:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Sie können versuchen, die Zahl "10" in Zelle "Sheet1!$H$20" zu ändern in "15", und das dynamische Diagramm zählt die neuesten 15 Datenreihen. Jetzt haben wir erfolgreich ein dynamisches Scroll-Diagramm mit Aspose.Cells für Python via .NET erstellt.
{{< app/cells/assistant language="python-net" >}}
