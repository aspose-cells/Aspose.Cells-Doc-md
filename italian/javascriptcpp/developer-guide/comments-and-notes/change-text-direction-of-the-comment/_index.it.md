---
title: Cambia la direzione del testo del commento con JavaScript tramite C++
linktitle: Cambia la Direzione del Testo del Commento
type: docs
weight: 10
url: /it/javascript-cpp/change-text-direction-of-the-comment/
description: Impara come cambiare la direzione del testo dei commenti usando Aspose.Cells for JavaScript tramite C++. Personalizza efficacemente le impostazioni di allineamento del commento.
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di aggiungere commenti alle celle per includere informazioni aggiuntive e evidenziare i dati. Gli sviluppatori potrebbero dover personalizzare il commento per specificare le impostazioni di allineamento e la direzione del testo. Script Aspose.Cells for Java tramite C++ fornisce API per svolgere questo compito.

{{% /alert %}}

Script Aspose.Cells for Java tramite C++ fornisce una proprietà [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) per impostare la direzione del testo di un commento. Il seguente esempio di codice dimostra l'uso della proprietà [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) per impostare la direzione del testo di un commento.

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
