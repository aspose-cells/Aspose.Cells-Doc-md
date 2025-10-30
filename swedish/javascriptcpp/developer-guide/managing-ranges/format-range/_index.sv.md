---
title: Formatera områden med JavaScript via C++
linktitle: Formatera områden
type: docs
weight: 105
url: /sv/javascript-cpp/how-to-format-a-range/
description: Lär dig hur du formaterar ett cellområde i Excel med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  
När du behöver tillämpa en stil på ett område kan du använda områdesformatering.  

## **Hur man formaterar ett område i Excel**  

För att formatera ett område med celler i Excel kan du använda de inbyggda formateringsalternativen som tillhandahålls av Excel. Så här kan du formatera en område med celler direkt i Excel:  

1. Öppna Excel och öppna arbetsboken som innehåller det område du vill formatera.  

2. Välj det område med celler som du vill formatera. Du kan klicka och dra för att markera området, eller så kan du använda tangentbordsgenvägar som Skift + Piltangenter för att utöka markeringen.  

3. När området är markerat högerklickar du på det markerade området och väljer "Formatera celler" från snabbmenyn. Alternativt kan du gå till fliken Start i Excel-ribbonen, klicka på rullgardinsmenyn "Format" i gruppen "Celler" och välja "Formatera celler".  

4. Dialogrutan "Formatera celler" visas. Här kan du välja olika formateringsalternativ att tillämpa på det markerade området. Till exempel kan du ändra teckensnittsstil, teckenstorlek, teckenfärg, nummerformat, linjer, bakgrundsfärg, etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.  

5. Efter att ha gjort de önskade formateringsändringarna klickar du på "OK"-knappen för att tillämpa formateringen på det markerade området.  

## **Hur man formaterar ett område med JavaScript**  

För att formatera ett område med Aspose.Cells for JavaScript via C++ kan du använda följande metoder:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  
3. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  

## **Exempelkod**  
I det här exemplet skapar vi en Excel-arbetsbok, lägger till en del provdata, får åtkomst till den första arbetsbladet och definierar två intervall("A1:C3" och "A4:C5"). Sedan skapar vi nya stilar, ställer in olika formateringsalternativ (t.ex., teckenfärg, fetstil) och tillämpar stilen på intervallet. Slutligen sparar vi arbetsboken i en ny fil.  
<br>  
![todo:image_alt_text](format-range.png)  

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);

            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet (already have ws, but keep variable for clarity)
            const worksheet = workbook.worksheets.get(0);

            // Define the range
            const range = worksheet.cells.createRange("A1:C3");

            // Apply formatting to the range
            const style = workbook.createStyle();
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.font = true;
            range.applyStyle(style, flag);

            // Define the range
            const range2 = worksheet.cells.createRange("A4:C5");

            // Apply formatting to the range
            const style2 = workbook.createStyle();
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            range2.setStyle(style2);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
