---
title: Gleichzeitiges Lesen von Cell-Werten in mehreren Threads
linktitle: Mehrere Threads
type: docs
weight: 1100
url: /de/java/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

Das gleichzeitige Lesen von Zellenwerten in mehreren Threads ist eine häufige Anforderung. Dieser Artikel erklärt, wie Sie Aspose.Cells für diesen Zweck verwenden.

{{% /alert %}}

 Um Zellenwerte in mehr als einem Thread gleichzeitig zu lesen, set[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) zu**wahr**Wenn Sie dies nicht tun, erhalten Sie möglicherweise die falschen Zellenwerte. Bitte beachten Sie, dass einige Funktionen wie das Formatieren von Zellenwerten für mehrere Threads nicht unterstützt werden. MultiThreadReading ermöglicht Ihnen also nur den Zugriff auf die Originaldaten der Zelle. Wenn Sie in einer Umgebung mit mehreren Threads versuchen, den formatierten Wert der Zelle abzurufen, z. B. durch Cell.getStringValue() für numerische Werte, erhalten Sie möglicherweise ein unerwartetes Ergebnis oder eine Ausnahme.

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

dann kommt folgende meldung:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Andernfalls läuft das Programm ohne Meldung, was bedeutet, dass alle aus Zellen gelesenen Werte korrekt sind.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
