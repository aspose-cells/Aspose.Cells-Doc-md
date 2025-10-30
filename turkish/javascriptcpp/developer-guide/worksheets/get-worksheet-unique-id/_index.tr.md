---
title: JavaScript kullanarak C++ ile çalışma sayfası benzersiz kimliği alın
linktitle: Çalışma sayfası benzersiz kimliğini alma
type: docs
weight: 190
url: /tr/javascript-cpp/get-worksheet-unique-id/
description: Bu makale, JavaScript kütüphanesi ve C++ API kullanarak programlama yoluyla Excel çalışma sayfası benzersiz kimliğini nasıl alacağınızı gösterir.
keywords: benzersiz kimlik excel çalışma sayfası JavaScript ile C++, benzersiz kimlik çalışma sayfası JavaScript ile C++
---

## **Çalışma sayfası benzersiz kimliğini alın**

Aspose.Cells for JavaScript ile C++ kullanarak, [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--) özelliğini kullanarak çalışma sayfasının benzersiz kimliğini alma imkanı sağlar. Aşağıdaki kod örneği, çalışma sayfasının benzersiz kimliğini yazdırmak için [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--) özelliğinin kullanımını gösterir. Aşağıdaki kod örneği, bu [örnek Excel dosyasını](105480213.xlsx) kullanır.

### Kaynak Kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Worksheet Unique Id Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Get Unique Id
            const uniqueId = worksheet.uniqueId;
            console.log("Unique Id: " + uniqueId);

            document.getElementById('result').innerHTML = '<p style="color: green;">Unique Id: ' + uniqueId + '</p>';
        });
    </script>
</html>
```
