---
title: JavaScript kullanarak C++ ile Ad ile Metin Kutusuna Erişim
linktitle: Ada Göre Metin Kutusuna Eriş
type: docs
weight: 230
url: /tr/javascript-cpp/access-the-text-box-by-the-name/
description: Aspose.Cells for JavaScript ile koleksiyondan adıyla metin kutusuna nasıl erişileceğini öğrenin. 
---

## Ada Göre Metin Kutusuna Eriş

 Eskiden, metin kutularına [**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--) koleksiyonundan indeks kullanılarak erişilirdi, ama şimdi koleksiyondan isimle de erişebilirsiniz. Bu, zaten adını bildiğiniz takdirde metin kutusuna hızlı ve kullanışlı bir erişim sağlar.

Aşağıdaki örnek kod öncelikle bir metin kutusu oluşturur ve ona bazı metin ve ad atar. Ardından aynı metin kutusuna adıyla erişir ve metnini yazdırır.

### Ad ile metin kutusuna erişim JavaScript kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            const idx = sheet.textBoxes.add(10, 10, 10, 10);

            const tb1 = sheet.textBoxes.get(idx);
            tb1.name = "MyTextBox";
            tb1.text = "This is MyTextBox";

            const tb2 = sheet.textBoxes.get("MyTextBox");

            console.log(tb2.text);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">TextBox added. Text from named TextBox: ${tb2.text}</p>`;
        });
    </script>
</html>
```

### Örnek kod tarafından oluşturulan konsol çıktısı



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
