---
title: Ändern von Text Daten in Zahlen
type: docs
weight: 150
url: /de/java/convert-text-numeric-data-to-number/
description: Erfahren Sie, wie Sie die als Text gespeicherten Zahlen in Zahlen konvertieren, indem Sie die Aspose.Cells for Java API verwenden.
keywords: excel Zahl als Text, excel Zahl als Text konvertieren Java, excel Zahl als Text numerische Daten in Zahl konvertieren, excel Zahl als Text numerische Daten in Zahl konvertieren Java, excel Zahl Text in Zahl konvertieren, excel Zahl Text in Zahl konvertieren Java, excel Zahl Text in Zahl mit Java konvertieren, numerischen Text in Zahl in Excel mit Java konvertieren, numerischen Text in Zahl in Excel mit Java konvertieren, numerischen String in Zahl in Excel mit Java konvertieren, excel Zahl als Text numerische Daten in Zahl konvertieren Java, excel numerischen String in Zahl konvertieren Java
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie numerische Daten, die als Text eingegeben wurden, in Zahlen umwandeln. Sie können Zahlen als Text in Microsoft Excel eingeben, indem Sie eine Apostroph vor einer Zahl setzen, zum Beispiel **'12345**. Excel behandelt die Zahl dann als Zeichenfolge. Aspose.Cells ermöglicht es Ihnen, Zeichenfolgen in Zahlen umzuwandeln.


## Konvertieren von als Text gespeicherten Zahlen in Zahlen in Excel
Sie können Zahlen, die als Text gespeichert sind, in Zahlen umwandeln, indem Sie ein paar einfache Schritte befolgen.
1. Wählen Sie eine einzelne Zelle oder einen Zellenbereich aus, der oben links einen Fehlerindikator hat.
1. Klicken Sie neben der ausgewählten Zelle oder dem ausgewählten Zellenbereich auf die Schaltfläche für den Fehler, die erscheint. Klicken Sie im Menü auf In Zahl umwandeln. 
<br>
<img src="4.png" width=70% />
1. Wenn die Warnschaltfläche nicht verfügbar ist, wählen Sie eine Spalte mit diesem Problem aus. Wenn Sie nicht die ganze Spalte konvertieren möchten, können Sie stattdessen eine oder mehrere Zellen auswählen. Stellen Sie nur sicher, dass die von Ihnen ausgewählten Zellen sich in derselben Spalte befinden, andernfalls funktioniert dieser Vorgang nicht. Die Option Text in Spalten wird in der Regel zum Aufteilen einer Spalte verwendet, aber sie kann auch dazu verwendet werden, eine einzelne Spalte von Text in Zahlen umzuwandeln. Klicken Sie auf der Registerkarte Daten auf Text in Spalten.
<br>
<img src="1.png" width=70% />
1. Klicken Sie in dem Popup-Fenster auf die Schaltfläche Fertig stellen.
<br>
<img src="2.png" width=70% />
1. Die als Text gespeicherten Zahlen werden in Zahlen umgewandelt.
<br>
<img src="3.png" width=70% />

## Konvertieren von als Text gespeicherten Zahlen in Zahlen mithilfe von Aspose.Cells für JAVA
Die API Aspose.Cells for Java bietet die Methode [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--), die verwendet werden kann, um alle Zeichenfolgen- oder Textnummern in Zahlen umzuwandeln.

Im folgenden Screenshot sind Zeichenfolgenzahlen in Zellen **A1:A17** zu sehen. Die Zeichenfolgenzahlen sind linksbündig ausgerichtet.
<br>
<img src="5.png" width=70% />

Diese Zeichenfolgenzahlen wurden in der folgenden Bildschirmaufnahme mithilfe von [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) in Zahlen umgewandelt. Wie Sie sehen können, sind sie jetzt rechtsbündig.
<br>
<img src="6.png" width=70% />

## Java-Code für die Umwandlung von Zeichenfolgennummerndaten in tatsächliche Zahlen
Der folgende Beispielcode veranschaulicht, wie man alle numerischen Zeichenfolgendaten in allen Arbeitsblättern in tatsächliche Zahlen umwandelt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
{{< app/cells/assistant language="java" >}}
