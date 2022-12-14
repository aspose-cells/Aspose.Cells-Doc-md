---
title: Cell'den HTML5 dizesini alın
type: docs
weight: 90
url: /tr/net/get-html5-string-from-cell/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, şunu kullanarak hücrenin HTML dizesini döndürür:[**HtmlString'i Getir**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) bir boole parametresini kabul eden yöntem. eğer geçersen**yanlış**parametre olarak Normal HTML döndürür, ancak geçerseniz**doğru** parametre olarak, HTML5 dizesini döndürür.

## **Cell'den HTML5 dizesini alın**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasının A1 hücresine bir miktar metin ekler. Daha sonra A1 hücresinden Normal HTML ve HTML5 dizesini alır.[**HtmlString'i Getir**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)yöntemini kullanır ve bunları konsolda yazdırır.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
