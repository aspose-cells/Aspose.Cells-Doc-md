---
title: Lesen von Zellwerten in mehreren Threads gleichzeitig.
linktitle: Mehrere Threads.
type: docs
weight: 1100
url: /de/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Java APIs Zellenwerte in mehreren Threads gleichzeitig lesen.
keywords: Java Lesen von Zellenwerten in mehreren Threads gleichzeitig, Mehrere Threads für Aspose.Cells for Java APIs.
---

{{% alert color="primary" %}}

Es ist häufig erforderlich, Zellwerte gleichzeitig in mehreren Threads zu lesen. Dieser Artikel erläutert, wie Sie Aspose.Cells zu diesem Zweck verwenden.

{{% /alert %}}

## **Wie Sie mit Aspose.Cells for Java Zellenwerte in mehreren Threads gleichzeitig lesen können**

Um Zellenwerte in mehr als einem Thread gleichzeitig zu lesen, setzen Sie [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) auf **wahr**. Andernfalls erhalten Sie möglicherweise falsche Zellenwerte. Bitte beachten Sie, dass einige Funktionen wie das Formatieren von Zellenwerten für Mehrfachthreads nicht unterstützt werden. Das MultiThreadReading ermöglicht es Ihnen nur, auf die ursprünglichen Zellendaten zuzugreifen. In einer Mehrfachthreads-Umgebung erhalten Sie bei dem Versuch, den formatierten Wert der Zelle zu erhalten, wie z.B. mittels Cell.getStringValue() für numerische Werte, möglicherweise ein unerwartetes Ergebnis oder eine Ausnahme.

Der folgende Code:

1. Erstellt ein Arbeitsblatt.
1. Fügt ein Arbeitsblatt hinzu.
1. Befüllt das Arbeitsblatt mit Zeichenfolgen.
1. Es erstellt dann zwei Threads, die gleichzeitig Werte aus zufälligen Zellen lesen.
   Wenn die gelesenen Werte korrekt sind, passiert nichts. Wenn die gelesenen Werte inkorrekt sind, wird eine Meldung angezeigt.

Wenn Sie diese Zeile kommentieren:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

dann wird die folgende Nachricht angezeigt:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Ansonsten läuft das Programm ohne Anzeige einer Meldung, was bedeutet, dass alle Werte, die aus den Zellen gelesen wurden, korrekt sind.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
