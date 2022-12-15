---
title: Holen Sie sich den HTML5-String von Cell
type: docs
weight: 40
url: /de/python-java/get-html5-string-from-cell/
---
## **Holen Sie sich den HTML5-String von Cell**
Mit Aspose.Cells for Python via Java können Sie die HTML-Zeichenfolge aus der Zelle abrufen. Dies kann durch die Verwendung von erreicht werden[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) Methode zur Verfügung gestellt von der API. Wenn Sie bestehen**FALSCH**als Parameter wird es Ihnen normales HTML zurückgeben, aber wenn Sie bestehen**Stimmt**Als Parameter wird eine HTML5-Zeichenfolge zurückgegeben.

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt Text in Zelle A1 des ersten Arbeitsblatts hinzu. Es ruft dann die normale HTML- und HTML5-Zeichenfolge aus Zelle A1 mithilfe von ab[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\))-Methode und druckt sie.
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Das Folgende ist die Ausgabe, die durch das oben bereitgestellte Code-Snippet generiert wird.
## **Ausgabe**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
