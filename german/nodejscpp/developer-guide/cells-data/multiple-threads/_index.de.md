---
title: Lesen von Zellwerten in mehreren Threads gleichzeitig.
linktitle: Mehrere Threads.
type: docs
weight: 1800
url: /de/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Lernen Sie, wie Sie Zellwerte in mehreren Threads gleichzeitig mithilfe der Aspose.Cells for Node.js via C++ API lesen.
keywords: Zellwerte in mehreren Threads gleichzeitig in Node.js via C++ lesen, Aspose.Cells C++ Mehrfäden, Daten in mehreren Threads lesen
---

{{% alert color="primary" %}}

Es ist häufig erforderlich, Zellwerte gleichzeitig in mehreren Threads zu lesen. Dieser Artikel erläutert, wie Sie Aspose.Cells zu diesem Zweck verwenden.

{{% /alert %}}

 Um Zellwerte in mehreren Threads gleichzeitig zu lesen, setzen Sie [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) auf **true**. Andernfalls könnten Sie falsche Zellwerte erhalten.

Der folgende Code:

1. Erstellt ein Arbeitsblatt.
1. Fügt ein Arbeitsblatt hinzu.
1. Befüllt das Arbeitsblatt mit Zeichenfolgen.
1. Es erstellt dann zwei Threads, die gleichzeitig Werte aus zufälligen Zellen lesen.
   Wenn die gelesenen Werte korrekt sind, passiert nichts. Wenn die gelesenen Werte inkorrekt sind, wird eine Meldung angezeigt.

Wenn Sie diese Zeile kommentieren:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

dann wird die folgende Nachricht angezeigt:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

Ansonsten läuft das Programm ohne Anzeige einer Meldung, was bedeutet, dass alle Werte, die aus den Zellen gelesen wurden, korrekt sind.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
