---
title: Gestion des objets OLE avec JavaScript via C++
linktitle: Gestion des objets OLE
type: docs
weight: 50
url: /fr/javascript-cpp/managing-ole-objects/
description: Apprenez à gérer les objets OLE dans Aspose.Cells for JavaScript via C++. Ajoutez, extrayez et manipulez des objets OLE dans les feuilles de calcul.
---

## **Introduction**  

OLE (Linking et Embedding d’Objets) est un cadre pour la technologie de documents composés. En bref, un document composé est quelque chose comme un bureau d'affichage pouvant contenir des objets visuels et informatifs de toutes sortes : texte, calendriers, animations, sons, vidéos en mouvement, 3D, actualités mises à jour en continu, contrôles, etc. Chaque objet de bureau est une entité de programme indépendante pouvant interagir avec un utilisateur et aussi communiquer avec d'autres objets sur le bureau.  

OLE est supporté par de nombreux programmes différents et est utilisé pour rendre le contenu créé dans un programme accessible dans un autre. Par exemple, vous pouvez insérer un document Microsoft Word dans Microsoft Excel. Pour voir quels types de contenu vous pouvez insérer, cliquez sur **Objet** dans le menu **Insertion**. Seuls les programmes installés sur l'ordinateur et supportant les objets OLE apparaissent dans la boîte **Type d'objet**.  

### **Insertion d'objets OLE dans la feuille de calcul**  

Aspose.Cells for JavaScript via C++ supporte l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. C'est pourquoi, Aspose.Cells possède la classe [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection), utilisée pour ajouter un nouvel objet OLE à la collection. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), représente un objet OLE. Elle possède plusieurs membres importants :  

- La propriété [**imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.  
- La propriété [**objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) spécifie les données de l'objet sous forme de tableau d'octets. Ces données seront affichées dans leur programme associé lors d'un double-clic sur l'icône de l'objet OLE.  

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.  

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

### **Extraction d'objets OLE dans le classeur**  

L'exemple suivant montre comment extraire des objets OLE dans un classeur. L'exemple récupère différents objets OLE à partir d'un fichier XLS existant et enregistre différents fichiers (DOC, XLS, PPT, PDF, etc.) en fonction du type de format de fichier de l'objet OLE.  

Après l'exécution du code, nous pouvons enregistrer différents fichiers en fonction de leurs types de format respectifs des objets OLE.  

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

### **Extraction des fichiers MOL intégrés**  

Aspose.Cells for JavaScript via C++ supporte l'extraction d'objets de types peu courants comme MOL (fichier de données moléculaires contenant des informations sur les atomes et les liaisons). Le code suivant montre comment extraire un fichier MOL intégré et l'enregistrer sur le disque en utilisant ce [fichier Excel d'exemple](94896196.xlsx).  

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

## **Sujets avancés**  
- [Accéder et modifier l'étiquette d'affichage de l'objet Ole lié](/cells/fr/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Rafraîchir automatiquement un objet OLE via Microsoft Excel en utilisant Aspose.Cells](/cells/fr/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extraire des objets OLE du classeur](/cells/fr/javascript-cpp/extract-ole-objects-from-workbook/)  
- [Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé](/cells/fr/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Insérer un fichier WAV en tant qu'objet Ole](/cells/fr/javascript-cpp/inserting-a-wav-file-as-an-ole-object/)
