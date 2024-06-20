---
title: Bereiche verwalten
linktitle: Bereiche
type: docs
weight: 75
url: /de/java/managing-ranges/
---

## **Einführung**

In Excel kann man mit einer Mausauswahlbox mehrere Zellen auswählen, die Auswahl der Zellen wird als "Bereich" bezeichnet.

Sie können beispielsweise in Zelle "A1" von Excel mit der linken Maustaste klicken und dann zu Zelle "C4" ziehen. Der ausgewählte rechteckige Bereich kann auch leicht als Objekt erstellt werden, indem Sie Aspose.Cells verwenden.

So erstellen Sie einen Bereich, fügen Werte ein, setzen Stil und führen weitere Operationen am "Bereich"-Objekt durch.

## **Bereiche verwalten mit Aspose.Cells**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung.

### **Bereich erstellen**

Wenn Sie einen rechteckigen Bereich erstellen möchten, der über A1:C4 reicht, können Sie den folgenden Code verwenden:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Wert in die Zellen des Bereichs eingeben**

Angenommen, Sie haben einen Zellenbereich, der sich über A1:C4 erstreckt. Die Matrix umfasst 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequenziell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0], Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Das folgende Beispiel zeigt, wie man einige Werte in die Zellen des Bereichs eingibt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Stellen Sie den Stil der Zellen des Bereichs ein**

Das folgende Beispiel zeigt, wie man den Stil der Zellen des Bereichs festlegt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

### **Aktuelles Gebiet des Bereichs erhalten**

CurrentRegion ist eine Eigenschaft, die ein Range-Objekt zurückgibt, das die aktuelle Region darstellt. 

Die aktuelle Region ist ein Bereich, der durch eine beliebige Kombination von leeren Zeilen und leeren Spalten begrenzt ist. Schreibgeschützt.

In Excel können Sie den Bereich "CurrentRegion" wie folgt erhalten:
1. Wählen Sie einen Bereich (Range1) mit dem Mausfeld aus.
2. Klicken Sie auf "Start - Bearbeiten - Suchen & Auswählen - Gehe zu - Besonderes - Aktuelle Region", oder verwenden Sie "Strg+Umschalt+*", dann sehen Sie, dass Excel automatisch einen Bereich (Range2) auswählt. Jetzt haben Sie es geschafft, Range2 ist die CurrentRegion von Range1.

Mit Aspose.Cells können Sie die Eigenschaft "Range.CurrentRegion" verwenden, um dieselbe Funktion auszuführen.

Bitte laden Sie die folgende Testdatei herunter, öffnen Sie sie in Excel, wählen Sie einen Bereich "A1:D7" mit dem Mausfeld aus, klicken Sie dann "Strg+Umschalt+*", dann sehen Sie, dass der Bereich "A1:C3" ausgewählt ist.

[current_region.xlsx](current_region.xlsx)

Führen Sie jetzt bitte das folgende Beispiel aus, sehen Sie, wie es in Aspose.Cells funktioniert:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Erweiterte Themen**
- [Autofüllbereich der Excel-Datei](/cells/de/java/autofill-ranges/)
- [Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen](/cells/de/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Bereiche von Excel kopieren](/cells/de/java/copy-ranges-of-Excel/)
- [Nur Datenbereich kopieren](/cells/de/java/copy-range-data-only/)
- [Datenbereich mit Stil kopieren](/cells/de/java/copy-range-data-with-style/)
- [Nur Bereichsstil kopieren](/cells/de/java/copy-range-style-only/)
- [Zeilenhöhen des Quellbereichs in den Zielbereich kopieren](/cells/de/java/copy-row-heights-of-source-range-to-destination-range/)
- [Union Range erstellen](/cells/de/java/create-union-range/)
- [Ausschneiden und Einfügen von Bereichen](/cells/de/java/cut-and-paste-cells/)
- [Bereiche löschen](/cells/de/java/delete-ranges-from-Excel/)
- [Erkennen von zusammengeführten Zellen in einem Arbeitsblatt](/cells/de/java/detect-merged-cells-in-a-worksheet/)
- [Adresse, Zellenanzahl, Versatz, Gesamte Spalte und Gesamte Zeile des Bereichs abrufen](/cells/de/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Bereich mit externen Links abrufen](/cells/de/java/get-range-with-external-links/)
- [Implementierung nicht aufeinanderfolgender Bereiche](/cells/de/java/implementing-non-sequential-ranges/)
- [Bereiche einfügen](/cells/de/java/insert-ranges-to-Excel/)
- [Zellbereich zusammenführen oder trennen](/cells/de/java/merge-or-unmerge-range-of-cells/)
- [Bereich von Zellen in einem Arbeitsblatt verschieben](/cells/de/java/move-range-of-cells-in-a-worksheet/)
- [Benannte Bereiche](/cells/de/java/named-ranges/)
- [Suchen und Ersetzen von Daten in einem Bereich](/cells/de/java/search-and-replace-data-in-a-range/)

