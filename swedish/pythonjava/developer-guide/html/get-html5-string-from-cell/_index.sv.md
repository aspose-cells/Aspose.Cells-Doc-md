---
title: Hämta HTML5-sträng från Cell
type: docs
weight: 40
url: /sv/python-java/get-html5-string-from-cell/
---
## **Hämta HTML5-sträng från Cell**
Med Aspose.Cells for Python via Java kan du få HTML-strängen från cellen. Detta kan uppnås genom att använda[getHtmlString(boolesk html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) metod som tillhandahålls av API. Om du godkänner**falsk**som en parameter kommer den att returnera normal HTML men om du klarar**Sann**som en parameter returnerar den HTML5-sträng.

Följande exempelkod skapar ett arbetsboksobjekt och lägger till lite text i cell A1 i det första kalkylbladet. Den får sedan strängen Normal HTML och HTML5 från cell A1 med hjälp av[getHtmlString(boolesk html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) metod och skriver ut dem.
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Följande är utdata som genereras av det ovan angivna kodavsnittet.
## **Produktion**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
