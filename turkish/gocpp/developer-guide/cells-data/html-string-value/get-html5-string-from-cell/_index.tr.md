---
title: Golang kullanarak C++ ile Hücreden HTML5 Dizisi Alma
linktitle: Hücreden HTML5 Dizgisini alın
type: docs
weight: 90
url: /tr/go-cpp/get-html5-string-from-cell/
description: Aspose.Cells for C++ API kullanarak hücreden HTML5 dizgisini nasıl alınır öğrenin.
keywords: Hücreden HTML5 dizesi al, Hücreden HTML5 dizesi al, Hücrenin HTML5 dizesini yönet
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, boolean parametre alan [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) metodunu kullanarak hücrenin HTML dizgisini döndürür. Eğer parametre olarak **false** verirseniz, Normal HTML döner, eğer **true** verirseniz, HTML5 dizesi döner.

## **Hücreden HTML5 Dizgisini Al**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışsayısının A1 hücresine bazı metinler ekler. Ardından, A1 hücresinden Normal HTML ve HTML5 dizelerini [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) yöntemini kullanarak alır ve bunları konsola yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **Konsol Çıktısı**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
