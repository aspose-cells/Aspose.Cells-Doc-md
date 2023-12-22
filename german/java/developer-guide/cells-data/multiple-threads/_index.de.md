---
title: Cell-Werte in mehreren Threads gleichzeitig lesen
linktitle: Mehrere Threads
type: docs
weight: 1100
url: /de/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Erfahren Sie, wie Sie Cell-Werte in mehreren Threads gleichzeitig mit Aspose.Cells for Java-APIs lesen.
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

Das gleichzeitige Lesen von Zellwerten in mehreren Threads ist eine häufige Anforderung. In diesem Artikel wird erläutert, wie Sie Aspose.Cells für diesen Zweck verwenden.

{{% /alert %}}

##  **So lesen Sie Cell-Werte in mehreren Threads gleichzeitig mit Aspose.Cells for Java**

 Um Zellwerte in mehr als einem Thread gleichzeitig zu lesen, legen Sie fest[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)zu *wahr**. Andernfalls erhalten Sie möglicherweise falsche Zellwerte. Bitte beachten Sie, dass einige Funktionen wie das Formatieren von Zellenwerten für mehrere Threads nicht unterstützt werden. Mit MultiThreadReading können Sie also nur auf die Originaldaten der Zelle zugreifen. Wenn Sie in einer Umgebung mit mehreren Threads versuchen, den formatierten Wert der Zelle abzurufen, z. B. mit Cell.getStringValue() für numerische Werte, erhalten Sie möglicherweise ein unerwartetes Ergebnis oder eine Ausnahme.

Der folgende Code:

1. Erstellt eine Arbeitsmappe.
1. Fügt ein Arbeitsblatt hinzu.
1. Füllt das Arbeitsblatt mit Zeichenfolgenwerten.
1. Anschließend werden zwei Threads erstellt, die gleichzeitig Werte aus zufälligen Zellen lesen.
 Wenn die gelesenen Werte korrekt sind, passiert nichts. Wenn die gelesenen Werte falsch sind, wird eine Meldung angezeigt.

Wenn Sie diese Zeile kommentieren:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

dann wird folgende Meldung angezeigt:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Andernfalls läuft das Programm ohne Anzeige einer Meldung, was bedeutet, dass alle aus den Zellen gelesenen Werte korrekt sind.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
