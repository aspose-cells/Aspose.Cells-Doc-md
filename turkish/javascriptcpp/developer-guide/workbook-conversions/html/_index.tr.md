---
title: HTML JavaScript ile C++ kullanımı
linktitle: HTML
type: docs
weight: 230
url: /tr/javascript-cpp/convert-excel-to-html/
---

## **Excel Çalışma Kitabını HTML'ye Dönüştürme**
Aspose.Cells API, elektronik tabloyu HTML formatına aktarmayı destekler. Bu amaçla, Aspose.Cells [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) sınıfını kullanarak çıktı HTML'sinin çeşitli yönlerini kontrol etme esnekliği sağlar.

 Aşağıdaki kod örneği, JavaScript ve C++ kullanarak bir çalışma kitabını HTML dosyası olarak kaydetmeyi gösterir:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **Excel Çalışma Kitabını MHTML Dosyalarına Dönüştürme**
MHTML, normal HTML'yi dış kaynaklar (örneğin, içerik bağlanan resimler, animasyonlar, sesler vb.) ile birleştirir ve tek bir dosyada tutar. .mht dosya uzantısına sahip e-postalar için kullanılır. Aspose.Cells, MHTML dosyalarını okuma ve yazmayı destekler.

 Aşağıdaki kod örneği, JavaScript ve C++ kullanarak çalışma kitabını MHTML dosyası olarak kaydetmeyi gösterir:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma](/cells/tr/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [HTML'den İçe Aktarırken Büyük Sayıların Üstel Görünümünü Engelle](/cells/tr/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [HTML Bağlantı Hedef Türünü Değiştirme](/cells/tr/javascript-cpp/change-the-html-link-target-type/)
- [Excel'i HTML'e dönüştür ve açıklama metni ekleyin](/cells/tr/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/tr/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [HTML içe aktarırken satır sonrası gereksiz boşlukları silin](/cells/tr/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [HTML'ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak](/cells/tr/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Çerçeve Betiklerini ve Belge Özelliklerini Dışa Aktarmayı Devre Dışı Bırak](/cells/tr/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel'den HTML'ye - Daha İyi Düzen için PresentationPreference Seçeneğini Kullan](/cells/tr/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.](/cells/tr/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel dosyasını HTML'e dönüştüren aşağıdaki örnek kod. Bu ekran görüntüsü, örnek Excel dosyasının Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.](/cells/tr/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Excel'den HTML'ye Databar, ColorScale ve IconSet Koşullu Biçimlendirmeyi Dışa Aktar](/cells/tr/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar](/cells/tr/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Excel'de belge çalışma kitabı ve çalışma sayfası özelliklerini HTML dönüşümünde dışa aktar](/cells/tr/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Excel'den HTML'e Grid Çizgileri ile Dışa Aktar](/cells/tr/javascript-cpp/export-excel-to-html-with-gridlines/)
- [HTML'e Baskı Alanı Aralığını Dışa Aktar](/cells/tr/javascript-cpp/export-print-area-range-to/)
- [CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle](/cells/tr/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma](/cells/tr/javascript-cpp/export-worksheet-css-separately-in-output/)
- [Web Tarayıcıları tarafından desteklenmeyen Birleşik Stil'in benzerini dışa aktar](/cells/tr/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek](/cells/tr/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [HTML'ye Kaydetme İşlemi Sırasında Gizli Çalışsayfa İçeriğinin Dışa Aktarılmasını Engelle](/cells/tr/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [HTML'e kaydetme sırasında dışa aktarılan çalışma sayfası html dosyası yolunu IFilePathProvider arabirimi vasıtasıyla sağlar](/cells/tr/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Kendini Kapatan Etiketleri Tanı](/cells/tr/javascript-cpp/recognise-self-closing-tags/)
- [Yayılan Elemanın Düzgünleşmiş Doldurmasını, Çalışma Kitaplarını HTML'e Dönüştürürken Renderle](/cells/tr/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Kolon genişliğini em veya yüzde gibi ölçeklenebilir birim olarak ayarlayın](/cells/tr/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [HTML olarak elektronik tabloyu oluştururken varsayılan yazı tipini ayarlayın](/cells/tr/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin](/cells/tr/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [HTML'nin Excel elektronik tablosuna yüklenmesi sırasında DIV etiketlerinin düzenini destekle](/cells/tr/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [ HTML'ye Kaydederken CSS Özel Özelliklerini Etkinleştir](/cells/tr/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)
