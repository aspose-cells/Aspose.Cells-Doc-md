---
title: Inserisci un immagine collegata da un indirizzo web con JavaScript tramite C++
linktitle: Inserisci un immagine collegata da un indirizzo web
type: docs
weight: 450
url: /it/javascript-cpp/insert-a-linked-picture-from-web-address/
description: Impara come inserire un immagine collegata da un indirizzo web in un foglio di lavoro utilizzando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}
A volte è necessario inserire un’immagine dal web (http://) in un foglio di lavoro. Per farlo, specifica l'URL dell’immagine e questa verrà scaricata ogni volta che il foglio di calcolo viene aperto in Excel. L’immagine non è incorporata fisicamente nel documento Excel, ma punta a una risorsa web.
{{% /alert %}}

## **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1. Fare clic sul menu **Inserisci** e selezionare **Immagine**.  
1. Specifica l'indirizzo web dell'immagine nella finestra di dialogo Inserisci immagine.

## **Utilizzando Aspose.Cells for JavaScript tramite C++**

Aspose.Cells for JavaScript tramite C++ supporta l'aggiunta di un'immagine collegata usando [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Il metodo restituisce un oggetto [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

L'esempio seguente mostra come aggiungere un'immagine collegata da un indirizzo web a un foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Insert Linked Picture Example</h1>
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

            if (fileInput.files.length) {
                // If file provided, use it as the base workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Otherwise create a new workbook
                var workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a linked picture (from Web Address) to B2 Cell.
            const pic = worksheet.shapes.addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");

            // Set the height and width of the inserted image.
            pic.heightInch = 1.04;
            pic.widthInch = 2.6;

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outLinkedPicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Linked picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
