---
title: Konvertieren Sie numerische Textdaten in Zahlen
type: docs
weight: 900
url: /de/net/convert-text-numeric-data-to-number/
description: Erfahren Sie, wie Sie in Excel als Text gespeicherte Zahlen mithilfe von Aspose.Cells for .NET API in Zahlen umwandeln.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
{{% alert color="primary" %}}

 Manchmal möchten Sie als Text eingegebene numerische Daten in Zahlen umwandeln. Zahlen können Sie in Microsoft Excel als Text eingeben, indem Sie z. B. ein Apostroph vor eine Zahl setzen**'12345**. Excel behandelt die Zahl dann als Zeichenfolge. Mit Aspose.Cells können Sie Zeichenfolgen in Zahlen umwandeln.

{{% /alert %}}

Aspose.Cells bietet die[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)Methode, die verwendet werden kann, um alle Zeichenfolgen oder numerischen Textdaten in Zahlen umzuwandeln.

 Der folgende Screenshot zeigt Zeichenfolgennummern in Zellen**A1:A17**. Stringnummern werden linksbündig ausgerichtet.

|**Eingabedatei: Als Textstrings eingegebene Zahlen**|
|:- |
|![todo: Bild_alt_Text](convert-text-numeric-data-to-number_1.png)|

Diese Zeichenfolgennummern wurden mithilfe von in Zahlen umgewandelt[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)im folgenden Screenshot. Wie Sie sehen können, sind sie jetzt rechtsbündig ausgerichtet.

|**Ausgabedatei: Die Zeichenfolgen wurden in Zahlen umgewandelt**|
|:- |
|![todo: Bild_alt_Text](convert-text-numeric-data-to-number_2.png)|

## C#-Code zum Konvertieren von numerischen Zeichenfolgendaten in tatsächliche Zahlen

Der folgende Beispielcode veranschaulicht, wie alle numerischen Zeichenfolgendaten in tatsächlichen Zahlen in allen Arbeitsblättern konvertiert werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
