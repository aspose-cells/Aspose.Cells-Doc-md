---
title: Fixieren der ersten Spalte(n) des Excel Arbeitsblatts
linktitle: Spalten fixieren
type: docs
weight: 190
url: /de/net/how-to-freeze-columns-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie mithilfe der C# Bibliothek und der .NET API linke Spalten von Excel Arbeitsblättern programmgesteuert einfrieren können.
keywords: Linke Spalten einfrieren, Erste Spalten einfrieren, Die Spalte(n) sperren
---

## **Einführung**

In diesem Artikel erfahren Sie, wie man die linken Spalten fixiert. Wenn Sie eine große Menge an Daten in einer Zeile haben, so dass Sie die linken Spalten beim horizontalen Scrollen des Arbeitsblatts nicht sehen können, können Sie die ersten Spalten fixieren und sperren, damit Sie diesen fixierten Bereich auch sehen können, wenn der Rest der Daten gescrollt wird. Sie können so die Überschriften in den linken Spalten leicht sehen.


## **Spalten in Excel einfrieren**

**![Linke Spalte(n) in Excel einfrieren](freeze-columns.png)**


1. Wenn Sie linke Spalte(n) einfrieren möchten, wählen Sie zuerst die Spalte unter der Spalte aus, die eingefroren werden soll.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicken Sie im Dropdown-Menü auf Spalte fixieren.
4. Wenn Sie nach unten scrollen, ist die erste Spalte immer in der linken Ansicht.

**![Eingefrorene Spalte](frozen-columns.png)**

Wie Sie sehen können, ist die erste Spalte eingefroren und immer oben im Blick, wenn Sie horizontal scrollen.

Eingefrorene Spalten ermöglichen es Ihnen, Ihre langen Daten anzuzeigen, ohne die erste Spalte im Auge behalten zu müssen.




## **Eingefrorene Spalten mit Aspose.Cells für .Net**
Es ist einfach, die ersten Spalten mit Aspose.Cells für .Net einzufrieren. 
Bitte verwenden Sie die [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)-Methode, um Spalte(n) an der ausgewählten Spalte einzufrieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Freezen Sie die erste Spalte mit der Methode Worksheet.FreezePanes().
3. Die Datei speichern.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
{{< app/cells/assistant language="csharp" >}}
