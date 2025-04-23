---
title: Fixieren der ersten Spalte(n) des Excel Arbeitsblatts
linktitle: Spalten fixieren
type: docs
weight: 190
url: /de/python-net/how-to-freeze-columns-of-excel-worksheet
description: In diesem Artikel lernst du, wie man die linken Spalten von Excel Arbeitsblättern programmgesteuert mit Aspose.Cells für Python via .NET fixiert.
keywords: Python Excel Bibliothek, Python Spalten fixieren, Python erste Spalten fixieren, Python Spalten sperren.
---

## **Einführung**

In diesem Artikel erfahren Sie, wie man die linken Spalten fixiert. Wenn Sie eine große Menge an Daten in einer Zeile haben, so dass Sie die linken Spalten beim horizontalen Scrollen des Arbeitsblatts nicht sehen können, können Sie die ersten Spalten fixieren und sperren, damit Sie diesen fixierten Bereich auch sehen können, wenn der Rest der Daten gescrollt wird. Sie können so die Überschriften in den linken Spalten leicht sehen.


## **Wie man Spalten in Excel fixiert**

**![Linke Spalte(n) in Excel einfrieren](freeze-columns.png)**


1. Wenn Sie linke Spalte(n) einfrieren möchten, wählen Sie zuerst die Spalte unter der Spalte aus, die eingefroren werden soll.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicken Sie im Dropdown-Menü auf Spalte fixieren.
4. Wenn Sie nach unten scrollen, ist die erste Spalte immer in der linken Ansicht.

**![Eingefrorene Spalte](frozen-columns.png)**

Wie Sie sehen können, ist die erste Spalte eingefroren und immer oben im Blick, wenn Sie horizontal scrollen.

Eingefrorene Spalten ermöglichen es Ihnen, Ihre langen Daten anzuzeigen, ohne die erste Spalte im Auge behalten zu müssen.




## **So fixierst du Spalten mit der Python Excel-Bibliothek Aspose.Cells für Python**
Es ist einfach, die erste(n) Spalte(n) mit Aspose.Cells für Python via .NET zu fixieren. Verwende die [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)-Methode, um Spalte(n) an der gewünschten Stelle zu fixieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Freezen Sie die erste Spalte mit der Methode Worksheet.FreezePanes().
3. Die Datei speichern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
