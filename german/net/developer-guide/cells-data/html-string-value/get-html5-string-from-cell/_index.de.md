---
title: Holen Sie sich die HTML5-Zeichenfolge von Cell
type: docs
weight: 90
url: /de/net/get-html5-string-from-cell/
description: Erfahren Sie, wie Sie die HTML5-Zeichenfolge von Cell bis Aspose.Cells, for .NET und API abrufen.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---
##  **Mögliche Nutzungsszenarien**

Aspose.Cells gibt die Zeichenfolge HTML der Zelle unter Verwendung von zurück[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) Methode, die einen booleschen Parameter akzeptiert. Wenn Sie bestehen**FALSCH** Als Parameter wird Normal HTML zurückgegeben, aber wenn Sie bestehen**WAHR** Als Parameter wird eine HTML5-Zeichenfolge zurückgegeben.

##  **Holen Sie sich die HTML5-Zeichenfolge von Cell**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt Text in Zelle A1 des ersten Arbeitsblatts hinzu. Anschließend werden die normale Zeichenfolge HTML und die HTML5-Zeichenfolge aus Zelle A1 mithilfe von abgerufen[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)Methode und druckt sie auf der Konsole aus.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

##  **Konsolenausgabe**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
