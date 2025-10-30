---
title: Arbeitsblätter verwalten
type: docs
weight: 20
url: /de/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Entwickler können Arbeitsblätter in Microsoft Excel-Dateien mithilfe der flexiblen API von Aspose.Cells problemlos programmgesteuert erstellen und verwalten. Dieses Thema beschreibt Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft Excel-Dateien.

{{% /alert %}} 

Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) -Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine Vielzahl von Methoden zum Verwalten von Arbeitsblättern.
## **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**
Um programmgesteuert eine neue Excel-Datei zu erstellen:

1. Erstellen Sie ein Objekt der Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
1. Rufen Sie die Methode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) der [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) -Sammlung auf. Ein leeres Arbeitsblatt wird automatisch der Excel-Datei hinzugefügt. Es kann referenziert werden, indem der Blattindex des neuen Arbeitsblatts an die [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) -Sammlung übergeben wird.
1. Holen Sie sich eine Arbeitsblatt-Referenz.
1. Arbeiten Sie an den Arbeitsblättern.
1. Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die Methode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) der Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) aufrufen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Arbeitsblätter mithilfe des Blattindex zugreifen**
Der folgende Beispielcode zeigt, wie ein Arbeitsblatt unter Angabe seines Index aufgerufen oder abgerufen werden kann.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Arbeitsblätter anhand des Blattindex entfernen**
Das Entfernen von Arbeitsblättern anhand des Namens funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn der Name des Arbeitsblatts nicht bekannt ist, verwenden Sie eine überladene Version der Methode [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat), die den Blattindex des Arbeitsblatts anstelle seines Blattnamens entgegennimmt.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
