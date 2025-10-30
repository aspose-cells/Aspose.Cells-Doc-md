---
title: Ändern von Text Daten in Zahlen
type: docs
weight: 900
url: /de/nodejs-cpp/convert-text-numeric-data-to-number/
description: Lernen Sie, wie Sie Nummern, die als Text in Excel gespeichert sind, mithilfe der Aspose.Cells for Node.js via C++ API in Zahlen umwandeln.
keywords: Excel Text in Zahl umwandeln, Excel Text in Zahl Node.js Code, Excel numerische Textdaten in Zahl umwandeln, Excel numerische Textdaten in Zahl Node.js Code, Excel numerischen Text in Zahl umwandeln, Excel numerischen Text in Zahl Node.js Code, Excel numerischen Text mit Node.js Code in Zahl umwandeln, numerischen Text in Excel mit Node.js Code in Zahl umwandeln, numerischen String in Excel mit Node.js Code in Zahl umwandeln, numerische Textdaten in Excel mit Node.js Code in Zahl umwandeln, numerischen String in Zahl in Excel mit Node.js Code umwandeln
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie numerische Daten, die als Text eingegeben wurden, in Zahlen umwandeln. Sie können Zahlen in Microsoft Excel als Text eingeben, indem Sie einen Apostroph vor die Zahl setzen, zum Beispiel **'12345**. Excel behandelt die Zahl dann als String. Aspose.Cells for Node.js via C++ ermöglicht es Ihnen, Strings in Zahlen umzuwandeln.


## Wie man in Excel Zahlen, die als Text gespeichert sind, in Zahlen umwandelt
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

## So konvertieren Sie in Excel gespeicherte Zahlen als Text mithilfe von Aspose.Cells for Node.js via C++
Aspose.Cells for Node.js via C++ stellt die Methode [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) bereit, die verwendet werden kann, um alle String- oder Textnumerikdaten in Zahlen umzuwandeln.

Im folgenden Screenshot sind Zeichenfolgenzahlen in Zellen **A1:A17** zu sehen. Die Zeichenfolgenzahlen sind linksbündig ausgerichtet.
<br>
<img src="5.png" width=70% />

Diese Zeichenfolgenzahlen wurden in der folgenden Bildschirmaufnahme mithilfe von [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) in Zahlen umgewandelt. Wie Sie sehen können, sind sie jetzt rechtsbündig.
<br>
<img src="6.png" width=70% />

## Node.js-Code zum Umwandeln von String-Zahlen in tatsächliche Zahlen

Der folgende Beispielcode veranschaulicht, wie man alle numerischen Zeichenfolgendaten in allen Arbeitsblättern in tatsächliche Zahlen umwandelt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ConvertTextNumericDatatoNumber.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
