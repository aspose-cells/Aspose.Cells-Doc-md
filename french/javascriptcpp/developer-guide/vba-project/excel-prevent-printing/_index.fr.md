---
title: Comment empêcher les utilisateurs d imprimer le fichier Excel avec JavaScript via C++
linktitle: Comment empêcher les utilisateurs d imprimer un fichier Excel
type: docs
weight: 600
url: /fr/javascript-cpp/how-to-prevent-printing-excel/
description: Apprenez comment empêcher les utilisateurs d imprimer des fichiers Excel en utilisant Aspose.Cells for JavaScript via C++.
keywords: impression excel, empêcher l impression excel, comment empêcher les utilisateurs d imprimer excel, excel empêcher l impression, empêcher l impression d un classeur, Empêcher les utilisateurs d imprimer l ensemble du classeur avec VBA.
---

## **Scénarios d'utilisation possibles**  
Dans notre travail quotidien, il peut y avoir des informations importantes dans le fichier Excel; afin de protéger ces données internes de la diffusion, la société ne nous permettra pas de les imprimer. Ce document vous explique comment empêcher les autres d'imprimer des fichiers Excel.  

## **Comment empêcher les utilisateurs d'imprimer un fichier dans MS-Excel**  
Vous pouvez appliquer le code VBA suivant pour protéger votre fichier spécifique contre l'impression.  
1. Ouvrez votre classeur que vous ne permettez pas aux autres d'imprimer.  
1. Sélectionnez l'onglet "Développeur" dans le ruban Excel et cliquez sur le bouton "Afficher le code" dans la section "Contrôles". Alternativement, vous pouvez maintenir les touches ALT + F11 pour ouvrir la fenêtre **Visual Basic for Applications**.  
<br>  
<img src="1.png" width=70% />  
1. Ensuite, dans l'Explorateur de projets à gauche, double-cliquez sur ThisWorkbook pour ouvrir le module, et ajoutez des codes VBA.  
<br>  
<img src="2.png" width=70% />  
1. Ensuite, enregistrez et fermez ce code, revenez au classeur, et lorsque vous imprimez le fichier exemple, il ne sera pas autorisé à être imprimé, et une boîte d'avertissement apparaîtra :  
<br>  
<img src="3.png" width=70% />  

## **Comment empêcher les utilisateurs d'imprimer un fichier Excel en utilisant Aspose.Cells for JavaScript via C++**  

Le code d'exemple suivant illustre comment empêcher les utilisateurs d'imprimer un fichier Excel :  

1. Charger le [fichier d'exemple](sample.xlsx).  
1. Obtenez l'objet VbaModuleCollection à partir de la propriété VbaProject du classeur.  
1. Obtenez l'objet VbaModule via le nom "ThisWorkbook".  
1. Définissez la propriété codes de VbaModule.  
1. Enregistrez le fichier d'exemple au format [xlsm](out.xlsm).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
