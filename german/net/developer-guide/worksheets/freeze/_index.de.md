---
title: Einfrieren von Fenstern des Excel Arbeitsblatts
linktitle: Fenster einfrieren
type: docs
weight: 190
url: /de/net/how-to-freeze-panes-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie Fenster von Excel Arbeitsblättern programmgesteuert mit der C# Bibliothek und der .NET API einfrieren können.
keywords: Fenster einfrieren, Fenster fixieren.
---

## **Einführung**

In diesem Artikel lernen wir, wie man Fenster fixiert. Wenn Sie eine große Menge von Daten unter einem gemeinsamen Header haben und den Header beim Scrollen des Arbeitsblatts nicht sehen können. Und jeder Datensatz enthält viele Daten. Sie können Fenster fixieren, damit Sie diesen eingefrorenen Anteil auch sehen können, wenn der Rest der Daten gescrollt wird. Sie können Header in den oberen Zeilen oder in den ersten Spalten leicht sehen. Das Fixieren und Lösen von Fenstern ändert nur die Ansicht der Daten, ohne die Daten selbst zu ändern.

## **In Excel**

**![Fenster einfrieren in Excel](Freeze-panes.png)**


1. Wenn Sie Fenster fixieren, Zeilen und Spalten fixieren möchten, wählen Sie zuerst eine Zelle (z. B. B2) aus.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Im Dropdown-Menü klicken Sie auf Fenster einfrieren.
4. Wenn Sie nach unten oder rechts scrollen, sind die erste Zeile und Spalte eingefroren.

**![Gefrorene Fenster](Frozen-Panes.png)**

Wie Sie sehen können, sind die erste Zeile und Spalte A eingefroren, die zweite Zeile ist 32 und die zweite sichtbare Spalte ist D. 

Fenster fixieren ermöglicht es Ihnen, Ihre große Datenmenge ohne zusätzliches Nachverfolgen von Zeilen- oder Spaltenbezeichnungen zu sehen.




## **Fenster fixieren mit Aspose.Cells für .Net**
Es ist einfach, Fenster mit Aspose.Cells für .Net einzufrieren. Bitte verwenden Sie die [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)-Methode, um Fenster an der ausgewählten Zelle zu fixieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Einfrieren von Fenstern mit der Worksheet.FreezePanes() Methode.
3. Die Datei speichern.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
