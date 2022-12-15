---
title: Zeitleiste einfügen
linktitle: Zeitleisten
type: docs
weight: 170
url: /de/java/create-timeline/
description: Erfahren Sie, wie Sie mit Aspose.Cells für Java eine Zeitleiste erstellen.
---
## **Mögliche Nutzungsszenarien**

 Anstatt Filter anzupassen, um Datumsangaben anzuzeigen, können Sie eine PivotTable-Zeitachse verwenden – eine dynamische Filteroption, mit der Sie einfach nach Datum/Uhrzeit filtern und mit einem Schieberegler den gewünschten Zeitraum vergrößern können. Microsoft Mit Excel können Sie eine Zeitleiste erstellen, indem Sie eine Pivot-Tabelle auswählen und dann auf klicken*Einfügen > Zeitachse*. Aspose.Cells für Java ermöglicht es Ihnen auch, eine Zeitleiste mit der Methode [**Worksheet.getTimelines.add()**] zu erstellen.

## **Erstellen Sie eine Zeitachse zu einer Pivot-Tabelle**

 Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die[Beispiel-Excel-Datei](input.xlsx) die die Pivot-Tabelle enthält. Anschließend erstellt es die Zeitachse basierend auf dem ersten Basis-Pivot-Feld. Schließlich speichert es die Arbeitsmappe in[Ausgang XLSX](output.xlsx) Format. Der folgende Screenshot zeigt die von Aspose.Cells erstellte Zeitleiste in der Excel-Ausgabedatei.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

