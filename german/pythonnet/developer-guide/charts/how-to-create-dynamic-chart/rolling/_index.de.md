---
title: Wie erstellt man ein dynamisches Rollbalkendiagramm
description: Erfahren Sie, wie Sie mit Aspose.Cells für Python via .NET ein dynamisches rollenbasiertes Diagramm erstellen. Unser Leitfaden zeigt Ihnen, wie Sie sanfte Datenübergänge und gleitende Durchschnittswerte in Ihrem Diagramm implementieren, um eine kontinuierliche und aktualisierte Anzeige zu gewährleisten.
keywords: Aspose.Cells für Python via .NET, Dynamisches Rollendiagramm, Datenübergänge, Sanfte Durchschnitte, Kontinuierliche Anzeige, Aktualisierte Visualisierung.
type: docs
weight: 74
url: /de/python-net/create-dynamic-rolling-chart/
---

## **Mögliche Verwendungsszenarien**
Ein dynamisches Rollbalkendiagramm bezieht sich auf eine grafische Darstellung, die Datenpunkte ständig verschiebt und aktualisiert. Es handelt sich um einen Diagrammtyp, der sich ständig selbst aktualisiert und dabei ein rollendes Fenster der neuesten Datenpunkte zeigt, während ältere Datenpunkte gelöscht werden, wenn neue hinzukommen.

Dynamische Rollbalkendiagramme werden häufig verwendet, um Trends und Muster in Echtzeit- oder Streaming-Daten zu visualisieren. Sie sind besonders nützlich in Szenarien, in denen zeitliche Aspekte und Veränderungen im Laufe der Zeit entscheidend sind, wie z.B. Börsenmarktanalysen, Wetterüberwachung oder Live-Performance-Verfolgung.

Diese Diagramme verwenden typischerweise Animationen oder automatisches Scrollen, um sicherzustellen, dass die aktuellsten Informationen stets präsentiert werden. Die Länge des rollenden Fensters kann angepasst werden, um einen bestimmten Zeitraum anzuzeigen, wie z.B. die letzten Stunde, den Tag oder die Woche.

Zusammenfassend ist ein dynamisches Rollbalkendiagramm eine kontinuierlich aktualisierte grafische Darstellung, die die neuesten Datenpunkte anzeigt und ältere löscht, so dass Benutzer Echtzeit-Trends und Muster beobachten können.

## **Verwenden Sie Aspose.Cells für Python via .NET, um ein dynamisches Rollendiagramm zu erstellen.**
In den nächsten Abschnitten zeigen wir Ihnen, wie Sie mit Aspose.Cells für Python via .NET ein dynamisches Rollendiagramm erstellen. Wir zeigen Ihnen den Code für das Beispiel sowie die mit diesem Code erstellte Excel-Datei.

## **Beispielcode**
Der folgende Beispielcode wird die [Datei für das dynamische Rollbalkendiagramm](DynamicRollingChart.xlsx) generieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-rolling-chart.py" >}}

## **Anmerkungen**
In der generierten Datei können Sie weiterhin Daten in den Spalten A und B hinzufügen, während das Diagramm dynamisch die neuesten 5 Datensätze zählt. Dies wird im Beispielcode mit der "OFFSET"-Formel durchgeführt:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Sie können versuchen, die Zahl "-5" in der Formel in "-10" zu ändern, und das dynamische Diagramm wird die letzten 10 Datenreihen zählen. Jetzt haben wir erfolgreich ein dynamisches Rollendiagramm mit Aspose.Cells für Python via .NET erstellt.
{{< app/cells/assistant language="python-net" >}}
