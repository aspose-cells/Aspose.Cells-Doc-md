---
title: So erstellen Sie ein Gantt Diagramm
linktitle: So erstellen Sie ein Gantt Diagramm
type: docs
weight: 72
url: /de/net/how-to-create-gantt-chart/
description: Erfahren Sie, wie Sie mit der Aspose.Cells for .NET API ein Gantt Diagramm erstellen.
keywords: C# Gantt Diagramm erstellen, Gantt Diagramm hinzufügen, Gantt Diagramm einfügen
---

## **Was ist ein Gantt-Diagramm?**

Ein Gantt-Diagramm ist eine Art Balkendiagramm, das einen Projektzeitplan veranschaulicht. Es zeigt die Anfangs- und Enddaten der verschiedenen Elemente eines Projekts. Jede Aufgabe oder Aktivität wird durch einen Balken dargestellt, dessen Länge ihrer Dauer entspricht. Gantt-Diagrams zeigen auch Abhängigkeiten zwischen Aufgaben, sodass Projektmanager die Reihenfolge der Aufgaben visualisieren können. Sie werden häufig im Projektmanagement verwendet, um Projekte effektiv zu planen, zu planen und zu verfolgen.

## **So erstellen Sie ein Gantt-Diagramm in Excel**

Sie können in Excel ein Gantt-Diagramm erstellen, indem Sie diese Schritte befolgen:
1. Fügen Sie einige Daten für das Gantt-Diagramm hinzu. 
<br>
<img src="00.png" width=50% />
1. Wähle die Daten aus und gehe zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapelte Balken. In unserem Beispiel sind das B1:B7, und dann Einfügen **Gestapeltes Balken**-Diagramm.
<br>
<img src="1.png" width=50% />

1. Wähle das Diagramm, **Daten auswählen**->**Hinzufügen**, setze den **Seriennamen** und **Serienwerte** wie folgt.
<br>
<img src="2.png" width=50% />

1. Wählen Sie das Diagramm aus, bearbeiten Sie die **Horizontalen (Kategorie) Achsenbeschriftungen**.
<br>
<img src="3.png" width=50% />

1. **Achse formatieren** des Y-Achse, wählen Sie **Kategorien umkehren**.
1. Wähle die **Blaue Serie** und setze **Füllung->Keine Füllung**.
1. **Achse formatieren** für die X-Achse, setze die **Minimalen und Maximalen** Werte (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Datenbeschriftungen hinzufügen** für das Diagramm, jetzt erhältst du ein Gantt-Diagramm.
<br>
<img src="0.png" width=50% />


## **So fügen Sie ein Gantt-Diagramm in Aspose.Cells hinzu**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispiel-Excel-Datei](sample.xlsx), die einige Beispieldaten enthält. Anschließend erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt die entsprechenden Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe XLSX-Format](result.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Gantt-Diagramm in der Ausgabedatei.
<br>
<img src="5.png" width=60% />

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
