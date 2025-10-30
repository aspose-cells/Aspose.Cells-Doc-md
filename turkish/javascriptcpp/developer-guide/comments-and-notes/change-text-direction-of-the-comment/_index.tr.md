---
title: C++ ile JavaScript kullanarak Yorumun Metin Yönünü Değiştirin
linktitle: Yorumun Metin Yönünü Değiştir
type: docs
weight: 10
url: /tr/javascript-cpp/change-text-direction-of-the-comment/
description: Aspose.Cells for JavaC++ ile Yorumların Metin yönünü nasıl değiştireceğinizi öğrenin. Yorum hizalama ayarlarını etkin şekilde özelleştirin.
---

{{% alert color="primary" %}}

Microsoft Excel, hücrelere ek bilgi eklemek ve veriyi vurgulamak için yorumlar eklemeye olanak tanır. Geliştiriciler, hizalama ayarlarını ve metin yönünü belirtmek için yorumu özelleştirmeleri gerekebilir. Aspose.Cells for JavaC++ ile betikleri, bu görevi yerine getirmek için API'ler sağlar.

{{% /alert %}}

Aspose.Cells for JavaC++ ile Yorumun metin yönünü ayarlamak için [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) özelliği sağlar. Aşağıdaki örnek kod, [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) özelliğinin kullanımıyla yorumun metin yönünü ayarlamayı göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment Shape</title>
    </head>
    <body>
        <h1>Add Comment Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, TextDirectionType } = AsposeCells;

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
            // Instantiate a new Workbook
            const wb = new Workbook();

            // Get the first worksheet
            const sheet = wb.worksheets.get(0);

            // Add a comment to A1 cell
            const commentIndex = sheet.comments.add("A1");
            const comment = sheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set its horizontal alignment setting
            comment.commentShape.textHorizontalAlignment = TextAlignmentType.Right;

            // Set the Text Direction - Right-to-Left
            comment.commentShape.textOrientationType = TextDirectionType.RightToLeft;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is test";

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutCommentShape.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
