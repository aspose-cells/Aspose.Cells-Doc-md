---
title: Arbeitsblätter verwalten
type: docs
weight: 20
url: /de/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Entwickler können mit Aspose.Cells flexible API problemlos Arbeitsblätter in Microsoft-Excel-Dateien programmgesteuert erstellen und verwalten. In diesem Thema werden Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft-Excel-Dateien beschrieben.

{{% /alert %}} 

 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das eine Excel-Datei darstellt. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Die Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern.
##  **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**
So erstellen Sie programmgesteuert eine neue Excel-Datei:

1.  Erstellen Sie ein Objekt von[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Klasse.
1.  Ruf den[Hinzufügen](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) Methode der[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung. Der Excel-Datei wird automatisch ein leeres Arbeitsblatt hinzugefügt. Es kann referenziert werden, indem der Blattindex des neuen Arbeitsblatts an übergeben wird[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung.
1. Besorgen Sie sich eine Arbeitsblattreferenz.
1. Arbeiten Sie an den Arbeitsblättern.
1. Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die aufrufen[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **Zugriff auf Arbeitsblätter mithilfe des Blattindex**
Der folgende Beispielcode zeigt, wie Sie auf ein Arbeitsblatt zugreifen oder es abrufen, indem Sie seinen Index angeben.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **Entfernen von Arbeitsblättern mithilfe des Blattindex**
 Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn Sie den Namen des Arbeitsblatts nicht kennen, verwenden Sie eine überladene Version des[RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)Methode, die den Blattindex des Arbeitsblatts anstelle seines Blattnamens verwendet.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
