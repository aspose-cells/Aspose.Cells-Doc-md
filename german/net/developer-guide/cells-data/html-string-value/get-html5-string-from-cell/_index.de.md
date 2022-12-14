---
title: Holen Sie sich den HTML5-String von Cell
type: docs
weight: 90
url: /de/net/get-html5-string-from-cell/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells gibt den HTML-String der Zelle mit dem zurück[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) Methode, die einen booleschen Parameter akzeptiert. Wenn Sie bestehen**FALSCH**als Parameter wird normales HTML zurückgegeben, aber wenn Sie übergeben**Stimmt** Als Parameter wird eine HTML5-Zeichenfolge zurückgegeben.

## **Holen Sie sich den HTML5-String von Cell**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt Text in Zelle A1 des ersten Arbeitsblatts hinzu. Es ruft dann die normale HTML- und HTML5-Zeichenfolge aus Zelle A1 mithilfe von ab[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)-Methode und gibt sie auf der Konsole aus.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
