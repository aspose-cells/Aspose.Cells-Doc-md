---
title: Hämta HTML5-sträng från Cell
type: docs
weight: 90
url: /sv/java/get-html5-string-from-cell/
---
## **Möjliga användningsscenarier**

Aspose.Cells returnerar HTML-strängen för cellen med hjälp av[**getHtmlString(boolesk html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)metod. Om du passerar**falsk**som en parameter kommer den att returnera normal HTML men om du klarar det**Sann**som en parameter returnerar den HTML5-sträng.

## **Hämta HTML5-sträng från Cell**

Följande exempelkod skapar ett arbetsboksobjekt och lägger till lite text i cell A1 i det första kalkylbladet. Den får sedan den normala HTML- och HTML5-strängen från cell A1 med hjälp av[**getHtmlString(boolesk html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)metod och skriver ut dem på konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
