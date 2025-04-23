---
title: Zeitachse einfügen
linktitle: Zeitachsen
type: docs
weight: 170
url: /de/nodejs-cpp/create-timeline/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ eine Zeitleiste erstellen.
---

## **Mögliche Verwendungsszenarien**

Anstatt Filter anzupassen, um Daten anzuzeigen, können Sie eine PivotTable-Zeitleiste verwenden—eine dynamische Filteroption, mit der Sie leicht nach Datum/Uhrzeit filtern und den Zeitraum mit einem Schieberegler vergrößern können. Microsoft Excel ermöglicht die Erstellung einer Zeitleiste, indem eine Pivot-Tabelle ausgewählt und dann die *Einfügen > Zeitleiste* -Option geklickt wird. Aspose.Cells for Node.js via C++ ermöglicht ebenfalls die Erstellung einer Zeitleiste mit der [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-)-Methode.

## **Erstellen Sie eine Zeitleiste für eine Pivottabelle**

Siehe den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](input.xlsx), die die Pivot-Tabelle enthält. Es erstellt dann die Zeitleiste basierend auf dem ersten Basis-Pivot-Feld. Abschließend speichert es die Arbeitsmappe im [Output XLSX](output.xlsx)-Format. Die folgende Bildschirmaufnahme zeigt die von Aspose.Cells for Node.js via C++ in der Ausgabedatei erstellte Zeitleiste.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

