---
title: Holen Sie sich den HTML5-String von Cell
type: docs
weight: 90
url: /de/java/get-html5-string-from-cell/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells gibt die Zeichenfolge HTML der Zelle zurück, die verwendet wird[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)Methode. Wenn Sie bestehen**FALSCH**Als Parameter wird es Ihnen Normal HTML zurückgeben, aber wenn Sie bestehen**wahr**Als Parameter wird eine HTML5-Zeichenfolge zurückgegeben.

## **Holen Sie sich den HTML5-String von Cell**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt Text in Zelle A1 des ersten Arbeitsblatts hinzu. Es ruft dann die Zeichenfolge Normal HTML und HTML5 aus Zelle A1 ab, indem es die verwendet[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)-Methode und gibt sie auf der Konsole aus.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
