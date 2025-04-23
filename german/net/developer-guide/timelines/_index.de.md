---
title: Zeitachse einfügen
linktitle: Zeitachsen
type: docs
weight: 170
url: /de/net/create-timeline/
description: Erfahren Sie, wie Sie mit Aspose.Cells eine Zeitleiste erstellen können.
---

## **Mögliche Verwendungsszenarien**

Anstatt Filter anzupassen, um Daten anzuzeigen, können Sie eine PivotTable-Zeitleiste verwenden - eine dynamische Filteroption, die es Ihnen ermöglicht, nach Datum/Uhrzeit zu filtern und den gewünschten Zeitraum mit einem Schieberegler schnell zu vergrößern. Microsoft Excel ermöglicht es Ihnen, eine Zeitleiste zu erstellen, indem Sie eine Pivottabelle auswählen und anschließend auf *Einfügen > Zeitleiste* klicken. Aspose.Cells ermöglicht es Ihnen ebenfalls, eine Zeitleiste mit der Methode [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index) zu erstellen.

## **Erstellen Sie eine Zeitleiste für eine Pivottabelle**

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispiel-Excel-Datei](input.xlsx), die die Pivottabelle enthält. Dann erstellt er die Zeitleiste basierend auf dem ersten Basis-Pivottabellenfeld. Schließlich speichert er die Arbeitsmappe im [Ausgabe-XLSX](output.xlsx)-Format. Der folgende Screenshot zeigt die von Aspose.Cells in der Ausgabe-Excel-Datei erstellte Zeitleiste.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}

{{< app/cells/assistant language="csharp" >}}
