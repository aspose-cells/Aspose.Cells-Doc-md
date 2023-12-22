---
title: Erste Spalte(n) des Excel-Arbeitsblatts einfrieren
linktitle: Spalten einfrieren
type: docs
weight: 190
url: /de/net/how-to-freeze-columns-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie linke Spalten von Excel-Arbeitsblättern programmgesteuert mithilfe der Bibliothek C# mit .NET API einfrieren.
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

In diesem Artikel erfahren Sie, wie Sie linke Spalten einfrieren.
Wenn Sie eine große Datenmenge in einer Zeile haben und Sie die linken Spalten nicht sehen können, wenn Sie horizontal im Arbeitsblatt nach unten scrollen. Sie können die erste(n) Spalte(n) einfrieren und sperren, sodass Sie diesen eingefrorenen Teil auch dann sehen können, wenn durch die restlichen Daten gescrollt wird. In den linken Spalten sind die Überschriften leicht zu erkennen.

{{% /alert %}}

##  **Spalten in Excel einfrieren**

**![Linke Spalte(n) in Excel einfrieren](freeze-columns.png)**


1. Wenn Sie die linke(n) Spalte(n) einfrieren möchten, wählen Sie zunächst die Spalte unter der Spalte aus, die eingefroren werden soll
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicken Sie im Dropdown-Menü auf Erste Spalte einfrieren.
4. Wenn Sie nach unten scrollen, befindet sich die erste Spalte immer in der linken Ansicht.

**![Fonzen-Spalte](frozen-columns.png)**

Wie Sie sehen, ist die erste Spalte eingefroren. Die erste Spalte bleibt beim horizontalen Scrollen immer oben in der Ansicht gesperrt.

Mit „Spalten einfrieren“ können Sie Ihre langen Daten anzeigen, ohne die erste Spalte im Auge behalten zu müssen.




##  **Spalten mit Aspose.Cells für .Net einfrieren**
Es ist einfach, die erste(n) Spalte(n) mit Aspose.Cells für .Net einzufrieren.
 Bitte nutzen Sie die[**Arbeitsblatt.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)Methode zum Fixieren der Spalte(n) an der ausgewählten Spalte.
1. Arbeitsmappe erstellen, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Frieren Sie die erste Spalte mit der Methode Worksheet.FreezePanes() ein.
3. Speichern Sie die Datei.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

 Beigefügt[Beispiel einer Excel-Quelldatei](Freeze.xlsx).
