---
title: Bereiche verwalten
linktitle: Bereiche
type: docs
weight: 105
url: /de/net/managing-ranges/
---

## **Einführung**

In Excel kann man mit einer Mausauswahlbox mehrere Zellen auswählen, die Auswahl der Zellen wird als "Bereich" bezeichnet.

Sie können beispielsweise in Zelle "A1" von Excel mit der linken Maustaste klicken und dann zu Zelle "C4" ziehen. Der ausgewählte rechteckige Bereich kann auch leicht als Objekt erstellt werden, indem Sie Aspose.Cells verwenden.

So erstellen Sie einen Bereich, fügen Werte ein, setzen Stil und führen weitere Operationen am "Bereich"-Objekt durch.

## **Bereiche verwalten mit Aspose.Cells**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung.

### **Bereich erstellen**

Wenn Sie einen rechteckigen Bereich erstellen möchten, der über A1:C4 reicht, können Sie den folgenden Code verwenden:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Wert in die Zellen des Bereichs eingeben**

Angenommen, Sie haben einen Zellenbereich, der sich über A1:C4 erstreckt. Die Matrix umfasst 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequenziell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0], Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Das folgende Beispiel zeigt, wie man einige Werte in die Zellen des Bereichs eingibt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Stellen Sie den Stil der Zellen des Bereichs ein**

Das folgende Beispiel zeigt, wie man den Stil der Zellen des Bereichs festlegt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Erweiterte Themen**
- [Autofüllbereich der Excel-Datei](/cells/de/net/autofill-ranges/)
- [Bereiche von Excel kopieren](/cells/de/net/copy-ranges-of-Excel/)
- [Nur Datenbereich kopieren](/cells/de/net/copy-range-data-only/)
- [Datenbereich mit Stil kopieren](/cells/de/net/copy-range-data-with-style/)
- [Nur Bereichsstil kopieren](/cells/de/net/copy-range-style-only/)
- [Union Range erstellen](/cells/de/net/create-union-range/)
- [Bereich ausschneiden und einfügen](/cells/de/net/cut-and-paste-cells/)
- [Bereiche löschen](/cells/de/net/delete-ranges-from-Excel/)
- [Adresse, Zellenanzahl, Versatz, Gesamte Spalte und Gesamte Zeile des Bereichs abrufen](/cells/de/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Bereiche einfügen](/cells/de/net/insert-ranges-to-Excel/)
- [Zellbereich zusammenführen oder trennen](/cells/de/net/merge-or-unmerge-range-of-cells/)
- [Bereich von Zellen in einem Arbeitsblatt verschieben](/cells/de/net/move-range-of-cells-in-a-worksheet/)
- [Arbeitsbuch- und arbeitsblattübergreifende benannte Bereiche erstellen](/cells/de/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Suchen und Ersetzen von Daten in einem Bereich](/cells/de/net/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="csharp" >}}
