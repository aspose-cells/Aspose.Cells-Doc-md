---
title: Cell'den HTML5 dizesini alın
type: docs
weight: 90
url: /tr/net/get-html5-string-from-cell/
description: Cell'den Aspose.Cells for .NET API'e kadar HTML5 dizesini nasıl alacağınızı öğrenin.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---
##  **Olası Kullanım Senaryoları**

Aspose.Cells, hücrenin HTML dizesini kullanarak döndürür.[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) Boole parametresini kabul eden yöntem. Eğer geçersen**YANLIŞ** parametre olarak Normal HTML değerini döndürür, ancak geçerseniz**doğru** parametre olarak HTML5 dizesini döndürecektir.

##  **Cell'den HTML5 dizesini alın**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasının A1 hücresine bir miktar metin ekler. Daha sonra Normal HTML ve HTML5 dizesini A1 hücresinden alır.[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)yöntemini kullanır ve bunları konsola yazdırır.

##  **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

##  **Konsol Çıkışı**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
