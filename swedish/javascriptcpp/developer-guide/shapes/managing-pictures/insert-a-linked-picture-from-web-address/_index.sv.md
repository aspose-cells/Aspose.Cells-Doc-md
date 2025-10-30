---
title: Infoga en länkad bild från webbadress med JavaScript via C++
linktitle: Infoga en länkad bild från webbadress
type: docs
weight: 450
url: /sv/javascript-cpp/insert-a-linked-picture-from-web-address/
description: Lär dig hur du infogar en länkad bild från en webbadress i ett arbetsblad med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Ibland behöver du infoga en bild från webben (http://) i ett kalkylblad. Ange bildens URL och bilden laddas ner varje gång kalkylbladet öppnas i Excel. Bilden är inte fysiskt inbäddad i Excel-dokumentet, utan pekar på en webbresurs.
{{% /alert %}}

## **Använda Microsoft Excel**

I Microsoft Excel (till exempel 2007):

1. Klicka på **Infoga** i menyn och välj **Bild**.  
1. Ange webbadressen för bilden i dialogrutan Infoga bild.

## **Använder Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ stöder att lägga till en länkad bild med [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Metoden returnerar ett [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture)-objekt.

Följande exempel visar hur man lägger till en länkad bild från en webbadress till ett arbetsblad.

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
