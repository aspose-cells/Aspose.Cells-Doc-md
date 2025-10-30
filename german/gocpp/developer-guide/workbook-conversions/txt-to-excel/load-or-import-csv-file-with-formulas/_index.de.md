---
title: CSV Datei mit Formeln laden oder importieren mit C++
linktitle: Laden oder Importieren von CSV Dateien mit Formeln
type: docs
weight: 350
url: /de/go-cpp/load-or-import-csv-file-with-formulas/
description: Laden oder importieren Sie eine CSV Datei mit Formeln mithilfe von Aspose.Cells mit Golang via C++.
---

{{% alert color="primary" %}} 

CSV-Dateien enthalten meist Textdaten und enthalten in der Regel keine Formeln. Es gibt jedoch Fälle, in denen CSV-Dateien Formeln enthalten können. Solche CSV-Dateien sollten durch Setzen von [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) auf **true** geladen werden. Sobald diese Eigenschaft auf **true** gesetzt ist, behandelt Aspose.Cells Formeln nicht als einfachen Text. Sie werden als Formeln behandelt, und die Aspose.Cells-Formelberechnungs-Engine verarbeitet sie wie üblich.

{{% /alert %}} 

Das folgende Beispiel zeigt, wie du eine CSV-Datei mit Formeln laden und importieren kannst. Du kannst jede CSV-Datei verwenden. Zur Veranschaulichung verwenden wir die [einfache CSV-Datei](5115034.csv), die folgende Daten enthält. Wie du siehst, enthält sie eine Formel.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
Der Code lädt zuerst die CSV-Datei, importiert sie erneut bei Zelle D4. Schließlich speichert er das Arbeitsbuch im XLSX-Format. Die [Ausgabedatei XLSX](5115052.xlsx) sieht folgendermaßen aus. Wie du siehst, enthalten die Zellen C3 und F4 Formeln und deren Ergebnis ist 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
