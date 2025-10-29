---
title: Évitez la page blanche dans le PDF de sortie lorsqu il n y a rien à imprimer avec JavaScript via C++
linktitle: Éviter une page vierge dans le PDF de sortie lorsqu il n y a rien à imprimer
type: docs
weight: 30
url: /fr/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Apprenez comment éviter les pages blanches dans le PDF de sortie lorsqu il n y a rien à imprimer en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur le sauvegarde en PDF via Aspose.Cells for JavaScript en C++, il génère une page blanche dans le PDF de sortie. Parfois, ce comportement par défaut est indésirable. Aspose.Cells fournit la propriété [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) pour gérer ce problème. Si vous la définissez sur **false**, une exception se produira chaque fois qu'il n'y aura rien à imprimer dans le PDF de sortie.

## **Éviter la page blanche dans le PDF final lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée un classeur vide puis le sauvegarde en PDF après avoir défini la propriété [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) sur **false**. Étant donné qu'il n'y a rien à imprimer dans le PDF de sortie, l'exception se produit comme montré ci-dessous.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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
                // No file selected - will create an empty workbook (to mirror original JavaScript behavior)
                document.getElementById('result').innerHTML = '<p>No file selected. Creating an empty workbook and attempting to save to PDF.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Loading selected workbook...</p>';
            }

            // Instantiate workbook from file if provided, otherwise create an empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create Pdf save options.
            const opts = new PdfSaveOptions();

            // Default value of OutputBlankPageWhenNothingToPrint is true.
            // Setting false means - Do not output blank page when there is nothing to print.
            opts.outputBlankPageWhenNothingToPrint = false;

            // Save workbook to Pdf format.
            // Note: If workbook has nothing to print and outputBlankPageWhenNothingToPrint is false,
            // this operation may throw an exception which will propagate (no try-catch per requirements).
            const outputData = workbook.save(SaveFormat.Pdf, opts);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Exception**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
