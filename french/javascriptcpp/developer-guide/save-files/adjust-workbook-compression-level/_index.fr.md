---
title: Ajuster le niveau de compression du classeur avec JavaScript via C++
linktitle: Ajuster le niveau de compression du classeur
type: docs
weight: 180
url: /fr/javascript-cpp/adjust-workbook-compression-level/
description: Apprenez comment ajuster le niveau de compression du classeur dans Aspose.Cells for JavaScript via C++.
---

## **Ajuster le niveau de compression du classeur**

Les développeurs peuvent ajuster le niveau de compression du classeur lorsqu'ils travaillent avec des classeurs plus volumineux. Les développeurs peuvent privilégier des tailles de fichier plus petites ou un temps de traitement plus court. Aspose.Cells for JavaScript via C++ fournit l'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) que vous pouvez utiliser pour définir le niveau de compression du classeur. L'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) offre les membres suivants.

- Niveau1 : La compression la plus rapide mais la moins efficace.  
- Niveau2 : Un peu plus lent, mais meilleur, que le niveau 1.  
- Niveau3 : Un peu plus lent, mais meilleur, que le niveau 2.  
- Niveau4 : Un peu plus lent, mais meilleur, que le niveau 3.  
- Level5: Un peu plus lent que le niveau 4, mais avec une meilleure compression.  
- Level6: Un bon équilibre entre la vitesse et l'efficacité de la compression.  
- Niveau7 : Compression vraiment bonne!  
- Level8: Meilleure compression que le niveau 7!  
- Niveau9 : La meilleure compression, où la meilleure signifie la plus grande réduction de la taille du flux de données d'entrée. C'est aussi la compression la plus lente.  

Le code suivant démontre l'utilisation de l'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) et compare le temps de conversion pour le Niveau1, Niveau6 et Niveau9. Vous pouvez également comparer les tailles des fichiers générés.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save XLSB with Compression Levels</title>
    </head>
    <body>
        <h1>Save XLSB with Different Compression Levels</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right:10px;"></a>
            <a id="downloadLink2" style="display: none; margin-right:10px;"></a>
            <a id="downloadLink3" style="display: none;"></a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsbSaveOptions, OoxmlCompressionType, Utils } = AsposeCells;

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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');
            const downloadLink3 = document.getElementById('downloadLink3');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create Xlsb save options
            const options = new XlsbSaveOptions();

            // Level 1
            let start = performance.now();
            options.compressionType = OoxmlCompressionType.Level1;
            const outputData1 = workbook.save(SaveFormat.Xlsb, options);
            let elapsedMs1 = performance.now() - start;

            const blob1 = new Blob([outputData1]);
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'LargeSampleFile_level_1_out.xlsb';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Level 1 XLSB';

            // Level 6
            start = performance.now();
            options.compressionType = OoxmlCompressionType.Level6;
            const outputData2 = workbook.save(SaveFormat.Xlsb, options);
            let elapsedMs2 = performance.now() - start;

            const blob2 = new Blob([outputData2]);
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'LargeSampleFile_level_6_out.xlsb';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Level 6 XLSB';

            // Level 9
            start = performance.now();
            options.compressionType = OoxmlCompressionType.Level9;
            const outputData3 = workbook.save(SaveFormat.Xlsb, options);
            let elapsedMs3 = performance.now() - start;

            const blob3 = new Blob([outputData3]);
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'LargeSampleFile_level_9_out.xlsb';
            downloadLink3.style.display = 'inline-block';
            downloadLink3.textContent = 'Download Level 9 XLSB';

            resultDiv.innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <ul>
                    <li>Level 1 Elapsed Time: ${elapsedMs1.toFixed(2)} ms</li>
                    <li>Level 6 Elapsed Time: ${elapsedMs2.toFixed(2)} ms</li>
                    <li>Level 9 Elapsed Time: ${elapsedMs3.toFixed(2)} ms</li>
                </ul>
            `;
        });
    </script>
</html>
```
