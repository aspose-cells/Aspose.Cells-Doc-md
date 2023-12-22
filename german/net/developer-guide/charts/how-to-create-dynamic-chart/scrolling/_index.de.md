---
title: So erstellen Sie ein dynamisches Scrolling-Diagramm
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET ein dynamisches Scroll-Diagramm erstellen. Unsere Schritt-für-Schritt-Anleitung zeigt, wie Sie reibungslose Datenübergänge und automatisches Scrollen in Ihrem Diagramm implementieren, um eine kontinuierliche und aktuelle Anzeige zu gewährleisten.
keywords: Aspose.Cells for .NET, Dynamic Scrolling Chart, Data Transitions, Smooth Scrolling, Continuous Display, Updating Visualization.
type: docs
weight: 75
url: /de/net/create-dynamic-scrolling-chart/
---
##  **Mögliche Nutzungsszenarien**
Bei einem dynamischen Scrolldiagramm handelt es sich um eine Art grafische Darstellung zur Anzeige von Daten, die sich im Laufe der Zeit ändern. Es wurde entwickelt, um eine Echtzeitansicht der Daten bereitzustellen und es Benutzern zu ermöglichen, kontinuierliche Aktualisierungen und Trends zu verfolgen. Das Diagramm aktualisiert sich kontinuierlich, wenn neue Daten hinzugefügt werden, und scrollt automatisch, um die neuesten Informationen anzuzeigen.

Dynamische Scrolling-Diagramme werden häufig in verschiedenen Branchen verwendet, beispielsweise im Finanzwesen, bei der Börsenanalyse, bei der Wetterverfolgung und bei der Analyse sozialer Medien. Sie ermöglichen es Benutzern, Datenmuster zu visualisieren und zu analysieren und fundierte Entscheidungen auf der Grundlage von Echtzeitinformationen zu treffen.

Diese Diagramme sind in der Regel interaktiv und ermöglichen dem Benutzer das Vergrößern oder Verkleinern, das Scrollen durch historische Daten und das Anpassen von Zeitintervallen. Sie unterstützen oft mehrere Datenreihen und bieten einen umfassenden Überblick über verschiedene Metriken und deren Korrelationen.

Insgesamt sind dynamische Scrolling-Diagramme wertvolle Werkzeuge zur Überwachung und Analyse von Zeitreihendaten, die die Entscheidungsfindung in Echtzeit erleichtern und die Datenvisualisierungsmöglichkeiten verbessern.

##  **Verwenden Sie Aspose Cells, um ein dynamisches Scrolling-Diagramm zu erstellen**
In den nächsten Abschnitten zeigen wir Ihnen, wie Sie mit Aspose.Cells ein dynamisches Scrolling-Diagramm erstellen. Wir zeigen Ihnen den Code für das Beispiel sowie die mit diesem Code erstellte Excel-Datei.

##  **Beispielcode**
 Der folgende Beispielcode generiert die[Dynamische Scrolling-Diagrammdatei](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-scrolling-chart.cs" >}}

##  **Anmerkungen**
In der generierten Datei können Sie die Bildlaufleiste bedienen, während das Diagramm dynamisch die letzten 10 Datensätze zählt. Dies geschieht mit der „OFFSET“-Formel im Beispielcode:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Sie können versuchen, die Zahl „10“ in „15“ in der Zelle „Sheet1!$H$20“ zu ändern, und das dynamische Diagramm zählt die letzten 15 Datensätze. Jetzt haben wir mit Aspose.Cells erfolgreich ein dynamisches Scrolldiagramm erstellt.
