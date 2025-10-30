---
title: JavaScript ile C++ kullanarak VBA Projesinin Korunduğunu ve Görüntülemeye Kilitlendiğini Kontrol Edin
linktitle: C# da Bir Çalışbookun VBA Projesinin Korunup Görüntüleme İçin Kilitli Olup Olmadığını Kontrol Et
type: docs
weight: 30
url: /tr/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Aspose.Cells for JavaScript kullanarak Excel dosyasındaki VBA projesinin korunup korunmadığını ve görüntülemeye kilitli olup olmadığını kontrol etmeyi öğrenin.
---

## JavaScript ile C++ kullanarak VBA Projesinin Korunduğunu ve Görüntülemeye Kilitlendiğini Kontrol Et

 Aspose.Cells, bir Excel dosyasının VBA (Visual Basic for Applications) Projesinin korunduğunu ve görüntülemeye kilitlendiğini kontrol etmenize olanak tanır. Bunun için API, [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) özelliği sağlar. Eğer korundusa, [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) özelliği **true** döner.

## **Örnek Kod**

Aşağıdaki örnek kod, [örnek Excel dosyasını](43352065.xlsm) yükler ve Excel dosyasının VBA (Visual Basic for Applications) Projesinin korunduğunu ve görüntülemeye kilitli olup olmadığını kontrol eder. Lütfen referans için Konsol Çıktısına da bakınız.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check VBA Project Protection Example</title>
    </head>
    <body>
        <h1>Check if VBA Project is Protected</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.xlsb,.csv" />
        <button id="runExample">Check VBA Protection</button>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm) to check.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the VBA project of the workbook.
            const vbaProject = workbook.vbaProject;

            // Whether "Lock project for viewing" is true or not.
            const isLocked = vbaProject ? vbaProject.islockedForViewing : null;

            if (isLocked === null) {
                resultDiv.innerHTML = '<p style="color: orange;">The workbook does not contain a VBA project.</p>';
            } else {
                resultDiv.innerHTML = `<p>Is VBA Project Locked for Viewing: <strong>${isLocked}</strong></p>`;
                console.log("Is VBA Project Locked for Viewing: " + isLocked);
            }
        });
    </script>
</html>
```

## **Konsol Çıktısı**

Sağlanan [örnek Excel dosyası](43352065.xlsm) ile yukarıdaki örnek kodun çalıştırılması durumunda elde edilen konsol çıkışı budur.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
