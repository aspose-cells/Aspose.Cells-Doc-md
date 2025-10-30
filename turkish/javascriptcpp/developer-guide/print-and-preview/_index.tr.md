---
title: C++ aracılığıyla JavaScript ile önizleme çalışma kitabı
linktitle: Çalışma kitabını önizle 
type: docs
weight: 70
url: /tr/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells, JavaScript ve C++ kullanarak Microsoft Excel kurulumu olmadan Excel dosyalarını yazdırmayı ve önizlemeyi destekler.
---

## **Yazdırma Önizlemesi**  

Milyonlarca sayfaya sahip Excel dosyalarının PDF veya resimlere dönüştürülmesi gereken durumlar olabilir. Bu tür dosyaları işlemek çok zaman ve kaynak tüketir. Bu durumda, Çalışma Kitabı ve Çalışma Sayfası Yazdırma Önizleme özelliği faydalı olabilir. Bu dosyaları dönüştürmeden önce toplam sayfa sayısını kontrol ederek dosyanın dönüştürülüp dönüştürülmeyeceğine karar verebilir. Bu makale, toplam sayfa sayısını öğrenmek için [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) sınıflarının kullanılmasına odaklanır.  

Aspose.Cells, yazdırma önizleme özelliği sağlar. API, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) sınıflarını içerir. Tüm çalışma kitabının yazdırma önizlemesini oluşturmak için, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) sınıfından bir örnek oluşturun ve yapıcıya [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) nesnelerini geçirin. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) sınıfı, oluşturulan önizlemedeki sayfa sayısını döndüren bir [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) metot sağlar. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) sınıfına benzer şekilde, [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) sınıfı belirli bir çalışma sayfası için yazdırma önizlemesi oluşturmak için kullanılır. Bir çalışma sayfasının yazdırma önizlemesini oluşturmak için [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) sınıfından bir örnek oluşturun ve yapıcıya [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) nesnelerini geçirin. [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) sınıfı ayrıca, oluşturulan önizlemede sayfa sayısını döndüren [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) metodunu sağlar.  

Aşağıdaki kod parçacığı, [örnek excel dosyası](94896177.xlsx) kullanılarak hem [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) hem de [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) sınıflarının kullanımını gösterir.  

### **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

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

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

Yukarıdaki kodun yürütülmesiyle oluşturulan çıktı aşağıdaki gibidir.  

### **Konsol Çıktısı**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Gelişmiş Konular**  
- [Elektronik Tabloları Görüntüleme Yazı Tiplerini Yapılandırma](/cells/tr/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Çalışma Sayfasını Görüntüye Dönüştür - Veri etrafındaki boşlukları kaldır](/cells/tr/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Çalışsayısı veya Sayfa Görseline ve Sayfa Sayfasına Çalışsayısı Dönüştürme](/cells/tr/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [ImageOrPrint Seçenekleri Kullanarak Çalışma Sayfasını Görüntüye Dönüştürme](/cells/tr/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar](/cells/tr/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [ImageOrPrintOptions Kullanarak Çalışma Sayfalarından Resimleri Çıkarma](/cells/tr/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Çalışma Sayfasının Önizlemesini Oluşturun](/cells/tr/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı](/cells/tr/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Sayfa Ayarları ve Yazdırma Seçenekleri](/cells/tr/javascript-cpp/page-setup-and-printing-options/)  
- [Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma](/cells/tr/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Çalışsayısını Grafiksel Ortama Dönüştürme](/cells/tr/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Çalışma Kitabı Rendeleme İçin Bireysel veya Özel Font Kümesini Belirtin](/cells/tr/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
