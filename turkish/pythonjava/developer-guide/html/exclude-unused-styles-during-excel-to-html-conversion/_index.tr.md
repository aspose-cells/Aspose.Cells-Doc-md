---
title: Excel'den HTML'ye dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Excel'den HTML'ye dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut**
Microsoft Excel dosyaları kullanılmayan birçok stil içerebilir. Bu dosyalar HTML formatına aktarıldığında, kullanılmayan stiller de dışa aktarılır. Bu, çıktı HTML'sinin boyutunun artmasıyla sonuçlanır. Aspose.Cells for Python via Java, Excel dosyasının HTML'ye dönüştürülmesi sırasında bu stillerin hariç tutulmasını destekler. Bunun için API,[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)Emlak. değerini ayarlama[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) mülkiyet**Doğru** kullanılmayan tüm stilleri çıktı HTML'sinden hariç tutacaktır.

Aşağıdaki ekran görüntüsü, HTML dosyasında değeri ayarlanarak kaldırılacak kullanılmayan stilleri gösterir.[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) mülkiyet**Doğru**.

![yapılacaklar:resim_alternatif_Metin](HtmlSaveOptions-Exclude-Unused-Styles.png)

Aşağıdaki örnek kod, Excel'den HTML'ye dönüştürme sırasında kullanılmayan stillerin kaldırılmasını gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
