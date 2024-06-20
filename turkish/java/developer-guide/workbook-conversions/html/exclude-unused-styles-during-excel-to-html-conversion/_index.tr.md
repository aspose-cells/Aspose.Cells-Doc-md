---
title: Excel den HTML ye Dönüşüm Sırasında Kullanılmayan Stilleri Hariç Tut
type: docs
weight: 30
url: /tr/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel dosyası çok sayıda kullanılmayan stili içerebilir. Excel dosyasını HTML formatına dışa aktardığınızda, bu kullanılmayan stiller de dışa aktarılır. Bu HTML'nin boyutunu artırabilir. HTML'ye dönüştürme sırasında kullanılmayan stilleri hariç tutabilirsiniz. Bunun için [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) özelliğini kullanarak dışa aktarım sırasında tüm kullanılmayan stilleri hariç tutabilirsiniz. Bu özelliği **true** olarak ayarladığınızda, tüm kullanılmayan stiller çıktı HTML'den hariç tutulur. Aşağıdaki ekran görüntüsü, çıktı HTML içinde örnek bir kullanılmayan stilin nasıl göründüğünü göstermektedir.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.**

Aşağıdaki örnek kod bir çalışma kitabı oluşturur ve kullanılmayan adlandırılmış bir stili oluşturur. [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) **true** olarak ayarlandığı için bu kullanılmayan adlandırılmış stil, [çıktı HTML'sine](61767781.zip) dışa aktarılmayacaktır. Ancak **false** olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme olarak görünecektir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
