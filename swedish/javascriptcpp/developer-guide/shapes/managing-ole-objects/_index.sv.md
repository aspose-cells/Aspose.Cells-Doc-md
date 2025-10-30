---
title: Hantera OLE objekt med JavaScript via C++
linktitle: Hantera OLE objekt
type: docs
weight: 50
url: /sv/javascript-cpp/managing-ole-objects/
description: Lär dig hur man hanterar OLE objekt i Aspose.Cells for JavaScript via C++. Lägg till, extrahera och manipulera OLE objekt inom kalkylblad.
---

## **Introduktion**  

OLE (Object Linking and Embedding) är ett ramverk för sammansatta dokumentteknologier. Kort sagt är ett sammansatt dokument något som en skrivbordsmiljö som kan innehålla visuella och informationsobjekt av alla slag: text, kalendrar, animationer, ljud, rörelsevideo, 3D, kontinuerligt uppdaterade nyheter, kontroller och så vidare. Varje skrivbordsobjekt är en självständig programenhet som kan interagera med användaren och även kommunicera med andra objekt på skrivbordet.  

OLE stöds av många olika program och används för att göra innehåll som skapats i ett program tillgängligt i ett annat. Till exempel kan du infoga ett Microsoft Word-dokument i Microsoft Excel. För att se vilka typer av innehåll du kan infoga, klicka på **Objekt** i **Infoga**-menyn. Endast program som är installerade på datorn och stödjer OLE-objekt visas i rutan **Objekttyp**.  

### **Infoga OLE-objekt i arbetsbladet**  

Aspose.Cells for JavaScript via C++ stöder att lägga till, extrahera och manipulera OLE-objekt i kalkylblad. Av den anledningen har Aspose.Cells klassen [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection), som används för att lägga till ett nytt OLE-objekt till samlingen. En annan klass, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:  

- Egenskapen [**imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) specificerar bild (ikonen) data av typ byte-array. Bilden kommer att visas för att visa OLE-objektet i kalkbladet.  
- Egenskapen [**objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) specificerar objektets data i form av en byte-array. Denna data kommer att visas i det relaterade programmet när du dubbelklickar på OLE-objektets ikon.  

Följande exempel visar hur man lägger till en OLE-objekt/-objekt i ett arbetsblad.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add OLE Object Example</title>
    </head>
    <body>
        <h1>Add OLE Object Example</h1>
        <p>
            Select an image to display for the OLE object (e.g., logo.jpg) and a file to embed into the OLE object (e.g., book1.xls).
        </p>
        <label>Image (for OLE display): <input type="file" id="imageInput" accept="image/*" /></label>
        <br/>
        <label>Object to embed (e.g., .xls): <input type="file" id="objectInput" accept=".xls,.xlsx,.doc,.docx,.pdf" /></label>
        <br/>
        <button id="runExample">Add OLE Object and Save</button>
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
            const imageInput = document.getElementById('imageInput');
            const objectInput = document.getElementById('objectInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE display.</p>';
                return;
            }
            if (!objectInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a file to embed into the OLE object.</p>';
                return;
            }

            // Read files
            const imageFile = imageInput.files[0];
            const objectFile = objectInput.files[0];

            const imageBuffer = await imageFile.arrayBuffer();
            const objectBuffer = await objectFile.arrayBuffer();

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            // Position: row 14, column 3, width 200, height 220 (same as JavaScript example)
            sheet.oleObjects.add(14, 3, 200, 220, new Uint8Array(imageBuffer));

            // Set embedded ole object data (converted setter to property assignment)
            sheet.oleObjects.get(0).objectData = new Uint8Array(objectBuffer);

            // Save the excel file (Excel97To2003 format to match .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Extrahera OLE-objekt i arbetsboken**  

Följande exempel visar hur man extraherar OLE-objekt i en arbetsbok. Exemplet hämtar olika OLE-objekt från en befintlig XLS-fil och sparar olika filer (DOC, XLS, PPT, PDF etc.) baserat på OLE-objektets filformatstyp.  

Efter att ha kört koden kan vi spara olika filer baserat på deras respektive OLE-objektets format.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Extract OLE Objects</title>
    </head>
    <body>
        <h1>Extract OLE Objects from Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Extract OLE Objects</button>
        <div id="downloadContainer"></div>
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
            const downloadContainer = document.getElementById('downloadContainer');
            const result = document.getElementById('result');
            downloadContainer.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the OleObject Collection in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const oles = worksheet.oleObjects;

            // Loop through all the oleobjects and extract each object.
            for (let i = 0; i < oles.count; i++) {
                const ole = oles.get(i);

                // Specify the output filename.
                let ext = 'jpg';

                // Specify each file format based on the oleobject format type.
                switch (ole.fileFormatType) {
                    case AsposeCells.FileFormatType.Doc:
                        ext = "doc";
                        break;
                    case AsposeCells.FileFormatType.Xlsx:
                        ext = "xlsx";
                        break;
                    case AsposeCells.FileFormatType.Ppt:
                        ext = "ppt";
                        break;
                    case AsposeCells.FileFormatType.Pdf:
                        ext = "pdf";
                        break;
                    case AsposeCells.FileFormatType.Unknown:
                        ext = "jpg";
                        break;
                    default:
                        ext = "bin";
                        break;
                }

                const fileName = `ole_${i}.${ext}`;

                // Save the oleobject as a new excel file if the object type is xlsx.
                if (ole.fileFormatType === AsposeCells.FileFormatType.Xlsx) {
                    const ms = new Uint8Array(ole.objectData);
                    const oleBook = new Workbook(ms);
                    oleBook.settings.isHidden = false;
                    const outputData = oleBook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = `Excel_File${i}.out.xlsx`;
                    link.textContent = `Download Excel_File${i}.out.xlsx`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                } else {
                    // Create the files based on the oleobject format types.
                    const data = ole.objectData;
                    const blob = new Blob([data]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                }
            }

            result.innerHTML = '<p style="color: green;">OLE object extraction completed. Use the links above to download the files.</p>';
        });
    </script>
</html>
```  

### **Extrahera inbäddad MOL-fil**  

Aspose.Cells for JavaScript via C++ stöder att extrahera objekt av sällsynta typer som MOL (molekylär datafil innehållande information om atomer och bindningar). Följande kodsnutt visar hur man extraherar en inbäddad MOL-fil och sparar den till disk med hjälp av denna [exempelfil i Excel](94896196.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects Example</title>
    </head>
    <body>
        <h1>Extract OLE Objects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            let index = 1;

            const worksheets = workbook.worksheets;
            const sheetCount = worksheets.count;
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            for (let i = 0; i < sheetCount; i++) {
                const sheet = worksheets.get(i);
                const oles = sheet.oleObjects;
                const oleCount = oles.count;
                for (let j = 0; j < oleCount; j++) {
                    const ole = oles.get(j);
                    const data = ole.objectData;
                    const blob = new Blob([data], { type: 'application/octet-stream' });
                    const url = URL.createObjectURL(blob);
                    const fileName = `OleObject${index}.mol`;
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    resultDiv.appendChild(link);
                    index++;
                }
            }

            if (!resultDiv.hasChildNodes()) {
                resultDiv.innerHTML = '<p>No OLE objects found in the workbook.</p>';
            } else {
                const info = document.createElement('p');
                info.style.color = 'green';
                info.textContent = 'OLE objects extracted. Click the links to download the extracted .mol files.';
                resultDiv.insertBefore(info, resultDiv.firstChild);
            }
        });
    </script>
</html>
```  

## **Fortsatta ämnen**  
- [Åtkomst och ändring av visningsmärket för det länkade OLE-objektet](/cells/sv/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Automatisk uppdatering av OLE-objekt via Microsoft Excel med Aspose.Cells](/cells/sv/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extrahera OLE-objekt från arbetsboken](/cells/sv/javascript-cpp/extract-ole-objects-from-workbook/)  
- [Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet](/cells/sv/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Infoga en WAV-fil som ett Ole-objekt](/cells/sv/javascript-cpp/inserting-a-wav-file-as-an-ole-object/)
