---
title: Impostare intestazioni e piè di pagina con JavaScript via C++
linktitle: Impostazione Intestazioni e piè di pagina
type: docs
weight: 30
url: /it/javascript-cpp/setting-headers-and-footers/
description: Questo articolo spiega come inserire programmaticamente un’immagine nell’intestazione e nel piè di pagina dei fogli di lavoro di Excel usando Aspose.Cells for JavaScript via C++. 
keywords: inserisci immagine nel piè di pagina intestazione di Excel JavaScript via C++, imposta comandi di script per intestazione e piè di pagina di Excel JavaScript via C++
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina sono le linee di testo visualizzate sotto il margine superiore o sopra il margine inferiore rispettivamente. È possibile aggiungere intestazioni e piè di pagina anche ai fogli di lavoro. Le intestazioni e i piè di pagina possono essere utilizzati per visualizzare informazioni utili come il numero di pagina, il nome dell'autore, il nome del tema o la data e l'ora. Le intestazioni e i piè di pagina sono gestiti utilizzando le impostazioni della pagina di setup.

{{% /alert %}}

## **Impostazione di intestazioni e piè di pagina**

Aspose.Cells for JavaScript via C++ permette di aggiungere intestazioni e piè di pagina ai fogli di lavoro in fase di esecuzione, ma si consiglia di impostare manualmente intestazioni e piè di pagina in un file pre-progettato per la stampa. Puoi usare Microsoft Excel come strumento GUI per impostare intestazioni e piè di pagina, risparmiando tempo di sviluppo. Aspose.Cells può importare il file e salvare le impostazioni.

Per aggiungere intestazioni e piè di pagina in fase di esecuzione, Aspose.Cells fornisce chiamate API speciali e comandi di script per formattare intestazioni e piè di pagina.

### **Comandi di script**

I comandi di script sono comandi speciali che consentono di impostare la formattazione di intestazioni e piè di pagina.

|**Comandi di script**|**Descrizione**|
| :- | :- |
|&P|Numero di pagina corrente|
|&G|Un'immagine|
|&N|Il numero totale di pagine|
|&D|La data corrente|
|&T|L'orario corrente|
|&A|Il nome del foglio di lavoro|
|&F|Il nome del file senza percorso|
|&&Testo|Mostra &Testo. Per esempio: &&WO sarà visualizzato come &WO|
|&"\<FontName>"|Rappresenta un nome di carattere. Ad esempio: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Rappresenta il nome del carattere con lo stile. Ad esempio: &"Arial,Grassetto"|
|&\<FontSize>|Rappresenta la dimensione del carattere. Ad esempio: “&14abc”. Ma, se questo comando è seguito da un numero normale da stampare nell'intestazione, questo dovrebbe essere separato da un carattere spazio dalla dimensione del carattere. Ad esempio: “&14 123”.|

### **Imposta Intestazioni e Piè di Pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) fornisce due metodi, [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) e [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-), usati per aggiungere intestazioni e piè di pagina a un foglio di lavoro. Questi metodi accettano solo due parametri:

- **Sezione** – la sezione in cui dovrebbe essere posizionata l'intestazione o il piè di pagina. Ci sono tre sezioni: sinistra, centro e destra, rappresentate rispettivamente da 0, 1 e 2.
- **Script** – lo script da utilizzare per l'intestazione o il piè di pagina. Questo script contiene comandi di script per formattare l'intestazione o il piè di pagina.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Inserire un'immagine nell'intestazione o nel piè di pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) ha altri due metodi, [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) e [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-), usati per inserire immagini nelle intestazioni e nei piè di pagina. Questi metodi accettano i parametri:

- **Sezione** – la sezione dell'intestazione o del piè di pagina in cui verrà posizionata l'immagine. Ci sono tre sezioni, sinistra, centro e destra, rappresentate dai valori 0, 1 e 2 rispettivamente.
- **Array di byte** – i dati grafici (i dati binari devono essere scritti nel buffer di un array di byte).

Dopo aver eseguito il codice sottostante e aperto il file, controlla l'intestazione del foglio di lavoro:

1. Nel menu **File**, seleziona **Imposta pagina**. Verrà visualizzata una finestra di dialogo.
1. Seleziona la scheda **Intestazione/Piè di pagina**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
