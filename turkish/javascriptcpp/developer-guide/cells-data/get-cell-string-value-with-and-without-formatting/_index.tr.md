---
title: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Alın
type: docs
weight: 240
url: /tr/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for JavaScript kullanılarak hücre dize değeri ile biçimlendirmeden nasıl alınacağını öğrenin.
keywords: Hücre Dize Değeri Alma, Biçimlendirmeyle veya Biçimlendirmesiz JavaScript ile C++, Hücre Dize Değeri Alma, Biçimlendirmeyle veya Biçimlendirmesiz JavaScript ile JavaScript ile C++
---

{{% alert color="primary" %}}

Aspose.Cells, hücrenin içeriğini, biçimlendirme olup olmamasına bakmaksızın almak için [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) özelliğini sağlar. Farz edelim ki, değeri 0.012345 olan bir hücreye sahipsiniz ve bunu yalnızca iki ondalık basamağı gösterecek şekilde biçimlendirdiniz. Excel’de 0.01 olarak görüntülenir. Dize değerlerini hem 0.01 hem de 0.012345 olarak almak için [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) özelliğini kullanabilirsiniz. [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) enum ile parametre olarak alır ve şu değerlere sahiptir

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Aşağıdaki örnek kod, [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) özelliğinin kullanımını açıklar.

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
        const { Workbook, SaveFormat, Cell } = AsposeCells;

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
            // Creating a new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Put value inside the cell
            cell.putValue(0.012345);

            // Format the cell that it should display 0.01 instead of 0.012345
            const style = cell.style;
            style.number = 2;
            cell.style = style;

            // Get string value as Cell Style
            let value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML = `<p>Formatted string value: ${value}</p>`;

            // Get string value without any formatting
            value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML += `<p>Unformatted string value: ${value}</p>`;

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
