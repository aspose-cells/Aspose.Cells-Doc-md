---
title: Benennen Sie doppelte Spalten beim Exportieren von Arbeitsblattdaten automatisch um
type: docs
weight: 250
url: /de/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **Mögliche Nutzungsszenarien**

Manchmal hat der Benutzer beim Exportieren von Daten aus dem Arbeitsblatt in die Datentabelle ein Problem mit doppelten Spalten. DataTable kann keine doppelten Spalten haben, daher müssen doppelte Spalten umbenannt werden, bevor Sie Arbeitsblattdaten in die Datentabelle exportieren können. Aspose.Cells kann die doppelten Spalten automatisch gemäß der von Ihnen festgelegten Strategie mit umbenennen[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) Eigentum. Wenn Sie angeben[**Strategie umbenennen**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, Spalten werden wie Spalte1, Spalte2, Spalte3 usw. umbenannt und wenn Sie angeben[**Strategie umbenennen**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Buchstabe, dann werden die Spalten wie SpalteA, SpalteB, SpalteC usw. umbenannt.

## **Benennen Sie doppelte Spalten beim Exportieren von Arbeitsblattdaten automatisch um**

 Der folgende Beispielcode fügt einige Daten in den ersten drei Spalten des Arbeitsblatts hinzu, aber alle Spalten haben denselben Namen, dh*Menschen* . Dann exportiert es die Daten aus dem Arbeitsblatt in die Datentabelle durch Angabe[**Strategie umbenennen**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Briefstrategie. Anschließend werden die Spaltennamen der von Aspose.Cells generierten Datentabelle gedruckt. Der folgende Screenshot zeigt die Datentabelle mit exportierten Daten im Visualizer. Wie Sie sehen können, wurden doppelte Spalten in PeopleA, PeopleB usw. umbenannt.

![todo: Bild_alt_Text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes als Referenz.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
