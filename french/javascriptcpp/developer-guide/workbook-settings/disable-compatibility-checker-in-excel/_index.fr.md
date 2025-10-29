---
title: Désactiver le Vérificateur de compatibilité dans Excel avec JavaScript via C++
linktitle: Désactiver le vérificateur de compatibilité dans Excel
type: docs
weight: 170
url: /fr/javascript-cpp/disable-compatibility-checker-in-excel/
description: Découvrez comment désactiver le vérificateur de compatibilité via le Script Aspose.Cells for Java avec l’API C++.
keywords: Désactiver le Vérificateur de compatibilité en JavaScript, Désactiver le Vérificateur de compatibilité dans Excel en JavaScript via C++, Désactiver le Vérificateur de compatibilité dans le classeur.
---

## Désactiver le Vérificateur de compatibilité dans les feuilles Excel en JavaScript  

{{% alert color="primary" %}}  
Le vérificateur de compatibilité de Microsoft Excel signale lorsque la sauvegarde d'un fichier dans un format de fichier antérieur pourrait entraîner des problèmes de fonctionnalité ou une perte de fidélité. Le vérificateur de compatibilité est une fonctionnalité de Microsoft Office Excel 2007 et de Microsoft Excel 2010.  

Lorsque vous enregistrez un classeur dans une version antérieure, Excel 97 à Excel 2003, à partir d'Excel 2007 ou d'Excel 2010, le vérificateur de compatibilité analyse le classeur pour voir s'il contient des fonctionnalités qui ne sont pas prises en charge par la version antérieure. Pour vous aider à prendre des décisions sur la manière de gérer les problèmes de compatibilité, le vérificateur de compatibilité affiche des boîtes de dialogue avec des options. Il peut également être utilisé pour créer un rapport sur les problèmes dans le classeur, ou désactiver la fonctionnalité.  

Parfois, vous avez besoin de désactiver le vérificateur de compatibilité pour une feuille de calcul particulière. Avec les API Aspose.Cells, vous pouvez le faire de manière programmatique afin que les utilisateurs ne soient pas frustrés ou confus par la boîte de dialogue du Vérificateur de compatibilité qui s'affiche lorsqu'ils sauvegardent manuellement le fichier dans Microsoft Excel.  
{{% /alert %}}  

## **Comment désactiver le vérificateur de compatibilité à l'aide de Microsoft Excel**  

Pour désactiver le vérificateur de compatibilité dans Microsoft Excel (par exemple Microsoft Excel 2007/2010) :  

- (Excel 2007) Sur le bouton Office, cliquez sur **Préparer**, puis sur **Exécuter le vérificateur de compatibilité**, puis désactivez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.  
- (Excel 2010) Sur l'onglet **Fichier**, cliquez sur **Informations**, puis **Vérifier les problèmes**, cliquez sur **Vérifier la compatibilité**, et enfin, désélectionnez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.  

## **Comment désactiver le vérificateur de compatibilité à l'aide des API Aspose.Cells**  

Définissez la propriété [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) sur **false** pour désactiver le Vérificateur de compatibilité de Microsoft Excel.  

### **Exemples de code**  

Les exemples de code suivants montrent comment désactiver le Vérificateur de compatibilité avec le Script Aspose.Cells for Java via C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
