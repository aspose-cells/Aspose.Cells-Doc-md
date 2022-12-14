---
title: Bereiche verwalten
linktitle: Bereiche
type: docs
weight: 105
url: /de/net/managing-ranges/
---
## **Einführung**

In Excel können Sie mehrere Zellen mit einer Mausboxauswahl auswählen, die Gruppe ausgewählter Zellen wird "Bereich" genannt.

Beispielsweise können Sie in Cell „A1“ des Excel mit der linken Maustaste klicken und dann in die Zelle „C4“ ziehen. Mit Aspose.Cells lässt sich die von Ihnen ausgewählte rechteckige Fläche auch ganz einfach als Objekt erstellen.

Hier erfahren Sie, wie Sie einen Bereich erstellen, einen Wert eingeben, einen Stil festlegen und weitere Operationen mit dem Objekt "Bereich" ausführen.

## **Verwalten von Bereichen mit Aspose.Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung.

### **Bereich erstellen**

Wenn Sie einen rechteckigen Bereich erstellen möchten, der sich über A1:C4 erstreckt, können Sie den folgenden Code verwenden:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Geben Sie den Wert in die Cells der Range ein**

Angenommen, Sie haben einen Zellbereich, der sich über A1:C4 erstreckt. Die Matrix ergibt 4 * 3 = 12 Zellen. Die einzelnen Range-Zellen sind der Reihe nach angeordnet: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Das folgende Beispiel zeigt, wie einige Werte in die Zellen des Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Set-Stil der Cells der Range**

Das folgende Beispiel zeigt, wie Sie den Stil der Zellen des Bereichs festlegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Holen Sie sich CurrentRegion des Bereichs**

 CurrentRegion ist eine Eigenschaft, die ein Range-Objekt zurückgibt, das die aktuelle Region darstellt.

Der aktuelle Bereich ist ein Bereich, der durch eine beliebige Kombination aus leeren Zeilen und leeren Spalten begrenzt ist. Schreibgeschützt.

In Excel können Sie den CurrentRegion-Bereich erhalten durch:
1. Wählen Sie mit der Mausbox einen Bereich (range1) aus.
2. Klicken Sie auf „Home – Bearbeiten – Suchen & Auswählen – Gehe zu Spezial – Aktuelle Region“ oder verwenden Sie „Strg+Umschalt+*“, Sie werden sehen, dass Excel Ihnen automatisch hilft, einen Bereich (Bereich2) auszuwählen, jetzt haben Sie es geschafft, Bereich2 ist die CurrentRegion von range1.

Mit Aspose.Cells können Sie die Eigenschaft „Range.CurrentRegion“ verwenden, um dieselbe Funktion auszuführen.

Bitte laden Sie die folgende Testdatei herunter, öffnen Sie sie in Excel, wählen Sie mit der Mausbox einen Bereich „A1:D7“ aus, klicken Sie dann auf „Strg+Shift+*“, Sie sehen den ausgewählten Bereich „A1:C3“.

[aktuelle_region.xlsx](current_region.xlsx)

Führen Sie nun bitte das folgende Beispiel aus, sehen Sie, wie es in Aspose.Cells funktioniert:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Themen vorantreiben**
- [AutoFill-Bereich der Excel-Datei](/cells/de/net/autofill-ranges/)
- [Bereiche von Excel kopieren](/cells/de/net/copy-ranges-of-Excel/)
- [Nur Bereichsdaten kopieren](/cells/de/net/copy-range-data-only/)
- [Bereichsdaten mit Stil kopieren](/cells/de/net/copy-range-data-with-style/)
- [Nur Bereichsstil kopieren](/cells/de/net/copy-range-style-only/)
- [Union-Bereich erstellen](/cells/de/net/create-union-range/)
- [Bereich ausschneiden und einfügen](/cells/de/net/cut-and-paste-cells/)
- [Bereiche löschen](/cells/de/net/delete-ranges-from-Excel/)
- [Holen Sie sich Adresse Cell. Zählen Sie den Offset der gesamten Spalte und der gesamten Zeile des Bereichs](/cells/de/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Bereiche einfügen](/cells/de/net/insert-ranges-to-Excel/)
- [Bereich von Cells zusammenführen oder aufheben](/cells/de/net/merge-or-unmerge-range-of-cells/)
- [Verschieben Sie den Bereich von Cells in einem Arbeitsblatt](/cells/de/net/move-range-of-cells-in-a-worksheet/)
- [Erstellen Sie benannte Bereiche für Arbeitsmappen und Arbeitsblätter](/cells/de/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Suchen und Ersetzen von Daten in einem Bereich](/cells/de/net/search-and-replace-data-in-a-range/)
