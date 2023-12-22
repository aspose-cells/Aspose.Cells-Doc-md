---
title: Cell-Werte in mehreren Threads gleichzeitig lesen
linktitle: Mehrere Threads
type: docs
weight: 1800
url: /de/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Erfahren Sie, wie Sie Cell-Werte in mehreren Threads gleichzeitig über Aspose.Cells for .NET API lesen.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

Das gleichzeitige Lesen von Zellwerten in mehreren Threads ist eine häufige Anforderung. In diesem Artikel wird erläutert, wie Sie Aspose.Cells für diesen Zweck verwenden.

{{% /alert %}}

 Um Zellwerte in mehr als einem Thread gleichzeitig zu lesen, legen Sie fest[**Arbeitsblatt.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)zu *wahr**. Andernfalls erhalten Sie möglicherweise falsche Zellwerte.

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

dann wird folgende Meldung angezeigt:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Andernfalls läuft das Programm ohne Anzeige einer Meldung, was bedeutet, dass alle aus den Zellen gelesenen Werte korrekt sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
