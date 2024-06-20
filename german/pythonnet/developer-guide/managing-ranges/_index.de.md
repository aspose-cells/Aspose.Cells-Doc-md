---
title: Bereiche verwalten
linktitle: Bereiche
type: docs
weight: 105
url: /de/python-net/managing-ranges/
description: Dieser Artikel zeigt, wie man Bereiche durch die Aspose.Cells für Python via .NET API verwaltet.
keywords: Python Excel Bibliothek, Python Bereiche verwalten, Bereich in Python erstellen, Wert in die Zellen des Bereichs in Python einfügen, Stil der Zellen des Bereichs in Python festlegen, Aktuellen Bereich des Bereichs in Python abrufen.
---

## **Einführung**

In Excel kann man mit einer Mausauswahlbox mehrere Zellen auswählen, die Auswahl der Zellen wird als "Bereich" bezeichnet.

Zum Beispiel können Sie in Excel mit der linken Maustaste auf Zelle "A1" klicken und dann bis zur Zelle "C4" ziehen. Der rechteckige Bereich, den Sie ausgewählt haben, kann auch einfach als Objekt unter Verwendung von Aspose.Cells für Python via .NET erstellt werden.

So erstellen Sie einen Bereich, fügen Werte ein, setzen Stil und führen weitere Operationen am "Bereich"-Objekt durch.

## **Bereiche verwalten mit Aspose.Cells für Python Excel-Bibliothek**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) stellt eine [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung bereit.

## **Wie man einen Bereich erstellt**

Wenn Sie einen rechteckigen Bereich erstellen möchten, der über A1:C4 reicht, können Sie den folgenden Code verwenden:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **Wie man Wert in die Zellen des Bereichs einfügt**

Angenommen, Sie haben einen Zellenbereich, der über A1:C4 reicht. Die Matrix umfasst 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequentiell angeordnet.

Das folgende Beispiel zeigt, wie man einige Werte in die Zellen des Bereichs eingibt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **Wie man den Stil der Zellen des Bereichs festlegt**

Das folgende Beispiel zeigt, wie man den Stil der Zellen des Bereichs festlegt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **Wie man den aktuellen Bereich des Bereichs abruft**

CurrentRegion ist eine Eigenschaft, die ein Range-Objekt zurückgibt, das die aktuelle Region darstellt. 

Die aktuelle Region ist ein Bereich, der durch eine beliebige Kombination von leeren Zeilen und leeren Spalten begrenzt ist. Schreibgeschützt.

In Excel können Sie den Bereich "CurrentRegion" wie folgt erhalten:
1. Wählen Sie einen Bereich (Range1) mit dem Mausfeld aus.
2. Klicken Sie auf "Start - Bearbeiten - Suchen & Auswählen - Gehe zu - Besonderes - Aktuelle Region", oder verwenden Sie "Strg+Umschalt+*", dann sehen Sie, dass Excel automatisch einen Bereich (Range2) auswählt. Jetzt haben Sie es geschafft, Range2 ist die CurrentRegion von Range1.

Mit Aspose.Cells für Python via .NET können Sie die Eigenschaft "Range.current_region" verwenden, um dieselbe Funktion auszuführen.

Bitte laden Sie die folgende Testdatei herunter, öffnen Sie sie in Excel, wählen Sie einen Bereich "A1:D7" mit dem Mausfeld aus, klicken Sie dann "Strg+Umschalt+*", dann sehen Sie, dass der Bereich "A1:C3" ausgewählt ist.

[current_region.xlsx](current_region.xlsx)

Bitte führen Sie nun das folgende Beispiel aus und sehen Sie, wie es in Aspose.Cells für Python via .NET funktioniert:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Erweiterte Themen**
- [Autofüllbereich der Excel-Datei](/cells/de/python-net/autofill-ranges/)
- [Bereiche von Excel kopieren](/cells/de/python-net/copy-ranges-of-excel/)
- [Nur Datenbereich kopieren](/cells/de/python-net/copy-range-data-only/)
- [Datenbereich mit Stil kopieren](/cells/de/python-net/copy-range-data-with-style/)
- [Nur Bereichsstil kopieren](/cells/de/python-net/copy-range-style-only/)
- [Union Range erstellen](/cells/de/python-net/create-union-range/)
- [Bereich ausschneiden und einfügen](/cells/de/python-net/cut-and-paste-cells/)
- [Bereiche löschen](/cells/de/python-net/delete-ranges-from-excel/)
- [Adresse, Zellenanzahl, Versatz, Gesamte Spalte und Gesamte Zeile des Bereichs abrufen](/cells/de/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Bereiche einfügen](/cells/de/python-net/insert-ranges-to-excel/)
- [Zellbereich zusammenführen oder trennen](/cells/de/python-net/merge-or-unmerge-range-of-cells/)
- [Bereich von Zellen in einem Arbeitsblatt verschieben](/cells/de/python-net/move-range-of-cells-in-a-worksheet/)
- [Arbeitsbuch- und arbeitsblattübergreifende benannte Bereiche erstellen](/cells/de/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Suchen und Ersetzen von Daten in einem Bereich](/cells/de/python-net/search-and-replace-data-in-a-range/)

