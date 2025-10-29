---  
title: Aperçu du classeur avec Node.js via C++  
linktitle: Aperçu du classeur 
type: docs  
weight: 70  
url: /fr/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells supporte l impression et l aperçu des fichiers Excel sans installation de Microsoft Excel en utilisant Node.js via C++.  
---  

## **Aperçu avant impression**  

Il peut arriver que des fichiers Excel avec des millions de pages doivent être convertis en PDF ou en images. Le traitement de tels fichiers consommera beaucoup de temps et de ressources. Dans ce cas, la fonction d'aperçu avant impression du classeur et de la feuille de calcul peut être utile. Avant de convertir ces fichiers, l'utilisateur peut vérifier le nombre total de pages, puis décider si le fichier doit être converti ou non. Cet article se concentre sur l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) pour connaître le nombre total de pages.  

Aspose.Cells fournit la fonction d'aperçu avant impression. Pour cela, l'API propose les classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/). Pour créer l'aperçu avant impression de l'ensemble du classeur, créez une instance de la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) en passant les objets [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) au constructeur. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) fournit une méthode [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) qui renvoie le nombre de pages dans l'aperçu généré. De manière similaire à la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) est utilisée pour générer un aperçu avant impression pour une feuille de calcul spécifique. Pour créer l'aperçu d'une feuille, créez une instance de la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) en passant les objets [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) au constructeur. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) offre également une méthode [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) qui renvoie le nombre de pages dans l'aperçu généré.  

Le code suivant démontre l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) en utilisant le [fichier Excel d'exemple](94896177.xlsx).  

### **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

Voici la sortie générée en exécutant le code ci-dessus.  

### **Sortie console**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Sujets avancés**  
- [Configuration des polices pour le rendu des feuilles de calcul](/cells/fr/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convertir une feuille de calcul en image - Supprimer les espaces autour des données](/cells/fr/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Conversion d'une feuille de calcul en image en utilisant des options d'image ou d'impression](/cells/fr/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Exporter une plage de cellules d'une feuille de calcul vers une image](/cells/fr/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur souhaitées](/cells/fr/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extraire des images des feuilles de calcul en utilisant des options d'image ou d'impression](/cells/fr/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Générer une miniature de la feuille de calcul](/cells/fr/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Afficher une page vierge lorsqu'il n'y a rien à imprimer](/cells/fr/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Configuration de la page et options d'impression](/cells/fr/nodejs-cpp/page-setup-and-printing-options/)  
- [Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions](/cells/fr/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Rendre la feuille de calcul dans le contexte graphique](/cells/fr/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Spécifier un ensemble de polices individuelles ou privées pour le rendu du classeur](/cells/fr/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

{{< app/cells/assistant language="nodejs-cpp" >}}
