---
title: Hämta HTML5-sträng från Cell
type: docs
weight: 90
url: /sv/net/get-html5-string-from-cell/
---
## **Möjliga användningsscenarier**

Aspose.Cells returnerar HTML-strängen för cellen med hjälp av[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) metod som accepterar en boolesk parameter. Om du passerar**falsk**som en parameter kommer den att returnera normal HTML men om du klarar det**Sann** som en parameter returnerar den HTML5-sträng.

## **Hämta HTML5-sträng från Cell**

Följande exempelkod skapar ett arbetsboksobjekt och lägger till lite text i cell A1 i det första kalkylbladet. Den får sedan den normala HTML- och HTML5-strängen från cell A1 med hjälp av[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)metod och skriver ut dem på konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
