---
title: XLSX Dosyasını JavaScript ile C++ kullanarak PDF Formatına dönüştürün
linktitle: XLSX Dosyasını PDF Biçimine Dönüştür
type: docs
weight: 30
url: /tr/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: Bu kılavuz, bir Excel dosyasını (XLSX) PDF formatına nasıl dönüştüreceğinizi anlatır Aspose.Cells for JavaScript ile C++ kullanarak. 
---

{{% alert color="primary" %}}

PDF (Taşınabilir Belge Biçimi), bu belgeleri oluşturmak için kullanılan yazılım, donanım ve işletim sisteminden bağımsız olarak belgeleri temsil eder. Bir PDF dosyası, aygıt bağımsız ve çözünürlük bağımsız bir şekilde metin, grafik ve resimlerin herhangi bir kombinasyonunu içerebilir. PDF dosyaları genellikle sıkıştırılır, bu nedenle orijinal dosyadan daha az yer kaplar.

Bazen, bir Microsoft Excel dosyasını PDF'ye dönüştürmeniz gerekir. Bunun için, hızlı, güvenli, doğru ve güvenilir bir çözüm gerekir ki, PDF belgelerini dünya genelinde dağıtabilesiniz. Bu görevi gerçekleştirebilecek birçok dönüşüm aracı vardır. Ancak, orijinal Excel belgesinin düzeninin çıktı PDF dosyasında korunması önemlidir. Resimler, grafikler, şekiller, veri biçimlendirmeleri, fontlar, özellikler, renkler, sayfa ayarları, metin yönü, sınırlar, grafikler vb. doğru ve kesin şekilde gösterilmelidir. [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) yüksek doğrulukta dönüşüm sağlar.

Bu belge, bir Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme vb.) PDF'ye nasıl dönüştürülebileceğine dair kapsamlı bir anlayış sağlamayı amaçlamaktadır. Bu amaçla, Aspose.Cells API kullanarak Excel dosyasını PDF'ye dönüştüren basit bir komut satırı uygulaması nasıl oluşturulacağı gösterilmektedir. Dönüşüm yüksek hassasiyet ve doğruluk ile gerçekleştirilir.

{{% /alert %}}

## **Excel'i PDF'ye Dönüştürme**

Bu örnekte, şablon olarak bir Excel dosyası (SampleInput.xlsx) kullanılmıştır. Çalışma kitabında grafikler ve resimler bulunan çalışma sayfaları bulunmaktadır. Her çalışma sayfası, fontlar, özellikler, renkler, gölgeleme efektleri ve kenarlıklar kullanılarak farklı biçimlendirme türleri içermektedir. İlk çalışma sayfasında bir sütun grafiği ve son sayfada bir resim bulunmaktadır.

### **Şablon Excel Dosyası**

Şablon dosyasında grafikler ve medya olarak resimler içeren üç çalışma sayfası bulunmaktadır. İlk çalışma sayfasında grafikler, son sayfada ise aşağıdaki ekran görüntülerinde gösterildiği gibi bir resim yer alır.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|

### **Dönüşüm Süreci**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) metodunu çağırmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerler gösterilir.

{{% /alert %}}

### **Sonuç**

Yukarıdaki kod çalıştırıldığında, bir PDF dosyası uygulama dizinindeki Dosyalar klasöründe oluşturulur.
Aşağıdaki ekran görüntüleri, PDF sayfalarını göstermektedir. Başlık ve altbilgilerin çıktı PDF dosyasında da korunduğuna dikkat edin.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|
