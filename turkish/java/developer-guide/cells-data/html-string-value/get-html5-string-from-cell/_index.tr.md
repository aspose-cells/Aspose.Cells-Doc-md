---
title: Cell'den HTML5 dizesini alın
type: docs
weight: 90
url: /tr/java/get-html5-string-from-cell/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, şunu kullanarak hücrenin HTML dizesini döndürür:[**getHtmlString(boole html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)yöntem. eğer geçersen**yanlış**parametre olarak size Normal HTML döndürür, ancak geçerseniz**doğru**parametre olarak, HTML5 dizesini döndürür.

## **Cell'den HTML5 dizesini alın**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasının A1 hücresine bir miktar metin ekler. Daha sonra A1 hücresinden Normal HTML ve HTML5 dizesini alır.[**getHtmlString(boole html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)yöntemini kullanır ve bunları konsolda yazdırır.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
