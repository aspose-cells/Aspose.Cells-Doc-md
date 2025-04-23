---
title: Slicer einfügen
linktitle: Slicer
type: docs
weight: 170
url: /de/nodejs-cpp/create-slicer/
description: Verwalten Sie die Slicer von Excel Dateien mit Aspose.Cells for Node.js via C++.
---

## **Mögliche Verwendungsszenarien**

Ein Slicer wird verwendet, um Daten schnell zu filtern. Er kann verwendet werden, um Daten sowohl in einer Tabelle als auch in einer Pivot-Tabelle zu filtern. Microsoft Excel ermöglicht es, einen Slicer durch Auswahl einer Tabelle oder Pivot-Tabelle zu erstellen und dann auf *Einfügen > Slicer* zu klicken. Aspose.Cells for Node.js via C++ ermöglicht auch die Erstellung eines Slicers mit der [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-)-Methode.

## **Erstellen Sie ein Schneidwerkzeug zu einem Pivot-Table**

Siehe den folgenden Beispielcode. Es lädt die [Beispieldatei Excel](67338470.xlsx), die die Pivot-Tabelle enthält. Es erstellt dann den Slicer basierend auf dem ersten Basis-Pivot-Feld. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX](67338471.xlsx) und im [Ausgabe-XLSB](67338472.xlsb)-Format. Der folgende Screenshot zeigt den von Aspose.Cells for Node.js via C++ erstellten Slicer in der Ausgabedatei.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Erstellen Sie ein Schneidwerkzeug zu Excel-Tabelle**

Bitte beachten Sie den folgenden Beispielcode. Es lädt die [Beispieldatei Excel](sampleCreateSlicerToExcelTable.xlsx), die eine Tabelle enthält. Anschließend wird der Slicer basierend auf der ersten Spalte erstellt. Schließlich speichert es die Arbeitsmappe im Format [output XLSX](outputCreateSlicerToExcelTable.xlsx).

### **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
