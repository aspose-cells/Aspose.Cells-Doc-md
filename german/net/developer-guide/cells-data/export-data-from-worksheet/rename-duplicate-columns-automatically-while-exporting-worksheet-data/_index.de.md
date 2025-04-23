---
title: Automatisches Umbenennen von Duplikatspalten beim Exportieren von Arbeitsblattdaten lernen
type: docs
weight: 250
url: /de/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Erfahren Sie, wie Sie durch die API Aspose.Cells for .NET lernen, Duplikatspalten automatisch beim Exportieren von Arbeitsblattdaten umbenennen.
keywords: Duplikatspalten beim Exportieren von Arbeitsblattdaten umbenennen, Duplikatspalten automatisch beim Exportieren in DataTable umbenennen
---

## **Mögliche Verwendungsszenarien**

Manchmal hat der Benutzer ein Problem mit Duplikatspalten beim Exportieren von Daten aus dem Arbeitsblatt in die Datentabelle. DataTable kann keine Duplikatspalten haben, daher müssen Duplikatspalten umbenannt werden, bevor Sie Arbeitsblattdaten in die Datentabelle exportieren können. Aspose.Cells kann die Duplikatspalten automatisch entsprechend der von Ihnen angegebenen Strategie mit [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) Eigenschaft umbenennen. Wenn Sie [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit angeben, werden die Spalten wie Spalte1, Spalte2, Spalte3 usw. umbenannt, und wenn Sie [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter angeben, werden die Spalten wie SpalteA, SpalteB, SpalteC usw. umbenannt.

## **Benennen Sie doppelte Spalten automatisch um, während Sie Arbeitsblattdaten exportieren**

Im folgenden Beispielcode werden einige Daten in die ersten drei Spalten des Arbeitsblatts eingefügt, aber alle Spalten haben denselben Namen, d.h. *People*. Dann werden die Daten aus dem Arbeitsblatt in die Datentabelle exportiert und die Strategie [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter angegeben. Anschließend werden die Spaltennamen der von Aspose.Cells generierten Datentabelle gedruckt. Der folgende Screenshot zeigt die Datentabelle mit exportierten Daten im Visualizer. Wie Sie sehen können, wurden die Duplikatspalten in PeopleA, PeopleB usw. umbenannt.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes als Referenz.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
