---
title: Obere Zeile(n) des Excel Arbeitsblatts einfrieren
linktitle: Zeilen einfrieren
type: docs
weight: 190
url: /de/python-net/how-to-freeze-rows-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie oberste Zeilen von Excel Tabellenblättern programmgesteuert einfrieren können, indem Sie Aspose.Cells für Python via .NET APIs verwenden.
keywords: Python Excel Bibliothek, Python Oberste Zeilen einfrieren, Python oberste Zeile einfrieren.
---

## **Einführung**

In diesem Artikel erfahren Sie, wie man die oberen Zeilen fixiert. Wenn Sie eine große Menge an Daten unter einer gemeinsamen Überschrift haben und beim Scrollen des Arbeitsblatts die Überschrift nicht sehen können, können Sie die oberen Zeilen fixieren, damit Sie diesen fixierten Bereich auch bei Scrollen der restlichen Daten sehen können. Sie können so die Überschriften in den oberen Zeilen leicht sehen.

## **Wie man Zeilen in Excel einfriert**

**![Oberste Zeile(n) in Excel einfrieren](Freeze-Rows.png)**


1. Wenn Sie die oberste Zeile(n) einfrieren möchten, wählen Sie zuerst die Zeile unter der Zeile aus, die eingefroren werden soll.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Wählen Sie im Dropdown-Menü "Oberste Zeile einfrieren" aus.
4. Wenn Sie nach unten scrollen, ist die erste Zeile immer im oberen Bereich zu sehen.

**![Feste Zeile](Frozen-Row.png)**

Wie Sie sehen können, ist die 1. Zeile eingefroren, die erste Zeile bleibt immer oben im Blick, wenn Sie nach unten scrollen.

Eingefrorene Zeilen ermöglichen es Ihnen, Ihre großen Daten ohne Überblick über die Zeilenbezeichnung anzuzeigen.




## **Wie man Zeilen mit Aspose.Cells für Python Excel-Bibliothek einfriert**
Es ist einfach, Zeile(n) mit Aspose.Cells für Python via .NET einzufrieren. Verwenden Sie bitte die [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)-Methode, um die Zeile(n) an der ausgewählten Zeile zu fixieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Friere die erste Zeile mit der Methode Worksheet.FreezePanes() ein.
3. Die Datei speichern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Row.py" >}}

Angehängte [Beispielquelle für Excel-Datei](../Freeze.xlsx).
