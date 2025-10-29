---
title: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions afin de lui donner la priorité
type: docs
weight: 30
url: /fr/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Scénarios d'utilisation possibles**

En définissant la propriété **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), vous pourriez vous attendre à ce que l'enregistrement en PDF ou en image définit cette police par défaut pour tout le texte dans un classeur qui a une police manquante (non installée).

Généralement, lors de l'enregistrement au format PDF ou image, Aspose.Cells pour Python via .NET tentera d'abord de définir la police par défaut du classeur (c'est-à-dire Workbook.DefaultStyle.Font). Si la police par défaut du classeur ne peut toujours pas afficher/rendre le texte correctement, Aspose.Cells pour Python via .NET essaiera de rendre avec la police mentionnée contre l'attribut DefaultFont dans [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

Pour répondre à vos attentes, nous avons une propriété booléenne nommée "**check_workbook_default_font**" dans [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). Vous pouvez la définir sur **false** pour désactiver la tentative avec la police par défaut du classeur ou laisser la configuration **default_font** dans [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

Le code d'exemple suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille) contient un texte défini à "Christmas Time Font text". Le nom de la police est "Christmas Time Personal Use" qui n'est pas installée sur la machine. Nous définissons l'attribut ***default_font*** de [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) sur "Times New Roman". Nous définissons également la propriété booléenne **check_workbook_default_font** sur **"false"** pour garantir que le texte de la cellule A1 est rendu avec la police "Times New Roman" et ne doit pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code rend la première feuille au format PNG et TIFF, puis à un fichier PDF.

{{% alert color="primary" %}}

La valeur par défaut de l'attribut ***CheckWorkbookDefaultFont*** est **true**.

{{% /alert %}}

Il s'agit de la capture d'écran du [fichier modèle](49446913.xlsx) utilisé dans le code exemple.

![todo:image_alt_text](1.png)

Il s'agit de l'image PNG de sortie après avoir défini la propriété [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) sur "Times New Roman".

![todo:image_alt_text](2.png)

Veuillez consulter la sortie [TIFF](48496672.tiff) après avoir défini la propriété [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) sur "Times New Roman".

Veuillez consulter le fichier de sortie [PDF](48496673.pdf) après avoir défini la propriété [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) sur "Times New Roman".

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
