---
title: Hücreden HTML5 dizesi al
type: docs
weight: 90
url: /tr/java/get-html5-string-from-cell/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, hücrenin HTML dizesini [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) yöntemini kullanarak döndürür. Bir parametre olarak **false** geçirirseniz, Normal HTML'u döndürecek ancak **true** geçirirseniz, HTML5 dizesini döndürecektir.

## **Hücreden HTML5 dizesi al**

Aşağıdaki örnek kod bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasının A1 hücresine bazı metinler ekler. Ardından [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) yöntemini kullanarak A1 hücresinden Normal HTML ve HTML5 dizesi alır ve bunları konsola yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
