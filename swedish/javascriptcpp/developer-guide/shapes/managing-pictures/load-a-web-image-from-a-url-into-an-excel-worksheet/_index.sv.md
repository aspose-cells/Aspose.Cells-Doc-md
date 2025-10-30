---
title: Ladda en webbild från en URL till ett Excel Arbetsblad med JavaScript via C++
linktitle: Ladda en webbild från en URL till ett Excel kalkylblad
type: docs
weight: 30
url: /sv/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Hur konverterar man en bild från URL till en faktisk Excel bild med Aspose.Cells for JavaScript via C++.
keywords: excel visa bild från url, excel url till bild, visa bild i excel från url, excel infoga bild från url, konvertera url till bild i excel, excel bild från url, ladda bild från url i excel, JavaScript, Excel
---

## Ladda en bild från en URL till ett Excel-kalkylblad

Aspose.Cells for JavaScript via C++ ger ett enkelt och lätt sätt att ladda bilder från URL:er till Excel-Arbetsblad. Den här artikeln förklarar hur man laddar ner bilddatan till en ström och sedan infogar den i arbetsbladet med Aspose.Cells API. Med den här metoden blir bilderna en del av Excel-filen och laddas inte ner varje gång arbetsbladet öppnas.

## Exempelkod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Det kan finnas fall där du alltid vill ha den uppdaterade bilden från en URL. För att uppnå detta kan du följa instruktionerna i artikeln [Infoga en länkad bild från webbadress](/cells/sv/javascript-cpp/insert-a-linked-picture-from-web-address/). Genom att följa denna metod laddas bilden från URL:en varje gång arbetsbladet öppnas.
{{% /alert %}}
