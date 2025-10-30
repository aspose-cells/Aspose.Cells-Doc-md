---
title: Inserisci immagini e forme nei file Excel con JavaScript tramite C++  
linktitle: Forme  
type: docs  
weight: 140  
url: /it/javascript-cpp/insert-shapes/  
description: Gestisci immagini, oggetti OLE e forme nei file Excel usando lo script Aspose.Cells for JavaScript tramite C++.  
---  

{{% alert color="primary" %}}  
A volte è necessario inserire alcune forme necessarie nel foglio di lavoro. Potresti dover inserire la stessa forma in posizioni diverse del foglio di lavoro. Oppure devi inserire in batch forme nel foglio di lavoro.  
Non preoccuparti! [Aspose.Cells](https://products.aspose.com/cells/) supporta tutte queste operazioni.  
{{% /alert %}}  

Le forme in Excel sono principalmente suddivise nei seguenti tipi:  
- **Immagini**  
- **Oggetti OLE**  
- **Linee**  
- **Rettangoli**  
- **Forme di base**  
- **Frecce a blocco**  
- **Forme di equazione**  
- **Diagrammi di flusso**  
- **Stelle e striscioni**  
- **Callout**  

Questo documento guida selezionerà una o due forme da ciascun tipo per creare dei campioni. Attraverso questi esempi, imparerai come usare [Aspose.Cells](https://products.aspose.com/cells/) per inserire la forma specificata nel foglio di lavoro.  

## **Aggiunta di immagini nel foglio di lavoro Excel usando JavaScript**  

Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:  
Basta chiamare il metodo [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) della raccolta [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Il metodo [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) accetta i seguenti parametri:  

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.  
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.  
- **Nome del file immagine**, il nome del file immagine, completo di percorso.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>
            Optional: select an existing Excel file to modify, or leave empty to create a new workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image to insert into the worksheet (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // If an Excel file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const arrayBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as Uint8Array
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Inserimento di oggetti OLE nel foglio di lavoro Excel usando JavaScript**  

Aspose.Cells supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells ha la classe [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection), usata per aggiungere un nuovo oggetto OLE alla lista di raccolta. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), rappresenta un oggetto OLE. Ha alcuni membri importanti:  

- La proprietà [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) specifica i dati dell'immagine (icona) di tipo array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.  
- La proprietà [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) specifica i dati dell'oggetto sotto forma di array di byte. Questi dati verranno visualizzati nel loro programma correlato quando fai doppio clic sull'icona dell'oggetto OLE.  

L'esempio seguente mostra come aggiungere un/i oggetto(i) OLE in un foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert OLE Object Example</h1>
        <p>
            Select an image to display as the OLE object's icon and an Excel file to embed as the OLE object.
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="excelInput" accept=".xls,.xlsx" />
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
            const excelInput = document.getElementById('excelInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE icon.</p>';
                return;
            }
            if (!excelInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file to embed.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const excelFile = excelInput.files[0];

            // Read files as ArrayBuffers
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const excelArrayBuffer = await excelFile.arrayBuffer();

            // Convert to Uint8Array for Aspose.Cells
            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(excelArrayBuffer);

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Set embedded ole object data.
            sheet.oleObjects.get(0).objectData = objectData;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object embedded successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Inserimento di una linea nel foglio di lavoro Excel usando JavaScript**  

La forma della linea appartiene alla categoria **lines**.  

*  

- Selezionare la cella dove si desidera inserire la linea  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Quindi, seleziona la linea tra le 'Forme recentemente usate' o 'Linee'  

![](line.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una linea nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

Il seguente esempio mostra come inserire una linea in un foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Line Example</h1>
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
            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Create workbook from uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Add the line to the worksheet
                sheet.shapes.addLine(2, 0, 2, 0, 100, 300);

                // Save workbook to XLSX format and create download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'sample.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Line added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](line2.png)  

## **Inserimento di una freccia a linea nel foglio di lavoro Excel usando JavaScript**  

La forma della freccia della linea appartiene alla categoria **Linee**. È un caso speciale di linea.  

*  

- Selezionare la cella dove si desidera inserire la freccia di linea  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona la freccia della linea da 'Forme usate di recente' o 'Linee'  

![](line_arrow1.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una freccia di linea nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire una freccia di linea in un foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Line Arrow Example</h1>
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

            // Loads the workbook which contains shapes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the line arrow to the worksheet
            let s = sheet.shapes.addLine(2, 0, 2, 0, 100, 300); // method 1
            // let s = sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
            // let s = sheet.shapes.addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

            // add a arrow at the line begin
            s.line.beginArrowheadStyle = AsposeCells.MsoArrowheadStyle.Arrow; // arrow type
            s.line.beginArrowheadWidth = AsposeCells.MsoArrowheadWidth.Wide; // arrow width
            s.line.beginArrowheadLength = AsposeCells.MsoArrowheadLength.Short; // arrow length

            // add a arrow at the line end
            s.line.endArrowheadStyle = AsposeCells.MsoArrowheadStyle.ArrowOpen; // arrow type
            s.line.endArrowheadWidth = AsposeCells.MsoArrowheadWidth.Narrow; // arrow width
            s.line.endArrowheadLength = AsposeCells.MsoArrowheadLength.Long; // arrow length

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.with_arrow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Arrow';

            document.getElementById('result').innerHTML = '<p style="color: green;">Arrow added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](line_arrow2.png)  

## **Inserimento di un rettangolo nel foglio di lavoro Excel usando JavaScript**  

La forma del rettangolo appartiene alla categoria **Rettangoli**.  

*  

- Selezionare la cella in cui si desidera inserire il rettangolo  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il rettangolo da 'Forme usate di recente' o 'Rettangoli'  

![](rectangle.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire un rettangolo nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un rettangolo in un foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Rectangle</title>
    </head>
    <body>
        <h1>Add Rectangle to Worksheet</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the rectangle to the worksheet
            sheet.shapes.addRectangle(2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rectangle added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](rectangle2.png)  

## **Inserimento di un cubo nel foglio di lavoro Excel usando JavaScript**  

La forma del cubo appartiene alla categoria **Forme di base**.  

*  

- Selezionare la cella in cui si desidera inserire il cubo  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il Cubo da **Forme di base**  

![](cube.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire un cubo nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un cubo in un foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Cube</title>
    </head>
    <body>
        <h1>Add Cube to Worksheet</h1>
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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the cube to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Cube added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](cube2.png)  

## **Inserimento di un callout con freccia a quadrato nel foglio di lavoro Excel usando JavaScript**  

La forma della freccia di testo appartiene alla categoria **Freccie di blocco**.  

*  

- Seleziona la cella in cui desideri inserire la freccia quadrupla di chiamata  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona la freccia di testo da **Freccie di blocco**  

![](callout_quad_arrow.png)  

***Utilizzando Aspose.Cells***  

Puoi utilizzare il seguente metodo per inserire una freccia quadrupla di chiamata nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire una freccia di testo in uno worksheet.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Callout Quad Arrow</title>
    </head>
    <body>
        <h1>Add Callout Quad Arrow Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            sheet.shapes.addAutoShape(AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](callout_quad_arrow2.png)  

## **Inserire un segno di moltiplicazione nel foglio di lavoro Excel usando JavaScript**  

La forma del simbolo di moltiplicazione appartiene alla categoria **Forme di equazione**.  

*  

- Seleziona la cella in cui desideri inserire il segno di moltiplicazione  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il simbolo di moltiplicazione da **Forme di equazione**  

![](multiplication_sign.png)  

***Utilizzando Aspose.Cells***  

Puoi utilizzare il seguente metodo per inserire un segno di moltiplicazione nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un simbolo di moltiplicazione in uno worksheet.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Multiply Sign</title>
    </head>
    <body>
        <h1>Add Multiplication Sign to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multiplication sign to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Multiplication sign added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](multiplication_sign2.png)  

## **Inserire un multidocumento nel foglio di lavoro Excel usando JavaScript**  

La forma del multidocumento appartiene alla categoria **FlowCharts**.  

*  

- Selezionare la cella in cui si desidera inserire il multidocumento  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il multidocumento da **FlowCharts**  

![](multidocument.png)  

***Utilizzando Aspose.Cells***  

Puoi utilizzare il seguente metodo per inserire un multidocumento nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un multidocumento in uno worksheet.  

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
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multidocument to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](multidocument2.png)  

## **Inserire una stella a cinque punte nel foglio di lavoro Excel usando JavaScript**  

La forma della stella a cinque punte appartiene alla categoria **Stelle e Bandiere**.  

*  

- Seleziona la cella in cui desideri inserire la stella a cinque punte  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Quindi, seleziona la stella a cinque punte da **Stelle e Bandiere**  

![](star_5_points.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una stella a cinque punte nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

Il seguente esempio mostra come inserire una stella a cinque punte in un foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Star Shape</title>
    </head>
    <body>
        <h1>Add Five-Pointed Star to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add the Five-pointed star to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Star shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](star_5_points2.png)  

## **Inserire una nuvola a bolla di pensiero nel foglio di lavoro Excel usando JavaScript**  

La forma della nuvola di pensieri appartiene alla categoria **Callouts**.  

*  

- Seleziona la cella in cui desideri inserire la nuvola a forma di fumetto  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Quindi, seleziona la nuvola di pensieri da **Callouts**  

![](thought_bubble_cloud.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una nuvola di pensiero nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

Il seguente esempio mostra come inserire una nuvola di pensieri nel foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Cloud Callout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the thought bubble cloud to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cloud callout added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](thought_bubble_cloud2.png)  

## **Argomenti avanzati**  
- [Modifica dei valori di regolazione della forma](/cells/it/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [Copia delle forme tra i fogli di lavoro](/cells/it/javascript-cpp/copy-shapes-between-worksheets/)  
- [Dati in forma non primitiva](/cells/it/javascript-cpp/data-in-non-primitive-shape/)  
- [Ricerca della posizione assoluta della forma all'interno del foglio di lavoro](/cells/it/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Ottieni punti di connessione dalla forma](/cells/it/javascript-cpp/get-connection-points-from-shape/)  
- [Gestione dei controlli](/cells/it/javascript-cpp/managing-controls/)  
- [Aggiungi icone al foglio di lavoro](/cells/it/javascript-cpp/insert-svg-to-excel/)  
- [Gestione di oggetti OLE](/cells/it/javascript-cpp/managing-ole-objects/)  
- [Gestione delle immagini](/cells/it/javascript-cpp/managing-pictures/)  
- [Gestisci Smart Art](/cells/it/javascript-cpp/managing-smartart/)  
- [Gestione casella di testo](/cells/it/javascript-cpp/managing-textbox-of-excel/)  
- [Aggiungere un'immagine WordArt al foglio di lavoro](/cells/it/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [Aggiornamento dei valori delle forme collegate](/cells/it/javascript-cpp/refresh-values-of-linked-shapes/)  
- [Invia la forma avanti o indietro all'interno del foglio di lavoro](/cells/it/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Gestire le opzioni di forma](/cells/it/javascript-cpp/managing-shape-options/)  
- [Gestire le opzioni di testo di forma](/cells/it/javascript-cpp/managing-shape-text-options/)  
- [Estensioni Web - Componenti aggiuntivi di Office](/cells/it/javascript-cpp/web-extensions-office-add-ins/)
