---
title: ODS Dosyalarında Hücre Doğrulamasını Al
type: docs
weight: 180
url: /tr/javascript-cpp/get-cell-validation-in-ods-files/
description: Hücre Doğrulamasını ODS Dosyalarında almak için Aspose.Cells for JavaScript C++ API kullanmayı öğrenin.
keywords: C++ aracılığıyla Hücre Doğrulamasını Al JavaScript, C++ aracılığıyla Hücre Doğrulamasını Edinin
---

## **ODS Dosyalarında Hücre Doğrulamasını Al**  

Aspose.Cells for JavaScript aracılığıyla C++ sayesinde, ODS dosyalarında bir hücreye uygulanan doğrulamayı alabilirsiniz. Bunu yapmak için API [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/) sınıfının [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) özelliğini sağlar.  

Aşağıdaki kod örneği, [kaynak ODS](101089354.ods) dosyasını yükleyerek ve A9 hücresinin doğrulamasını okuyarak [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) özelliğinin kullanımını gösterir.  

### **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
