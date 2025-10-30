---
title: JavaScript kullanarak C++ ile Çalışma Sayfasını Koruma ve Koruma Kaldırma
linktitle: Çalışma Sayfasını Koruma ve Kaldırma
type: docs
weight: 40
url: /tr/javascript-cpp/protect-and-unprotect-worksheets/
description: Aspose.Cells for JavaScript kullanarak Excel dosyalarının çalışma sayfasını C++ ile koruyun ve koruma kaldırın.
---

{{% alert color="primary" %}}  
Excel çalışma sayfanızdaki verilerin yanlışlıkla veya kasıtlı olarak değişmesini, taşınmasını veya silinmesini engellemek için hücreleri kilitleyebilir ve sayfayı bir şifre ile koruyabilirsiniz.  
{{% /alert %}}  

## **MS Excel'de Çalışma Sayfasını Koruma ve Kaldırma**  

**![çalışma sayfasını koruma ve kaldırma](protect-and-unprotect-worksheet.png)**  

1. Tıklayın **İncele > Sayfayı Koru**.  
1. **Şifre kutusuna** bir şifre girin.  
1. **izin ver** seçeneklerini seçin.  
1. **Tamam**'ı seçin, şifreyi teyit etmek için tekrar girin, ardından tekrar **Tamam**'ı seçin.  

## **Aspose.Cells for JavaScript kullanarak C++ ile Çalışma Sayfasını Koruyun**  
Excel dosyalarının çalışma sayfasını korumak için sadece aşağıdaki basit kod satırlarına ihtiyaç vardır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Aspose.Cells for JavaScript kullanarak C++ ile Çalışma Sayfasını Korumayı kaldırın**  
Sayfa korumasını kaldırmak Aspose.Cells API ile kolaydır. Eğer sayfa parola korumalıysa, doğru parola gereklidir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Gelişmiş Konular**  
- [Excel XP’den bu yana Gelişmiş Koruma Ayarları](/cells/tr/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Çalışma Sayfasının Şifre Korunup Korunmadığını Algılama](/cells/tr/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Çalışma Sayfalarını Koruma](/cells/tr/javascript-cpp/protecting-worksheets/)  
- [Bir Çalışma Sayfasını Korumayı Kaldırma](/cells/tr/javascript-cpp/unprotect-a-worksheet/)  
- [Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulama](/cells/tr/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
