---
title: Définir le mode de calcul des formules du classeur avec JavaScript via C++
linktitle: Définir le mode de calcul de formule du classeur
description: Cet article présente comment définir le mode de calcul des formules d un classeur dans Microsoft Excel avec Aspose.Cells for JavaScript via C++. En chargeant un fichier Excel existant ou en créant un nouveau, nous pouvons utiliser la propriété fournie par Aspose.Cells pour définir le mode de calcul des formules et obtenir le résultat. Enfin, nous sauvegardons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, classeur, mode de calcul de formule, paramètres, JavaScript via C++
type: docs
weight: 110
url: /fr/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excel vous permet de définir le mode de calcul de formule, c'est-à-dire la manière dont les formules sont calculées. Il existe trois valeurs possibles  

- Automatique - recalculer chaque fois qu'une modification est apportée, et à chaque ouverture d'un classeur.  
- Automatique sauf pour les tables de données - recalculer chaque fois qu'une modification est apportée, mais en excluant les tables de données.  
- Manuel - recalculer seulement lorsque l'utilisateur le demande explicitement en appuyant sur F9 ou CTRL+ALT+F9, ou lorsque le classeur est enregistré.  
{{% /alert %}}  

Pour définir le mode de calcul des formules dans Microsoft Excel :  

1. Sélectionnez **Formules** puis **Options de calcul**.  
1. Sélectionnez l'une des options.  

Aspose.Cells for JavaScript via C++ permet également de définir le **Mode de Calcul de Formule** en utilisant la propriété [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--) du mode. Vous pouvez lui attribuer l'énumération [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype) qui possède l'une des valeurs suivantes :  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
