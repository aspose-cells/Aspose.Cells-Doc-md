---
title: Lesen von Zellwerten in mehreren Threads gleichzeitig.
linktitle: Mehrere Threads.
type: docs
weight: 1800
url: /de/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Erfahren Sie, wie Sie Cell Werte gleichzeitig in mehreren Threads durch die API Aspose.Cells for .NET lesen.
keywords: Lesen Sie Zellwerte gleichzeitig in mehreren Threads, Aspose.Cells C# mehrere Threads, Lesen von Daten in mehreren Threads.
---

{{% alert color="primary" %}}

Es ist häufig erforderlich, Zellwerte gleichzeitig in mehreren Threads zu lesen. Dieser Artikel erläutert, wie Sie Aspose.Cells zu diesem Zweck verwenden.

{{% /alert %}}

Um gleichzeitig Zellwerte in mehreren Threads zu lesen, setzen Sie [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) auf **true**. Andernfalls erhalten Sie möglicherweise die falschen Zellwerte.

Der folgende Code:

1. Erstellt ein Arbeitsblatt.
1. Fügt ein Arbeitsblatt hinzu.
1. Befüllt das Arbeitsblatt mit Zeichenfolgen.
1. Es erstellt dann zwei Threads, die gleichzeitig Werte aus zufälligen Zellen lesen.
   Wenn die gelesenen Werte korrekt sind, passiert nichts. Wenn die gelesenen Werte inkorrekt sind, wird eine Meldung angezeigt.

Wenn Sie diese Zeile kommentieren:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

dann wird die folgende Nachricht angezeigt:

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Ansonsten läuft das Programm ohne Anzeige einer Meldung, was bedeutet, dass alle Werte, die aus den Zellen gelesen wurden, korrekt sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
