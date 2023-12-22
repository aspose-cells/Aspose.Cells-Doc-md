---
title: So erstellen Sie ein dynamisches Rolldiagramm
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET ein dynamisches Rolldiagramm erstellen. Unser Leitfaden zeigt, wie Sie reibungslose Datenübergänge und gleitende Durchschnitte in Ihrem Diagramm implementieren, um eine kontinuierliche und aktuelle Anzeige zu gewährleisten.
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /de/net/create-dynamic-rolling-chart/
---
##  **Mögliche Nutzungsszenarien**
Ein dynamisches Rolldiagramm bezieht sich auf eine grafische Darstellung, die Datenpunkte anzeigt, die sich im Laufe der Zeit ständig ändern und aktualisieren. Dabei handelt es sich um eine Art Diagramm, das sich ständig selbst aktualisiert und ein rollierendes Fenster mit den neuesten Datenpunkten anzeigt, während ältere Datenpunkte verworfen werden, wenn neue hinzukommen.

Dynamische Rolldiagramme werden üblicherweise zur Visualisierung von Trends und Mustern in Echtzeit- oder Streaming-Daten verwendet. Sie sind besonders nützlich in Szenarien, in denen zeitliche Aspekte und Veränderungen im Laufe der Zeit von entscheidender Bedeutung sind, wie z. B. Börsenanalysen, Wetterüberwachung oder Live-Performance-Tracking.

Diese Diagramme verwenden in der Regel Animationen oder Mechanismen zum automatischen Scrollen, um sicherzustellen, dass immer die aktuellsten Informationen angezeigt werden. Die Länge des Rollfensters kann angepasst werden, um einen bestimmten Zeitraum anzuzeigen, beispielsweise die letzte Stunde, den letzten Tag oder die letzte Woche.

Zusammenfassend ist ein dynamisches Rolldiagramm eine kontinuierlich aktualisierte grafische Darstellung, die die neuesten Datenpunkte anzeigt und ältere verwirft, sodass Benutzer Trends und Muster in Echtzeit beobachten können.

##  **Verwenden Sie Aspose Cells, um ein dynamisches Rolldiagramm zu erstellen**
In den nächsten Abschnitten zeigen wir Ihnen, wie Sie mit Aspose.Cells ein dynamisches Rolldiagramm erstellen. Wir zeigen Ihnen den Code für das Beispiel sowie die mit diesem Code erstellte Excel-Datei.

##  **Beispielcode**
 Der folgende Beispielcode generiert die[Dynamische Rolling-Chart-Datei](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

##  **Anmerkungen**
In der generierten Datei können Sie weiterhin Daten in den Spalten A und B hinzufügen, während das Diagramm dynamisch die letzten fünf Datensätze zählt. Dies geschieht mit der „OFFSET“-Formel im Beispielcode:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Sie können versuchen, die Zahl „-5“ in „-10“ in der Formel zu ändern. Das dynamische Diagramm zählt dann die letzten 10 Datensätze. Jetzt haben wir erfolgreich ein dynamisches Rolldiagramm mit Aspose.Cells erstellt.
