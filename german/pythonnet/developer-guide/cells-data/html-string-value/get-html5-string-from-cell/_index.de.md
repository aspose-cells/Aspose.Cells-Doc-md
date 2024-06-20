---
title: HTML5 String aus Zelle abrufen
type: docs
weight: 90
url: /de/python-net/get-html5-string-from-cell/
description: Erfahren Sie, wie Sie mit der Aspose.Cells for Python via .NET API den HTML5 String aus einer Zelle erhalten.
keywords: Python Excel Bibliothek, Python HTML5 String aus Zelle erhalten, HTML5 String aus Zelle mit Python erhalten, HTML5 String der Zelle in Python verwalten.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for Python via .NET gibt den HTML-String der Zelle mit der [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool)-Methode zurück, die einen booleschen Parameter akzeptiert. Wenn Sie **false** als Parameter übergeben, wird es Normal HTML zurückgeben, aber wenn Sie **true** als Parameter übergeben, wird es einen HTML5-String zurückgeben.

## **Holen Sie sich HTML5-String aus der Zelle**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt etwas Text in Zelle A1 des ersten Arbeitsblatts ein. Anschließend wird der Normal HTML- und HTML5-String aus Zelle A1 mit der Methode [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) geholt und auf der Konsole gedruckt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
