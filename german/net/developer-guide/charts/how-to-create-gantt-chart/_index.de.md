---
title: Wie man ein Gantt Diagramm erstellt
linktitle: Wie man ein Gantt Diagramm erstellt
type: docs
weight: 72
url: /de/net/how-to-create-gantt-chart/
description: Lernen Sie, wie man ein Gantt Diagramm mit Aspose.Cells for .NET API erstellt.
keywords: C# ein Gantt Diagramm erstellen, ein Gantt Diagramm hinzufügen, ein Gantt Diagramm einfügen
---

## **Was ist ein Gantt-Diagramm**

Ein Gantt-Diagramm ist ein Typ von Balkendiagramm, das einen Projektzeitplan veranschaulicht. Es zeigt die Start- und Enddaten der verschiedenen Elemente eines Projekts. Jede Aufgabe oder Aktivität wird durch eine Leiste dargestellt, deren Länge ihrer Dauer entspricht. Gantt-Diagramme zeigen auch Abhängigkeiten zwischen Aufgaben an, was es Projektmanagern ermöglicht, die Reihenfolge zu visualisieren, in der Aufgaben abgeschlossen werden müssen. Sie werden in der Projektplanung weit verbreitet eingesetzt, um Projekte effektiv zu planen, zu terminieren und zu verfolgen.

## **Wie man ein Gantt-Diagramm in Excel erstellt**

Sie können ein Gantt-Diagramm in Excel erstellen, indem Sie diese Schritte befolgen:
1. Fügen Sie einige Daten für das Gantt-Diagramm hinzu. 
<br>
<img src="00.png" width=50% />
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. In unserem Beispiel handelt es sich um B1:B7, und fügen Sie dann das **Gestapelte Balken**-Diagramm ein.
<br>
<img src="1.png" width=50% />

1. Wählen Sie das Diagramm aus, **Daten auswählen**->**Hinzufügen**, und legen Sie die **Serienname** und den **Serienwert** wie folgt fest.
<br>
<img src="2.png" width=50% />

1. Wählen Sie das Diagramm aus, bearbeiten Sie die **Horizontale(Kategorie) Achsenbeschriftungen**.
<br>
<img src="3.png" width=50% />

1. **Achse formatieren** die Y-Achse, wählen Sie **Kategorien in umgekehrter Reihenfolge** aus.
1. Wählen Sie die **Blaue Serie** aus und setzen Sie die **Füllung->Keine Füllung**.
1. **Achse formatieren** die X-Achse, legen Sie das **Minimum und Maximum**(1/5/2019:43470,1/30/2019:43494) fest.
<br>
<img src="4.png" width=50% />

1. **Datenbeschriftungen hinzufügen** für das Diagramm, nun erhalten Sie ein Gantt-Diagramm.
<br>
<img src="0.png" width=50% />


## **So fügen Sie ein Gantt-Diagramm in Aspose.Cells hinzu**
Bitte sehen Sie den folgenden Beispielcode. Es lädt die [Beispieldatei Excel](sample.xlsx), die einige Beispieldaten enthält. Dann erstellt es das gestapelte Balkendiagramm basierend auf den anfänglichen Daten und setzt relevante Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX-Format](result.xlsx). Der folgende Screenshot zeigt das Gantt-Diagramm, das von Aspose.Cells in der Ausgabe-Excel-Datei erstellt wurde.
<br>
<img src="5.png" width=60% />

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

