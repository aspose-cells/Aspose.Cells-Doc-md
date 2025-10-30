---
title: VBA Kodunun İmzalı olup olmadığını JavaScript ile C++ kullanarak kontrol edin
linktitle: VBA Kodunun İmzalı Olup Olmadığını Kontrol Et
type: docs
weight: 100
url: /tr/javascript-cpp/check-if-vba-code-is-signed/
description: Aspose.Cells for JavaScript kullanarak VBA kod projesinin imzalanıp imzalanmadığını kontrol etmeyi öğrenin. 
---

{{% alert color="primary" %}}

Aspose.Cells, kullanıcının VBA kod projesinin imzalı olup olmadığını kontrol etmesine izin verir. Lütfen VBA kod projesinin imzalı olup olmadığını kontrol etmek için [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki kod, [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) özelliği kullanılarak VBA kodunun imzalanıp imzalanmadığını nasıl kontrol edeceğinizi gösterir. Bu kodu test etmek için herhangi bir Excel dosyanızı kullanabilirsiniz. Test amacıyla, aşağıdaki kodda kullanılan [bu Excel dosyasını](5115032.xlsm) kullanabilirsiniz.

## **JavaScript ile VBA Kodunun İmzalanıp İmzalanmadığını Kontrol Et**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## Konsol Çıkışı

Aşağıda sağlanan bağlantıdaki [örnek excel dosyası](5115032.xlsm) kullanılarak yukarıdaki kodun konsol çıktısı bulunmaktadır.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
