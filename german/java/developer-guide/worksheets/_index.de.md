---
title: Arbeitsblätter verwalten
linktitle: Arbeitsblätter
type: docs
weight: 60
url: /de/java/manage-worksheets/
---
{{% alert color="primary" %}}

Entwickler können mit dem flexiblen API von Aspose.Cells problemlos Arbeitsblätter in ihren Excel-Dateien programmgesteuert erstellen und verwalten. In diesem Thema werden einige Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Excel-Dateien erläutert.

{{% /alert %}}

Das Verwalten von Arbeitsblättern mit Aspose.Cells ist so einfach wie das ABC. In diesem Abschnitt beschreiben wir, wie wir:

1. Erstellen Sie eine neue Excel-Datei von Grund auf und fügen Sie ein Arbeitsblatt hinzu
1. Fügen Sie Arbeitsblätter zu Designer-Tabellen hinzu
1. Zugriff auf Arbeitsblätter mit Blattname
1. Entfernen Sie ein Arbeitsblatt aus einer Excel-Datei unter Verwendung seines Blattnamens
1. Entfernen Sie ein Arbeitsblatt aus einer Excel-Datei, indem Sie seinen Blattindex verwenden

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) die eine Excel-Datei darstellt.[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Die Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Sehen wir uns an, wie wir diese grundlegenden APIs nutzen können.

## **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**

 Um eine neue Excel-Datei programmgesteuert zu erstellen, müssten Entwickler ein Objekt von erstellen[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Excel-Datei darstellt. Dann können Entwickler anrufen[**hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) Methode der[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Wenn wir anrufen[**hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() )-Methode wird der Excel-Datei automatisch ein leeres Arbeitsblatt hinzugefügt, auf das verwiesen werden kann, indem der Blattindex des neu hinzugefügten Arbeitsblatts an die übergeben wird[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Nachdem die Arbeitsblattreferenz abgerufen wurde, können Entwickler an ihren Arbeitsblättern gemäß ihren Anforderungen arbeiten. Nachdem die Arbeit an den Arbeitsblättern erledigt ist, können Entwickler ihre neu erstellte Excel-Datei mit neuen Arbeitsblättern speichern, indem sie das aufrufen[**sparen**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) Methode der[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Klasse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Hinzufügen von Arbeitsblättern zu einer Designer-Tabelle**

Das Hinzufügen von Arbeitsblättern zu einer Designer-Tabellenkalkulation ist völlig identisch mit dem oben beschriebenen Ansatz, mit der Ausnahme, dass die Excel-Datei bereits erstellt wurde und wir diese Excel-Datei zuerst öffnen müssen, bevor wir ihr ein Arbeitsblatt hinzufügen können. Eine Designer-Tabellenkalkulation kann geöffnet werden, indem der Dateipfad oder Stream während der Initialisierung übergeben wird[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Klasse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Zugriff auf Arbeitsblätter mit Blattname**

Entwickler können auf jedes Arbeitsblatt zugreifen oder es abrufen, indem sie seinen Namen oder Index angeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Entfernen von Arbeitsblättern unter Verwendung des Blattnamens**

 Manchmal müssen Entwickler möglicherweise Arbeitsblätter aus vorhandenen Excel-Dateien entfernen, und diese Aufgabe kann durch Aufrufen von ausgeführt werden[**entfernenBei**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) Methode der[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Sammlung. Wir können den Blattnamen an die übergeben[**entfernenBei**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String))-Methode zum Entfernen eines bestimmten Arbeitsblatts.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Arbeitsblätter mit Blattindex entfernen**

Der obige Ansatz zum Entfernen von Arbeitsblättern funktioniert gut, wenn Entwickler bereits die Blattnamen der zu löschenden Arbeitsblätter kennen. Was aber, wenn Sie den Blattnamen des Arbeitsblatts, das Sie aus Ihrer Excel-Datei entfernen möchten, nicht kennen?

 Nun, unter solchen Umständen können Entwickler eine überladene Version von verwenden[**entfernenBei**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int))-Methode, die den Blattindex des Arbeitsblatts anstelle seines Blattnamens verwendet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Themen vorantreiben**
- [Blätter aktivieren und Cell im Arbeitsblatt aktivieren](/cells/de/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Kopieren und verschieben Sie Arbeitsblätter innerhalb und zwischen Arbeitsmappen](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Kopieren und Verschieben von Arbeitsblättern](/cells/de/java/copying-and-moving-worksheets/)
- [Zählen Sie die Anzahl der Zellen im Arbeitsblatt](/cells/de/java/count-number-of-cells-in-the-worksheet/)
- [Leere Arbeitsblätter erkennen](/cells/de/java/detecting-empty-worksheets/)
- [Finden Sie heraus, ob das Arbeitsblatt ein Dialogblatt ist](/cells/de/java/find-if-the-worksheet-is-dialog-sheet/)
- [Holen Sie sich die eindeutige ID des Arbeitsblatts](/cells/de/java/get-worksheet-unique-id/)
- [Hintergrundbild in Excel einfügen](/cells/de/java/insert-background-image-to-excel/)
- [Erstellen, bearbeiten oder entfernen Sie Szenarien aus Arbeitsblättern](/cells/de/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Seitenumbrüche verwalten](/cells/de/java/managing-page-breaks/)
- [Seiteneinrichtungsfunktionen](/cells/de/java/page-setup-features/)
- [Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen](/cells/de/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Verwenden Sie die Sheet.SheetId-Eigenschaft von OpenXml mit Aspose.Cells](/cells/de/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Arbeiten mit dem Hintergrund in ODS-Dateien](/cells/de/java/working-with-background-in-ods-files/)
- [Arbeitsblattansichten](/cells/de/java/worksheet-views/)
