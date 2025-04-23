---
title: Arbeitsblätter verwalten
type: docs
weight: 20
url: /de/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

Entwickler können Arbeitsblätter in Microsoft Excel-Dateien mithilfe der flexiblen API von Aspose.Cells problemlos programmgesteuert erstellen und verwalten. Dieses Thema beschreibt Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft Excel-Dateien.

{{% /alert %}}

Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)die eine Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine Vielzahl von Methoden zur Verwaltung von Arbeitsblättern.

## **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**

Um programmgesteuert eine neue Excel-Datei zu erstellen:

1. Erstellen Sie ein Objekt der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse.
1. Rufen Sie die [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) Methode der [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung auf. Ein leeres Arbeitsblatt wird automatisch zur Excel-Datei hinzugefügt. Dieses kann durch Übergabe des Blattindex an die [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung referenziert werden.
1. Holen Sie sich eine Arbeitsblatt-Referenz.
1. Arbeiten Sie an den Arbeitsblättern.
1. Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) Methode der [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse aufrufen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Arbeitsblätter mithilfe des Blattindex zugreifen**

Der folgende Beispielcode zeigt, wie ein Arbeitsblatt unter Angabe seines Index aufgerufen oder abgerufen werden kann.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Arbeitsblätter anhand des Blattindex entfernen**

Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn Sie den Namen des Arbeitsblatts nicht kennen, verwenden Sie eine überladene Version der [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) Methode, die den Blattindex anstelle des Blattnamens akzeptiert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
