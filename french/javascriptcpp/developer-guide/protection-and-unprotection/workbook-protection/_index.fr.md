---
title: Protéger et Déprotéger la structure du classeur avec JavaScript via C++
linktitle: Protéger et déprotéger la structure du classeur
type: docs
weight: 40
url: /fr/javascript-cpp/protect-and-unprotect-workbook-structure/
description: Protéger et déprotéger la structure du classeur des fichiers Excel en utilisant JavaScript via C++.
---


{{% alert color="primary" %}}  
Pour empêcher les autres utilisateurs de voir des feuilles de calcul cachées, d'ajouter, de déplacer, de supprimer ou de masquer des feuilles de calcul, et de renommer des feuilles de calcul, vous pouvez protéger la structure de votre classeur Excel avec un mot de passe.  
{{% /alert %}}  


## **Protéger et déprotéger la structure du classeur dans MS Excel**  

**![Protéger et déprotéger la structure du classeur](protect-and-unprotect-workbook-structure.png)**  

1. Cliquez sur **Relecture > Protéger le classeur**.  
1. Entrez un mot de passe dans **la boîte de mot de passe**.  
1. Sélectionnez **OK**, saisissez à nouveau le mot de passe pour le confirmer, puis sélectionnez à nouveau **OK**.  


## **Protéger la structure du classeur en utilisant le script Aspose.Cells for JavaScript via C++**  
Il suffit d'utiliser les lignes de code suivantes pour implémenter la protection de la structure du classeur Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Protect workbook structure with a password
            workbook.protect(ProtectionType.Structure, "password");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1_protected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Déprotéger la structure du classeur en utilisant le script Aspose.Cells for JavaScript via C++**  
La déprotection de la structure du classeur est facile avec l'API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Unprotect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Workbook</button>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            workbook.unprotect("password");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/(\.xlsx|\.xls|\.csv)$/i, '');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook structure unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Remarque : un mot de passe correct est requis.  
{{% /alert %}}
