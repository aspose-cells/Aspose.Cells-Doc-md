---
title: Golang kullanarak C++ ile Excel den HTML ye dönüşüm sırasında kullanılmayan Stil seçeneklerini hariç tutma
linktitle: Kullanılmayan Stilleri Hariç Tutma
type: docs
weight: 30
url: /tr/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Aspose.Cells for C++ kullanarak Excel den HTML ye dönüştürürken kullanılmayan stilleri nasıl hariç tutacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel dosyaları birçok kullanılmayan stil içerebilir. Excel dosyasını HTML'ye aktarırken, bu kullanılmayan stiller de dışa aktarılır ve bu da HTML boyutunu artırabilir. Excel dosyasını HTML'ye dönüştürürken kullanılmayan stilleri hariç tutmak için [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) özelliğini kullanabilirsiniz. Bunu **true** olarak ayarladığınızda, tüm kullanılmayan stiller çıkış HTML'sinden hariç tutulur. Aşağıdaki ekran görüntüsü, çıkış HTML'sinde yer alan bir kullanılmayan stil örneğini gösterir.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.**

 Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ayrıca kullanılmayan bir isimli stil de ekler. [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) **true** olarak ayarlandığından, bu kullanılmayan isimli stil çıkış HTML'sine aktarılmaz. Ancak, onu **false** yaparsanız, bu kullanılmayan stil çıkış HTML'sinde bulunur ve bu durumu yukarıdaki ekran görüntüsünde görebilirsiniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
