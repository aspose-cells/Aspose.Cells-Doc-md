---
title: Timeline mit Golang über C++ einfügen
linktitle: Zeitachsen
type: docs
weight: 170
url: /de/go-cpp/create-timeline/
description: Erfahren Sie, wie Sie mit Aspose.Cells in C++ eine Zeitleiste erstellen.
---

## **Mögliche Verwendungsszenarien**

Anstatt Filter anzupassen, um Daten anzuzeigen, können Sie eine PivotTable-Zeitleiste verwenden - eine dynamische Filteroption, mit der Sie einfach nach Datum/Uhrzeit filtern und mit einem Schieberegler in den Zeitraum hineinzoomen können. Microsoft Excel ermöglicht es Ihnen, eine Zeitleiste zu erstellen, indem Sie eine Pivot-Tabelle auswählen und dann auf *Einfügen > Zeitleiste* klicken. Aspose.Cells ermöglicht ebenfalls die Erstellung einer Zeitleiste mit der [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/) Methode.

## **Erstellen Sie eine Zeitleiste für eine Pivottabelle**

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispiel-Excel-Datei](input.xlsx), die die Pivottabelle enthält. Dann erstellt er die Zeitleiste basierend auf dem ersten Basis-Pivottabellenfeld. Schließlich speichert er die Arbeitsmappe im [Ausgabe-XLSX](output.xlsx)-Format. Der folgende Screenshot zeigt die von Aspose.Cells in der Ausgabe-Excel-Datei erstellte Zeitleiste.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}
