---
title: JavaScript ile Çalışma Kitabı Yapısını Koruma ve Koruma Kaldırma C++ ile
linktitle: Çalışma Kitabı Yapısını Koruma Altına Alma ve Korumasız Yapma
type: docs
weight: 40
url: /tr/javascript-cpp/protect-and-unprotect-workbook-structure/
description: JavaScript kullanarak C++ ile Excel dosyalarının çalışma kitabı yapısını koruma ve koruma kaldırma.
---


{{% alert color="primary" %}}  
Diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, çalışma sayfalarını ekleme, taşıma, silme veya gizleme işlemlerini yapmalarını engellemek ve çalışma sayfalarını yeniden adlandırmak için Excel çalışma kitabınızın yapısını bir şifre ile koruyabilirsiniz.  
{{% /alert %}}  


## **MS Excel'de Çalışma Kitabı Yapısını Koruma ve Kaldırma**  

**![çalışma kitabı yapısını koruma ve kaldırma](protect-and-unprotect-workbook-structure.png)**  

1. Tıklayın **İncele > Çalışma Kitabını Koru**.  
1. **Şifre kutusuna** bir şifre girin.  
1. **Tamam**'ı seçin, şifreyi teyit etmek için tekrar girin, ardından tekrar **Tamam**'ı seçin.  


## **Aspose.Cells for JavaScript kullanarak Çalışma Kitabı Yapısını C++ ile Koruyun**  
Excel dosyalarının çalışma sayfasını korumak için sadece aşağıdaki basit kod satırlarına ihtiyaç vardır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Protect workbook structure with a password
            workbook.protect(ProtectionType.Structure, "password");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1_protected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Aspose.Cells for JavaScript kullanarak Çalışma Kitabı Yapısını C++ ile Korumayı kaldırın**  
Aspose.Cells API ile çalışma kitabı yapısını korumak kolaydır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Unprotect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            workbook.unprotect("password");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/(\.xlsx|\.xls|\.csv)$/i, '');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook structure unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Not: Doğru bir şifre gerekli.  
{{% /alert %}}
