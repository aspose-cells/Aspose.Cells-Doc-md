---
title: Créer et copier des plages nommées avec JavaScript via C++
linktitle: Créer un accès et copier les plages nommées
type: docs
weight: 200
url: /fr/javascript-cpp/create-access-and-copy-named-ranges/
description: Apprenez comment créer, accéder et copier des plages nommées dans Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Introduction**  

Normalement, les étiquettes de colonne et de ligne sont utilisées pour faire référence à des cellules individuelles. Il est possible de créer des noms descriptifs pour représenter des cellules, plages de cellules, formules ou valeurs constantes. Le mot **nom** peut se référer à une chaîne de caractères représentant une cellule, une plage de cellules, une formule ou une valeur constante. Assigner un nom à une plage signifie que cette plage de cellules peut être référencée par son nom. Utilisez des noms faciles à comprendre, comme Produits, pour faire référence à des plages difficiles à comprendre, comme Ventes!C20:C30. Les étiquettes peuvent être utilisées dans des formules qui font référence à des données sur la même feuille; si vous souhaitez représenter une plage sur une autre feuille, vous pouvez utiliser un nom. *Les plages nommées sont parmi les fonctionnalités les plus puissantes de Microsoft Excel, en particulier lorsqu'elles sont utilisées comme plage source pour des contrôles de liste, des tableaux croisés dynamiques, des graphiques, etc.*  

## **Travailler avec les plages nommées en utilisant Microsoft Excel**  

### **Créer des plages nommées**  

 Les étapes suivantes décrivent comment nommer une cellule ou une plage de cellules en utilisant **MS Excel**. Cette méthode s'applique à **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, et **2002**.  

1. Sélectionnez la cellule ou la plage de cellules que vous souhaitez nommer.  
2. Cliquez sur la **zone de nom** à l'extrémité gauche de la barre de formule.  
3. Tapez le nom pour les cellules.  
4. Appuyez sur ENTER.  

{{% alert color="primary" %}}  
Vous ne pouvez pas nommer une cellule pendant que vous modifiez le contenu de la cellule.  
{{% /alert %}}  

## **Travailler avec la plage nommée en utilisant Aspose.Cells**  

Ici, nous utilisons l'API Aspose.Cells pour effectuer la tâche.  
Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).  

### **Créer une plage nommée**  

Il est possible de créer une plage nommée en appelant la méthode surchargée [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Une version typique de la méthode [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) prend les paramètres suivants :  

- Nom de la cellule en haut à gauche, nom de la cellule en haut à gauche dans la plage.  
- Nom de la cellule inférieure droite, le nom de la cellule inférieure droite de la plage.  

Lorsque la méthode [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) est appelée, elle renvoie la plage nouvellement créée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). Utilisez cet objet [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) pour configurer la plage nommée. Par exemple, définissez le nom de la plage en utilisant la propriété [**name**](https://reference.aspose.com/cells/javascript-cpp/range/#name--). L'exemple suivant montre comment créer une plage nommée de cellules qui s'étend de B4 à G14.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating a named range
            const range = worksheet.cells.createRange("B4", "G14");

            // Setting the name of the named range
            range.name = "TestRange";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Saisir des données dans les cellules de la plage nommée**  

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le modèle  

- **JavaScript**: Plage[ligne,colonne]  

Disons que vous avez une plage nommée de cellules qui s'étend de A1 à C4. La matrice comprend 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].  

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :  

- firstRow renvoie l'indice de la première ligne dans la plage nommée.  
- firstColumn renvoie l'indice de la première colonne dans la plage nommée.  
- rowCount renvoie le nombre total de lignes dans la plage nommée.  
- columnCount renvoie le nombre total de colonnes dans la plage nommée.  

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = workbook.worksheets.get(0);

            // Create a range of cells based on H1:J4.
            const range = worksheet1.cells.createRange("H1", "J4");

            // Name the range.
            range.name = "MyRange";

            // Input some data into cells in the range.
            range.get(0, 0).value = "USA";
            range.get(0, 1).value = "SA";
            range.get(0, 2).value = "Israel";
            range.get(1, 0).value = "UK";
            range.get(1, 1).value = "AUS";
            range.get(1, 2).value = "Canada";
            range.get(2, 0).value = "France";
            range.get(2, 1).value = "India";
            range.get(2, 2).value = "Egypt";
            range.get(3, 0).value = "China";
            range.get(3, 1).value = "Philipine";
            range.get(3, 2).value = "Brazil";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rangecells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range populated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **Identifier les cellules dans la plage nommée**  

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le schéma :  

- **JavaScript**: Plage[ligne,colonne]  

Si vous avez une plage nommée qui s'étend de A1 à C4, la matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0] ,Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].  

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :  

- firstRow renvoie l'indice de la première ligne dans la plage nommée.  
- firstColumn renvoie l'indice de la première colonne dans la plage nommée.  
- rowCount renvoie le nombre total de lignes dans la plage nommée.  
- columnCount renvoie le nombre total de colonnes dans la plage nommée.  

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Named Range</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Getting the specified named range
            const range = workbook.worksheets.rangeByName("TestRange");

            if (!range) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
                return;
            }

            // Identify range cells and display properties
            const firstRow = range.firstRow;
            const firstColumn = range.firstColumn;
            const rowCount = range.rowCount;
            const columnCount = range.columnCount;

            const html = [
                `<p>First Row : ${firstRow}</p>`,
                `<p>First Column : ${firstColumn}</p>`,
                `<p>Row Count : ${rowCount}</p>`,
                `<p>Column Count : ${columnCount}</p>`
            ].join('');

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

### **Accéder aux plages nommées**  

#### **Accéder à une plage nommée spécifique**  

Appelez la méthode [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) de la collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) pour obtenir une plage par le nom spécifié. Une méthode [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) typique prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). L'exemple suivant montre comment accéder à une plage spécifiée par son nom.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const worksheets = workbook.worksheets;
            const range = worksheets.rangeByName("TestRange");

            if (range !== null) {
                document.getElementById('result').innerHTML = `<p>Named Range : ${range.refersTo}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
            }
        });
    </script>
</html>
```  

#### **Accéder à toutes les plages nommées dans une feuille de calcul**  

Appelez la méthode [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) de la collection [**worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) pour obtenir toutes les plages nommées dans une feuille de calcul. La méthode [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) retourne un tableau de toutes les plages nommées dans la collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).  

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Named Ranges</title>
    </head>
    <body>
        <h1>Get Named Ranges Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting all named ranges
            const ranges = workbook.worksheets.namedRanges;

            if (ranges) {
                // Some collections expose 'count', others may expose 'length'
                const total = (typeof ranges.count !== 'undefined') ? ranges.count : ranges.length;
                document.getElementById('result').innerHTML = `<p style="color: green;">Total Number of Named Ranges: ${total}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No named ranges found.</p>';
            }
        });
    </script>
</html>
```  

### **Copier les plages nommées**  

Aspose.Cells fournit la méthode [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-pasteoptions-) pour copier une plage de cellules avec mise en forme dans une autre plage.  

L'exemple suivant montre comment copier une plage source de cellules dans une autre plage nommée.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Ranges</title>
    </head>
    <body>
        <h1>Copy Ranges Example</h1>
        <p>Select an Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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

            // Instantiate a new Workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            const range1 = worksheet.cells.createRange("E12", "I12");

            // Name the range.
            range1.name = "MyRange";

            // Set the outline border to the range.
            range1.outlineBorder = { borderType: BorderType.TopBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.BottomBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.LeftBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.RightBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };

            // Input some data with some formattings into a few cells in the range.
            range1.get(0, 0).putValue("Test");
            range1.get(0, 4).putValue("123");

            // Create another range of cells.
            const range2 = worksheet.cells.createRange("B3", "F3");

            // Name the range.
            range2.name = "testrange";

            // Copy the first range into second range.
            range2.copy(range1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyranges.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
