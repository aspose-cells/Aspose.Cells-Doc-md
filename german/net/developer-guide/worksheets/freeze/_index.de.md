---
title: Bereiche des Excel-Arbeitsblatts einfrieren
linktitle: Scheiben einfrieren
type: docs
weight: 190
url: /de/net/how-to-freeze-panes-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie Bereiche von Excel-Arbeitsblättern programmgesteuert mithilfe der Bibliothek C# mit .NET API einfrieren.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

In diesem Artikel erfahren Sie, wie Sie Fenster einfrieren.
Wenn Sie eine große Datenmenge unter einer gemeinsamen Überschrift haben, können Sie die Überschrift nicht sehen, wenn Sie im Arbeitsblatt nach unten scrollen. Und jeder Datensatz enthält viele Daten. Sie können Bereiche einfrieren, sodass Sie diesen eingefrorenen Teil auch dann sehen können, wenn der Rest der Daten gescrollt wird. Sie können die Überschriften in den oberen Zeilen oder ersten Spalten leicht erkennen. Durch das Einfrieren und Aufheben der Fixierung von Fenstern ändert sich nur die Ansicht der Daten, ohne dass sich die Daten selbst ändern.

{{% /alert %}}

##  **In Excel**

**![Fenster in Excel einfrieren](Freeze-panes.png)**


1. Wenn Sie Fensterbereiche, Zeilen und Spalten einfrieren möchten, wählen Sie zunächst eine Zelle aus (z. B. B2).
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicken Sie im Dropdown-Menü auf Fenster einfrieren.
4. Wenn Sie nach unten oder rechts scrollen, werden die erste Zeile und Spalte eingefroren.

**![Fonzen panes](Frozen-Panes.png)**

 Wie Sie sehen können, sind die erste Zeile und Spalte A eingefroren, die zweite Zeile ist 32 und die zweite sichtbare Spalte ist D.

Mit eingefrorenen Fenstern können Sie Ihre großen Datenmengen anzeigen, ohne die Zeilen- oder Spaltenbezeichnung im Auge behalten zu müssen.




##  **Fenster mit Aspose.Cells für .Net einfrieren**
 Es ist einfach, Fenster mit Aspose.Cells für .Net einzufrieren. Bitte nutzen Sie die[**Arbeitsblatt.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)Methode zum Einfrieren von Fenstern am ausgewählten Cell.
1. Arbeitsmappe erstellen, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Fenster mit der Methode Worksheet.FreezePanes() einfrieren.
3. Speichern Sie die Datei.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Beigefügt[Beispiel einer Excel-Quelldatei](Freeze.xlsx).
