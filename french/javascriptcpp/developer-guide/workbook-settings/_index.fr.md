---
title: Gérer les paramètres des fichiers de feuilles Excel avec JavaScript via C++
linktitle: Paramètres du classeur
type: docs
weight: 185
url: /fr/javascript-cpp/workbook-settings/
description: Gérer les paramètres des fichiers Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Vue d'ensemble des paramètres du classeur**
Travailler avec des fichiers Excel implique divers paramètres qui peuvent être manipulés programmatiquement en utilisant Aspose.Cells for JavaScript via C++. Ce document décrit comment gérer efficacement ces paramètres.

## **Scénarios d'utilisation possibles**
Les scénarios suivants illustrent quand vous pourriez avoir besoin de gérer les paramètres du classeur :
- Ajustement des options d'affichage
- Définir le mode de calcul
- Configuration des paramètres de mise en page

## **Gestion des paramètres du classeur en utilisant Aspose.Cells for JavaScript via C++**
Cet exemple démontre comment gérer les paramètres du classeur tels que les options de calcul et d'affichage.

1. Créez un nouveau classeur ou chargez-en un existant.
2. Modifiez les paramètres du classeur selon vos besoins.
3. Enregistrez le classeur pour conserver les changements.

### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Propriétés et méthodes clés des paramètres du classeur**
Aspose.Cells for JavaScript via C++ offre plusieurs propriétés et méthodes pour ajuster les paramètres du classeur :
- **Workbook.settings** : Accède aux paramètres du classeur.
- **Settings.calculationMode** : Définit le mode de calcul pour le classeur.
- **Settings.showGridLines** : Active ou désactive les lignes de grille à l'écran.

## **Conclusion**
Gérer les paramètres du classeur en Aspose.Cells for JavaScript via C++ est simple et offre de nombreuses options pour personnaliser le comportement des fichiers Excel. En utilisant les paramètres disponibles, vous pouvez adapter le classeur à vos besoins spécifiques.
