---
title: Inaktivera kompatibilitetskollen i Excel med JavaScript via C++
linktitle: Inaktivera kompatibilitetskontroll i Excel
type: docs
weight: 170
url: /sv/javascript-cpp/disable-compatibility-checker-in-excel/
description: Lär dig hur du inaktiverar kompatibilitetskollen genom Aspose.Cells for JavaScript via C++ API.
keywords: JavaScript inaktivera kompatibilitetskollen, Excel inaktivera kompatibilitetskollen i JavaScript via C++, Inaktivera kompatibilitetskollen i arbetsboken.
---

## Inaktivera kompatibilitetskollen i Excel-arbetsblad i JavaScript  

{{% alert color="primary" %}}  
Microsoft Excels kompatibilitetskontroll flaggar för när en fil sparas i ett tidigare filformat kan orsaka funktionalitetsproblem eller förlust av fidelitet. Kompatibilitetskontrollen är en funktion i Microsoft Office Excel 2007 och Microsoft Excel 2010.  

När du sparar en arbetsbok i en tidigare version, Excel 97 genom Excel 2003, från Excel 2007 eller Excel 2010 skannar kompatibilitetskontrollen arbetsboken för att se om den innehåller funktioner som inte stöds av den tidigare versionen. För att hjälpa dig fatta beslut om hur du hanterar kompatibilitetsproblem visar kompatibilitetskontrollen dialogrutor med alternativ. Den kan också användas för att skapa en rapport om eventuella problem i arbetsboken eller inaktivera funktionen.  

Ibland måste du inaktivera kompatibilitetskontrollen för ett särskilt kalkylblad. Med Aspose.Cells API:erna kan du göra detta programmatiskt så att användare inte blir frustrerade eller förvirrade av dialogrutan för kompatibilitetskontroll som dyker upp när de sparar om filen manuellt i Microsoft Excel.  
{{% /alert %}}  

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Microsoft Excel**  

För att inaktivera kompatibilitetskontrollen i Microsoft Excel (t.ex. Microsoft Excel 2007/2010):  

- (Excel 2007) Klicka på Office-knappen, klicka på **Förbered**, klicka på **Kör kompatibilitetskontroll**, och avmarkera sedan alternativet **Kontrollera kompatibilitet när du sparar arbetsboken**.  
- (Excel 2010) På fliken Fil klickar du på **Info**, sedan **Sök efter problem**, klickar på **Kontrollera kompatibilitet** och avmarkerar till sist alternativet **Kontrollera kompatibilitet när du sparar den här arbetsboken**.  

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Aspose.Cells API:er**  

Ställ in egenskapen [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) till **false** för att inaktivera Microsoft Excels kompatibilitetskontroll.  

### **Kodexempel**  

Följande kodexempel visar hur man inaktiverar kompatibilitetskollen med Aspose.Cells for JavaScript via C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
