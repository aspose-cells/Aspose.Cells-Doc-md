---
title: Cell'den HTML5 dizesini alın
type: docs
weight: 40
url: /tr/python-java/get-html5-string-from-cell/
---
## **Cell'den HTML5 dizesini alın**
Aspose.Cells for Python via Java kullanarak, hücreden HTML dizesini alabilirsiniz. Bu kullanılarak elde edilebilir[getHtmlString(boole html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) API tarafından sağlanan yöntem.**yanlış**parametre olarak size Normal HTML döndürür, ancak geçerseniz**doğru**parametre olarak, HTML5 dizesini döndürür.

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasının A1 hücresine bir miktar metin ekler. Daha sonra A1 hücresinden Normal HTML ve HTML5 dizesini alır.[getHtmlString(boole html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) yöntemini kullanır ve bunları yazdırır.
## **Basit kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Aşağıdaki, yukarıda sağlanan kod parçacığı tarafından üretilen çıktıdır.
## **Çıktı**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
