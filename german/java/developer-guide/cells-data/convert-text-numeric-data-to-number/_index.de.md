---
title: Konvertieren Sie numerische Textdaten in Zahlen
type: docs
weight: 150
url: /de/java/convert-text-numeric-data-to-number/
description: Erfahren Sie, wie Sie als Text gespeicherte Zahlen mithilfe von Aspose.Cells for Java API in Zahlen umwandeln.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
{{% alert color="primary" %}}

 Manchmal möchten Sie als Text eingegebene numerische Daten in Zahlen umwandeln. Zahlen können Sie in Microsoft Excel als Text eingeben, indem Sie z. B. ein Apostroph vor eine Zahl setzen**'12345**. Excel behandelt die Zahl dann als Zeichenfolge. Mit Aspose.Cells können Sie Zeichenfolgen in Zahlen umwandeln.

{{% /alert %}}

Aspose.Cells for Java API bietet die[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue())-Methode, die verwendet werden kann, um alle Zeichenfolgen oder numerischen Textdaten in Zahlen umzuwandeln.

 Der folgende Screenshot zeigt Zeichenfolgennummern in Zellen**A1:A17**. Stringnummern werden linksbündig ausgerichtet.

**Eingabedatei: Als Textstrings eingegebene Zahlen** 

![todo: Bild_alt_Text](convert-text-numeric-data-to-number_1.png)

Diese Zeichenfolgennummern wurden mithilfe von in Zahlen umgewandelt[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) im folgenden Screenshot. Wie Sie sehen können, sind sie jetzt rechtsbündig ausgerichtet.

**Ausgabedatei: Die Zeichenfolgen wurden in Zahlen umgewandelt** 

![todo: Bild_alt_Text](convert-text-numeric-data-to-number_2.png)

Der folgende Beispielcode veranschaulicht, wie alle numerischen Zeichenfolgendaten in tatsächlichen Zahlen in allen Arbeitsblättern konvertiert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
