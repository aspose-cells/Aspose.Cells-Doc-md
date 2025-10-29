---
title: Optimisation de l utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données
type: docs
weight: 110
url: /fr/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Lors de la construction d'un classeur avec de grands ensembles de données, ou de la lecture d'un gros fichier Microsoft Excel, la quantité totale de RAM que le processus va prendre est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face au défi. Aspose.Cells propose des options et des appels API pertinents pour réduire, réduire et optimiser l'utilisation de la mémoire. De plus, cela peut aider le processus à travailler de manière plus efficace et à s'exécuter plus rapidement.

Utiliser l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) pour optimiser l'utilisation de la mémoire utilisée pour les données des cellules afin de réduire le coût total de la mémoire. Lors de la construction d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).

{{% /alert %}}

## **Optimisation de la mémoire**

L’exemple suivant montre comment optimiser l’utilisation de la mémoire lors du travail avec de grandes quantités de données en Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Attention**

L'option par défaut, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) est appliquée pour toutes les versions. Pour certaines situations, telles que la construction d'un classeur avec un grand ensemble de données pour les cellules, l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) peut optimiser l'utilisation de la mémoire et réduire le coût de la mémoire pour l'application. Cependant, cette option peut dégrader les performances dans certains cas particuliers comme suit.

1. **Accéder de manière aléatoire et répétée aux cellules**: La séquence la plus efficace pour accéder à la collection de cellules est cellule par cellule dans une rangée, puis rangée par rangée. Surtout, si vous accédez aux lignes/cellules par l'énumérateur acquis à partir de [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) et [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), les performances seraient maximisées avec [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
1. **Insertion & Suppression de cellules & de rangées**: Veuillez noter que s'il y a beaucoup d'opérations d'insertion/suppression de Cellules/Rangées, la dégradation des performances sera notable pour le mode [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) par rapport au mode [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/). 
1. **Traitement sur différents types de cellules**: Si la plupart des cellules contiennent des valeurs de chaîne ou des formules, le coût de la mémoire sera le même que le mode [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) mais s'il y a beaucoup de cellules vides, ou les valeurs des cellules sont numériques, booléennes, etc., l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) offrira de meilleures performances.
