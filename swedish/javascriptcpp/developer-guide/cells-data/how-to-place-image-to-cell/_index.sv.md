---
title: Hur man infogar bild i cell
type: docs
weight: 130
url: /sv/javascript-cpp/how-to-insert-picture-in-cell/
description: Lär dig hur du infogar en bild i en cell med Aspose.Cells for JavaScript via C++.
keywords: Hur man infogar bild i cell, Infoga bild över celler, Placera bild i cell, Placera bild över celler, Hur man placerar bild i cell, Hur man placerar bild över celler, Växla mellan bild i cell och bild över celler, Växla mellan Plats i cell och Plats över celler
---

## **Möjliga användningsscenario**
Bilden ger en touch av ljus till ditt kalkylblad och ger en visuell representation av innehållet. De gör det också lättare för dig att förstå datan och komma på insikter. Även om du har kunnat använda bilder i Excel under många år, har Excel bara nyligen aktiverat funktionen att bilder blir faktiska cellvärden. Även om layouten på ritningen ändras kommer den fortfarande att vara kopplad till datan. Du kan använda den i tabeller, sortera, filtrera, inkludera i formler och så vidare!

## **Hur man infogar bild i cell med Excel**
Om hur man infogar en bild i en cell i Excel, följ dessa steg:

1. Gå till fliken Infoga och klicka på alternativet Bilder.
2. Välj **Plats i cell**. Välj en av följande källor från rullgardinsmenyn Infoga bild från (**Den här enheten**, **Lagerbilder** och **Onlinebilder**). Den här enheten för att infoga bild från din enhet. Lagerbilder för att infoga bild från lagerbilder. Onlinebilder för att infoga bild från webben.
<br>
<img src="1.png" width=60% />
3. Välj bild och infoga bild i en cell.
<br>
<img src="8.png" width=60% />

## **Hur man infogar bild över celler med Excel**
Om hur man infogar en bild över celler i Excel, följ dessa steg:

1. Gå till fliken Infoga och klicka på alternativet Bilder.
2. Välj **Plats över celler**. Välj en av följande källor från rullgardinsmenyn Infoga bild från (**Den här enheten**, **Lagerbilder** och **Onlinebilder**). Den här enheten för att infoga bild från din enhet. Lagerbilder för att infoga bild från lagerbilder. Onlinebilder för att infoga bild från webben.
<br>
<img src="2.png" width=60% />
3. Välj bild och infoga bild över celler.
<br>
<img src="3.png" width=60% />

## **Hur man växlar mellan bild i cell och bild över celler med Excel**
Du kan enkelt växla från **Bild i cell** till **Bild över celler**. Följ dessa steg:
1. Högerklicka på cellen och välj **Bild i cell** > **Placera över celler**. 
<br>
<img src="4.png" width=60% />
2. Resultatet efter växlingen är följande:
<br>
<img src="5.png" width=60% />

## **Hur man växlar från Bild över celler till Bild i cell med hjälp av Excel**
Du kan enkelt växla från **Bild över celler** till **Bild i cell**. Följ dessa steg:
1. Högerklicka på bilden och välj **Placera i cell**. 
<br>
<img src="6.png" width=60% />
2. Resultatet efter växlingen är följande:
<br>
<img src="7.png" width=60% />

## ** Hur man infogar bild i cell med Aspose.Cells for JavaScript via C++**
Infoga bild i cell med hjälp av Aspose.Cells. Se följande exempelkod. Efter att ha utfört exempelkoden infogas en bild i en cell.
1. Skapa en Workbook-objekt. 
2. Hämta cellen där du vill infoga bilden.
3. Ange Cell.EmbeddedImage-egenskapen. 
4. Slutligen sparas arbetsboken i [utdata XLSX](ut.xlsx)-format. 

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
