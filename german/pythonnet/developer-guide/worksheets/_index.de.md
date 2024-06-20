---
title: Arbeitsblätter von Microsoft Excel Dateien verwalten
linktitle: Arbeitsblätter
type: docs
weight: 90
url: /de/python-net/manage-worksheets/
description: Dieser Artikel zeigt, wie Arbeitsblätter von Microsoft Excel Dateien mit der Aspose.Cells for Python via .NET API verwaltet werden.
keywords: Python Excel Bibliothek, Arbeitsblätter von Microsoft Excel Dateien mit Python verwalten, Arbeitsblatt in Python hinzufügen, Arbeitsblatt in Python entfernen, Arbeitsblätter zu neuer Excel Datei hinzufügen, Arbeitsblätter zu Designer Tabelle in Python hinzufügen, Arbeitsblätter über Blattnamen in Python abrufen, Arbeitsblätter über Blattnamen in Python entfernen, Arbeitsblätter über Blattindex in Python entfernen, Blätter aktivieren und eine Zelle aktivieren.
---


{{% alert color="primary" %}}

Entwickler können Arbeitsblätter in Microsoft Excel-Dateien mithilfe der flexiblen API von Aspose.Cells einfach programmgesteuert erstellen und verwalten. Dieses Thema beschreibt Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft Excel-Dateien.

{{% /alert %}}

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine Sammlung von [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern.

## **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**

Um programmgesteuert eine neue Excel-Datei zu erstellen:

1. Erstellen Sie ein Objekt der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Rufen Sie die Methode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) der Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) auf. Ein leeres Arbeitsblatt wird automatisch zur Excel-Datei hinzugefügt. Es kann durch Übergeben des Blattindex des neuen Arbeitsblatts an die Sammlung [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) referenziert werden.
1. Holen Sie sich eine Arbeitsblatt-Referenz.
1. Arbeiten Sie an den Arbeitsblättern.
1. Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die Methode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) aufrufen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **Hinzufügen von Arbeitsblättern zu einer Designer-Tabelle**

Der Prozess zum Hinzufügen von Arbeitsblättern zu einem Designer-Arbeitsblatt ist derselbe wie das Hinzufügen eines neuen Arbeitsblatts, mit der Ausnahme, dass die Excel-Datei bereits existiert und daher geöffnet werden sollte, bevor Arbeitsblätter hinzugefügt werden. Ein Designer-Arbeitsblatt kann durch die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) geöffnet werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **Arbeitsblätter über Blattnamen abrufen**

Greifen Sie auf jedes Arbeitsblatt zu, indem Sie dessen Namen oder Index angeben.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **Arbeitsblätter über Blattnamen entfernen**

Um Arbeitsblätter aus einer Datei zu entfernen, rufen Sie die Methode [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) der Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) auf. Geben Sie den Blattnamen an die Methode [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) an, um ein bestimmtes Arbeitsblatt zu entfernen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **Arbeitsblätter über Blattindex entfernen**

Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn der Arbeitsblattname nicht bekannt ist, verwenden Sie die Methode [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int), die den Tabellenindex des Arbeitsblatts anstelle seines Tabellennamens akzeptiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **Blätter aktivieren und eine Zelle in Arbeitsblatt aktivieren**

Manchmal benötigen Sie ein bestimmtes Arbeitsblatt, das aktiv und angezeigt wird, wenn ein Benutzer eine Microsoft Excel-Datei in Excel öffnet. Ebenso möchten Sie möglicherweise eine bestimmte Zelle aktivieren und die Bildlaufleisten so einstellen, dass die aktive Zelle angezeigt wird.
Aspose.Cells ist in der Lage, all diese Aufgaben zu erledigen.

Ein **aktives Tabellenblatt** ist ein Blatt, an dem Sie arbeiten: Der Name des aktiven Blattes auf der Registerkarte ist standardmäßig fett gedruckt.

Eine **aktive Zelle** ist eine ausgewählte Zelle, in die Daten eingegeben werden, wenn Sie mit der Eingabe beginnen. Es ist jeweils nur eine Zelle aktiv. Die aktive Zelle ist durch einen starken Rahmen hervorgehoben.

### **Blätter aktivieren und eine Zelle aktivieren**

Aspose.Cells bietet spezifische API-Aufrufe zur Aktivierung eines Blattes und einer Zelle an. Zum Beispiel ist die Eigenschaft [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) nützlich, um das aktive Blatt in einer Arbeitsmappe festzulegen.
Ebenso wird die Eigenschaft [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) verwendet, um eine aktive Zelle im Arbeitsblatt festzulegen und abzurufen.

Um sicherzustellen, dass die horizontalen oder vertikalen Bildlaufleisten auf die Zeilen- und Spaltenindexposition eingestellt sind, um bestimmte Daten anzuzeigen, verwenden Sie die Eigenschaften [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) und [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/).

Das folgende Beispiel zeigt, wie ein Arbeitsblatt aktiviert und eine aktive Zelle darin markiert wird. In der generierten Ausgabe werden die Bildlaufleisten gescrollt, um die 2. Zeile und 2. Spalte als erste sichtbare Zeile und Spalte zu zeigen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

