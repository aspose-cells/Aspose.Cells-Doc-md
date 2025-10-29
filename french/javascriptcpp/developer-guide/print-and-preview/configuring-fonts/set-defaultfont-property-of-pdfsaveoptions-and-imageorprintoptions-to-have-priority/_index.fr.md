---
title: Définir la propriété DefaultFont des options PdfSaveOptions et ImageOrPrintOptions pour prioriser avec JavaScript via C++
linktitle: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions afin de lui donner la priorité
type: docs
weight: 30
url: /fr/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Découvrez comment définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions en utilisant Aspose.Cells for JavaScript via C++. Assurez un rendu correct des polices lorsque des polices manquent.
---

## **Scénarios d'utilisation possibles**

En définissant la propriété **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), vous pourriez vous attendre à ce que l'enregistrement en PDF ou en image définit cette police par défaut pour tout le texte dans un classeur qui a une police manquante (non installée).

En général, lors de l'enregistrement en PDF ou en image, Aspose.Cells for JavaScript via C++ tentera d'abord de définir la police par défaut du classeur (`Workbook.DefaultStyle.Font`). Si la police par défaut du classeur ne peut toujours pas afficher/rendre le texte correctement, alors Aspose.Cells tentera de rendre avec la police mentionnée dans l'attribut DefaultFont dans [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions). 

Pour répondre à votre attente, nous avons une propriété booléenne nommée "**CheckWorkbookDefaultFont**" dans [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). Vous pouvez la définir sur **false** pour désactiver l'essai de la police par défaut du classeur ou laisser la définition de **DefaultFont** dans [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

Le code d'exemple suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille) a un texte défini sur "Christmas Time Font text". Le nom de la police est "Christmas Time Personal Use" qui n'est pas installée sur la machine. Nous définissons l'attribut **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) à "Times New Roman". Nous configurons également la propriété booléenne **CheckWorkbookDefaultFont** à **"false"** pour garantir que le texte de la cellule A1 est rendu avec la police "Times New Roman" et ne doit pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code rend la première feuille en formats PNG et TIFF. Finalement, il la rend en format PDF.

{{% alert color="primary" %}}

La valeur par défaut de l'attribut **CheckWorkbookDefaultFont** est **true**.

{{% /alert %}}

Il s'agit de la capture d'écran du [fichier modèle](49446913.xlsx) utilisé dans le code exemple.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Voici l’image PNG de sortie après avoir réglé la propriété [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) à "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Voir l’image [TIFF](48496672.tiff) de sortie après avoir réglé la propriété [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) à "Times New Roman".

Voir le fichier [PDF](48496673.pdf) après avoir réglé la propriété [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) à "Times New Roman".

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Default Font for Export (PNG, TIFF, PDF)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadPng" style="display: none;">Download PNG</a><br/>
            <a id="downloadTiff" style="display: none;">Download TIFF</a><br/>
            <a id="downloadPdf" style="display: none;">Download PDF</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender, WorkbookRender, PdfSaveOptions } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Rendering to PNG while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            const imgOpt = new ImageOrPrintOptions();
            imgOpt.imageType = ImageType.Png;
            imgOpt.checkWorkbookDefaultFont = false;
            imgOpt.defaultFont = "Times New Roman";

            const sr = new SheetRender(workbook.worksheets.get(0), imgOpt);
            const pngData = sr.toImage(0);
            const pngBlob = new Blob([pngData], { type: 'image/png' });
            const downloadPng = document.getElementById('downloadPng');
            downloadPng.href = URL.createObjectURL(pngBlob);
            downloadPng.download = 'out1_imagePNG.png';
            downloadPng.style.display = 'inline-block';
            downloadPng.textContent = 'Download PNG';

            // Rendering to TIFF while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            imgOpt.imageType = ImageType.Tiff;
            const wr = new WorkbookRender(workbook, imgOpt);
            const tiffData = wr.toImage();
            const tiffBlob = new Blob([tiffData], { type: 'image/tiff' });
            const downloadTiff = document.getElementById('downloadTiff');
            downloadTiff.href = URL.createObjectURL(tiffBlob);
            downloadTiff.download = 'out1_imageTIFF.tiff';
            downloadTiff.style.display = 'inline-block';
            downloadTiff.textContent = 'Download TIFF';

            // Rendering to PDF while setting the default font and checkWorkbookDefaultFont
            const saveOptions = new PdfSaveOptions();
            saveOptions.defaultFont = "Times New Roman";
            saveOptions.checkWorkbookDefaultFont = false;
            const pdfData = workbook.save(SaveFormat.Pdf, saveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            const downloadPdf = document.getElementById('downloadPdf');
            downloadPdf.href = URL.createObjectURL(pdfBlob);
            downloadPdf.download = 'out1_pdf.pdf';
            downloadPdf.style.display = 'inline-block';
            downloadPdf.textContent = 'Download PDF';

            resultEl.innerHTML = '<p style="color: green;">Export completed. Click the links above to download the generated files.</p>';
        });
    </script>
</html>
```
