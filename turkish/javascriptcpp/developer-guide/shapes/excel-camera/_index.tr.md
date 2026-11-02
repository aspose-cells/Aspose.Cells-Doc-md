---
title: Aspose.Cells for JavaScript via C++ ile Excel Kamera
linktitle: Aspose.Cells for JavaScript via C++ ile Excel Kamera
description: Excel Kamera'yı Aspose.Cells for JavaScript via C++ ile kullanarak bir hücre aralığına bağlı, kaynak verileri değiştiğinde yenilenen ve kaynak alanının tüm biçimlendirmesini koruyan dinamik bir resim oluşturmayı öğrenin.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Excel Camera, dinamik resim, bağlı resim, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /tr/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Kamera, bir hücre aralığının canlı görüntüsünü oluşturan ve sıradan bir resim gibi çizim katmanında yer alan bir çalışma sayfası nesnesidir. Aspose.Cells iki oluşturma modunu destekler: kaynak verileri değiştiğinde otomatik olarak yenilenen dinamik bir resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan statik bir resim. Bu makale, düzeninize uygun yaklaşımı seçebilmeniz için her iki yaklaşımı da ele alır.

## Excel Kamera Nedir?
Excel Kamera, esas olarak çalışma sayfasının çizim katmanında belirli bir satıra ve sütuna sabitlenmiş bir resim nesnesidir. Sıradan bir eklenmiş resimden farklı olarak Kamera, `"A1:F10"` gibi bir A1 stili formül aracılığıyla bir kaynak aralığa bağlıdır. Bu aralıktaki hücrelerden herhangi biri değiştiğinde Kamera'nın görüntüsü, yeni içeriği yansıtacak şekilde otomatik olarak yenilenir. Kamera, kaynak alanın tüm biçimlendirmesini — kenarlıkları, arka plan renklerini, yazı tiplerini ve sayı biçimlerini — korur; böylece hücrelerde görünen her şey Kamera'nın görüntüsünde de yer alır. Bu özellik; verileri tekrarlamadan veya kaydırmadan ayrı bir bölgenin görünür önizlemesini istediğiniz panolar, özetler, yan paneller ve rapor düzenleri için özellikle yararlıdır. İki noktaya dikkat edilmelidir: çalışma kitabını kaydetmeden önce `updateSelectedValue()` çağrılmalıdır ve dosya HTML veya PDF olarak dışa aktarılmalıdır. Bu biçimler, canlı yeniden hesaplama yerine gömülü resim verisine dayanır.

## Yöntem 1 — Dinamik Kamera Resmi Ekleme
Dinamik Kamera en yaygın yaklaşımdır ve Excel'in yerleşik Kamera aracının işleyişini en iyi yansıtır. Başlangıçta resim içeriği olmayan bir resim eklenir; ardından bu resme kaynak aralığını başvuran bir `formula` atanır. `formula` atandıktan sonra `updateSelectedValue()` çağrısı gömülü resim verisini yeniler ve bu veriyi referans verilen kaynak hücrelerle güncel tutar. Kamera, ayrı bir sınıf aracılığıyla uygulanmaz; tamamen standart `Picture` türü üzerine kuruludur.
Kullanılan temel API'ler şunlardır:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — belirtilen satır ve sütuna sabitlenmiş bir resim ekler. `image` parametresine `null` geçirilmesi, dinamik bir Kamera için yer tutucu işlevi gören boş bir resim oluşturur. Metot, yeni resmin dizinini döndürür.
- `worksheet.getPictures().get(index)` — koleksiyondaki belirli bir `Picture` nesnesini alır.
- `picture.formula` — Kamera'nın yansıttığı kaynak aralığın A1 stili başvurusunu tutan bir dize özelliği; örneğin `"A1:F10"`.
- `picture.updateSelectedValue()` — `formula` ile başvurulan hücrelerden gömülü resim verisini yenileyen `void` türünde bir metot.

{{% alert color="primary" %}}
`updateSelectedValue()`, çıktı biçimi HTML veya PDF olduğunda kaydetmeden önce MUTLAKA çağrılmalıdır; aksi halde dışa aktarılan dosya resim verisini içermez ve Kamera oluşturulan çıktıda boş görünür.
Aşağıdaki kod bir çalışma kitabı oluşturur, 10. satır ve 6. sütuna sabitlenmiş boş bir resim ekler, onu `formula` özelliğiyle `A1:F10` kaynak aralığına bağlar, gömülü resim verisini yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Dinamik Kamera: boş bir resim ekle, Formula ile A1:F10 aralığına bağla, ardından yenile
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Yöntem 2 — Statik Kamera Resmi Ekleme
Statik Kamera, esas olarak bir hücre aralığının tek seferlik işlenmiş önizlemesidir. Canlı bir bağlantıyı sürdürmek yerine, aralık bir kez resim baytlarına işlenir; bu baytlar bir `Buffer` içine sarılır ve normal bir resim olarak eklenir. Görüntü içeriği oluşturma anında sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Kullanılan temel API'ler şunlardır:
- `cells.createRange(address)` — `"A1:F10"` gibi bir A1 stili adresten `Range` nesnesi oluşturur.
- `range.toImage(options)` — aralığı resim baytlarına işler. `null` geçirilmesi varsayılan işleme seçeneklerini kullanır; çıktıyı daha ayrıntılı denetlemek için aşırı yüklemeler bulunur.
- `Buffer.from(imageBytes)` — işlenmiş resim baytlarını, `worksheet.getPictures().add` çağrısına aktarılabilecek bir `Buffer` içine sarar.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — resmi belirtilen satır ve sütuna sabitler; bu kez işleme sonucunda oluşturulan `Buffer` nesnesi geçirilir.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, `range.toImage(null)` aracılığıyla onu resim baytlarına işler, baytları bir `Buffer` içine sarar, resmi 10. satır ve 6. sütuna sabitler ve çalışma kitabını kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Statik Kamera: Range oluştur, baytlara dönüştür, MemoryStream içine sar, resim olarak ekle
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Dinamik ve Statik Arasında Seçim Yapma
- **Dinamik Kamera:** Her yeniden hesaplamada güncellenir, `updateSelectedValue()` çağrısından sonra HTML ve PDF biçimlerinde dışa aktarılmayı destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Kamera:** Hiç güncellenmeyen tek seferlik bir işlemedir; canlı bir veri aynası yerine derleme zamanında gömülen sabit bir görsel anlık görüntü istediğinizde yararlıdır.
Aspose.Cells, `picture.formula` ve `updateSelectedValue()` kullanılarak oluşturulan dinamik ve otomatik yenilenen Kamera ile `range.toImage` ve `Buffer` kullanılarak oluşturulan statik ve tek seferlik Kamera yaklaşımlarını destekler. Çıktınızın kaynak hücrelerle eşitlenmesi gerekiyorsa dinamik yaklaşımı; yalnızca derleme zamanında sabit bir görsel anlık görüntüye ihtiyaç duyuyorsanız statik yaklaşımı seçin.

## İlgili Makaleler
- [Sparkline'ı Aspose.Cells for JavaScript via C++ ile Görüntüye ve HTML'ye Dönüştür](/cells/tr/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Aspose.Cells for JavaScript via C++ ile Özet Tablosuna Filtre Alanları Ekle](/cells/tr/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ ile Özet Tablolarına Biçimler Uygula](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}