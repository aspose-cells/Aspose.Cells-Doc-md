---
title: Convertir un fichier XLSX en format PDF avec JavaScript via C++
linktitle: Convertir un fichier XLSX au format PDF
type: docs
weight: 30
url: /fr/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: Ce guide explique comment convertir un fichier Excel (XLSX) en format PDF en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) représente des documents indépendamment du logiciel, du matériel et du système d'exploitation utilisé pour créer ces documents. Un fichier PDF peut être un document avec n'importe quelle combinaison de texte, de graphiques et d'images de manière indépendante de l'appareil et de la résolution. Les fichiers PDF sont souvent compressés, de sorte qu'ils occupent moins d'espace que le fichier d'origine.

Parfois, vous avez besoin de convertir un fichier Microsoft Excel en PDF. Pour cela, vous avez besoin d'une solution rapide, sécurisée, précise et fiable qui vous permet de distribuer des documents PDF dans le monde entier. De nombreux outils de conversion peuvent accomplir cette tâche. Mais vous devez vous assurer que la mise en page du document Excel d'origine est conservée dans le fichier PDF de sortie. Les images, graphiques, formes, mise en forme des données, polices, attributs, couleurs, paramètres de mise en page, orientation du texte, bordures, graphiques, etc., doivent être rendus avec précision et exactitude. [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) garantit une conversion de haute fidélité.

Ce document est conçu pour fournir une compréhension complète de la façon dont un document Microsoft Excel (contenant des images, des graphiques, du formatage, etc.) peut être converti en PDF. À cette fin, il montre comment créer une application console simple en JavaScript via C++ qui convertit un fichier Excel en PDF en utilisant l'API Aspose.Cells. La conversion est effectuée avec un haut degré de précision et d'exactitude.

{{% /alert %}}

## **Conversion d'Excel en PDF**

Cet exemple utilise un fichier Excel (SampleInput.xlsx) comme modèle. Le classeur contient des feuilles avec des graphiques et des images. Chaque feuille contient différents types de formats utilisant des polices, des attributs, des couleurs, des effets de shading, et des bordures. Il y a un graphique en colonnes sur la première feuille et une image sur la dernière.

### **Le fichier Excel modèle**

Le fichier modèle comporte trois feuilles, dont des graphiques et des images en tant que médias. La première feuille comporte des graphiques et la dernière une image, comme le montrent les captures d'écran ci-dessous.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|

### **Processus de conversion**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) juste avant de convertir la feuille en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les bonnes valeurs sont affichées dans le PDF.

{{% /alert %}}

### **Résultat**

Lorsque le code ci-dessus est exécuté, un fichier PDF est créé dans le dossier Files de votre répertoire d'application.
Les captures d'écran suivantes montrent les pages PDF. Notez que les en-têtes et pieds de pages sont également conservés dans le fichier PDF de sortie.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|
