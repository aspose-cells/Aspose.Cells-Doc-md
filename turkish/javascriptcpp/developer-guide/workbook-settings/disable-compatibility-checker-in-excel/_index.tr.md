---
title: Excel de Uyumluluk Denetleyicisini C++ ile JavaScript sayesinde Devre Dışı Bırak
linktitle: Excel de Uyumluluk Denetimini Devre Dışı Bırakma
type: docs
weight: 170
url: /tr/javascript-cpp/disable-compatibility-checker-in-excel/
description: C++ API üzerinden Aspose.Cells for JavaScript kullanarak uyumluluk denetleyicisini nasıl devre dışı bırakacağınızı öğrenin.
keywords: JavaScript ile Uygula, Excel de Uyumluluk Denetleyicisini JavaScript ile C++ üzerinden Devre Dışı Bırak, Çalışma Kitabında Uyumluluk Denetleyicisini Devre Dışı Bırak.
---

## Excel Çalışma Sayfalarında Uyumluluk Denetleyicisini JavaScript ile Devre Dışı Bırakma  

{{% alert color="primary" %}}  
Microsoft Excel'in Uyumluluk Denetçisi, bir dosyayı önceki bir dosya biçiminde kaydedildiğinde işlevsellik sorunlarına veya sadelik kaybına neden olabilecek özellikleri tespit eder. Uyumluluk Denetçisi, Microsoft Office Excel 2007 ve Microsoft Excel 2010'un bir özelliğidir.  

Excel 2007 veya 2003'ten Excel 2007 veya 2010'a kaydederken, Uyumluluk Denetçisi, daha önceki sürüm tarafından desteklenmeyen özellikleri içeren bir dosya olup olmadığını kontrol etmek için çalışma kitabını tarar. Uyumluluk sorunları hakkında kararlar vermenize yardımcı olmak için, Uyumluluk Denetçisi, seçenekleri içeren iletişim kutuları görüntüler. Ayrıca, çalışma kitabındaki herhangi bir sorun hakkında bir rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.  

Bazen, belirli bir elektronik tablo için Uyumluluk Denetleyicisini devre dışı bırakmanız gerekebilir. Aspose.Cells API'leri ile bunu programlı olarak yapabilirsiniz, böylece kullanıcılar manuel olarak Microsoft Excel'de dosyayı yeniden kaydettiklerinde Uyumluluk Denetleyicisi ileti kutusu nedeniyle hayal kırıklığı yaşamaz veya karışıklık yaşamazlar.  
{{% /alert %}}  

## **Microsoft Excel'de Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**  

Microsoft Excel'de Uyumluluk Denetçisini devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):  

- (Excel 2007) Office düğmesine tıklayın, **Hazırla**'yı tıklayın, ardından **Uyumluluk Denetleyicisini Çalıştır**'ı tıklayın ve **Bu çalışma kitabını kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.  
- (Excel 2010) Dosya sekmesine tıklayın, sonra **Bilgi**'ye tıklayın, **Sorunları kontrol et**'i tıklayın, **Uyumluluğu Kontrol Et**'i tıklayın ve son olarak **Bu çalışbook'u kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.  

## **Aspose.Cells API'ları kullanarak Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**  

Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) özelliğini **false** olarak ayarlayın.  

### **Kod Örnekleri**  

Aşağıdaki kod örnekleri, C++ ile Aspose.Cells for JavaScript kullanarak Uyumluluk Denetleyicisini nasıl devre dışı bırakacağınızı gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
