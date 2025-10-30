---
title: Kullanıcıların Excel Dosyasını Yazdırmasını Nasıl Önlerim JavaScript ile C++ kullanarak
linktitle: Excel Dosyasının Yazdırılmasını Nasıl Engelleriz
type: docs
weight: 600
url: /tr/javascript-cpp/how-to-prevent-printing-excel/
description: Excel dosyalarını yazdırmaktan kullanıcıları nasıl alıkoyacağınızı öğrenin Aspose.Cells for JavaScript kullanarak C++ ile.
keywords: excel yazdırma, excel yazdırmayı engelleme, kullanıcıların excel i yazdırmaması nasıl engellenir, excel yazdırma engelleme, çalışma kitabının yazdırılmasını engelleme, Kullanıcıların VBA ile tam çalışma kitabını yazdırmalarını engelleyin.
---

## **Olası Kullanım Senaryoları**  
Günlük çalışmalarımızda, Excel dosyasında önemli bilgiler olabilir; iç verilerin yayılmasını önlemek için şirketimiz bunların yazdırılmasını engelleyecektir. Bu belge, başkalarının Excel dosyalarını yazdırmasını nasıl engelleyeceğinizi anlatacaktır.  

## **MS-Excel'de Kullanıcıların Dosyayı Yazdırmasını Nasıl Engelleriz**  
Aşağıdaki VBA kodunu kullanarak belirli dosyanızın yazdırılmasını engelleyebilirsiniz.  
1. Başkalarına yazdırmalarına izin vermediğiniz çalışma kitabınızı açın.  
1. Excel şeridinde "Geliştirici" sekmesini seçin ve "Kod Görüntüle" düğmesine tıklayın "Kontroller" bölümünde. Alternatif olarak, Microsoft Visual Basic for Applications penceresini açmak için ALT + F11 tuşlarını basılı tutabilirsiniz.  
<br>  
<img src="1.png" width=70% />  
1. Ardından sol Project Explorer'da, BuÇalışma kitabına çift tıklayın ve modülü açın, birkaç VBA kodu ekleyin.  
<br>  
<img src="2.png" width=70% />  
1. Daha sonra bu kodu kaydedin ve kapatın, tekrar çalışma kitabına dönün ve şimdi örnek dosyayı yazdırmak istediğinizde, yazdırılamayacak ve aşağıdaki uyarı kutusunu alacaksınız:  
<br>  
<img src="3.png" width=70% />  

## ** Aspose.Cells for JavaScript kullanarak kullanıcıların Excel dosyasını yazdırmasını nasıl engellersiniz**  

Aşağıdaki örnek kod, kullanıcıların Excel dosyasını yazdırmasını nasıl engelleyeceğinizi gösterir:  

1. [Örnek dosyayı](örnek.xlsx) yükleyin.  
1. VbaProject özelliğinden VbaModuleCollection nesnesini alın.  
1. "ThisWorkbook" adıyla VbaModule nesnesini alın.  
1. VbaModule'nin kodları özelliğini ayarlayın.  
1. Örnek dosyayı [xlsm biçimine](out.xlsm) kaydedin.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
