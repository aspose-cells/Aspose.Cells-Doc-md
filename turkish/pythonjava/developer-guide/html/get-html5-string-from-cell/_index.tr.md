---
title: Hücreden HTML5 dizesi al
type: docs
weight: 40
url: /tr/python-java/get-html5-string-from-cell/
---

## **Hücreden HTML5 dizesi al**
Aspose.Cells for Python via Java kullanarak hücreden HTML dizesi alabilirsiniz. Bunun için API tarafından sağlanan [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) yöntemi kullanılır. Parametre olarak **false** geçirirseniz Normal HTML, **true** geçirirseniz HTML5 dizisi döndürür.

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasının A1 hücresine bazı metin ekler. Daha sonra [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) yöntemini kullanarak hücreden Normal HTML ve HTML5 dizesi alır ve bunları yazdırır.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Yukarıda sağlanmış olan kod parçası tarafından üretilen çıktı aşağıda gösterilmiştir.
## **Çıktı**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
