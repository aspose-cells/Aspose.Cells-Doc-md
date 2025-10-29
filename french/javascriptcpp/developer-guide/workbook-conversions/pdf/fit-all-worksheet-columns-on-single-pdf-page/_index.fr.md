---
title: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF avec JavaScript via C++
linktitle: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 160
url: /fr/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Parfois, vous voulez générer un fichier PDF qui adapte toutes les colonnes d'une feuille de calcul sur une seule page. La propriété [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) offre cette fonctionnalité de manière très facile à utiliser. Les calculs complexes tels que la hauteur et la largeur du PDF de sortie sont gérés en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

## **Adapter les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) assure que toutes les colonnes d'une feuille sont rendues sur une seule page PDF, même si les lignes peuvent s'étendre sur plusieurs pages en fonction des données de la feuille.

Le code d'exemple ci-dessous montre comment utiliser la propriété [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) pour afficher une grande feuille de calcul de 100 colonnes.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Create and initialize an instance of Workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and initialize an instance of PdfSaveOptions
            const saveOptions = new PdfSaveOptions();
            // Set AllColumnsInOnePagePerSheet to true (converted from setter to property)
            saveOptions.allColumnsInOnePagePerSheet = true;

            // Save Workbook to PDF format by passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF généré peut afficher le contenu dans une taille très petite. Il reste lisible lorsqu'il est agrandi dans une application de visualisation telle que Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
