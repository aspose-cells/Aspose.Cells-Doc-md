---
title: Excel den HTML ye Dönüşüm Sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel dosyası birçok kullanılmayan stili içerebilir. Excel dosyasını HTML formatına dönüştürdüğünüzde, bu kullanılmayan stiller de dışa aktarılır. Bu HTML'nin boyutunu artırabilir. Kullanılmayan stilleri HTML'ye dönüştürme sırasında dışarıda bırakmak için [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) özelliğini true olarak ayarladığınızda, tüm kullanılmayan stiller çıktı HTML'den dışarıda bırakılır. Aşağıdaki ekran görüntüsü, çıktı HTML içindeki bir örnek kullanılmayan stili gösterir.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.**

Aşağıdaki örnek kod bir çalışma kitabı oluşturur ve kullanılmayan bir adlandırılmış stili oluşturur. [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles), **true** olarak ayarlandığından, bu kullanılmayan adlandırılmış stil [çıktı HTML](61767778.zip) içine aktarılmayacaktır. Ancak **false** olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunur ve yukarıdaki ekran görüntüsünde HTML işaretlemede görebilirsiniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
