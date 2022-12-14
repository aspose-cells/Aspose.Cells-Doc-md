---
title: Gleichzeitiges Lesen von Cell-Werten in mehreren Threads
linktitle: Mehrere Threads
type: docs
weight: 1800
url: /de/net/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

Das gleichzeitige Lesen von Zellenwerten in mehreren Threads ist eine häufige Anforderung. Dieser Artikel erklärt, wie Sie Aspose.Cells für diesen Zweck verwenden.

{{% /alert %}}

 Um Zellenwerte in mehr als einem Thread gleichzeitig zu lesen, set[**Arbeitsblatt.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) zu**Stimmt**. Wenn Sie dies nicht tun, erhalten Sie möglicherweise die falschen Zellenwerte.

Der folgende Code:

1. Erstellt eine Arbeitsmappe.
1. Fügt ein Arbeitsblatt hinzu.
1. Füllt das Arbeitsblatt mit Zeichenfolgenwerten.
1. Anschließend werden zwei Threads erstellt, die gleichzeitig Werte aus zufälligen Zellen lesen.
 Wenn die gelesenen Werte korrekt sind, passiert nichts. Wenn die gelesenen Werte falsch sind, wird eine Meldung angezeigt.

Wenn Sie diese Zeile kommentieren:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

dann kommt folgende meldung:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Andernfalls läuft das Programm ohne Meldung, was bedeutet, dass alle aus Zellen gelesenen Werte korrekt sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
