---
title: Konvertieren Sie numerische Textdaten in Zahlen
type: docs
weight: 900
url: /de/net/convert-text-numeric-data-to-number/
description: Erfahren Sie, wie Sie in Excel als Text gespeicherte Zahlen mit Aspose.Cells for .NET API in Zahlen umwandeln.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
##  **Mögliche Nutzungsszenarien**
Manchmal möchten Sie als Text eingegebene numerische Daten in Zahlen umwandeln. Sie können Zahlen als Text in Microsoft Excel eingeben, indem Sie vor einer Zahl ein Apostroph setzen, zum Beispiel *'12345**. Excel behandelt die Zahl dann als Zeichenfolge. Mit Aspose.Cells können Sie Zeichenfolgen in Zahlen umwandeln.


##  So konvertieren Sie als Text gespeicherte Zahlen in Zahlen in Excel
Mit ein paar einfachen Schritten können Sie als Text gespeicherte Zahlen in Zahlen umwandeln.
1. Wählen Sie eine einzelne Zelle oder einen Zellbereich aus, der/die in der oberen linken Ecke eine Fehleranzeige aufweist.
1.  Klicken Sie neben der ausgewählten Zelle oder dem ausgewählten Zellbereich auf die angezeigte Fehlerschaltfläche. Klicken Sie im Menü auf „In Zahl konvertieren“.
<br>
<img src="4.png" width=70% />
1. Wenn die Warnschaltfläche nicht verfügbar ist, wählen Sie eine Spalte mit diesem Problem aus. Wenn Sie nicht die gesamte Spalte konvertieren möchten, können Sie stattdessen eine oder mehrere Zellen auswählen. Stellen Sie jedoch sicher, dass sich die von Ihnen ausgewählten Zellen in derselben Spalte befinden, da dieser Vorgang sonst nicht funktioniert. Die Schaltfläche „Text in Spalten“ wird normalerweise zum Teilen einer Spalte verwendet, kann aber auch zum Konvertieren einer einzelnen Textspalte in Zahlen verwendet werden. Klicken Sie auf der Registerkarte „Daten“ auf „Text in Spalten“.
<br>
<img src="1.png" width=70% />
1. Klicken Sie im Popup-Fenster auf die Schaltfläche „Fertig stellen“.
<br>
<img src="2.png" width=70% />
1. Die als Text gespeicherten Zahlen werden in Zahlen umgewandelt.
<br>
<img src="3.png" width=70% />

## So konvertieren Sie als Text gespeicherte Zahlen mit Aspose.Cells for .NET in Zahlen
Aspose.Cells bietet die[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)Methode, mit der alle numerischen Zeichenfolgen- oder Textdaten in Zahlen umgewandelt werden können.

Der folgende Screenshot zeigt Zeichenfolgennummern in den Zellen *A1:A17**. Zeichenfolgennummern werden linksbündig ausgerichtet.
<br>
<img src="5.png" width=70% />

 Diese Zeichenfolgennummern wurden mit in Zahlen umgewandelt[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)im folgenden Screenshot. Wie Sie sehen, sind sie jetzt rechtsbündig.
<br>
<img src="6.png" width=70% />

##  C#-Code zum Konvertieren numerischer Zeichenfolgedaten in tatsächliche Zahlen

Der folgende Beispielcode veranschaulicht, wie alle numerischen Zeichenfolgedaten in allen Arbeitsblättern in tatsächliche Zahlen konvertiert werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
