---
title: Verwalten Sie Arbeitsblätter von Microsoft Excel-Dateien.
linktitle: Arbeitsblätter
type: docs
weight: 90
url: /de/net/manage-worksheets/
description: Arbeitsblatt hinzufügen, Arbeitsblatt entfernen und aktives Blatt mit Aspose.Cells.
---
{{% alert color="primary" %}}

Entwickler können Arbeitsblätter in Microsoft-Excel-Dateien einfach programmgesteuert mit Aspose.Cells' flexible API erstellen und verwalten. In diesem Thema werden Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft-Excel-Dateien beschrieben.

{{% /alert %}}

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern.

## **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**

So erstellen Sie programmgesteuert eine neue Excel-Datei:

1.  Erstellen Sie ein Objekt der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse.
1.  Ruf den ... an[**Addieren**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) Methode der[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Klasse. Der Excel-Datei wird automatisch ein leeres Arbeitsblatt hinzugefügt. Es kann darauf verwiesen werden, indem der Blattindex des neuen Arbeitsblatts an die übergeben wird[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung.
1. Besorgen Sie sich eine Arbeitsblattreferenz.
1. Bearbeiten Sie die Arbeitsblätter.
1.  Speichern Sie die neue Excel-Datei mit neuen Arbeitsblättern, indem Sie die aufrufen[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse'[**Speichern**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Hinzufügen von Arbeitsblättern zu einer Designer-Tabelle**

 Der Vorgang zum Hinzufügen von Arbeitsblättern zu einem Designer-Arbeitsblatt ist der gleiche wie beim Hinzufügen eines neuen Arbeitsblatts, mit der Ausnahme, dass die Excel-Datei bereits vorhanden ist und daher geöffnet werden sollte, bevor Arbeitsblätter hinzugefügt werden. Eine Designer-Tabelle kann mit geöffnet werden[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Zugriff auf Arbeitsblätter mit Blattname**

Greifen Sie auf ein beliebiges Arbeitsblatt zu, indem Sie seinen Namen oder Index angeben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Entfernen von Arbeitsblättern unter Verwendung des Blattnamens**

Um Arbeitsblätter aus einer Datei zu entfernen, rufen Sie die auf[**EntfernenBei**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) Methode von[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Klasse. Übergeben Sie den Blattnamen an die[**EntfernenBei**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)Methode zum Entfernen eines bestimmten Arbeitsblatts.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Arbeitsblätter mit Blattindex entfernen**

 Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn Sie den Namen des Arbeitsblatts nicht kennen, verwenden Sie eine überladene Version von[**EntfernenBei**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)Methode, die den Blattindex des Arbeitsblatts anstelle seines Blattnamens verwendet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Aktivieren von Blättern und Aktivieren von Cell im Arbeitsblatt**

Manchmal muss ein bestimmtes Arbeitsblatt aktiv sein und angezeigt werden, wenn ein Benutzer eine Microsoft-Excel-Datei in Excel öffnet. Ebenso möchten Sie vielleicht eine bestimmte Zelle aktivieren und die Bildlaufleisten so einstellen, dass sie die aktive Zelle anzeigen.
Aspose.Cells ist in der Lage, all diese Aufgaben zu erledigen.

 Ein**aktives Blatt** ist ein Blatt, an dem Sie gerade arbeiten: Der Name des aktiven Blatts auf der Registerkarte ist standardmäßig fett.

 Ein**aktive Zelle** ist eine ausgewählte Zelle, die Zelle, in die Daten eingegeben werden, wenn Sie mit der Eingabe beginnen. Es ist immer nur eine Zelle aktiv. Die aktive Zelle wird durch einen dicken Rahmen hervorgehoben.

### **Blätter aktivieren und Cell aktivieren**

Aspose.Cells bietet spezifische API-Aufrufe zum Aktivieren eines Blatts und einer Zelle. Zum Beispiel die[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)-Eigenschaft ist nützlich, um das aktive Blatt in einer Arbeitsmappe festzulegen.
Ähnlich,[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)-Eigenschaft wird verwendet, um eine aktive Zelle im Arbeitsblatt festzulegen und abzurufen.

Um sicherzustellen, dass sich die horizontalen oder vertikalen Bildlaufleisten an der Zeilen- und Spaltenindexposition befinden, an der Sie bestimmte Daten anzeigen möchten, verwenden Sie die[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) und[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)Eigenschaften.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt aktivieren und eine aktive Zelle darin erstellen. In der generierten Ausgabe werden die Bildlaufleisten gescrollt, um die 2. Zeile und 2. Spalte als ihre erste sichtbare Zeile und Spalte zu machen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Themen vorantreiben**
- [Kopieren und Verschieben von Arbeitsblättern](/cells/de/net/copying-and-moving-worksheets/)
- [Zählen Sie die Anzahl der Zellen im Arbeitsblatt](/cells/de/net/count-number-of-cells-in-the-worksheet/)
- [Leere Arbeitsblätter erkennen](/cells/de/net/detecting-empty-worksheets/)
- [Finden Sie heraus, ob das Arbeitsblatt ein Dialogblatt ist](/cells/de/net/find-if-the-worksheet-is-dialog-sheet/)
- [Holen Sie sich die eindeutige ID des Arbeitsblatts](/cells/de/net/get-worksheet-unique-id/)
- [Erstellen, bearbeiten oder entfernen Sie Szenarien aus Arbeitsblättern](/cells/de/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Seitenumbrüche verwalten](/cells/de/net/managing-page-breaks/)
- [Seiteneinrichtungsfunktionen](/cells/de/net/page-setup-features/)
- [Drucken Sie mehrere Kopien eines Arbeitsblatts](/cells/de/net/print-multiple-copies-of-a-worksheet/)
- [Verwenden Sie die Sheet.SheetId-Eigenschaft von OpenXml mit Aspose.Cells](/cells/de/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Arbeitsblattansichten](/cells/de/net/worksheet-views/)

