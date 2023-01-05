---
title: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité
type: docs
weight: 30
url: /fr/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Scénarios d'utilisation possibles**

 Lors du réglage du**Police par défaut** propriété de[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) et[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) , vous pourriez vous attendre à ce que l'enregistrement dans PDF ou l'image définisse cela**Police par défaut** à tout le texte du classeur qui a une police manquante (non installée).

 Généralement, lors de l'enregistrement au format PDF ou image, Aspose.Cells essaiera d'abord de définir la police par défaut du classeur (c'est-à-dire,[**Workbook.DefaultStyle.FontWorkbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ). Si la police par défaut du classeur ne peut toujours pas afficher/rendre le texte correctement, alors Aspose.Cells essaiera de rendre avec la police mentionnée contre**Police par défaut** attribut dans[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Pour faire face à votre attente, nous avons une propriété booléenne nommée "**CheckWorkbookDefaultFont** " dans[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) . Vous pouvez le définir sur false pour désactiver la police par défaut du classeur ou laisser le**Police par défaut** s'installer[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

L'exemple de code suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille de calcul) a un texte défini sur "Texte de police de l'heure de Noël". Le nom de police est "Christmas Time Personal Use" qui n'est pas installé sur la machine. Nous fixons**Police par défaut**attribut de[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Options d'image ou d'impression**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)à "Times New Roman". Nous fixons également**CheckWorkbookDefaultFont**Propriété booléenne à "**faux**" qui garantit que le texte de la cellule A1 est rendu avec la police "Times New Roman" et ne doit pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code rend la première feuille de calcul aux formats d'image PNG et TIFF. Il rend finalement au format de fichier PDF.

{{% alert color="primary" %}}

 La valeur par défaut de***CheckWorkbookDefaultFont*** l'attribut est**vrai**.

{{% /alert %}}

Ceci est la capture d'écran du[fichier modèle](49446914.xlsx)utilisé dans l'exemple de code.

![tâche : image_autre_texte](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Il s'agit de l'image de sortie PNG après avoir défini le[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)propriété à "Times New Roman".

![tâche : image_autre_texte](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Voir la sortie[TIFF](out1_imageTIFF.tiff)l'image après avoir réglé le[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)propriété à "Times New Roman".

Voir la sortie[PDF](out1_pdf.pdf)fichier après avoir défini le[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)propriété à "Times New Roman".

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
