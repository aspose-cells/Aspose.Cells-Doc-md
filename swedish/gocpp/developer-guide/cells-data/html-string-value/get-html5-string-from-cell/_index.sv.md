---
title: Hämta HTML5 sträng från cell med Golang via C++
linktitle: Få HTML5 sträng från Cell
type: docs
weight: 90
url: /sv/go-cpp/get-html5-string-from-cell/
description: Lär dig hur du får HTML5 strängen från en cell med API n Aspose.Cells for C++.
keywords: Få HTML5 sträng från cell, Hämta HTML5 sträng från cell, Hantera HTML5 sträng i cell
---

## **Möjliga användningsscenario**

Aspose.Cells returnerar HTML-strängen för cellen med metoden [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) som tar ett boolean-parameter. Om du skickar **false** som parameter, returnerar den Normal HTML, men om du skickar **true**, returnerar den HTML5-sträng.

## **Få HTML5-sträng från Cell**

Följande provkod skapar en arbetsbok och lägger till lite text i cell A1 på den första kalkylbladet. Den hämtar sedan normal HTML och HTML5-sträng från cell A1 med metoden [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) och skriver ut dem på konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **Konsoloutput**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
