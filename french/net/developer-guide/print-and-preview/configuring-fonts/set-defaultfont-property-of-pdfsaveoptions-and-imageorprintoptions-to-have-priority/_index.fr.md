---
title: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions afin de lui donner la priorité
type: docs
weight: 30
url: /fr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Scénarios d'utilisation possibles**

En définissant la propriété **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), vous pourriez vous attendre à ce que l'enregistrement en PDF ou en image définit cette police par défaut pour tout le texte dans un classeur qui a une police manquante (non installée).

Généralement, lors de l'enregistrement en PDF ou en image, Aspose.Cells essaiera d'abord de définir la police par défaut du classeur (c'est-à-dire, Workbook.DefaultStyle.Font). Si la police par défaut du classeur ne peut toujours pas afficher/rendre correctement le texte, alors Aspose.Cells essaiera de le rendre avec la police mentionnée contre l'attribut DefaultFont dans [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions).

Pour répondre à votre attente, nous avons une propriété booléenne nommée "**CheckWorkbookDefaultFont**" dans [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions). Vous pouvez la définir sur **false** pour désactiver l'essai de la police par défaut du classeur ou laisser la définition de **DefaultFont** dans [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

Le code d'exemple suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille de calcul) contient un texte défini comme "Texte de police de Noël". Le nom de la police est "Christmas Time Personal Use" qui n'est pas installée sur la machine. Nous définissons l'attribut ***DefaultFont*** de [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) sur "Times New Roman". Nous définissons également la propriété booléenne **CheckWorkbookDefaultFont** sur **"false"** pour garantir que le texte de la cellule A1 sera rendu avec la police "Times New Roman" et ne devrait pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code rend la première feuille de calcul au format PNG et TIFF. Il le rend finalement au format de fichier PDF.

{{% alert color="primary" %}}

La valeur par défaut de l'attribut ***CheckWorkbookDefaultFont*** est **true**.

{{% /alert %}}

Il s'agit de la capture d'écran du [fichier modèle](49446913.xlsx) utilisé dans le code exemple.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Il s'agit de l'image PNG de sortie après avoir défini la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) sur "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Veuillez consulter la sortie [TIFF](48496672.tiff) après avoir défini la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) sur "Times New Roman".

Veuillez consulter le fichier de sortie [PDF](48496673.pdf) après avoir défini la propriété [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) sur "Times New Roman".

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
{{< app/cells/assistant language="csharp" >}}
