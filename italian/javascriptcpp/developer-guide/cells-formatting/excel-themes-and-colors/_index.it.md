---
title: Temi e Colori di Excel
linktitle: Temi e Colori di Excel  
type: docs  
weight: 100  
url: /it/javascript-cpp/excel-themes-and-colors/  
description: Scopri come usare schemi di colori personalizzati con Script via C++.  
keywords: JavaScript Crea e Applica Schemi di Colori, JavaScript crea programmaticamente uno schema di colori personalizzato, come applicare programmaticamente uno schema di colori personalizzato in JavaScript, come usare lo schema di colori in Excel con JavaScript  
---

## **Come Applicare e Creare uno Schema Colori in Excel**  
I temi del documento facilitano il coordinamento dei colori, dei caratteri e degli effetti di formattazione grafica dei documenti di Excel e consentono di aggiornarli rapidamente.  
I temi offrono un aspetto unificato con stili nominati, effetti grafici e altri oggetti utilizzati in un workbook. Ad esempio, lo stile Accent1 appare diverso nei temi Office e Apex. Spesso, si applica un tema al documento e poi lo si modifica secondo le preferenze.  

### **Come Applicare uno Schema Colori in Excel**  
1. Apri Excel e vai alla scheda "Layout di pagina" nel nastro di Excel.  
1. Fai clic sul pulsante "Colori" nella sezione "Temi".  
<br>  
<img src="color.png" width=70% />  
1. Scegli una combinazione di colori che corrisponda alle tue esigenze o passa il mouse su uno schema per vedere un'anteprima in tempo reale.  

### **Come creare un set di colori personalizzato in Excel**  
Puoi creare il tuo set di colori per dare al tuo documento un aspetto fresco e unico o per conformarti agli standard del marchio della tua organizzazione.  

1. Apri Excel e vai alla scheda "Layout di pagina" nel nastro di Excel.  
1. Fai clic sul pulsante "Colori" nella sezione "Temi".  
1. Fai clic sul pulsante "Personalizza colori...".  
<br>  
<img src="color2.png" width=70% />  

1. Nella finestra di dialogo "Crea nuovi colori tema", puoi selezionare i colori per ciascun elemento facendo clic sul menù a discesa accanto ad essi. Puoi scegliere i colori dalla palette o definire colori personalizzati utilizzando l'opzione "Altri colori".  
<br>  
<img src="color3.png" width=70% />  
1. Dopo aver selezionato tutti i colori desiderati, fornisci un nome per il tuo set di colori personalizzato nel campo "Nome".  

1. Fai clic sul pulsante "Salva" per salvare il tuo set di colori personalizzato. Il tuo set di colori personalizzato sarà ora disponibile nel menù a discesa "Colori" per un uso futuro.  

## **Come creare e applicare un set di colori in Aspose.Cells**  
Aspose.Cells offre funzionalità per personalizzare temi e colori.  

### **Come creare un tema di colori personalizzato in Aspose.Cells**  
Se nel file sono utilizzati i colori del tema, non è necessario modificare ogni cella singolarmente; basta modificare i colori nel tema.  

Nell'esempio seguente viene mostrato come applicare temi personalizzati con i colori desiderati. Utilizziamo un file modello creato manualmente in Microsoft Excel 2007.  

Il seguente esempio carica un file modello XLSX, definisce i colori per diversi tipi di colore del tema, applica i colori personalizzati e salva il file Excel.  

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



### **Come applicare colori tema in Aspose.Cells**  
Il seguente esempio applica i colori di primo piano e di carattere di una cella in base ai tipi di colore predefiniti del tema (del workbook). Salva anche il file Excel su disco.  


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


### **Come ottenere e impostare colori tema in Aspose.Cells**  
Di seguito sono riportati alcuni metodi e proprietà che implementano i colori tema.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): Usato per impostare il colore di primo piano.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): Usato per impostare il colore di sfondo.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): Usato per impostare il colore del font.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): Usato per ottenere un colore del tema.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): Usato per impostare un colore del tema.  

L'esempio seguente mostra come ottenere e impostare i colori del tema.  

Il seguente esempio utilizza un file modello XLSX, ottiene i colori per diversi tipi di colore del tema, modifica i colori e salva il file Microsoft Excel.  

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


## **Argomenti avanzati**  
- [Estrai dati tema dal file Excel](/cells/it/javascript-cpp/extract-theme-data-from-excel-file/)
