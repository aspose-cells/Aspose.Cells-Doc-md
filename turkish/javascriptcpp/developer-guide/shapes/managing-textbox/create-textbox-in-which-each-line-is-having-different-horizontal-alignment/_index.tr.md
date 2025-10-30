---
title: Her satır farklı Yatay Hizalamaya sahip bir Metin Kutusu oluşturmak JavaScript ve C++ ile
linktitle: Her bir satırın farklı Yatay Hizalamaya sahip olduğu bir Metin Kutusu Oluştur
type: docs
weight: 310
url: /tr/javascript-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Her satırın farklı yatay hizalama yapabileceği bir Metin Kutusu nasıl oluşturulur öğrenin Aspose.Cells for JavaScript ile C++ kullanılarak.
---

{{% alert color="primary" %}}
Paragraf metnin yatay hizalamasını [**TextParagraph.alignmentType**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/#alignmentType--) özelliği kullanarak ayarlayabilirsiniz.
{{% /alert %}}

Aşağıdaki örnek kod üç satır oluşturur ve her birinin yatay hizalamasını ayarlar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add TextBox and Set Paragraph Alignment</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Utils } = AsposeCells;

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
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add text box inside the sheet.
            ws.shapes.addTextBox(2, 0, 2, 0, 80, 400);

            // Access first shape which is a text box and set its text.
            const shape = ws.shapes.get(0);
            shape.text = "Sign up for your free phone number.\nCall and text online for free.\nCall your friends and family.";

            // Access the first paragraph and set its horizontal alignment to left.
            let p = shape.textBody.textParagraphs.get(0);
            p.alignmentType = TextAlignmentType.Left;

            // Access the second paragraph and set its horizontal alignment to center.
            p = shape.textBody.textParagraphs.get(1);
            p.alignmentType = TextAlignmentType.Center;

            // Access the third paragraph and set its horizontal alignment to right.
            p = shape.textBody.textParagraphs.get(2);
            p.alignmentType = TextAlignmentType.Right;

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
