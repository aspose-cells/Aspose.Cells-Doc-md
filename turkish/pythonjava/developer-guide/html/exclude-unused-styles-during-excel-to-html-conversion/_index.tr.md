---
title: Excel den HTML ye Dönüşüm Sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.**
Microsoft Excel dosyaları birçok kullanılmayan stili içerebilir. Bu dosyalar HTML biçimine dönüştürüldüğünde, kullanılmayan stiller de dışarı aktarılır. Bu, çıktı HTML'in boyutunun artmasına neden olur. Aspose.Cells for Python via Java, Excel dosyasının HTML'e dönüştürülmesi sırasında bu stilleri hariç tutmayı destekler. Bunun için API, [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) özelliğini sağlar. [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) özelliğinin değerini **True** olarak ayarlamak kullanılmayan tüm stilleri çıktı HTML'den hariç tutar.

Aşağıdaki ekran görüntüsü, [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) özelliğinin değerini **True** olarak ayarlayarak kaldırılacak olan HTML dosyasındaki kullanılmayan stilleri gösterir.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Aşağıdaki örnek kod, Excel'den HTML'e dönüşüm sırasında kullanılmayan stilleri kaldırmayı gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
