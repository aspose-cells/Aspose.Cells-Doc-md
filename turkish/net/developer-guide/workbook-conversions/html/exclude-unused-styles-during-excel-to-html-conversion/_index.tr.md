---
title: Excel'den HTML'ye dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Olası Kullanım Senaryoları**

Microsoft Excel dosyası kullanılmayan birçok stil içerebilir. Excel dosyasını HTML biçiminde dışa aktardığınızda, bu kullanılmayan stiller de dışa aktarılır. Bu, HTML'nin boyutunu artırabilir. Kullanılmayan stilleri Excel dosyasının HTML'ye dönüştürülmesi sırasında hariç tutabilirsiniz.[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) Emlak. Ayarladığınızda**doğru**kullanılmayan tüm stiller çıktı HTML'sinden hariç tutulur. Aşağıdaki ekran görüntüsü, çıktı HTML'sinin içinde kullanılmayan örnek bir stil görüntüler.

![yapılacaklar:resim_alternatif_Metin](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excel'den HTML'ye dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut**

Aşağıdaki örnek kod, bir çalışma kitabı ve ayrıca kullanılmayan bir adlandırılmış stil oluşturur. Beri[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) ayarlandı**doğru** , bu kullanılmayan adlandırılmış stil şuraya aktarılmayacak:[çıktı HTML'si](61767778.zip) . Ama eğer ayarlarsan**yanlış**, daha sonra bu kullanılmayan stil, yukarıdaki ekran görüntüsünde gösterildiği gibi HTML işaretlemesinde görebileceğiniz çıktı HTML'sinin içinde yer alacaktır.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
