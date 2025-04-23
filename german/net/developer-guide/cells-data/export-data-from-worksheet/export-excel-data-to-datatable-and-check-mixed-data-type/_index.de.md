---
title: Excel Daten in DataTable exportieren und gemischte Datentypen überprüfen
type: docs
weight: 280
url: /de/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for .NET Excel Daten in DataTable exportieren und gemischte Datentypen überprüfen können.
keywords: Excel Daten in DataTable exportieren und gemischte Datentypen überprüfen, Arbeitsbuchdaten in DataTable exportieren und gemischte Datentypen überprüfen, Daten in DataTable exportieren und gemischte Datentypen überprüfen, Arbeitsblattdaten in DataTable exportieren und gemischte Datentypen überprüfen
---

## **Mögliche Verwendungsszenarien**
Wenn eine Spalte Daten verschiedener Typen enthält, wirft das Programm eine Typausnahme beim Exportieren von Daten in eine DataTable. Beim Exportieren von Daten in eine DataTable bewertet Aspose.Cells standardmäßig den Datentyp für die Werte basierend auf dem allerersten (Zellen-) Wert in der Spalte. Wenn der Wert eine Zahl ist, bedeutet das, dass der Datentyp der Spalte numerisch wäre, was vernünftig ist. Wenn der allererste Wert eine Zahl ist, aber alphanumerische Daten oder Werte in der Spalte vorhanden sind, sollte ein Stringdatentyp zugewiesen werden. Um damit umzugehen, verwenden Sie bitte [ExportDataTable-Überlastung](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1), die [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) und versuchen Sie, das [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Boolean-Attribut auf "true" zu setzen, wenn eine Spalte sowohl numerische als auch Zeichenfolgenwerte enthält, um Fehler zu vermeiden.

## **Excel-Daten in DataTable exportieren und gemischte Datentypen überprüfen**

Das folgende Beispiel erläutert die Verwendung der Eigenschaft [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) zum Exportieren von Excel-Daten in eine DataTable. Bitte sehen Sie die [Beispiel-Excel-Datei](sample.xlsx), deren Bildschirmfoto und die Konsolenausgabe als Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **Screenshot**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Konsolenausgabe**

Unten finden Sie die Konsolenausgabe des obigen Beispielscodes

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
