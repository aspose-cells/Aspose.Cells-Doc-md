---
title: Infoga bilder och former i Excel filer med JavaScript via C++  
linktitle: Former  
type: docs  
weight: 140  
url: /sv/javascript-cpp/insert-shapes/  
description: Hantera bilder, OLE objekt och former i Excel filer med Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}  
Ibland måste du infoga vissa nödvändiga former i kalkylbladet. Du kan behöva infoga samma form på olika positioner i kalkylbladet. Eller så måste du batchinfoga former i kalkylbladet.  
Var inte orolig! [Aspose.Cells](https://products.aspose.com/cells/) stöder alla dessa operationer.  
{{% /alert %}}  

Former i Excel är huvudsakligen indelade i följande typer:  
- **Bilder**  
- **OleObjekt**  
- **Linjer**  
- **Rektanglar**  
- **Grundformer**  
- **Blockpilar**  
- **Ekvationformer**  
- **Flödesscheman**  
- **Stjärnor och banderoller**  
- **Inrop**  

Detta guide-dokument kommer att välja en eller två former från varje typ för att skapa exempel. Genom dessa exempel kommer du att lära dig hur du använder [Aspose.Cells](https://products.aspose.com/cells/) för att infoga den specificerade formen i kalkylbladet.  

## **Lägga till Bilder i Excel-Arbetsblad med JavaScript**  

Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:  
 Anropa helt enkelt [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)-metoden för [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) objektet). [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)-metoden tar följande parametrar:  

- **Övre vänstra radindex**, indexet för den övre vänstra raden.  
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.  
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.  

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

## **Infoga OLE-objekt i Excel-Arbetsblad med JavaScript**  

Aspose.Cells stöder tillägg, extrahering och manipulation av OLE-objekt i kalkylblad. Av denna anledning har Aspose.Cells klassen [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection), som används för att lägga till ett nytt OLE-objekt till listan. En annan klass, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:  

- Egenskapen [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) specificerar bild (ikonen) data av typ byte-array. Bilden kommer att visas för att visa OLE-objektet i kalkbladet.  
- Egenskapen [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) specificerar objektets data i form av en byte-array. Denna data kommer att visas i det relaterade programmet när du dubbelklickar på OLE-objektets ikon.  

Följande exempel visar hur man lägger till en OLE-objekt/-objekt i ett arbetsblad.  

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

## **Infoga en linje i Excel-Arbetsblad med JavaScript**  

Linjens form tillhör kategorin **lines**.  

*  

- Välj cellen där du vill infoga linjen  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan linjen från 'Senast använda former' eller 'Lines'  

![](line.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en linje i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Metoden returnerar ett [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en linje i ett kalkylblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](line2.png)  

## **Infoga en linjepil i Excel-Arbetsblad med JavaScript**  

Formen av linjepilen tillhör kategorin **Lines**. Det är ett specialfall av linje.  

*  

- Välj cellen där du vill infoga linjepilen  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan linjepilen från 'Senast använda former' eller 'Lines'  

![](line_arrow1.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en linjepil i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Metoden returnerar ett [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en linje pil i ett kalkylblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](line_arrow2.png)  

## **Infoga en rektangel i Excel-Arbetsblad med JavaScript**  

Formen av rektangeln tillhör kategorin **Rectangles**.  

*  

- Välj cellen där du vill infoga rektangeln  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan rektangeln från 'Senast använda former' eller 'Rectangles'  

![](rectangle.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en rektangel i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Metoden returnerar ett [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett rektangel i ett kalkylblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](rectangle2.png)  

## **Infoga en kub i Excel-Arbetsblad med JavaScript**  

Kubens form tillhör kategorin **Grundformer**.  

*  

- Välj cellen där du vill infoga kuben  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan Kuben från **Grundformer**  

![](cube.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en kub i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/javascript-cpp/shape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en kub i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](cube2.png)  

## **Infoga en callout-quad-pekare i Excel-Arbetsblad med JavaScript**  

Formen av callout-quad-kommando tillhör kategorin **Blockpilar**.  

*  

- Välj cellen där du vill infoga återuppringningspilar  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan callout-quad-kommando från **Blockpilar**  

![](callout_quad_arrow.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga återuppringningspilar i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/javascript-cpp/shape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett callout-quad-kommando i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](callout_quad_arrow2.png)  

## **Infoga multiplikationstecken till Excel-arbetsblad med JavaScript**  

Formen av multiplikationstecknet tillhör kategorin **Ekvationsformer**.  

*  

- Välj cellen där du vill infoga multiplikationstecknet  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan multiplikationstecknet från **Ekvationsformer**  

![](multiplication_sign.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga ett multiplikationstecken i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/javascript-cpp/shape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett multiplikations-tecken i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](multiplication_sign2.png)  

## **Infoga ett flerdokument till Excel-arbetsblad med JavaScript**  

Formen av flerdokumentet tillhör kategorin **Flödesscheman**.  

*  

- Välj cellen där du vill infoga multi-dokument  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan flerdokumentet från **Flödesscheman**  

![](multidocument.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga ett multi-dokument i arbetsbladet.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/javascript-cpp/shape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett flerdokument i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](multidocument2.png)  

## **Infoga en femuddig stjärna till Excel-arbetsblad med JavaScript**  

Formen av femuddig stjärna tillhör kategorin **Stjärnor och Band**.  

*  

- Välj cellen där du vill infoga Femuddig stjärna  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan femuddig stjärna från **Stjärnor och Band**  

![](star_5_points.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en Femuddig stjärna i arbetsbladet.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/javascript-cpp/shape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en femuddig stjärna i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](star_5_points2.png)  

## **Infoga en tankebubbla till Excel-arbetsblad med JavaScript**  

Formen av tankebubblan tillhör kategorin **Callouts**.  

*  

- Välj cellen där du vill infoga pratbubblan  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan tankebubblan från **Callouts**  

![](thought_bubble_cloud.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en pratbubbla i arbetsbladet.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/javascript-cpp/shape)-objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en tankebubbla i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](thought_bubble_cloud2.png)  

## **Fortsatta ämnen**  
- [Ändra justeringsvärden för formen](/cells/sv/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [Kopiera former mellan kalkylblad](/cells/sv/javascript-cpp/copy-shapes-between-worksheets/)  
- [Data i icke-primitiv form](/cells/sv/javascript-cpp/data-in-non-primitive-shape/)  
- [Hitta absolut position av formen inuti kalkylbladet](/cells/sv/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Hämta anslutningspunkter från formen](/cells/sv/javascript-cpp/get-connection-points-from-shape/)  
- [Hantera kontroller](/cells/sv/javascript-cpp/managing-controls/)  
- [Lägg till ikoner i kalkylbladet](/cells/sv/javascript-cpp/insert-svg-to-excel/)  
- [Hantera OLE-objekt](/cells/sv/javascript-cpp/managing-ole-objects/)  
- [Hantera bilder](/cells/sv/javascript-cpp/managing-pictures/)  
- [Hantera SmartArt](/cells/sv/javascript-cpp/managing-smartart/)  
- [Hantera TextBox](/cells/sv/javascript-cpp/managing-textbox-of-excel/)  
- [Lägg till WordArt-vattenstämpel på arbetsbladet](/cells/sv/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [Uppdatera värdena i länkade former](/cells/sv/javascript-cpp/refresh-values-of-linked-shapes/)  
- [Skicka form framåt eller bakåt inne i Arbetsbladet](/cells/sv/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Hantera formalternativ](/cells/sv/javascript-cpp/managing-shape-options/)  
- [Hantera textalternativ för formen](/cells/sv/javascript-cpp/managing-shape-text-options/)  
- [Webbutökningar - Office-tillägg](/cells/sv/javascript-cpp/web-extensions-office-add-ins/)
