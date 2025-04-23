---
title: Arbeitsblätter verwalten
linktitle: Arbeitsblätter
type: docs
weight: 60
url: /de/java/manage-worksheets/
---

{{% alert color="primary" %}}

Entwickler können Arbeitsblätter in ihren Excel-Dateien mithilfe der flexiblen API von Aspose.Cells problemlos erstellen und verwalten. In diesem Thema werden einige Ansätze zur Hinzufügung und Entfernung von Arbeitsblättern in Excel-Dateien diskutiert.

{{% /alert %}}

Arbeitsblätter mit Aspose.Cells zu verwalten ist kinderleicht. In diesem Abschnitt wird beschrieben, wie wir:

1. eine neue Excel-Datei von Grund auf erstellen und ein Arbeitsblatt hinzufügen
1. Arbeitsblätter zu Designer-Arbeitsmappen hinzufügen
1. Arbeitsblätter anhand des Blattnamens abrufen
1. Ein Arbeitsblatt aus einer Excel-Datei mithilfe des Blattnamens entfernen
1. Ein Arbeitsblatt aus einer Excel-Datei mithilfe des Blattindex entfernen

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse enthält einen [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), der den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Schauen wir uns an, wie wir diese Grundmenge an APIs nutzen können.

## **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**

Um eine neue Excel-Datei programmgesteuert zu erstellen, müssen Entwickler ein Objekt der [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse erstellen, das eine Excel-Datei repräsentiert. Dann können Entwickler die [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--)-Methode der [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) aufrufen. Wenn wir die [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--)-Methode aufrufen, wird automatisch ein leeres Arbeitsblatt zur Excel-Datei hinzugefügt, auf das durch Übergeben des Blattindex des neu hinzugefügten Arbeitsblatts an die [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Bezug genommen werden kann. Nachdem die Arbeitsblattreferenz erhalten ist, können Entwickler an ihren Arbeitsblättern gemäß ihren Anforderungen arbeiten. Nach Abschluss der Arbeit an den Arbeitsblättern können Entwickler ihre neu erstellte Excel-Datei mit neuen Arbeitsblättern durch Aufrufen der [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)-Methode der [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Arbeitsblätter zu einem Designer-Arbeitsblatt hinzufügen**

Der Vorgang des Hinzufügens von Arbeitsblättern zu einer Designer-Arbeitsmappe ist vollständig identisch mit dem oben beschriebenen Ansatz, außer dass die Excel-Datei bereits erstellt ist und wir diese Excel-Datei zuerst öffnen müssen, bevor wir ein Arbeitsblatt hinzufügen können. Eine Designer-Arbeitsmappe kann durch Übergeben des Dateipfads oder Streams beim Initialisieren der [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse geöffnet werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Zugriff auf Arbeitsblätter mithilfe des Blattnamens**

Entwickler können auf beliebiges Arbeitsblatt zugreifen, indem sie dessen Namen oder Index angeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Arbeitsblätter anhand des Blattnamens entfernen**

Manchmal müssen Entwickler Arbeitsblätter aus vorhandenen Excel-Dateien entfernen, und diese Aufgabe kann durch Aufrufen der [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-)-Methode der [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)-Sammlung durchgeführt werden. Wir können den Blattnamen an die [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-)-Methode übergeben, um ein bestimmtes Arbeitsblatt zu entfernen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Arbeitsblätter anhand des Blattindex entfernen**

Der oben genannte Ansatz zum Entfernen von Arbeitsblättern funktioniert gut, wenn Entwickler bereits die Blattnamen der zu löschenden Arbeitsblätter kennen. Aber was ist, wenn Sie den Blattnamen des Arbeitsblatts nicht kennen, das Sie aus Ihrer Excel-Datei entfernen möchten?

Nun, in solchen Fällen können Entwickler eine überladene Version der [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-int-)-Methode verwenden, die anstelle seines Blattnamens den Blattnummernindex des Arbeitsblatts verwendet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Erweiterte Themen**
- [Blätter aktivieren und eine Zelle im Arbeitsblatt aktivieren](/cells/de/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben](/cells/de/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Arbeitsblätter kopieren und verschieben](/cells/de/java/copying-and-moving-worksheets/)
- [Anzahl der Zellen im Arbeitsblatt zählen](/cells/de/java/count-number-of-cells-in-the-worksheet/)
- [Erkennen von leeren Arbeitsblättern](/cells/de/java/detecting-empty-worksheets/)
- [Feststellen, ob das Arbeitsblatt ein Dialogblatt ist](/cells/de/java/find-if-the-worksheet-is-dialog-sheet/)
- [Arbeitsblatt eindeutige ID abrufen](/cells/de/java/get-worksheet-unique-id/)
- [Hintergrundbild in Excel einfügen](/cells/de/java/insert-background-image-to-excel/)
- [Erstellen, Manipulieren oder Entfernen von Szenarien aus Arbeitsblättern](/cells/de/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Seitenumbrüche verwalten](/cells/de/java/managing-page-breaks/)
- [Seiteneinrichtungsfunktionen](/cells/de/java/page-setup-features/)
- [Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen](/cells/de/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Verwenden Sie die *Sheet.SheetId*-Eigenschaft von OpenXml mit Aspose.Cells](/cells/de/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Arbeiten mit Hintergründen in ODS-Dateien](/cells/de/java/working-with-background-in-ods-files/)
- [Arbeitsblattansichten](/cells/de/java/worksheet-views/)
{{< app/cells/assistant language="java" >}}
