---
title: Zeitachse einfügen
linktitle: Zeitachsen
type: docs
weight: 170
url: /de/java/create-timeline/
description: Erfahren Sie, wie Sie mit Aspose.Cells für Java eine Zeitachse erstellen können.
---

## **Mögliche Verwendungsszenarien**

Anstatt Filter anzupassen, um Daten anzuzeigen, können Sie eine PivotTable-Zeitleiste verwenden - eine dynamische Filteroption, mit der Sie ganz einfach nach Datum/Uhrzeit filtern und den gewünschten Zeitraum mit einer Schiebereglersteuerung vergrößern können. Microsoft Excel ermöglicht es Ihnen, eine Zeitachse zu erstellen, indem Sie eine Pivot-Tabelle auswählen und dann auf *Einfügen > Zeitachse* klicken. Auch Aspose.Cells für Java ermöglicht es Ihnen, eine Zeitachse mit der Methode [**Worksheet.getTimelines.add()**] zu erstellen.

## **Erstellen Sie eine Zeitleiste für eine Pivottabelle**

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispiel-Excel-Datei](input.xlsx), die die Pivottabelle enthält. Dann erstellt er die Zeitleiste basierend auf dem ersten Basis-Pivottabellenfeld. Schließlich speichert er die Arbeitsmappe im [Ausgabe-XLSX](output.xlsx)-Format. Der folgende Screenshot zeigt die von Aspose.Cells in der Ausgabe-Excel-Datei erstellte Zeitleiste.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

