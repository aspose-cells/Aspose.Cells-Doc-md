---
title: C++ kullanarak JavaScript ile Bir Çalışma Kitabındaki VBA projesinin İmzalanıp İmzalanmadığını kontrol edin
linktitle: Bir Çalışmada VBA Projesinin İmzalı Olup Olmadığını Kontrol Edin
type: docs
weight: 70
url: /tr/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aspose.Cells for JavaScript kullanarak bir çalışma kitabındaki VBA projesinin imzalanıp imzalanmadığını kontrol etmeyi öğrenin.
---

{{% alert color="primary" %}}

Microsoft Excel üzerinden **Araçlar > Dijital İmzalar...** menü komutunu kullanarak VBA projenizin imzalı olup olmadığını kontrol edebilirsiniz. Benzer şekilde, Aspose.Cells [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) özelliğini kullanarak programlı olarak da kontrol edebilirsiniz.

{{% /alert %}}

## **JavaScript ile Bir Çalışma Kitabındaki VBA projesinin İmzalanıp İmzalanmadığını kontrol edin**

 Aşağıdaki kod çalışma kitabını yükler ve VBA projesinin imzalanıp imzalanmadığını [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) özelliği kullanarak kontrol eder. Proje imzalanmışsa **true**, değilse **false** döner.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```
