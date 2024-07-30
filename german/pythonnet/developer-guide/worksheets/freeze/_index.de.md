---
title: Einfrieren von Fenstern des Excel Arbeitsblatts
linktitle: Fenster einfrieren
type: docs
weight: 190
url: /de/python-net/how-to-freeze-panes-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie Sie programmgesteuert die Fensterbereiche von Excel Arbeitsblättern mit den Aspose.Cells für Python via .NET APIs fixieren.
keywords: Python Excel Bibliothek, Python Fixpaneeinstellungen, Fenster in Python fixieren.
---

## **Einführung**

In diesem Artikel lernen wir, wie man Fenster fixiert. Wenn Sie eine große Menge von Daten unter einem gemeinsamen Header haben und den Header beim Scrollen des Arbeitsblatts nicht sehen können. Und jeder Datensatz enthält viele Daten. Sie können Fenster fixieren, damit Sie diesen eingefrorenen Anteil auch sehen können, wenn der Rest der Daten gescrollt wird. Sie können Header in den oberen Zeilen oder in den ersten Spalten leicht sehen. Das Fixieren und Lösen von Fenstern ändert nur die Ansicht der Daten, ohne die Daten selbst zu ändern.

## ***Wie man Panee in Excel festhält**

**![Fenster einfrieren in Excel](Freeze-panes.png)**


1. Wenn Sie Fenster fixieren, Zeilen und Spalten fixieren möchten, wählen Sie zuerst eine Zelle (z. B. B2) aus.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Im Dropdown-Menü klicken Sie auf Fenster einfrieren.
4. Wenn Sie nach unten oder rechts scrollen, sind die erste Zeile und Spalte eingefroren.

**![Gefrorene Fenster](Frozen-Panes.png)**

Wie Sie sehen können, sind die erste Zeile und Spalte A eingefroren, die zweite Zeile ist 32 und die zweite sichtbare Spalte ist D. 

Fenster fixieren ermöglicht es Ihnen, Ihre große Datenmenge ohne zusätzliches Nachverfolgen von Zeilen- oder Spaltenbezeichnungen zu sehen.




## **Wie man Panee mit der Aspose.Cells für die Python Excel-Bibliothek fixiert**
Mit Aspose.Cells für Python via .NET ist es einfach, Panee zu fixieren. Bitte verwenden Sie die [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)-Methode, um die Panee an der ausgewählten Zelle zu fixieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Einfrieren von Fenstern mit der Worksheet.FreezePanes() Methode.
3. Die Datei speichern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
