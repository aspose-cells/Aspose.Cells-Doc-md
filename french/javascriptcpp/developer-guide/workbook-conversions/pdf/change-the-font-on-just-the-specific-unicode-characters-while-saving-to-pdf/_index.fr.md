---
title: Modifier la police uniquement pour certains caractères Unicode lors de l enregistrement en PDF avec JavaScript via C++
linktitle: Modifier la police uniquement des caractères Unicode spécifiques lors de l enregistrement en PDF
type: docs
weight: 260
url: /fr/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Apprenez comment changer la police de caractères Unicode spécifiques lors de l enregistrement en PDF avec Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Certains caractères Unicode ne sont pas affichables par la police spécifiée par l'utilisateur. Un de ces caractères Unicode est **Non-breaking Hyphen** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec **Times New Roman**, mais il peut être affiché avec d'autres polices comme **Arial Unicode MS**.

 Lorsqu'un tel caractère apparaît à l'intérieur d'un mot ou d'une phrase en police spécifique comme Times New Roman, Aspose.Cells change la police de tout le mot ou de la phrase en une police pouvant afficher ce caractère, comme Arial Unicode ou MS.

 Cependant, ce comportement est indésirable pour certains utilisateurs qui souhaitent uniquement que la police de ce caractère spécifique soit modifiée plutôt que toute la phrase ou le mot.

 Pour traiter ce problème, Aspose.Cells fournit la propriété `PdfSaveOptions.isFontSubstitutionCharGranularity` qui doit être définie sur vrai afin que seule la police des caractères non affichables soit modifiée pour une police affichable, tandis que le reste du mot ou de la phrase reste dans la police d'origine.

{{% /alert %}} 

## **Exemple**
La capture d'écran suivante compare les deux fichiers PDF générés par le code d'exemple ci-dessous.

 L'un est généré sans définir la propriété `PdfSaveOptions.isFontSubstitutionCharGranularity` et l'autre après avoir défini cette propriété sur vrai.

 Comme vous pouvez le voir dans le premier PDF, la police de la phrase entière a changé de Times New Roman à Arial Unicode MS à cause du tiret non sécable. Dans le second PDF, seule la police du tiret non sécable a changé.

|**Premier fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Deuxième fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Code d'exemple**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
