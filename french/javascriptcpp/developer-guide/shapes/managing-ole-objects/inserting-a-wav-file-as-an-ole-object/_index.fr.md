---
title: Insertion d un fichier WAV en tant qu objet OLE avec JavaScript via C++
linktitle: Insertion d un fichier WAV en tant qu objet Ole
type: docs
weight: 70
url: /fr/javascript-cpp/inserting-a-wav-file-as-an-ole-object/
description: Découvrez comment insérer un fichier WAV en tant qu objet OLE dans les feuilles de calcul Excel en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Aspose.Cells offre la fonctionnalité d'ajouter différents types d'objets OLE dans les feuilles Excel. Nous verrons dans les exemples de code suivants comment ajouter un fichier WAV en tant qu'objet OLE en utilisant les API simples fournies par Aspose.Cells. 

{{% /alert %}} 


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells OLE Object Example</title>
    </head>
    <body>
        <h1>Add OLE Object to Workbook</h1>
        <p>Select an image (used as OLE display) and an object file (e.g., WAV) to embed.</p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="objectInput" accept=".wav,.mp3,.pdf,.doc,.docx,application/*" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const objectInput = document.getElementById('objectInput');
            if (!imageInput.files.length || !objectInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select both an image file and an object file.</p>';
                return;
            }

            // Read selected files
            const imageFile = imageInput.files[0];
            const objectFile = objectInput.files[0];

            const imageArrayBuffer = await imageFile.arrayBuffer();
            const objectArrayBuffer = await objectFile.arrayBuffer();

            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(objectArrayBuffer);

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add Ole Object (using image as the display/content preview)
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Configure the added OLE object
            const intIndex = 0;
            const oleObject = workbook.worksheets.get(0).oleObjects.get(intIndex);
            oleObject.fileFormatType = AsposeCells.FileFormatType.Unknown;
            oleObject.objectData = objectData;
            oleObject.objectSourceFullName = objectFile.name;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'testWAV.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">OLE object added successfully. Click the download link to get the modified workbook.</p>';
        });
    </script>
</html>
```
