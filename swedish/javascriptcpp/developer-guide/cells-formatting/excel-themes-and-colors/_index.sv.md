---
title: Excel teman och färger
linktitle: Excel teman och färger  
type: docs  
weight: 100  
url: /sv/javascript-cpp/excel-themes-and-colors/  
description: Lär dig hur man använder anpassade färgscheman med Aspose.Cells for JavaScript via C++.  
keywords: JavaScript Skapa och tillämpa färgscheman, JavaScript programmeringsmässigt skapa ett anpassat färgschema, hur man tillämpar ett anpassat färgschema i JavaScript, JavaScript hur man använder färgscheman i Excel  
---

## **Hur man tillämpar och skapar färgschema i Excel**  
Dokumentteman gör det enkelt att koordinera färger, teckensnitt och grafisk formateringseffekter för Excel-dokument och uppdatera dem snabbt.  
Teman ger ett enhetligt utseende med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel ser Accent1-stilen olika ut i Office- och Apex-teman. Ofta tillämpar du ett dokumenttema och ändrar det sedan som du vill ha det.  

### **Hur man tillämpar ett färgschema i Excel**  
1. Öppna Excel och gå till fliken "Sidlayout" i Excel-ribbonen.  
1. Klicka på knappen "Färger" i avsnittet "Teman".  
<br>  
<img src="color.png" width=70% />  
1. Välj en färgpalett som matchar dina krav eller sväva över en schema för att se en förhandsgranskning i realtid.  

### **Hur man skapar en anpassad färgpalett i Excel**  
Du kan skapa din egen färguppsättning för att ge ditt dokument en fräsch, unik look eller följa din organisations varumärkesstandard.  

1. Öppna Excel och gå till fliken "Sidlayout" i Excel-ribbonen.  
1. Klicka på knappen "Färger" i avsnittet "Teman".  
1. Klicka på knappen "Anpassa färger...".  
<br>  
<img src="color2.png" width=70% />  

1. I dialogrutan "Skapa nya temafärger" kan du välja färger för varje element genom att klicka på färgnedtagningarna bredvid dem. Du kan välja färger från paletten eller definiera anpassade färger med hjälp av alternativet "Fler färger".  
<br>  
<img src="color3.png" width=70% />  
1. Efter att ha valt alla önskade färger, ange ett namn för din anpassade färgpalett i fältet "Namn".  

1. Klicka på knappen "Spara" för att spara din anpassade färgpalett. Din anpassade färgpalett kommer nu att finnas tillgänglig i rullgardinsmenyn "Färger" för framtida användning.  

## **Hur man skapar och tillämpar färgpalett i Aspose.Cells**  
Aspose.Cells ger funktioner för anpassning av teman och färger.  

### **Hur man skapar anpassat färgtema i Aspose.Cells**  
Om temafärger används i filen behöver vi inte ändra varje cell individuellt; vi behöver bara ändra färgerna i temat.  

Nedan följer ett exempel på hur man tillämpar anpassade teman med önskade färger. Vi använder en provmall manuellt skapad i Microsoft Excel 2007.  

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, tillämpar de anpassade färgerna och sparar Excel-filen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **Hur man tillämpar temafärger i Aspose.Cells**  
Följande exempel tillämpar en cells förgrunds- och teckensfärger baserat på standardtema (arbetsbokens) färgtyper. Det sparar också Excel-filen till disk.  


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
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Hur man får och ställer in temafärger i Aspose.Cells**  
Nedan följer några metoder och egenskaper som implementerar temafärger.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): Används för att sätta förgrundsfärgen.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): Används för att sätta bakgrundsfärgen.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): Används för att sätta teckenfärgen.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): Används för att få en temafärg.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): Används för att sätta en temafärg.  

Följande exempel visar hur man hämtar och ställer in tema färger.  

Följande exempel använder en mall XLSX-fil, hämtar färger för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

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

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **Fortsatta ämnen**  
- [Extrahera temadata från Excel-fil](/cells/sv/javascript-cpp/extract-theme-data-from-excel-file/)
