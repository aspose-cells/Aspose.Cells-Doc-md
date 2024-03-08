---
title: Exportieren Sie Excel-Daten in DataTable und prüfen Sie den gemischten Datentyp
type: docs
weight: 280
url: /de/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Erfahren Sie, wie Sie Excel-Daten in DataTable exportieren und gemischte Datentypen über Aspose.Cells for .NET API überprüfen.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **Mögliche Nutzungsszenarien**
 Wenn eine Spalte Daten verschiedener Typen enthält, löst das Programm beim Exportieren von Daten in eine DataTable eine Typausnahme aus. Beim Exportieren von Datentabellen wertet Aspose.Cells standardmäßig den Datentyp für die Werte basierend auf dem allerersten (Zellen-)Wert in der Spalte aus. Wenn der Wert also eine Zahl ist, bedeutet dies, dass der Datentyp der Spalte numerisch ist, was sinnvoll ist. Wenn der allererste Wert eine Zahl ist, die Spalte jedoch alphanumerische Daten oder Werte enthält, sollte ein String-Datentyp zugewiesen werden. Um damit klarzukommen, verwenden Sie bitte[ExportDataTable-Überladung](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) was beinhaltet[ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) und versuche es einzustellen[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Boolesches Attribut auf „true“, wenn eine Spalte sowohl numerische als auch Zeichenfolgenwerte enthält, um einen Fehler zu vermeiden.

##  **Exportieren Sie Excel-Daten in DataTable und prüfen Sie den gemischten Datentyp**

 Das folgende Beispiel erläutert die Verwendung von[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Eigenschaft zum Exportieren von Excel-Daten in eine Datentabelle. Bitte sehen Sie sich ... an[Beispiel-Excel-Datei](sample.xlsx), seinen Screenshot und die Konsolenausgabe als Referenz.

###  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **Bildschirmfoto**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **Konsolenausgabe**

Unten finden Sie die Konsolen-Debug-Ausgabe des obigen Beispielcodes

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
