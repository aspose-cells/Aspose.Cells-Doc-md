---
title: JavaScript kullanarak Excel Çalışma Kitabının VBA Projesini Parola ile Koruyun, C++ ile
linktitle: Excel Çalışma Kitabının VBA Projesini Parola Koruması
type: docs
weight: 10
url: /tr/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/
description: Aspose.Cells for JavaScript kullanarak C++ ile bir Excel çalışma kitabının VBA projesini parola koruma altına almayı öğrenin.
---

## **JavaScript kullanarak Excel Çalışma Kitabının VBA Projesini Parola ile Koruyun, C++ ile**

Aspose.Cells for JavaScript kullanarak C++ ile bir çalışma kitabının VBA (Görsel Temel Uygulamaları) Projesini parola ile koruyabilirsiniz [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#protect-boolean-string-) yöntemiyle.  

## **Örnek Kod**  

Aşağıdaki örnek kod, [örnek Excel dosyasını](43352067.xlsm) yükler, VBA Projesine erişir ve ona parola ile korur. Son olarak, [çıktı Excel dosyasına](43352068.xlsm) kaydeder.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Protect VBA Project Example</title>
    </head>
    <body>
        <h1>Protect VBA Project Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Protect VBA Project</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the VBA project of the workbook (converted getter to property)
            const vbaProject = workbook.vbaProject;

            // Lock the VBA project for viewing with password
            vbaProject.protect(true, "11");

            // Save the output Excel file (as .xlsm)
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputPasswordProtectVBAProject.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA project protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
