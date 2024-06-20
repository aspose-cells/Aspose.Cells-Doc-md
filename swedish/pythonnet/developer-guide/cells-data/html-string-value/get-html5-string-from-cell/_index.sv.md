---
title: Hämta HTML5 sträng från cell
type: docs
weight: 90
url: /sv/python-net/get-html5-string-from-cell/
description: Lär dig hur man hämtar HTML5 sträng från cell genom Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Hämta HTML5 sträng från cell med Python, Hämtningsbar HTML5 sträng från cell med Python, Hantera HTML5 sträng av cell i Python.
---

## **Möjliga användningsscenario**

Aspose.Cells for Python via .NET returnerar HTML-strängen från cellen med metoden [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) som accepterar en boolesk parameter. Om du passerar **false** som parameter kommer den att returnera normal HTML, men om du passerar **true** som parameter kommer den att returnera en HTML5-sträng.

## **Hämta HTML5-sträng från cell**

Följande provkod skapar en arbetsbok och lägger till lite text i cell A1 på den första kalkylbladet. Den hämtar sedan normal HTML och HTML5-sträng från cell A1 med metoden [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) och skriver ut dem på konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Konsoloutput**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
