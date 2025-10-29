---
title: Obtenez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter 
type: docs  
weight: 320  
url: /fr/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Apprenez comment obtenir tous les indices de lignes cachées après avoir rafraîchi AutoFilter en utilisant le script Aspose.Cells for Java via API C++.  
keywords: Obtenir tous les indices de lignes cachées après le rafraîchissement d AutoFilter en JavaScript via C++, Obtenir tous les indices de lignes cachées après le rafraîchissement d AutoFilter en JavaScript via C++, Récupérer tous les indices de lignes cachées après le rafraîchissement d AutoFilter en JavaScript via C++  
---

## **Scénarios d'utilisation possibles**  

Lorsque vous appliquez un filtre automatique sur des cellules de la feuille de calcul, certaines lignes sont automatiquement masquées. Mais il se peut que certaines lignes soient déjà masquées manuellement par l'utilisateur Excel et ne soient pas masquées par un filtre automatique. Il devient donc difficile de savoir quelles lignes sont masquées par le filtre automatique et lesquelles le sont manuellement. Le script Aspose.Cells for Java via C++ traite ce problème à l’aide de l’Array [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-). Cette méthode renvoie les indices de toutes les lignes qui sont masquées par le filtre automatique mais pas manuellement par l’utilisateur Excel.  

## **Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre**  

Veuillez voir le code exemple suivant qui charge le fichier Excel [exemple](64716909.xlsx) contenant certaines lignes masquées manuellement par l'utilisateur Excel. Le code applique le filtre automatique et le rafraîchit en utilisant la méthode [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-) qui retourne les indices des lignes masquées par le filtre automatique. Il affiche ensuite les indices des lignes masquées sur la console avec les noms et valeurs des cellules.  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Sortie console**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
