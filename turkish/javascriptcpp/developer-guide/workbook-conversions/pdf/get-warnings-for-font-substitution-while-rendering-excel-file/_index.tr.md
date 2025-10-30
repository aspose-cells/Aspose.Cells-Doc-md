---
title: Excel dosyasını PDF ye dönüştürürken Font Değiştirme Uyarılarını alma
linktitle: Excel Dosyasını Rendelerken Yazı Tiplerinin Yerine Kullanılacak Uyarıları Alma
type: docs
weight: 230
url: /tr/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: C++ kullanarak Excel dosyalarını PDF ye dönüştürürken font değiştirme uyarılarını nasıl alacağınızı öğrenin.
---

{{% alert color="primary" %}}  

Bazen, bir Microsoft Excel dosyasını PDF'e render ederken, Aspose.Cells fontları değiştirir. Aspose.Cells, geliştiricilerin hangi belirli fontun değiştirildiğini bildiren bir uyarı ile ilgili bir özellik sağlar. Bu, bir Aspose.Cells tarafından render edilmiş PDF'nin orijinal Microsoft Excel dosyasından farklı görünmesinin nedenini belirlemenize ve uygun işlemleri almanıza yardımcı olabilecek faydalı bir özelliktir. Örneğin, eksik fontları yükleyerek render sonuçlarının aynı görünmesini sağlamak gibi.

{{% /alert %}}  

Excel dosyasını PDF’ye dönüştürürken yazı tipi değişimini uyarıları almak için, IWarningCallback arayüzünü uygulayın ve PdfSaveOptions.warningCallback özelliğini sizin uyguladığınız arayüz ile ayarlayın.

Aşağıdaki ekran görüntüsü, aşağıdaki kodda kullanacağımız kaynak Excel dosyasını göstermektedir. A6 ve A7 hücrelerinde, Microsoft Excel tarafından düzgün bir şekilde render edilmeyen fontlarda bazı metinler bulunmaktadır.

|**Tüm fontlar düzgün bir şekilde render edilmiyor**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells, A6 ve A7 hücrelerindeki yazı tiplerini aşağıda gösterildiği gibi uygun yazı tipleriyle değiştirecektir.

|**Değiştirilen fontlar**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Kaynak Dosya ve Çıktı PDF'sini İndir**  
Kaynak Excel dosyasını ve çıktı PDF'sini aşağıdaki bağlantılardan indirebilirsiniz

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Kod**  
Aşağıdaki kod, IWarningCallback’i uygular ve PdfSaveOptions.warningCallback özelliğine uygulanan arayüzü atar. Artık bir hücrede herhangi bir font değiştirildiğinde, Aspose.Cells bir uyarı tetikler ve WarningCallback.Warning() metodunu çağırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **Çıktı**  
Kaynak Excel dosyasının PDF olarak dönüştürülmesinden sonra uyarılar şu şekilde hata ayıklama konsoluna çıktı verilir:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF formatına dönüştürmeden hemen önce Workbook.calculateFormula metodunu çağırmak en iyisidir. Bu sayede formül bağımlı değerler tekrar hesaplanacak ve PDF'de doğru değerler görüntülenecektir.

{{% /alert %}}
