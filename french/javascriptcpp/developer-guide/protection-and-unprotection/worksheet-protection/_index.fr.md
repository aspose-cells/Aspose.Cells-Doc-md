---
title: Protéger et déprotéger la feuille de calcul avec JavaScript via C++
linktitle: Protéger et déprotéger la feuille de calcul
type: docs
weight: 40
url: /fr/javascript-cpp/protect-and-unprotect-worksheets/
description: Protéger et déprotéger la feuille de calcul des fichiers Excel avec le script Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Pour empêcher d'autres utilisateurs de modifier, déplacer ou supprimer accidentellement ou délibérément des données dans une feuille de calcul, vous pouvez verrouiller les cellules de votre feuille de calcul Excel, puis protéger la feuille avec un mot de passe.  
{{% /alert %}}  

## **Protéger et déprotéger une feuille de calcul dans MS Excel**  

**![Protéger et déprotéger la feuille de calcul](protéger-et-déprotéger-la-feuille-de-calcul.png)**  

1. Cliquez sur **Révision > Protéger la feuille**.  
1. Entrez un mot de passe dans **la boîte de mot de passe**.  
1. Sélectionnez les options **autoriser**.  
1. Sélectionnez **OK**, saisissez à nouveau le mot de passe pour le confirmer, puis sélectionnez à nouveau **OK**.  

## **Protéger la feuille de calcul en utilisant le script Aspose.Cells for JavaScript via C++**  
Il suffit d'utiliser les lignes de code suivantes pour implémenter la protection de la structure du classeur Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Déprotéger la feuille de calcul en utilisant le script Aspose.Cells for JavaScript via C++**  
La déprotection de la feuille de calcul est facile avec l'API Aspose.Cells. Si la feuille est protégée par mot de passe, un mot de passe correct est requis.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Sujets avancés**  
- [Paramètres de protection avancés depuis Excel XP](/cells/fr/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Détecter si la feuille de calcul est protégée par mot de passe](/cells/fr/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Protection des feuilles de calcul](/cells/fr/javascript-cpp/protecting-worksheets/)  
- [Déprotéger une feuille de calcul](/cells/fr/javascript-cpp/unprotect-a-worksheet/)  
- [Vérifier le mot de passe utilisé pour protéger la feuille de calcul](/cells/fr/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
