---
title: Bilder und Formen in Excel Dateien mit JavaScript via C++ einfügen  
linktitle: Formen  
type: docs  
weight: 140  
url: /de/javascript-cpp/insert-shapes/  
description: Verwalten von Bildern, OLE Objekten und Formen in Excel Dateien mit Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}  
Manchmal müssen Sie einige notwendige Formen in das Arbeitsblatt einfügen. Sie müssen möglicherweise die gleiche Form an verschiedenen Positionen des Arbeitsblatts einfügen. Oder Sie müssen Stapel von Formen in das Arbeitsblatt einfügen.  
Keine Sorge! [Aspose.Cells](https://products.aspose.com/cells/) unterstützt all diese Operationen.  
{{% /alert %}}  

Die Formen in Excel werden hauptsächlich in die folgenden Typen unterteilt:  
- **Bilder**  
- **OLE-Objekte**  
- **Linien**  
- **Rechtecke**  
- **Grundformen**  
- **Blockpfeile**  
- **Gleichungsformen**  
- **Flussdiagramme**  
- **Sterne und Banner**  
- **Legenden**  

Dieses Leitfadendokument wählt eine oder zwei Formen aus jedem Typ aus, um Muster zu erstellen. Durch diese Beispiele lernen Sie, wie man [Aspose.Cells](https://products.aspose.com/cells/) benutzt, um die angegebene Form in das Arbeitsblatt einzufügen.  

## **Hinzufügen von Bildern im Excel-Arbeitsblatt mit JavaScript**  

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:  
Rufen Sie einfach die [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)-Methode der [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)-Sammlung auf (verkapselt im [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Objekt). Die [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)-Methode nimmt folgende Parameter:   

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.  
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.  
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.  

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

## **Einfügen von OLE-Objekten in Excel-Arbeitsblätter mit JavaScript**  

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Verwalten von OLE-Objekten in Arbeitsblättern. Zu diesem Zweck enthält Aspose.Cells die [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection)-Klasse, die verwendet wird, um ein neues OLE-Objekt zur Sammlungsliste hinzuzufügen. Eine andere Klasse, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), stellt ein OLE-Objekt dar. Sie besitzt einige wichtige Mitglieder:  

- Die [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--)-Eigenschaft gibt die Bild- (Symbol-) Daten vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt zu zeigen.  
- Die [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--)-Eigenschaft gibt die Objekt-Daten in Form eines Byte-Arrays an. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie doppelt auf das OLE-Objekt-Icon klicken.  

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.  

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

## **Einfügen einer Linie in das Excel-Arbeitsblatt mit JavaScript**  

Die Form der Linie gehört zur Kategorie **Linien**.  

*  

- Wählen Sie die Zelle aus, in die Sie die Linie einfügen möchten.  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann die Linie aus 'Kürzlich verwendete Formen' oder 'Linien'  

![](line.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um eine Linie im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Die Methode gibt ein [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man eine Linie in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](line2.png)  

## **Einfügen eines Linienpfeils in das Excel-Arbeitsblatt mit JavaScript**  

Der Form des Linienpfeils gehört zur Kategorie **Linien**. Es ist eine Spezialform der Linie.  

*  

- Wählen Sie die Zelle aus, in der Sie den Linienpfeil einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann den Linienpfeil aus 'Kürzlich verwendete Formen' oder 'Linien'  

![](line_arrow1.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um einen Linienpfeil in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Die Methode gibt ein [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man einen Linienpfeil in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](line_arrow2.png)  

## **Einfügen eines Rechtecks in das Excel-Arbeitsblatt mit JavaScript**  

Die Form des Rechtecks gehört zur Kategorie **Rechtecke**.  

*  

- Wählen Sie die Zelle, in die Sie das Rechteck einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann das Rechteck aus 'Kürzlich verwendete Formen' oder 'Rechtecke'  

![](rectangle.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um ein Rechteck im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Die Methode gibt ein [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man ein Rechteck in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](rectangle2.png)  

## **Einfügen eines Würfels in das Excel-Arbeitsblatt mit JavaScript**  

Die Form des Würfels gehört zur Kategorie **Grundformen**.  

*  

- Wählen Sie die Zelle, in die Sie den Würfel einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann den Würfel aus **Grundformen**  

![](cube.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um einen Würfel im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man einen Würfel in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](cube2.png)  

## **Einfügen eines Callout-Quadrupelpfeils in das Excel-Arbeitsblatt mit JavaScript**  

Die Form des Callout-Quadratpfeils gehört zur Kategorie **Blockpfeile**.  

*  

- W�hlen Sie die Zelle aus, in die Sie den Callout-Quad-Pfeil einf�gen m�chten.  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann den Callout-Quadratpfeil aus **Blockpfeile**  

![](callout_quad_arrow.png)  

***Mit Aspose.Cells verwenden***  

Sie k�nnen die folgende Methode verwenden, um einen Callout-Quad-Pfeil in das Arbeitsblatt einzuf�gen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man eine Callout-Quadratapplikation in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](callout_quad_arrow2.png)  

## **Einfügen eines Multiplikationszeichens in das Excel-Arbeitsblatt mit JavaScript**  

Die Form des Multiplikationszeichens gehört zur Kategorie **Gleichungsformen**.  

*  

- Wählen Sie die Zelle aus, in der Sie das Multiplikationszeichen einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie das Multiplikationszeichen aus **Gleichungsformen**  

![](multiplication_sign.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um ein Multiplikationszeichen im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man ein Multiplikationszeichen in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](multiplication_sign2.png)  

## **Einfügen eines Multidokument in das Excel-Arbeitsblatt mit JavaScript**  

Die Form des Multi-Dokuments gehört zur Kategorie **Flowcharts**.  

*  

- Wählen Sie die Zelle aus, in der Sie das Multi-Dokument einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie das Multi-Dokument aus **Flowcharts**  

![](multidocument.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um ein Multidokument in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man ein Multi-Dokument in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](multidocument2.png)  

## **Einfügen eines fünfzackigen Sterns in das Excel-Arbeitsblatt mit JavaScript**  

Die Form des fünfzackigen Sterns gehört zur Kategorie **Sterne und Banner**.  

*  

- Wählen Sie die Zelle aus, in die Sie den Fünfzackigen Stern einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie den fünfzackigen Stern aus **Sterne und Banner**  

![](star_5_points.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um einen Fünfzackigen Stern in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man einen fünfzackigen Stern in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](star_5_points2.png)  

## **Einfügen einer Gedankenblase in das Excel-Arbeitsblatt mit JavaScript**  

Die Form der Gedankenblasenwolke gehört zur Kategorie **Callouts**.  

*  

- Wählen Sie die Zelle aus, in die Sie die Gedankenblasenwolke einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie die Gedankenblasenwolke aus **Callouts**  

![](thought_bubble_cloud.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um eine Gedankenblasenwolke in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man eine Gedankenblasenwolke in ein Arbeitsblatt einfügt.  

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

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](thought_bubble_cloud2.png)  

## **Erweiterte Themen**  
- [Ändern der Anpassungswerte der Form](/cells/de/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [Formen zwischen Arbeitsblättern kopieren](/cells/de/javascript-cpp/copy-shapes-between-worksheets/)  
- [Daten in nicht primitiver Form](/cells/de/javascript-cpp/data-in-non-primitive-shape/)  
- [Absolute Position der Form im Arbeitsblatt finden](/cells/de/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Verbindungspunkte von Form erhalten](/cells/de/javascript-cpp/get-connection-points-from-shape/)  
- [Steuerungen verwalten](/cells/de/javascript-cpp/managing-controls/)  
- [Symbole zum Arbeitsblatt hinzufügen](/cells/de/javascript-cpp/insert-svg-to-excel/)  
- [OLE-Objekte verwalten](/cells/de/javascript-cpp/managing-ole-objects/)  
- [Bilder verwalten](/cells/de/javascript-cpp/managing-pictures/)  
- [SmartArt verwalten](/cells/de/javascript-cpp/managing-smartart/)  
- [TextBox verwalten](/cells/de/javascript-cpp/managing-textbox-of-excel/)  
- [Fügen Sie dem Arbeitsblatt eine WordArt-Wasserzeichen hinzu](/cells/de/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [Werte verlinkter Formen aktualisieren](/cells/de/javascript-cpp/refresh-values-of-linked-shapes/)  
- [Form nach vorn oder hinten im Arbeitsblatt senden](/cells/de/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Formoptionen verwalten](/cells/de/javascript-cpp/managing-shape-options/)  
- [Textoptionen der Form verwalten](/cells/de/javascript-cpp/managing-shape-text-options/)  
- [Weberweiterungen - Office-Add-Ins](/cells/de/javascript-cpp/web-extensions-office-add-ins/)
