---
title: Pivot-Felder in der PivotTable mit Go via C++ gruppieren
linktitle: Pivot-Felder in der PivotTable mit Go via C++ gruppieren
description: Erfahren Sie, wie Sie mit Aspose.Cells for Go via C++ Pivot-Felder in einer PivotTable gruppieren.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, PivotTable, Pivot-Feld, Pivot-Felder gruppieren, GroupBy, PivotField, Datumsgruppierung, Go
type: docs
weight: 80
url: /de/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Microsoft Excel ermöglicht es Ihnen, Pivot-Felder **in** der PivotTable zu gruppieren. Wenn zu einem Pivot-Feld eine große Datenmenge vorhanden ist, ist es häufig hilfreich, diese in Gruppen einzuteilen. Aspose.Cells bietet diese Funktion ebenfalls über die Methode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) an.

## **Pivot-Felder in der PivotTable gruppieren**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716818.xlsx) und führt mithilfe der Methode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) eine Gruppierung des ersten Pivot-Felds durch. Anschließend aktualisiert er die PivotTable, berechnet deren Daten und speichert die Arbeitsmappe als [Ausgabe-Excel-Datei](64716817.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Wie im Screenshot zu sehen ist, ist das erste Pivot-Feld nun nach Monaten und Quartalen gruppiert.
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}