---
title: Benennen Sie doppelte Spalten beim Exportieren von Arbeitsblattdaten automatisch um
type: docs
weight: 250
url: /de/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Erfahren Sie, wie Sie doppelte Spalten automatisch umbenennen, während Sie Arbeitsblattdaten über Aspose.Cells for .NET API exportieren.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **Mögliche Nutzungsszenarien**

 Manchmal stößt der Benutzer beim Exportieren von Daten aus dem Arbeitsblatt in die Datentabelle auf das Problem doppelter Spalten. DataTable darf keine doppelten Spalten enthalten, daher müssen doppelte Spalten umbenannt werden, bevor Sie Arbeitsblattdaten in die Datentabelle exportieren können. Aspose.Cells kann die doppelten Spalten automatisch entsprechend der von Ihnen angegebenen Strategie umbenennen[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) Eigentum. Wenn Sie angeben[**Strategie umbenennen**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, Spalten werden wie Spalte1, Spalte2, Spalte3 usw. umbenannt und wenn Sie angeben[**Strategie umbenennen**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, dann werden die Spalten wie SpalteA, SpalteB, SpalteC usw. umbenannt.

##  **Benennen Sie doppelte Spalten beim Exportieren von Arbeitsblattdaten automatisch um**

Der folgende Beispielcode fügt einige Daten in die ersten drei Spalten des Arbeitsblatts ein, aber alle Spalten haben den gleichen Namen, z. B. *Personen*. Anschließend exportiert es die Daten aus dem Arbeitsblatt in die Datentabelle, indem es Folgendes angibt[**Strategie umbenennen**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Briefstrategie. Anschließend werden die Spaltennamen der von Aspose.Cells generierten Datentabelle gedruckt. Der folgende Screenshot zeigt die Datentabelle mit exportierten Daten im Visualizer. Wie Sie sehen können, wurden doppelte Spalten in „PersonenA“, „PersonenB“ usw. umbenannt.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes als Referenz.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
