---
title: Schriftarteinstellungen mit JavaScript über C++
linktitle: Schriftart Einstellungen
description: Aspose.Cells ist eine JavaScript Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt das Festlegen der Schriftarteinstellungen von Zellen und ermöglicht es Benutzern, den Schriftstil und die Eigenschaften von Zellen anzupassen. Dieser Artikel stellt vor, wie man die Aspose.Cells Bibliothek verwendet, um die Schriftarteinstellungen von Zellen festzulegen.
keywords: Aspose.Cells, Zellen, Schriftarteinstellungen, Stile, Eigenschaften, JavaScript über C++
type: docs
weight: 30
url: /de/javascript-cpp/cells-font-settings/
---

{{% alert color="primary" %}}  
Das Erscheinungsbild eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können den Namen, den Stil, die Größe, die Farbe und andere Effekte der Schriftarten umfassen. Ganz wie Microsoft Excel unterstützt auch Aspose.Cells das Konfigurieren der Schriftarteinstellungen von Zellen.  
{{% /alert %}}  

## **Konfigurieren von Schriftarteinstellungen**  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse dar.  

Aspose.Cells bietet die [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Klasse mit den [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) und [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)-Methoden, die zum Abrufen und Festlegen des Formatierungsstils einer Zelle verwendet werden. Die [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Klasse bietet Eigenschaften zum Konfigurieren der Schriftarteinstellungen.  

### **Schriftartname festlegen**  

Entwickler können jede Schriftart auf den Text in einer Zelle anwenden, indem sie die [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)-Methode des [**name**](https://reference.aspose.com/cells/javascript-cpp/font/#name-string-)-Objekts verwenden.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font name to "Times New Roman"
            style.font.name = "Times New Roman";

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Schriftschnitt auf Fett setzen**  

Entwickler können den Text fett machen, indem sie die [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)-Objekt [**isBold**](https://reference.aspose.com/cells/javascript-cpp/font/#isBold-boolean-) Methode auf **true** setzen.   

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font weight to bold
            style.font.isBold = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and A1 updated. Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **Schriftgröße festlegen**  

Stellen Sie die Schriftgröße mit der [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)-Objekt [**size**](https://reference.aspose.com/cells/javascript-cpp/font/#size-number-)-Methode ein.  

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
            const resultDiv = document.getElementById('result');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.count;
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font size to 14
            style.font.size = 14;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Schriftfarbe festlegen**  

Verwenden Sie die [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)-Methode des [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-)-Objekts, um die Schriftfarbe festzulegen. Wählen Sie eine beliebige Farbe aus der Color-Enumeration (Teil von JavaScript) aus und weisen Sie diese der [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-)-Methode zu.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Worksheet and Set Cell Style Example</h1>
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
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font color to blue
            style.font.color = AsposeCells.Color.Blue;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Schriftart-Unterstrich-Typ festlegen**  

Verwenden Sie die [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) Objekt- [**underline**](https://reference.aspose.com/cells/javascript-cpp/font/#underline-fontunderlinetype-) Methode, um Text zu unterstreichen. Aspose.Cells bietet verschiedene vordefinierte Unterstreichungstypen in der [**FontUnderlineType**](https://reference.aspose.com/cells/javascript-cpp/fontunderlinetype) Enumeration.  

|**Schriftart-Unterstreichungstypen**|**Beschreibung**|  
| :- | :- |  
|Accounting|Einzelne Buchhaltungsunterstreichung|  
|Double|Doppelte Unterstreichung|  
|DoubleAccounting|Doppelte Buchhaltungsunterstreichung|  
|None|Keine Unterstreichung|  
|Single|Einfache Unterstreichung|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontUnderlineType } = AsposeCells;

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font to be underlined
            style.font.underline = FontUnderlineType.Single;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready to download.</p>';
        });
    </script>
</html>
```


### **Einstellung des Durchgestrichen-Effekts**  

Strichen Sie durch, indem Sie die [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) Objekt- [**isStrikeout**](https://reference.aspose.com/cells/javascript-cpp/font/#isStrikeout-boolean-) Methode auf **true** setzen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the strike out effect on the font
            style.font.isStrikeout = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Einstellen des Tiefgestellt-Effekts**  

Apply subscript by setting the [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) object's [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) method to **true**.  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Add Worksheet</h1>
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
            const resultDiv = document.getElementById('result');

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet and get its index
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access the "A1" cell
            const cell = worksheet.cells.get("A1");

            // Set value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtain the style of the cell
            const style = cell.style;

            // Set strikeout on the font
            style.font.isStrikeout = true;

            // Apply the style to the cell
            cell.style = style;

            // Save the workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **Einstellen des Hochgestellt-Effekts auf Schriftart**  

Entwickler können den Hochstelleneffekt auf die Schriftart anwenden, indem sie die [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) Methode des [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) Objekts auf **true** setzen.  

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting superscript effect
            style.font.isSuperscript = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


## **Erweiterte Themen**  
- [Hoch- und Tiefgestellt-Effekte auf Schriftarten anwenden](/cells/de/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen](/cells/de/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
