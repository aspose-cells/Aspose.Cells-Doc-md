---
title: JavaScript ve C++ kullanarak Bir çalışma kitabında düzenli ifadeyle metni değiştirin
linktitle: Düzenli İfade Kullanarak Bir Çalışma Kitabındaki Metni Değiştirme
type: docs
weight: 90
url: /tr/javascript-cpp/replace-text-in-a-workbook-using-regular-expression/
description: C++ kullanarak düzenli ifadeyle çalışma kitabında metni değiştirme
---

Aspose.Cells, çalışma kitabında metni düzenli ifadeyle değiştirme özelliği sunar. Bunun için API, [**ReplaceOptions**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions) sınıfının [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) özelliğini sağlar. [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) özelliğinin **true** olarak ayarlanması, aranacak anahtarın bir düzenli ifade olacağını gösterir.

Aşağıdaki kod parçacığı, [örnek Excel dosyası](101089318.xlsx) kullanılarak [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) özelliğinin kullanımını gösterir. Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089319.xlsx) referans olması için eklenmiştir.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Regex Replace Example</title>
    </head>
    <body>
        <h1>Regex Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ReplaceOptions } = AsposeCells;

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

            const replaceOptions = new ReplaceOptions();
            replaceOptions.caseSensitive = false;
            replaceOptions.matchEntireCellContents = false;
            replaceOptions.regexKey = true;

            workbook.replace("\\bKIM\\b", "^^^TIM^^^", replaceOptions);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RegexReplace_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Regex replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
