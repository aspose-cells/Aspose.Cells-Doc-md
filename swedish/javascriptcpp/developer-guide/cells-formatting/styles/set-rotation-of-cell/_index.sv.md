---
title: Hur man roterar text i en cell
linktitle: Hur man roterar text i en cell  
type: docs  
weight: 80  
url: /sv/javascript-cpp/how-to-rotate-text-of-cell/  
description: Lär dig hur du roterar texten i en cell programmässigt med Aspose.Cells for JavaScript via C++.  
keywords: JavaScript via C++ rotera texten i Cell, JavaScript programmering för att rotera celltext i arbetsboken, programmässigt inställa cellens rotationsvinkel i arbetsboken, JavaScript hur man roterar celltext i excel  
---

## **Rotera texten iCell i Aspose.Cells for JavaScript via C++**

Aspose.Cells är en kraftfull JavaScript-komponent som gör det möjligt för utvecklare att arbeta med Excel-ark programmässigt. En av funktionerna som erbjuds av Aspose.Cells är möjligheten att rotera celler, vilket tillåter dig att anpassa textens orientering och förbättra den visuella presentationen av dina data. I detta dokument kommer vi att utforska hur man roterar celler med Aspose.Cells.

## **Hur man roterar text i cell i Excel**
För att rotera en cell i Excel kan du använda följande steg:
1. Öppna Excel och välj den cell eller det cellområde som du vill rotera.
1. Högerklicka på den markerade cellen/cellerna och välj "Formatera celler" i snabbmenyn. Alternativt kan du gå till fliken "Hem" i Excels menyflik, klicka på rullgardinsmenyn "Formatera" i gruppen "Celler" och välj "Formatera celler".
1. I dialogrutan "Formatera celler" navigerar du till fliken "Justering".
1. Under avsnittet "Orientering" ser du alternativen för att rotera texten. Du kan direkt ange önskad rotationsvinkel i grader i rutan "Grader". Positiva värden roterar texten moturs, och negativa värden roterar den medurs.
<br>
![todo:image_alt_text](alignment.png)
1. När du har valt önskad rotation klickar du på "OK" för att tillämpa ändringarna. Den valda cellen/cellerna kommer nu att vara roterade enligt din valda rotationsvinkel eller orientering.

## **Hur man roterar text i cell med hjälp av Aspose.Cells API**

[**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-)-egenskapen gör det bekvämt att rotera celler. För att rotera celler i Aspose.Cells måste du följa dessa steg:
1. Läs in Excel-arbetsboken  
<br>
Först måste du läsa in Excel-arbetsboken med hjälp av Aspose.Cells. Du kan använda Workbook-klassen för att öppna en befintlig Excel-fil eller skapa en ny. 

1. Kom åt arbetsbladet  
<br>
När arbetsboken har lästs in måste du komma åt det arbetsblad där du vill rotera cellerna. Du kan antingen komma åt arbetsbladet genom dess index eller namn. 

1. Rotera texten i cellen  
<br>
Nu när du har åtkomst till arbetsbladet kan du rotera cellerna genom att ändra Style-objektet för de önskade cellerna. Style-objektet låter dig ställa in olika formateringsalternativ, inklusive rotation. 

1. Spara arbetsboken  
<br>
Efter att ha roterat cellerna kan du spara den modifierade arbetsboken till en fil eller ström med hjälp av Save -metoden.

## **JavaScript Exempel kod**

Se följande kod, den skapar ett arbetsboksobjekt och ställer in olika rotationsvinklar för flera celler. Skärmbilden visar resultatet efter körning av exemplet.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
