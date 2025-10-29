---
title: Obtenez des avertissements lors du chargement du fichier Excel avec JavaScript via C++
linktitle: Obtenir des avertissements lors du chargement du fichier Excel
type: docs
weight: 110
url: /fr/javascript-cpp/get-warnings-while-loading-excel-file/
description: Apprenez à capturer les avertissements lors du chargement d’un fichier Excel en utilisant Aspose.Cells for JavaScript via C++. Gérez efficacement les classeurs corrompus mais chargeables.
---

## **Scénarios d'utilisation possibles**

Parfois, l’utilisateur tente de charger un classeur qui est quelque peu corrompu mais pouvant être chargé. Dans ce cas, Aspose.Cells génère des avertissements lors du chargement du classeur. Ces avertissements peuvent être interceptés en implémentant l’interface [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) et en configurant la propriété [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--).

## **Obtenir des avertissements lors du chargement d'un fichier Excel**

Le code d’exemple suivant explique comment obtenir des avertissements lors du chargement d’un fichier Excel. Le code charge le [fichier Excel d’exemple](sampleDuplicateDefinedName.xlsx) qui affiche un avertissement [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) lors du chargement. Cet avertissement est ensuite capturé par la méthode [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) qui affiche les messages d’avertissement sur la console. Ensuite, le code enregistre le classeur sous le nom [fichier Excel de sortie](outputDuplicateDefinedName.xlsx). Si vous ouvrez le fichier Excel dans Microsoft Excel, ce dernier affichera également cet avertissement comme montré dans cette capture d’écran. Veuillez également vérifier la sortie de la console pour mieux comprendre.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **Sortie console**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
