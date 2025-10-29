---
title: Trimer les lignes et colonnes blanches en tête lors de l exportation de feuilles de calcul au format CSV avec JavaScript via C++
linktitle: Supprimer les lignes et colonnes vides initiales lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 100
url: /fr/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Apprenez comment supprimer les lignes et colonnes blanches en tête lors de l exportation de feuilles de calcul au format CSV en utilisant le script Aspose.Cells for Java via C++.
---

## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV contient des colonnes ou des lignes vides initiales. Par exemple, considérez cette ligne

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, Microsoft Excel ignore ces lignes et colonnes vides initiales.

Par défaut, le script Aspose.Cells for Java via C++ ne supprime pas les colonnes et lignes blanches en tête lors de la sauvegarde, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, alors Aspose.Cells fournit la propriété [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--). Veuillez la définir sur **true** et ainsi toutes les lignes et colonnes blanches en tête seront éliminées lors de la sauvegarde.

{{% alert color="primary" %}}

Avant la version 20.4 du script Aspose.Cells for Java via C++, la valeur par défaut de [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) était **false**. Depuis la version 20.4, la valeur par défaut de [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) est **true.**

{{% /alert %}}

## **Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV**

Le code suivant charge le [fichier Excel source](sampleTrimBlankColumns.xlsx) qui possède deux colonnes vides en tête. Il sauvegarde d'abord le fichier Excel au format CSV sans modification, puis définit la propriété [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) à **true** et le sauvegarde à nouveau. La capture d'écran montre le [fichier Excel source](sampleTrimBlankColumns.xlsx), le fichier CSV de sortie sans troncature, et le fichier CSV de sortie avec troncature.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Trim Blank Columns</title>
    </head>
    <body>
        <h1>Trim Blank Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a>
        <a id="downloadLink2" style="display: none; margin-left: 10px;">Download Result 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Load source workbook
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save in csv format (without trimming)
            const outputData1 = wb.save(SaveFormat.Csv);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithoutTrimBlankColumns.csv';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CSV Without Trimming';

            // Now save again with TrimLeadingBlankRowAndColumn as true
            const opts = new TxtSaveOptions();
            opts.trimLeadingBlankRowAndColumn = true;

            // Save in csv format (with trimming)
            const outputData2 = wb.save(opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputTrimBlankColumns.csv';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download CSV With Trimmed Blank Columns';

            resultDiv.innerHTML = '<p style="color: green;">Files generated. Use the links above to download the CSVs.</p>';
        });
    </script>
</html>
```
