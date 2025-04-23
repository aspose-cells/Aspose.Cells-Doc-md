---
title: Aktivieren von Blättern und Aktivieren einer Zelle im Arbeitsblatt
type: docs
weight: 5
url: /de/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

Manchmal müssen Sie ein bestimmtes Arbeitsblatt aktivieren und anzeigen, wenn ein Benutzer eine Microsoft Excel-Datei in Excel öffnet. Ebenso möchten Sie möglicherweise eine bestimmte Zelle aktivieren und die Bildlaufleisten so einstellen, dass die aktive Zelle angezeigt wird. Aspose.Cells ist dazu in der Lage, wie unten demonstriert wird.

- Ein **aktives Blatt** ist ein Blatt, an dem gearbeitet wird: Der Name des aktiven Blatts auf der Registerkarte ist standardmäßig fettgedruckt.
- Eine **aktive Zelle** ist eine ausgewählte Zelle, in die Daten eingegeben werden, wenn Sie mit dem Tippen beginnen. Es ist immer nur eine Zelle aktiv. Die aktive Zelle ist durch einen kräftigen Rahmen hervorgehoben.

{{% /alert %}}

## **Aktivieren von Blättern und Aktivieren einer Zelle**

Aspose.Cells bietet spezifische API-Aufrufe zum Aktivieren eines Arbeitsblatts und einer Zelle. Zum Beispiel ist die Eigenschaft [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) nützlich, um das aktive Arbeitsblatt in einer Arbeitsmappe festzulegen. Ebenso kann die Eigenschaft [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) verwendet werden, um eine aktive Zelle im Arbeitsblatt zu setzen und abzurufen.

Um sicherzustellen, dass die horizontalen oder vertikalen Bildlaufleisten an der gewünschten Zeilen- und Spaltenindexposition angezeigt werden, verwenden Sie die Eigenschaften [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) und [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn).

Das folgende Beispiel zeigt, wie ein Arbeitsblatt aktiviert und eine aktive Zelle darin erstellt wird. Der folgende Output wird beim Ausführen des Codes generiert. Die Bildlaufleisten werden verschoben, um die 2. Zeile und die 2. Spalte als erste sichtbare Zeile und Spalte anzuzeigen.

**Die Zelle B2 als aktive Zelle setzen**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java-Code zum Festlegen eines aktiven Arbeitsblatts in Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

Im **Evaluierungs**-Modus, das heißt, ohne eine gültige Lizenz festzulegen, ist das aktive Arbeitsblatt immer dasjenige mit dem Evaluierungswasserzeichen. Dieses Verhalten kann nur durch Festlegen der Lizenz zu Beginn der Anwendung außer Kraft gesetzt werden.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
