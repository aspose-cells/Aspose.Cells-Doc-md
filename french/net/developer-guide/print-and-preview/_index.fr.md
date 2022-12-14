---
title: Imprimer et prévisualiser le classeur
linktitle: Imprimer et prévisualiser
type: docs
weight: 70
url: /fr/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells prend en charge l'impression et la prévisualisation des fichiers Excel sans Microsoft installation d'Excel.
---
{{% alert color="primary" %}}

Après avoir créé une feuille de calcul, vous souhaitez souvent en imprimer une copie papier. Cet article explique comment imprimer des feuilles de calcul avec Aspose.Cells.

{{% /alert %}}

## **Imprimer Présentation**

Microsoft Excel suppose que vous souhaitez imprimer toute la zone de la feuille de calcul, sauf si vous spécifiez une sélection. Pour imprimer avec Aspose.Cells, importez d'abord l'espace de noms Aspose.Cells.Rendering dans le programme. Il a plusieurs classes utiles, par exemple,[**FeuilleRendu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) et[**ClasseurRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Imprimer avec SheetRender**

 La[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) classe représente une feuille de calcul et a le[**VersImprimante**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)méthode qui peut imprimer une feuille de calcul. L'exemple de code suivant montre comment imprimer une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Imprimer à l'aide de WorkbookRender**

 Pour imprimer un classeur entier, parcourez les feuilles et imprimez-les, ou utilisez le[**ClasseurRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)classer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells fournit également des surcharges pour le[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) et[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) méthodes, il est donc possible de définir le nom du travail d'impression lors de l'impression de feuilles de calcul Excel. Par défaut, tous les travaux d'impression sont créés avec le nom "Document".

{{% /alert %}}

## **Aperçu avant impression**

Il peut y avoir des cas où des fichiers Excel avec des millions de pages doivent être convertis en PDF ou en images. Le traitement de tels fichiers consommera beaucoup de temps et de ressources. Dans de tels cas, la fonctionnalité Aperçu avant impression du classeur et de la feuille de calcul peut s'avérer utile. Avant de convertir de tels fichiers, l'utilisateur peut vérifier le nombre total de pages, puis décider si le fichier doit être converti ou non. Cet article se concentre sur l'utilisation de[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)et[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)classes pour connaître le nombre total de pages.

 Aspose.Cells fournit la fonction d'aperçu avant impression. Pour cela, le API fournit[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) et[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) Des classes. Pour créer l'aperçu avant impression de l'ensemble du classeur, créez une instance de[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) classe en passant[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) et[**Options d'image ou d'impression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objets au constructeur. La[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) classe offre une[**Nombre de pages évaluées**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) méthode qui renvoie le nombre de pages dans l'aperçu généré. Semblable à[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)classe, la[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)La classe est utilisée pour générer un aperçu avant impression pour une feuille de calcul spécifique. Pour créer l'aperçu avant impression d'une feuille de calcul, créez une instance de[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)classe en passant[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)et[**Options d'image ou d'impression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)objets au constructeur. La[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)classe offre également une[**Nombre de pages évaluées**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)méthode qui renvoie le nombre de pages dans l'aperçu généré.

L'extrait de code suivant illustre l'utilisation des deux[**ClasseurImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)et[**FeuilleImpressionAperçu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) cours en utilisant le[exemple de fichier excel](94896177.xlsx).

### **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Voici la sortie générée en exécutant le code ci-dessus.

### **Sortie console**

Nombre de pages du classeur : 1
Nombre de pages de la feuille de calcul : 1


## **Sujets avancés**
- [Configuration des polices pour le rendu des feuilles de calcul](/cells/fr/net/configuring-fonts-for-rendering-spreadsheets/)
- [Convertir la feuille de calcul en image - Supprimer les espaces autour des données](/cells/fr/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Conversion d'une feuille de calcul en image à l'aide des options ImageOrPrint](/cells/fr/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Exporter la plage de Cells dans une feuille de calcul vers une image](/cells/fr/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Exporter une feuille de calcul ou un graphique dans une image avec la largeur et la hauteur souhaitées](/cells/fr/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extraire des images de feuilles de calcul à l'aide d'ImageOrPrintOptions](/cells/fr/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Générer une vignette de la feuille de calcul](/cells/fr/net/generate-thumbnail-of-the-worksheet/)
- [Sortir une page vierge lorsqu'il n'y a rien à imprimer](/cells/fr/net/output-blank-page-when-there-is-nothing-to-print/)
- [Configuration de la page et options d'impression](/cells/fr/net/page-setup-and-printing-options/)
- [Impression d'une plage de pages à l'aide de SheetRender et WorkbookRender](/cells/fr/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Rendu de la séquence de pages à l'aide des propriétés PageIndex et PageCount de ImageOrPrintOptions](/cells/fr/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Rendre la feuille de calcul dans le contexte graphique](/cells/fr/net/render-worksheet-to-graphic-context/)
- [Spécifier un ensemble de polices individuel ou privé pour le rendu du classeur](/cells/fr/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Spécifiez le nom du travail ou du document lors de l'impression avec Aspose.Cells](/cells/fr/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
