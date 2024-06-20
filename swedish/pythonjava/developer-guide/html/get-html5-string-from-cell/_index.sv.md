---
title: Hämta HTML5 sträng från cell
type: docs
weight: 40
url: /sv/python-java/get-html5-string-from-cell/
---

## **Hämta HTML5-sträng från cell**
Med Aspose.Cells för Python via Java kan du få HTML-strängen från cellen. Detta kan åstadkommas genom att använda metoden [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) som tillhandahålls av API:et. Om du skickar **falskt** som ett parameter kommer den att returnera Normal HTML men om du skickar **sant** som ett parameter kommer den att returnera en HTML5-sträng.

Följande kodexempel skapar en arbetsboksobjekt och lägger till lite text i cell A1 på den första arbetsbladet. Sedan hämtas Normal HTML- och HTML5-strängen från cell A1 med hjälp av metoden [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) och skrivs ut.
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Följande är den utmatning som genererats av det tidigare angivna kodexemplet.
## **Output**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
