---
title: JavaScript aracılığıyla C++ ile Çalışma Sayfasını Korumadan Kaldırma
linktitle: Bir Çalışma Sayfasının Korumasını Kaldır
type: docs
weight: 20
url: /tr/javascript-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Bir geliştirici, çalışma sayfasındaki korumayı çalışma zamanında kaldırarak dosyaya bazı değişiklikler yapabilir mi? Bu, Aspose.Cells ile kolayca yapılabilir.

{{% /alert %}}

## **Bir Çalışma Sayfasını Korumayı Kaldırma**

### **Microsoft Excel Kullanımı**

Çalışma sayfasından korumayı kaldırmak için:

**Araçlar** menüsünden, **Koruma** ardından **Sayfayı Koru** seçin. Koruma kaldırılır, sayfa şifrelenmiş değilse. Bu durumda, bir iletişim kutusu şifre istemektedir. Şifreyi girin ve sayfa koruması kaldırılacaktır.

### **Aspose.Cells Kullanarak Basit Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

Bir çalışma sayfasını, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) metodunu çağırarak korumasını kaldırabilirsiniz. Şifre koruması olmayan, basitçe korunmamış bir çalışma sayfası, şifre ile korunmamış olanıdır. Bu tür çalışma sayfaları, parametre geçirmeden [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) metodunu çağırarak korunma kaldırılabilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet without a password
            worksheet.unprotect();

            // Saving the Workbook in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Aspose.Cells Kullanarak Şifre Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

Şifre ile korunan çalışma sayfası, parolayla korunmuş bir çalışma sayfasıdır. Bu tür çalışma sayfaları, şifreyi parametre olarak alan [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) metodunun aşırı yüklenmiş bir versiyonunu çağırarak korunabilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet with a password (empty password in original code)
            worksheet.unprotect("");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
