---
title: Hämta HTML5 sträng från cell
type: docs
weight: 90
url: /sv/net/get-html5-string-from-cell/
description: Lär dig hur du får HTML5 sträng från cellen genom Aspose.Cells for .NET API.
keywords: Få HTML5 sträng från cell, Hämta HTML5 sträng från cell, Hantera HTML5 sträng i cell
---

## **Möjliga användningsscenario**

Aspose.Cells returnerar HTML-strängen från cellen med hjälp av [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) -metoden som accepterar en boolesk parameter. Om du passerar **false** som parameter returneras vanlig HTML men om du passerar **true** som parameter returneras en HTML5-sträng.

## **Hämta HTML5-sträng från cell**

Följande provkod skapar en arbetsbok och lägger till lite text i cell A1 på den första kalkylbladet. Den hämtar sedan normal HTML och HTML5-sträng från cell A1 med metoden [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) och skriver ut dem på konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
