---
title: Arbeitsblätter von Microsoft Excel Dateien verwalten
linktitle: Arbeitsblätter
type: docs
weight: 90
url: /de/net/manage-worksheets/
description: Arbeitsblatt hinzufügen, Arbeitsblatt entfernen und Aktivieren Sie das Arbeitsblatt mit Aspose.Cells.
---


{{% alert color="primary" %}}

Entwickler können Arbeitsblätter in Microsoft Excel-Dateien mithilfe der flexiblen API von Aspose.Cells einfach programmgesteuert erstellen und verwalten. Dieses Thema beschreibt Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft Excel-Dateien.

{{% /alert %}}

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine Sammlung von [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern.

## **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**

Um programmgesteuert eine neue Excel-Datei zu erstellen:

1. Erstellen Sie ein Objekt der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Rufen Sie die Methode [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) der Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) auf. Ein leeres Arbeitsblatt wird automatisch zur Excel-Datei hinzugefügt. Es kann durch Übergeben des Blattindex des neuen Arbeitsblatts an die Sammlung [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) referenziert werden.
1. Holen Sie sich eine Arbeitsblatt-Referenz.
1. Arbeiten Sie an den Arbeitsblättern.
1. Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die Methode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) aufrufen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Arbeitsblätter zu einem Designer-Arbeitsblatt hinzufügen**

Der Prozess zum Hinzufügen von Arbeitsblättern zu einem Designer-Arbeitsblatt ist derselbe wie das Hinzufügen eines neuen Arbeitsblatts, mit der Ausnahme, dass die Excel-Datei bereits existiert und daher geöffnet werden sollte, bevor Arbeitsblätter hinzugefügt werden. Ein Designer-Arbeitsblatt kann durch die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) geöffnet werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Zugriff auf Arbeitsblätter mithilfe des Blattnamens**

Greifen Sie auf jedes Arbeitsblatt zu, indem Sie dessen Namen oder Index angeben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Arbeitsblätter anhand des Blattnamens entfernen**

Um Arbeitsblätter aus einer Datei zu entfernen, rufen Sie die Methode [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) der Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) auf. Geben Sie den Blattnamen an die Methode [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) an, um ein bestimmtes Arbeitsblatt zu entfernen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Arbeitsblätter anhand des Blattindex entfernen**

Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn Sie den Namen des Arbeitsblatts nicht kennen, verwenden Sie eine überladene Version der Methode [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat), die den Blattindex des Arbeitsblatts anstelle seines Blattnamens verwendet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Aktivierung von Tabellen und Markierung einer aktiven Zelle im Arbeitsblatt**

Manchmal benötigen Sie ein bestimmtes Arbeitsblatt, das aktiv und angezeigt wird, wenn ein Benutzer eine Microsoft Excel-Datei in Excel öffnet. Ebenso möchten Sie möglicherweise eine bestimmte Zelle aktivieren und die Bildlaufleisten so einstellen, dass die aktive Zelle angezeigt wird.
Aspose.Cells ist in der Lage, all diese Aufgaben zu erledigen.

Ein **aktives Tabellenblatt** ist ein Blatt, an dem Sie arbeiten: Der Name des aktiven Blattes auf der Registerkarte ist standardmäßig fett gedruckt.

Eine **aktive Zelle** ist eine ausgewählte Zelle, in die Daten eingegeben werden, wenn Sie mit der Eingabe beginnen. Es ist jeweils nur eine Zelle aktiv. Die aktive Zelle ist durch einen starken Rahmen hervorgehoben.

### **Aktivierung von Tabellen und Markierung einer Zelle als aktiv**

Aspose.Cells bietet spezifische API-Aufrufe zur Aktivierung eines Blattes und einer Zelle an. Zum Beispiel ist die Eigenschaft [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) nützlich, um das aktive Blatt in einer Arbeitsmappe festzulegen.
Ebenso wird die Eigenschaft [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) verwendet, um eine aktive Zelle im Arbeitsblatt festzulegen und abzurufen.

Um sicherzustellen, dass die horizontalen oder vertikalen Bildlaufleisten auf die Zeilen- und Spaltenindexposition eingestellt sind, um bestimmte Daten anzuzeigen, verwenden Sie die Eigenschaften [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) und [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn).

Das folgende Beispiel zeigt, wie ein Arbeitsblatt aktiviert und eine aktive Zelle darin markiert wird. In der generierten Ausgabe werden die Bildlaufleisten gescrollt, um die 2. Zeile und 2. Spalte als erste sichtbare Zeile und Spalte zu zeigen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Erweiterte Themen**
- [Arbeitsblätter kopieren und verschieben](/cells/de/net/copying-and-moving-worksheets/)
- [Anzahl der Zellen im Arbeitsblatt zählen](/cells/de/net/count-number-of-cells-in-the-worksheet/)
- [Erkennen von leeren Arbeitsblättern](/cells/de/net/detecting-empty-worksheets/)
- [Feststellen, ob das Arbeitsblatt ein Dialogblatt ist](/cells/de/net/find-if-the-worksheet-is-dialog-sheet/)
- [Arbeitsblatt eindeutige ID abrufen](/cells/de/net/get-worksheet-unique-id/)
- [Erstellen, Manipulieren oder Entfernen von Szenarien aus Arbeitsblättern](/cells/de/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Seitenumbrüche verwalten](/cells/de/net/managing-page-breaks/)
- [Seiteneinrichtungsfunktionen](/cells/de/net/page-setup-features/)
- [Mehrere Kopien eines Arbeitsblatts drucken](/cells/de/net/print-multiple-copies-of-a-worksheet/)
- [Verwenden Sie die *Sheet.SheetId*-Eigenschaft von OpenXml mit Aspose.Cells](/cells/de/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Arbeitsblattansichten](/cells/de/net/worksheet-views/)

