---
title: Convertir un fichier Excel en format PDF compatible PDF/A 1a avec JavaScript via C++
linktitle: Convertir un fichier Excel en format PDF compatible avec PDF/A 1a
type: docs
weight: 130
url: /fr/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Apprenez comment convertir des fichiers Excel en fichiers PDF conformes à PDF/A en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

PDF/A est une version unique de PDF conçue pour la conservation à long terme des documents. PDF/A est une version normalisée ISO du format de document portable (PDF) qui intègre toutes les polices utilisées dans le document dans le fichier PDF. PDF/A diffère de PDF en interdisant certaines fonctionnalités, telles que le lien de police (au lieu de l'intégration de police) et le cryptage. Aspose.Cells for JavaScript via C++ vous permet d'enregistrer les fichiers Excel en fichiers PDF conformes à PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u sont pris en charge). Ce sujet explique comment sauvegarder le classeur Excel en fichier PDF conformes à PDF/A (PDF/A-1a).  

## **Convertir le fichier Excel au format PDF Compatible avec PDF/A-1a**  

Les développeurs peuvent utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) pour définir différents attributs pour la conversion. La définition de différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le PDF de sortie. La propriété la plus importante est [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) qui vous permet d'enregistrer les fichiers Excel au format PDF/A conforme.  

 Le code d'exemple suivant explique comment convertir un fichier Excel en format PDF compatible avec PDF/A-1a. Veuillez voir le [PDF de sortie](outputCompliancePdfA1a.pdf) ainsi que la capture d'écran pour référence.  

## **Capture d'écran**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
