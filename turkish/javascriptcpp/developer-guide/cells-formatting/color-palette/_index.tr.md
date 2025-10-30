---
title: Renk Paletini Nasıl Kullanılır
linktitle: Renk Paletini Nasıl Kullanılır
type: docs
weight: 80
url: /tr/javascript-cpp/excel-color-palette/
description: JavaScript kodu ile palete özel renkler ekleyin ve Aspose.Cells for JavaScript via C++ kullanarak Excel renk paletini kullanın.
keywords: JavaScript ile palete özel renkler ekleyin, JavaScript ile programlı olarak Excel renk paleti, çalışma kitabında renk paleti nasıl kullanılır, JavaScript ile Excel’de renk paleti nasıl kullanılır
---

## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells for JavaScript via C++ ile, paletin mevcut renklerini kullanmanın yanı sıra özel renkler de kullanılabilir. Özel bir renk kullanmadan önce, onu önce palete ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

## **Paletine Özel Renkler Ekleyin**

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) adlı bir sınıf sağlar; bu, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) sınıfı, aşağıdaki parametreleri kullanarak paleti değiştirmek için özel bir renk eklemek amacıyla [**changePalette(Color, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) metodunu sağlar:

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            const isInPaletteBefore = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteBefore);
            resultDiv.innerHTML = `<p>Is Orchid in palette before change: ${isInPaletteBefore}</p>`;

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(Color.Orchid, 55);

            const isInPaletteAfter = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteAfter);
            resultDiv.innerHTML += `<p>Is Orchid in palette after change: ${isInPaletteAfter}</p>`;

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}
