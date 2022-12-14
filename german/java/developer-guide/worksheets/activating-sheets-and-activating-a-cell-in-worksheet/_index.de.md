---
title: Blätter aktivieren und Cell im Arbeitsblatt aktivieren
type: docs
weight: 5
url: /de/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

Manchmal muss ein bestimmtes Arbeitsblatt aktiv sein und angezeigt werden, wenn ein Benutzer eine Microsoft-Excel-Datei in Excel öffnet. Ebenso möchten Sie vielleicht eine bestimmte Zelle aktivieren und die Bildlaufleisten so einstellen, dass sie die aktive Zelle anzeigen. Aspose.Cells ist in der Lage, all diese Aufgaben zu erledigen, wie unten gezeigt.

-  Ein**aktives Blatt** ist ein Blatt, an dem Sie gerade arbeiten: Der Name des aktiven Blatts auf der Registerkarte ist standardmäßig fett.
-  Ein**aktive Zelle** ist eine ausgewählte Zelle, die Zelle, in die Daten eingegeben werden, wenn Sie mit der Eingabe beginnen. Es ist immer nur eine Zelle aktiv. Die aktive Zelle wird durch einen dicken Rahmen hervorgehoben.

{{% /alert %}}

## **Aktivieren von Blättern und Aktivieren einer Cell**

Aspose.Cells bietet spezifische API-Aufrufe zum Aktivieren eines Blatts und einer Zelle. Zum Beispiel die[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)-Eigenschaft ist nützlich, um das aktive Blatt in einer Arbeitsmappe festzulegen. Ebenso die[**Arbeitsblatt.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)-Eigenschaft kann verwendet werden, um eine aktive Zelle im Arbeitsblatt festzulegen und abzurufen.

Um sicherzustellen, dass sich die horizontalen oder vertikalen Bildlaufleisten an der Zeilen- und Spaltenindexposition befinden, an der Sie bestimmte Daten anzeigen möchten, verwenden Sie die[**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)und[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)Eigenschaften.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt aktivieren und eine aktive Zelle darin erstellen. Beim Ausführen des Codes wird die folgende Ausgabe generiert. Die Bildlaufleisten werden gescrollt, um die 2. Zeile und 2. Spalte als ihre erste sichtbare Zeile und Spalte zu machen.

**Festlegen der B2-Zelle als aktive Zelle**

![todo: Bild_alt_Text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java-Code zum Festlegen eines aktiven Arbeitsblatts in Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 Im**Auswertung** Modus, das heißt; Ohne das Festlegen einer gültigen Lizenz ist das aktive Arbeitsblatt immer dasjenige, das das Evaluierungswasserzeichen enthält. Dieses Verhalten kann nur durch das Setzen der Lizenz beim Start der Anwendung außer Kraft gesetzt werden.

{{% /alert %}}
