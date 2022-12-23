---
title: HTML'e Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelleyin
type: docs
weight: 90
url: /tr/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML'e kaydedebilirsiniz. Ancak çalışma kitabı gizli çalışma sayfaları içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini HTML çıktısına verir (_ dosyalar) çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css, vb. dosyaları içeren dizin. Bazen, gizli çalışma sayfalarının içeriğini bu şekilde dışa aktarmak uygun olmaz. Örneğin, gizli çalışma sayfasında dışa aktarılmaması gereken resimler varsa,_dosyalar dizini.

{{% /alert %}}

Aspose.Cells şunları sağlar:[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) Emlak. varsayılan olarak,[**ExportGizliÇalışma Sayfası**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) özellik şu şekilde ayarlandı:**doğru**. olarak ayarlarsanız**YANLIŞ**, ardından Aspose.Cells gizli çalışma sayfası içeriklerini dışa aktarmaz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Gizli çalışma sayfalarının dışa aktarılıp aktarılmayacağını kontrol etmenin dışında, çalışma kitabını HTML'e vermek için ek ayarlar da yapılandırabilirsiniz. Aşağıdaki makaleler, çalışma kitaplarını HTML'e vermek için Aspose.Cells tarafından desteklenen diğer özellikleri göstermektedir.

- [Excel'i başlıklarla HTML'e dönüştürün](/cells/tr/java/convert-excel-to-html-with-headings/)
- [Excel'den HTML'e dönüştürme sırasında Kullanılmayan Stilleri Hariç Tut](/cells/tr/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel dosyasını HTML'e Kaydederken Yorumları Dışa Aktar](/cells/tr/java/export-comments-while-saving-excel-file-to-html/)
- [HTML'e kaydederken CrossHideRight ile Yer Paylaşımlı İçeriği Gizleme](/cells/tr/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Kenarlık Stili Web Tarayıcıları tarafından desteklenmediğinde benzer Kenarlık Stilini dışa aktarın](/cells/tr/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
