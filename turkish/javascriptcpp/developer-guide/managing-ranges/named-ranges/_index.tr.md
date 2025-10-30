---
title: JavaScript ile C++ kullanarak Çalışma Kitabı ve Çalışma Sayfası Kapsamlı Adlandırılmış Aralıklar oluşturma
linktitle: Adlandırılmış Aralık
type: docs
weight: 40
url: /tr/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: C++ kullanarak JavaScript ile çalışma kitabı ve çalışma sayfası kapsamlı adlandırılmış aralıklar nasıl oluşturulur öğrenin. 
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara çalışma kitabı (aynı zamanda genel kapsam olarak da bilinir) ve çalışma sayfası olmak üzere iki farklı kapsamla adlandırılmış aralıkları tanımlama imkanı tanır.

- Bir çalışma kitabı kapsamına sahip adlandırılmış aralıklar, sadece isimlerini kullanarak o çalışma kitabındaki herhangi bir çalışma sayfasından erişilebilir.
- Çalışma sayfası kapsamlı adlandırılmış aralıklar, oluşturulduğu belirli çalışma sayfasına referansla erişilir.

C++ kullanarak JavaScript ile çalışma kitabı ve çalışma sayfası kapsama alanı olan adlandırılmış aralıklar ekleme işlevselliği sağlar. Çalışma sayfası kapsamlı adlandırılmış aralık oluştururken, çalışma sayfası referansı kullanılmalıdır.

{{% /alert %}} 
## **Çalışma Kitabı Kapsamlı Adlandırılmış Aralık Ekleme**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>WorkbookScope Named Range Example</title>
    </head>
    <body>
        <h1>WorkbookScope Named Range Example</h1>
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

            // If a file is provided, load it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells from Cell A1 to C10
            const workbookScope = cells.createRange("A1", "C10");

            // Assign the name to workbook scope named range
            workbookScope.name = "workbookScope";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookScope.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range "workbookScope" created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
## **Çalışma Sayfası Kapsamlı Adlandırılmış Aralık Ekleme**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Assign Range Name Example</h1>
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

            // Create new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells
            const localRange = cells.createRange("A1", "C10");

            // Assign name to range with sheet reference
            localRange.name = "Sheet1!local";

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala](/cells/tr/javascript-cpp/create-access-and-copy-named-ranges/)
- [Biçimlendir ve Adlandırılmış Aralıkları Değiştir](/cells/tr/javascript-cpp/format-and-modify-named-ranges/)
- [Harici Bağlantıları Olan Aralığı Al](/cells/tr/javascript-cpp/get-range-with-external-links/)
- [Sıralı Olmayan Aralıkları Uygulama](/cells/tr/javascript-cpp/implementing-non-sequential-ranges/)
