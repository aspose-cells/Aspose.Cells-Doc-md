---
title: So erstellen Sie ein Tornado-Diagramm
type: docs
weight: 73
url: /de/net/create-tornado-chart/
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET API ein Tornado-Diagramm erstellen.
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
---
##  **Einführung**
Ein Tornado-Diagramm, auch Tornado-Diagramm oder Tornado-Graph genannt, ist eine Art Datenvisualisierung, die häufig für Sensitivitätsanalysen in Excel verwendet wird. Es hilft Ihnen, die Auswirkungen sich ändernder Variablen auf ein bestimmtes Ergebnis oder Ergebnis zu verstehen.

##  **So erstellen Sie ein Tornado-Diagramm in Excel**
Sie können ein Tornado-Diagramm in Excel erstellen, indem Sie die folgenden Schritte ausführen:
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen -> Diagramme -> Säulen- oder Balkendiagramm einfügen -> Gestapeltes Balkendiagramm. Klick es an.
<br>
<img src="1.png" width=70% />
2. Y-Achse ändern: Klicken Sie mit der rechten Maustaste auf die y-Achse. Klicken Sie auf die Formatachse. Klicken Sie in den Etiketten auf das Dropdown-Menü „Etikettenposition“ und wählen Sie „Niedriges Element“ aus.
<br>
<img src="2.png" width=70% />
3. Wählen Sie einen beliebigen Balken aus und gehen Sie zur Formatierung. Stellen Sie eine geeignete Spaltbreite ein.
<br>
<img src="3.png" width=70% />
4. Entfernen wir das Minuszeichen (-) aus der Tornado-Karte. Wählen Sie die x-Achse aus. Gehen Sie zur Formatierung. Klicken Sie in den Achsenoptionen auf die Zahl. Wählen Sie in der Kategorie „Benutzerdefiniert“ aus. Schreiben Sie im Formatcode ###0,###0. Klicken Sie auf Hinzufügen.
<br>
<img src="4.png" width=70% />
5. Klicken Sie auf die Y-Achse und gehen Sie zu den Achsenoptionen. Aktivieren Sie in den Achsenoptionen die Option „Kategorien in umgekehrter Reihenfolge“.
<br>
<img src="5.png" width=70% />

##  **So fügen Sie ein Tornado-Diagramm in Aspose.Cells hinzu**
 Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die[Beispiel-Excel-Datei](sample.xlsx) das einige Beispieldaten enthält. Anschließend erstellt es das gestapelte Balkendiagramm auf Grundlage der Ausgangsdaten und legt relevante Eigenschaften fest. Schließlich wird die Arbeitsmappe gespeichert[Ausgabeformat XLSX](out.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Tornado-Diagramm in der Excel-Ausgabedatei.
<br>
<img src="6.png" width=70% />

###  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}