---
title: Aperçu du classeur avec JavaScript via C++
linktitle: Aperçu du classeur 
type: docs
weight: 70
url: /fr/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells supporte l impression et l aperçu des fichiers Excel sans installation de Microsoft Excel en utilisant JavaScript via C++.
---

## **Aperçu avant impression**  

Il peut arriver que des fichiers Excel avec des millions de pages doivent être convertis en PDF ou en images. Le traitement de tels fichiers consommera beaucoup de temps et de ressources. Dans ce cas, la fonction d'aperçu avant impression du classeur et de la feuille de calcul peut être utile. Avant de convertir ces fichiers, l'utilisateur peut vérifier le nombre total de pages, puis décider si le fichier doit être converti ou non. Cet article se concentre sur l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) pour connaître le nombre total de pages.  

Aspose.Cells fournit la fonction d'aperçu avant impression. Pour cela, l'API propose les classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/). Pour créer l'aperçu avant impression de l'ensemble du classeur, créez une instance de la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) en passant les objets [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) au constructeur. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) fournit une méthode [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) qui renvoie le nombre de pages dans l'aperçu généré. De manière similaire à la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) est utilisée pour générer un aperçu avant impression pour une feuille de calcul spécifique. Pour créer l'aperçu d'une feuille, créez une instance de la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) en passant les objets [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) au constructeur. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) offre également une méthode [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) qui renvoie le nombre de pages dans l'aperçu généré.  

Le code suivant démontre l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) en utilisant le [fichier Excel d'exemple](94896177.xlsx).  

### **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

Voici la sortie générée en exécutant le code ci-dessus.  

### **Sortie console**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Sujets avancés**  
- [Configuration des polices pour le rendu des feuilles de calcul](/cells/fr/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convertir une feuille de calcul en image - Supprimer les espaces autour des données](/cells/fr/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Conversion d'une feuille de calcul en image en utilisant des options d'image ou d'impression](/cells/fr/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Exporter une plage de cellules d'une feuille de calcul vers une image](/cells/fr/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur souhaitées](/cells/fr/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extraire des images des feuilles de calcul en utilisant des options d'image ou d'impression](/cells/fr/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Générer une miniature de la feuille de calcul](/cells/fr/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Afficher une page vierge lorsqu'il n'y a rien à imprimer](/cells/fr/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Configuration de la page et options d'impression](/cells/fr/javascript-cpp/page-setup-and-printing-options/)  
- [Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions](/cells/fr/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Rendre la feuille de calcul dans le contexte graphique](/cells/fr/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Spécifier un ensemble de polices individuelles ou privées pour le rendu du classeur](/cells/fr/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
