---
title: HTML5 String aus Zelle mit Golang via C++ abrufen
linktitle: HTML5 Zeichenfolge aus Zelle abrufen
type: docs
weight: 90
url: /de/go-cpp/get-html5-string-from-cell/
description: Lernen Sie, wie man die HTML5 Zeichenfolge aus einer Zelle mit der API Aspose.Cells for C++ erhält.
keywords: Holen Sie den HTML5 String aus der Zelle, HTML5 String aus der Zelle erhalten, HTML5 String der Zelle verwalten
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells gibt die HTML-Zeichenfolge der Zelle mit der [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/)-Methode zurück, die einen booleschen Parameter akzeptiert. Wenn Sie **false** als Parameter übergeben, wird normales HTML zurückgegeben, aber wenn Sie **true** übergeben, wird HTML5-String zurückgegeben.

## **HTML5-Zeichenfolge aus Zelle erhält**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt etwas Text in Zelle A1 des ersten Arbeitsblatts ein. Anschließend wird der Normal HTML- und HTML5-String aus Zelle A1 mit der Methode [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) geholt und auf der Konsole gedruckt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
