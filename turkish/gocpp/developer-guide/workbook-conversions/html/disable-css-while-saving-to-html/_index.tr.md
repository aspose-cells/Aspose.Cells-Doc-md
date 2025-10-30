---
title: HTML yi kaydederken CSS i devre dışı bırakma Golang ve C++ ile
linktitle: HTML yi kaydederken CSS yi devre dışı bırak
type: docs
weight: 320
url: /tr/go-cpp/disable-css-while-saving-to-html/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye kaydederken CSS yi devre dışı bırakmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir Excel dosyasını tek sayfa HTML olarak kaydettiğinizde, genellikle CSS öğeleri HTML dosyasına gömülü olur ve HEAD bölümünde bulunur. Bu dosyayı eposta içeriği/gövdesi olarak ekte gönderseniz, çoğu e-posta istemcisi CSS öğelerini kaldırır, bu da düzgün görüntülenmemeye neden olur. Aspose.Cells'in 24.12 sürümü, CSS'yi isteğe bağlı olarak devre dışı bırakmanıza olanak sağlayan bir seçenek sunar, böylece stiller doğrudan HTML öğeleri içinde uygulanabilir. Eposta içeriği/gövdesi olarak HTML'yi ayarlamak istiyorsanız, lütfen [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) özelliğini kullanın ve **true** yapın.

## **CSS'yi devre dışı bırakırken HTML'ye kaydetme**

 [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) özelliğinin kullanımını gösteren örnek kod.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
