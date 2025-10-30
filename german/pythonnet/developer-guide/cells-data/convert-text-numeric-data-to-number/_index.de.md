---
title: Ändern von Text Daten in Zahlen
type: docs
weight: 900
url: /de/python-net/convert-text-numeric-data-to-number/
description: Erfahren Sie, wie Sie Zahlen, die in Excel als Text gespeichert sind, in Zahlen umwandeln können, indem Sie die API Aspose.Cells for Python via .NET verwenden.
keywords: python excel text in zahl umwandeln, python excel text in zahl umwandeln, python excel text in zahl, python excel text in zahl, python excel text in zahl, python excel text in zahl, excel text in zahl umwandeln mit python, text in zahl in excel mit python umwandeln, text in zahl in excel mit python umwandeln, text in zahl in excel mit python excel bibliothek umwandeln, python excel text in zahl, text in zahl in excel mit python umwandeln.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie numerische Daten, die als Text eingegeben wurden, in Zahlen umwandeln. Sie können Zahlen als Text in Microsoft Excel eingeben, indem Sie vor einer Zahl ein Apostroph setzen, zum Beispiel **'12345**. Excel behandelt dann die Zahl als Zeichenfolge. Aspose.Cells for Python via .NET ermöglicht es Ihnen, Zeichenfolgen in Zahlen umzuwandeln.


## **So wandeln Sie in Excel gespeicherte Zahlen in Text in Zahlen um**
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

## **So wandeln Sie in Excel gespeicherte Zahlen in Text in Zahlen um, indem Sie die Aspose.Cells for Python Excel-Bibliothek verwenden**
Aspose.Cells for Python via .NET bietet die Methode [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/), die dazu verwendet werden kann, alle Zeichenfolgen- oder Text-Daten in Zahlen umzuwandeln.

Im folgenden Screenshot sind Zeichenfolgenzahlen in Zellen **A1:A17** zu sehen. Die Zeichenfolgenzahlen sind linksbündig ausgerichtet.
<br>
<img src="5.png" width=70% />

Diese Zeichenfolgenzahlen wurden in der folgenden Bildschirmaufnahme mithilfe von [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) in Zahlen umgewandelt. Wie Sie sehen können, sind sie jetzt rechtsbündig.
<br>
<img src="6.png" width=70% />

## **Python-Code zum Umwandeln von Zeichenfolgenzahlen in tatsächliche Zahlen**

Der folgende Beispielcode veranschaulicht, wie man alle numerischen Zeichenfolgendaten in allen Arbeitsblättern in tatsächliche Zahlen umwandelt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
{{< app/cells/assistant language="python-net" >}}
