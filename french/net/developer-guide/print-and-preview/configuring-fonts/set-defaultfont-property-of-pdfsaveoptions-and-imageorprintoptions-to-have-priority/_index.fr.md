---
title: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité
type: docs
weight: 30
url: /fr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Scénarios d'utilisation possibles**

 Lors du réglage du**Police par défaut** propriété de**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** et**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, vous pouvez vous attendre à ce que l'enregistrement au format PDF ou image définisse DefaultFont sur tout le texte d'un classeur dont la police est manquante (non installée).

 Généralement, lors de l'enregistrement au format PDF ou image, Aspose.Cells essaiera d'abord de définir la police par défaut du classeur (c'est-à-dire Workbook.DefaultStyle.Font). Si la police par défaut du classeur ne peut toujours pas afficher/rendre correctement le texte, alors Aspose.Cells essaiera de rendre avec la police mentionnée contre l'attribut DefaultFont dans**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

Pour faire face à votre attente, nous avons une propriété booléenne nommée "**CheckWorkbookDefaultFont** " dans**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . Vous pouvez le régler sur**faux**pour désactiver la police par défaut du classeur ou laisser le**Police par défaut** s'installer**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

 L'exemple de code suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille de calcul) a un texte défini sur "Texte de police de l'heure de Noël". Le nom de police est "Christmas Time Personal Use" qui n'est pas installé sur la machine. Nous fixons***Police par défaut*** attribut de**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** à "Times New Roman". Nous fixons également**CheckWorkbookDefaultFont** Propriété booléenne à**"faux"** qui garantit que le texte de la cellule A1 est rendu avec la police "Times New Roman" et ne doit pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code restitue la première feuille de calcul aux formats d'image PNG et TIFF. Il rend finalement au format de fichier PDF.

{{% alert color="primary" %}}

 La valeur par défaut de***CheckWorkbookDefaultFont*** l'attribut est**vrai**.

{{% /alert %}}

 Ceci est la capture d'écran du[fichier modèle](49446913.xlsx) utilisé dans l'exemple de code.

![tâche : image_autre_texte](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Il s'agit de l'image PNG de sortie après avoir défini le**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**propriété à "Times New Roman".

![tâche : image_autre_texte](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 Voir la sortie[TIFF](48496672.tiff) l'image après avoir réglé le**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**propriété à "Times New Roman".

Voir la sortie[PDF](48496673.pdf)fichier après avoir défini le**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**propriété à "Times New Roman".

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
