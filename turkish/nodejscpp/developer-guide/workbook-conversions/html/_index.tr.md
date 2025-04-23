---
title: HTML ile Node.js kullanarak C++
linktitle: HTML
type: docs
weight: 230
url: /tr/nodejs-cpp/convert-excel-to-html/
---

## **Excel Çalışma Kitabını HTML'ye Dönüştürme**
Aspose.Cells API, elektronik tabloyu HTML formatına aktarmayı destekler. Bu amaçla, Aspose.Cells [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) sınıfını kullanarak çıktı HTML'sinin çeşitli yönlerini kontrol etme esnekliği sağlar.

Aşağıdaki kod örneği, Node.js kullanarak bir çalışma kitabını HTML dosyası olarak kaydetmeyi göstermektedir:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **Excel Çalışma Kitabını MHTML Dosyalarına Dönüştürme**
MHTML, normal HTML'yi dış kaynaklar (örneğin, içerik bağlanan resimler, animasyonlar, sesler vb.) ile birleştirir ve tek bir dosyada tutar. .mht dosya uzantısına sahip e-postalar için kullanılır. Aspose.Cells, MHTML dosyalarını okuma ve yazmayı destekler.

Aşağıdaki kod örneği, Node.js kullanarak bir çalışma kitabını MHTML dosyası olarak kaydetmeyi göstermektedir.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **Gelişmiş Konular**
- [HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma](/cells/tr/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [HTML'den İçe Aktarırken Büyük Sayıların Üstel Görünümünü Engelle](/cells/tr/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [HTML Bağlantı Hedef Türünü Değiştirme](/cells/tr/nodejs-cpp/change-the-html-link-target-type/)
- [Excel'i HTML'e dönüştür ve açıklama metni ekleyin](/cells/tr/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/tr/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [HTML içe aktarırken satır sonrası gereksiz boşlukları silin](/cells/tr/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [HTML'ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak](/cells/tr/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Çerçeve Betiklerini ve Belge Özelliklerini Dışa Aktarmayı Devre Dışı Bırak](/cells/tr/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel'den HTML'ye - Daha İyi Düzen için PresentationPreference Seçeneğini Kullan](/cells/tr/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.](/cells/tr/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel dosyasını HTML'e dönüştüren aşağıdaki örnek kod. Bu ekran görüntüsü, örnek Excel dosyasının Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.](/cells/tr/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Excel'den HTML'ye Databar, ColorScale ve IconSet Koşullu Biçimlendirmeyi Dışa Aktar](/cells/tr/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar](/cells/tr/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Excel'de belge çalışma kitabı ve çalışma sayfası özelliklerini HTML dönüşümünde dışa aktar](/cells/tr/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Excel'den HTML'e Grid Çizgileri ile Dışa Aktar](/cells/tr/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [HTML'e Baskı Alanı Aralığını Dışa Aktar](/cells/tr/nodejs-cpp/export-print-area-range-to/)
- [CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle](/cells/tr/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma](/cells/tr/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Web Tarayıcıları tarafından desteklenmeyen Birleşik Stil'in benzerini dışa aktar](/cells/tr/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek](/cells/tr/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [HTML'ye Kaydetme İşlemi Sırasında Gizli Çalışsayfa İçeriğinin Dışa Aktarılmasını Engelle](/cells/tr/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [HTML'e kaydetme sırasında dışa aktarılan çalışma sayfası html dosyası yolunu IFilePathProvider arabirimi vasıtasıyla sağlar](/cells/tr/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Kendini Kapatan Etiketleri Tanı](/cells/tr/nodejs-cpp/recognise-self-closing-tags/)
- [Yayılan Elemanın Düzgünleşmiş Doldurmasını, Çalışma Kitaplarını HTML'e Dönüştürürken Renderle](/cells/tr/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Kolon genişliğini em veya yüzde gibi ölçeklenebilir birim olarak ayarlayın](/cells/tr/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [HTML olarak elektronik tabloyu oluştururken varsayılan yazı tipini ayarlayın](/cells/tr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin](/cells/tr/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [HTML'nin Excel elektronik tablosuna yüklenmesi sırasında DIV etiketlerinin düzenini destekle](/cells/tr/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [ HTML'ye Kaydederken CSS Özel Özelliklerini Etkinleştir](/cells/tr/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
