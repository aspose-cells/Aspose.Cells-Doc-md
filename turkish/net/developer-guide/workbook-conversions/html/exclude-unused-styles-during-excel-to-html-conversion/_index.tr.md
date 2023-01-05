---
title: Excel'den HTML'e dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Olası Kullanım Senaryoları**

Microsoft Excel dosyası kullanılmayan birçok stil içerebilir. Excel dosyasını HTML biçiminde dışa aktardığınızda bu kullanılmayan stiller de dışa aktarılır. Bu, HTML'in boyutunu artırabilir. Excel dosyasının HTML'e dönüştürülmesi sırasında kullanılmayan stilleri,[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) Emlak. Ayarladığınızda**doğru**, kullanılmayan tüm stiller HTML çıkışından hariç tutulur. Aşağıdaki ekran görüntüsü, HTML çıktısı içindeki kullanılmayan bir stil örneğini gösterir.

![yapılacaklar:resim_alternatif_metin](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excel'den HTML'e dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut**

Aşağıdaki örnek kod, bir çalışma kitabı ve ayrıca kullanılmayan bir adlandırılmış stil oluşturur. Beri[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) ayarlandı**doğru** , bu kullanılmayan adlandırılmış stil şuraya aktarılmayacak:[çıkış HTML](61767778.zip) . Ama eğer ayarlarsan**YANLIŞ**, bu kullanılmayan stil, yukarıdaki ekran görüntüsünde gösterildiği gibi HTML işaretlemesinde görebileceğiniz HTML çıktısının içinde yer alacaktır.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
