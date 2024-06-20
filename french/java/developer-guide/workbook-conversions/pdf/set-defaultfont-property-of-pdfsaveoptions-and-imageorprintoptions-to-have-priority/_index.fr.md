---
title: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions afin de lui donner la priorité
type: docs
weight: 30
url: /fr/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Scénarios d'utilisation possibles**

Lors du réglage de la propriété **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), vous pourriez vous attendre à ce que l'enregistrement au format PDF ou image définisse cette **DefaultFont** pour tout le texte dans le classeur qui a une police manquante (non installée).

Généralement, lors de l'enregistrement au format PDF ou image, Aspose.Cells essaiera d'abord de définir la police par défaut du classeur (c'est-à-dire, [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)). Si la police par défaut du classeur ne peut toujours pas montrer/rendre le texte correctement, alors Aspose.Cells essaiera de le rendre avec la police mentionnée contre l'attribut **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Pour répondre à votre attente, nous avons une propriété booléenne nommée "**CheckWorkbookDefaultFont**" dans [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions). Vous pouvez la définir sur false pour désactiver l'essai de la police par défaut du classeur ou laisser le réglage **DefaultFont** dans [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

Le code d'exemple suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille de calcul) contient un texte défini sur "Christmas Time Font text". Le nom de la police est "Christmas Time Personal Use" qui n'est pas installée sur la machine. Nous définissons l'attribut **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) sur "Times New Roman". Nous définissons également la propriété booléenne **CheckWorkbookDefaultFont** sur "**false**" ce qui garantit que le texte de la cellule A1 est rendu avec la police "Times New Roman" et ne devrait pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code rend la première feuille de calcul aux formats d'image PNG et TIFF. Il rend enfin au format de fichier PDF.

{{% alert color="primary" %}}

La valeur par défaut de l'attribut ***CheckWorkbookDefaultFont*** est **true**.

{{% /alert %}}

Il s'agit de la capture d'écran du [fichier modèle](49446914.xlsx) utilisé dans le code d'exemple.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Il s'agit de l'image PNG de sortie après avoir défini la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) sur "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Voir l'image [TIFF de sortie](out1_imageTIFF.tiff) après avoir défini la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) sur "Times New Roman".

Voir le fichier [PDF de sortie](out1_pdf.pdf) après avoir défini la propriété [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) sur "Times New Roman".

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
