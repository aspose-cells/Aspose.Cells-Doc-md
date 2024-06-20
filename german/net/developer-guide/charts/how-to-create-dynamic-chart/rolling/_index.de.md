---
title: Wie erstellt man ein dynamisches Rollbalkendiagramm
description: Erfahren Sie, wie Sie ein dynamisches Rollbalkendiagramm unter Verwendung von Aspose.Cells for .NET erstellen können. Unser Leitfaden zeigt, wie Sie sanfte Datenübergänge und gleitende Durchschnitte in Ihrem Diagramm implementieren können, um eine kontinuierliche und aktualisierte Anzeige zu erreichen.
keywords: Aspose.Cells for .NET, Dynamisches Rollbalkendiagramm, Datenübergänge, Sanfte Durchschnitte, Kontinuierliche Anzeige, Aktualisierte Visualisierung.
type: docs
weight: 74
url: /de/net/create-dynamic-rolling-chart/
---

## **Mögliche Verwendungsszenarien**
Ein dynamisches Rollbalkendiagramm bezieht sich auf eine grafische Darstellung, die Datenpunkte ständig verschiebt und aktualisiert. Es handelt sich um einen Diagrammtyp, der sich ständig selbst aktualisiert und dabei ein rollendes Fenster der neuesten Datenpunkte zeigt, während ältere Datenpunkte gelöscht werden, wenn neue hinzukommen.

Dynamische Rollbalkendiagramme werden häufig verwendet, um Trends und Muster in Echtzeit- oder Streaming-Daten zu visualisieren. Sie sind besonders nützlich in Szenarien, in denen zeitliche Aspekte und Veränderungen im Laufe der Zeit entscheidend sind, wie z.B. Börsenmarktanalysen, Wetterüberwachung oder Live-Performance-Verfolgung.

Diese Diagramme verwenden typischerweise Animationen oder automatisches Scrollen, um sicherzustellen, dass die aktuellsten Informationen stets präsentiert werden. Die Länge des rollenden Fensters kann angepasst werden, um einen bestimmten Zeitraum anzuzeigen, wie z.B. die letzten Stunde, den Tag oder die Woche.

Zusammenfassend ist ein dynamisches Rollbalkendiagramm eine kontinuierlich aktualisierte grafische Darstellung, die die neuesten Datenpunkte anzeigt und ältere löscht, so dass Benutzer Echtzeit-Trends und Muster beobachten können.

## **Verwenden Sie Aspose.Cells, um ein dynamisches Rollbalkendiagramm zu erstellen**
In den nächsten Absätzen zeigen wir Ihnen, wie Sie unter Verwendung von Aspose.Cells ein dynamisches Rollbalkendiagramm erstellen. Wir zeigen Ihnen den Code für das Beispiel, sowie die mit diesem Code erstellte Excel-Datei.

## **Beispielcode**
Der folgende Beispielcode wird die [Datei für das dynamische Rollbalkendiagramm](DynamicRollingChart.xlsx) generieren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

## **Anmerkungen**
In der generierten Datei können Sie weiterhin Daten in den Spalten A und B hinzufügen, während das Diagramm dynamisch die neuesten 5 Datensätze zählt. Dies wird im Beispielcode mit der "OFFSET"-Formel durchgeführt:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Sie können versuchen, die Zahl "-5" in der Formel zu "-10" zu ändern, und das dynamische Diagramm wird die neuesten 10 Datensätze zählen. Jetzt haben wir erfolgreich ein dynamisches Rollbalkendiagramm unter Verwendung von Aspose.Cells erstellt.
