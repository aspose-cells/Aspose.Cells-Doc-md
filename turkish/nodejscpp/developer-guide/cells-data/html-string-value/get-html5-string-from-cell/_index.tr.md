---
title: Hücreden HTML5 dizesi al
type: docs
weight: 90
url: /tr/nodejs-cpp/get-html5-string-from-cell/
description: Aspose.Cells for Node.js via C++ API si aracılığıyla hücreden HTML5 dizgisini nasıl alınacağını öğrenin.
keywords: Hücreden HTML5 dizgisini alın Node.js üzerinden C++ ile, hücreden HTML5 dizgisini alın Node.js üzerinden C++, hücrenin HTML5 dizgesini yönet Node.js üzerinden C++
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, boolean parametre kabul eden [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) yöntemiyle hücrenin HTML dizgesini döndürür. Eğer **false** parametre olarak geçerseniz, Normal HTML döner, **true** geçerseniz HTML5 dizgisi döner.

## **Hücreden HTML5 dizesi al**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasındaki A1 hücresine bazı metinler ekler. Daha sonra A1 hücresinden Normal HTML ve HTML5 dizgilerini alır, ve bunları konsola yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Konsol Çıktısı**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
