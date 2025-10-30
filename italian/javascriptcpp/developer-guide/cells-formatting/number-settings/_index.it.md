---
title: Impostazioni numero
linktitle: Impostazioni numero
description: Aspose.Cells è una libreria JavaScript per lavorare con file di fogli di calcolo che supporta molte impostazioni diverse del numero di celle. Questo articolo introduce come usare la libreria Aspose.Cells per gestire le impostazioni numeriche delle celle per regolare i formati numerici nei fogli di calcolo.
keywords: Aspose.Cells, libreria JavaScript, foglio elettronico, impostazioni del numero di cella, formattazione, gestione, formati di numeri e date
type: docs
weight: 10
url: /it/javascript-cpp/cells-number-settings/
---

## **Come impostare i formati di visualizzazione dei numeri e delle date**  

Una funzione molto potente di Microsoft Excel è che permette agli utenti di impostare i formati di visualizzazione dei valori numerici e delle date. Sappiamo che i dati numerici possono essere usati per rappresentare valori diversi tra cui decimali, valute, percentuali, frazioni o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in formati diversi a seconda del tipo di informazione che rappresentano. Allo stesso modo, ci sono molti formati in cui una data o ora può essere visualizzata.  
Aspose.Cells supporta questa funzionalità e consente agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.  

### **Come impostare i formati di visualizzazione in Microsoft Excel**  

Per impostare i formati di visualizzazione in Microsoft Excel:  

1. Fai clic con il pulsante destro del mouse su qualsiasi cella.  
2. Selezionare **Formato celle**. Apparirà una finestra di dialogo che permette di impostare i formati di visualizzazione di qualsiasi tipo di valore.  

Sul lato sinistro della finestra di dialogo, ci sono molte categorie di valori come **Generale**, **Numero**, **Valuta**, **Contabile**, **Data**, **Ora**, **Percentuale**, ecc. Aspose.Cells supporta tutti questi formati di visualizzazione.  

Aspose.Cells fornisce un modulo, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che rappresenta un file Excel. Il modulo [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dal modulo [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Il modulo [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) rappresenta un oggetto del modulo [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).  

Aspose.Cells fornisce la proprietà [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) per il modulo [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Questa proprietà viene usata per ottenere e impostare il formato di una cella. Il modulo [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) fornisce alcune proprietà utili per gestire i formati di visualizzazione di numeri e date.  

### **Come utilizzare i formati numerici incorporati**  

Aspose.Cells offre alcuni formati numerici integrati per configurare i formati di visualizzazione di numeri e date. Questi formati numerici integrati possono essere applicati usando la proprietà [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) dell'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Tutti i formati numerici integrati sono assegnati a valori numerici unici. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato alla proprietà [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) dell'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) per applicare il formato di visualizzazione. Questo metodo è veloce. I formati numerici integrati supportati da Aspose.Cells sono elencati di seguito.  

|**Valore**|**Tipo**|**Stringa di formato**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **Come utilizzare i formati numerici personalizzati**  

Per definire la propria stringa di formato personalizzata per impostare il formato di visualizzazione, utilizzare la proprietà [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) dell'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Questo metodo non è rapido come l'uso di formati preimpostati, ma è più flessibile.  

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

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

Se si utilizza la proprietà [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) per impostare il formato numerico, qualsiasi formato precedente impostato con la proprietà [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) viene sovrascritto e viceversa.  

{{% /alert %}}  

## **Argomenti avanzati**  
- [Verificare il formato numerico personalizzato quando si imposta Style.Custom Property](/cells/it/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Elenco dei formati numerici supportati](/cells/it/javascript-cpp/list-of-supported-number-formats/)  
- [Render Personalizzare data formato modello g e ge mm dd](/cells/it/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Specificare Personalizzare numerico Decimale e Gruppo Separatori per Cartella di lavoro](/cells/it/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Specifica di formattazione pattern personalizzato DBNum](/cells/it/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
