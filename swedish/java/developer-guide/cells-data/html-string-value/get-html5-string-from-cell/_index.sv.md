---
title: Hämta HTML5 sträng från cell
type: docs
weight: 90
url: /sv/java/get-html5-string-from-cell/
---

## **Möjliga användningsscenario**

Aspose.Cells returnerar HTML-strängen från cellen med metoden [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString). Om du skickar **false** som parameter, kommer den returnera Normal HTML men om du skickar **true** som parameter, kommer den returnera HTML5-strängen.

## **Hämta HTML5-sträng från cell**

Följande exemplarkod skapar en arbetsbok och lägger till lite text i cell A1 i det första arket. Sedan hämtar den Normal HTML och HTML5-strängen från cell A1 med hjälp av metoden [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) och skriver ut dem i konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
