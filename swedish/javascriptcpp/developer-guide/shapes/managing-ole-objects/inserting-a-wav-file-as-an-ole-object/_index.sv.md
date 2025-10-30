---
title: Infoga en WAV fil som ett Ole objekt med JavaScript via C++
linktitle: Infoga en WAV fil som ett Ole objekt
type: docs
weight: 70
url: /sv/javascript-cpp/inserting-a-wav-file-as-an-ole-object/
description: Lär dig hur du infogar en WAV fil som ett OLE objekt i Excel arbetsblad med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Aspose.Cells erbjuder funktionalitet för att lägga till olika typer av OLE-objekt i Excel-ark. Vi kommer att se i följande kodexempel hur man lägger till en WAV-fil som ett OLE-objekt med de enkla API:er som Aspose.Cells tillhandahåller. 

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
