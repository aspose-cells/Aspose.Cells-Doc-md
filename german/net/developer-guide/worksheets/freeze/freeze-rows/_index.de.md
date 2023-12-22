---
title: Obere Zeile(n) des Excel-Arbeitsblatts einfrieren
linktitle: Zeilen einfrieren
type: docs
weight: 190
url: /de/net/how-to-freeze-rows-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie die oberen Zeilen von Excel-Arbeitsblättern programmgesteuert mithilfe der Bibliothek C# mit .NET API einfrieren.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

In diesem Artikel erfahren Sie, wie Sie die oberste(n) Zeile(n) einfrieren.
Wenn Sie eine große Datenmenge unter einer gemeinsamen Überschrift haben, können Sie die Überschrift nicht sehen, wenn Sie im Arbeitsblatt nach unten scrollen. Sie können die oberste(n) Zeile(n) einfrieren, sodass Sie diesen eingefrorenen Teil auch dann sehen können, wenn durch die restlichen Daten gescrollt wird. In den oberen Zeilen sind die Überschriften leicht zu erkennen.

{{% /alert %}}

##  **Zeilen in Excel einfrieren**

**![Oberste Zeile(n) in Excel einfrieren](Freeze-Rows.png)**


1. Wenn Sie die oberste(n) Zeile(n) einfrieren möchten, wählen Sie zunächst die Zeile unter der Zeile aus, die eingefroren werden soll
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicken Sie im Dropdown-Menü auf „Obere Zeile fixieren“.
4. Wenn Sie nach unten scrollen, befindet sich die erste Zeile immer in der Draufsicht.

**![Fonzen-Reihe](Frozen-Row.png)**

Wie Sie sehen, ist die erste Zeile eingefroren. Die erste Zeile bleibt immer oben in der Ansicht, wenn Sie nach unten scrollen.

Mit „Zeilen einfrieren“ können Sie Ihre großen Datenmengen anzeigen, ohne die Zeilenbezeichnung im Auge zu behalten.




##  **Zeilen mit Aspose.Cells für .Net einfrieren**
 Es ist einfach, Zeilen mit Aspose.Cells für .Net einzufrieren.
 Bitte nutzen Sie die[**Arbeitsblatt.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)Methode zum Fixieren von Zeilen in der ausgewählten Zeile.
1. Arbeitsmappe erstellen, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Frieren Sie die erste Zeile mit der Methode Worksheet.FreezePanes() ein.
3. Speichern Sie die Datei.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

 Beigefügt[Beispiel einer Excel-Quelldatei](../Freeze.xlsx).
