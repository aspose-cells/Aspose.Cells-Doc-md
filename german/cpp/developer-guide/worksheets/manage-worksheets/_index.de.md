---
title: Arbeitsblätter verwalten
type: docs
weight: 20
url: /de/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Entwickler können mit Aspose.Cells flexible API problemlos Arbeitsblätter in Microsoft Excel-Dateien programmgesteuert erstellen und verwalten. In diesem Thema werden Vorgehensweisen zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft Excel-Dateien beschrieben.

{{% /alert %}} 

 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) die eine Excel-Datei darstellt. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)-Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern.
## **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**
So erstellen Sie programmgesteuert eine neue Excel-Datei:

1.  Erstellen Sie ein Objekt der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Klasse.
1.  Ruf den ... an[Addieren](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) Methode der[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Sammlung. Der Excel-Datei wird automatisch ein leeres Arbeitsblatt hinzugefügt. Es kann darauf verwiesen werden, indem der Blattindex des neuen Arbeitsblatts an die übergeben wird[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung.
1. Besorgen Sie sich eine Arbeitsblattreferenz.
1. Bearbeiten Sie die Arbeitsblätter.
1.  Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die aufrufen[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Zugriff auf Arbeitsblätter über den Blattindex**
Der folgende Beispielcode zeigt, wie Sie auf ein beliebiges Arbeitsblatt zugreifen oder es abrufen, indem Sie seinen Index angeben.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Arbeitsblätter mit Blattindex entfernen**
 Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn Sie den Namen des Arbeitsblatts nicht kennen, verwenden Sie eine überladene Version von[EntfernenBei](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)Methode, die den Blattindex des Arbeitsblatts anstelle seines Blattnamens verwendet.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
