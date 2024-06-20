---
title: HTML5 String aus Zelle abrufen
type: docs
weight: 40
url: /de/python-java/get-html5-string-from-cell/
---

## **Holen Sie sich HTML5-String aus der Zelle**
Mit Aspose.Cells für Python via Java können Sie den HTML-String aus der Zelle erhalten. Dies kann durch Verwendung der Methode [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) der API erreicht werden. Wenn Sie **false** als Parameter übergeben, wird Ihnen normaler HTML zurückgegeben. Wenn Sie **true** als Parameter übergeben, wird Ihnen ein HTML5-String zurückgegeben.

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt etwas Text in Zelle A1 des ersten Arbeitsblatts hinzu. Anschließend werden der normale HTML und der HTML5 String aus Zelle A1 mit der Methode [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) abgerufen und gedruckt.
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Das folgende ist die Ausgabe, die durch den obigen Codeausschnitt generiert wird.
## **Ergebnis**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
