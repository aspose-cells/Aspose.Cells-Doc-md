---
title: HTML ye Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelleyin
type: docs
weight: 90
url: /tr/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML olarak kaydedebilirsiniz. Ancak, çalışma kitabı gizli çalışma sayfalarını içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini (_files) dizinine dışa aktarır. Bu dizin, çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css gibi dosyalar içerir. Bazı durumlarda, gizli çalışma sayfalarının bu şekilde içeriğinin dışa aktarılması uygun olmayabilir. Örneğin, gizli çalışma sayfası dışa aktarılmaması gereken resimler içeriyorsa.

{{% /alert %}}

Aspose.Cells, [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) özelliğini sağlar. Varsayılan olarak, [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) özelliği **true** olarak ayarlanmıştır. Eğer **false** olarak ayarlarsanız, o zaman Aspose.Cells gizli çalışma sayfası içeriğini dışa aktarmaz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Gizli çalışma sayfalarını dışa aktarılıp dışa aktarılmayacağını kontrol etmenin yanı sıra, çalışma kitabını HTML'ye dışa aktarmak için ek ayarlamaları da yapılabilmektedir. Aşağıdaki makaleler, Aspose.Cells tarafından çalışma kitaplarını HTML'ye dışa aktarmak için desteklenen diğer özellikleri göstermektedir.

- [Başlıkları İle Excel'i HTML'e Dönüştürme](/cells/tr/java/convert-excel-to-html-with-headings/)
- [Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.](/cells/tr/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar](/cells/tr/java/export-comments-while-saving-excel-file-to-html/)
- [Web Tarayıcıları tarafından desteklenmeyen Birleşik Stil'in benzerini dışa aktar](/cells/tr/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle](/cells/tr/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
{{< app/cells/assistant language="java" >}}
