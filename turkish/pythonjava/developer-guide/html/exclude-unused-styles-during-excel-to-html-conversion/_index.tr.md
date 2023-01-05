---
title: Excel'den HTML'e dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Excel'den HTML'e dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut**
Microsoft Excel dosyaları kullanılmayan birçok stil içerebilir. Bu dosyalar HTML formatında dışa aktarıldığında kullanılmayan stiller de dışa aktarılır. Bu, HTML çıktısının boyutunun artmasıyla sonuçlanır. Aspose.Cells for Python via Java, Excel dosyasının HTML'e dönüştürülmesi sırasında bu stillerin hariç tutulmasını destekler. Bunun için API,[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)Emlak. değerini ayarlama[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) mülkiyet**Doğru** kullanılmayan tüm stilleri HTML çıktısından hariç tutacaktır.

Aşağıdaki ekran görüntüsü, değeri ayarlanarak kaldırılacak olan HTML dosyasındaki kullanılmayan stilleri gösterir.[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) mülkiyet**Doğru**.

![yapılacaklar:resim_alternatif_metin](HtmlSaveOptions-Exclude-Unused-Styles.png)

Aşağıdaki örnek kod, Excel'den HTML'e dönüştürme sırasında kullanılmayan stillerin kaldırılmasını gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
