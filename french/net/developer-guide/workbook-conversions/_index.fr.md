---
title: Convertir Excel en PDF, en image et dans d autres formats
linktitle: Conversions de classeur
type: docs
weight: 65
url: /fr/net/convert-workbook-to-different-formats/
description: Convertir des fichiers Excel en Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML et plus encore.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion entre de nombreux formats. Techniquement, la conversion consiste à charger un classeur dans un format de fichier et à le sauvegarder dans un autre.

{{% /alert %}}

## **Convertir un classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Microsoft Excel en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Convertir un classeur Excel en JPG**
Aspose.Cells prend en charge la conversion de fichiers Excel en JPG.
L'exemple de code ci-dessous montre comment sauvegarder un classeur en JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Convertir un classeur Excel en image**
Aspose.Cells prend en charge la conversion de fichiers Excel en images.
L'exemple de code ci-dessous montre comment sauvegarder un classeur en images.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Convertir un classeur Excel en XPS**

Le format de document XPS se compose de balises XML structurées qui définissent la mise en page d'un document et l'apparence visuelle de chaque page, ainsi que des règles de rendu pour la distribution, l'archivage, le rendu, le traitement et l'impression de documents.

Le langage de balisage pour XPS est un sous-ensemble de XAML qui lui permet d'incorporer des éléments graphiques vectoriels dans des documents, en utilisant XAML pour baliser les primitives de la Fondation Windows Presentation (WPF). Les éléments utilisés sont décrits en termes de chemins et d'autres primitives géométriques.

Un fichier XPS est en fait une archive ZIP Unicode utilisant les Conventions d'Emballage Ouvert, contenant les fichiers constituant le document. Il comprend un fichier de balisage XML pour chaque page, du texte, des polices intégrées, des images raster, des graphiques vectoriels 2D, ainsi que des informations de gestion des droits numériques. Le contenu d'un fichier XPS peut être examiné simplement en l'ouvrant avec une application prenant en charge les fichiers ZIP.

À partir de Aspose.Cells 6.0.0, la conversion de Microsoft Excel en XPS est prise en charge.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Convertir Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supporte la conversion de fichiers Excel en fichiers Ods, Sxc et Fods. L'exemple de code ci-dessous montre comment convertir le [modèle](book1.xlsx) en fichiers Ods, Sxc et Fods.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Conversion de Classeur Excel en Fichiers MHTML**

Le format MHTML combine du HTML normal avec des ressources externes (c'est-à-dire du contenu généralement lié tel que des images, des animations, de l'audio, etc.) dans un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.

Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier MHTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Conversion de Classeur Excel en HTML**

L'API Aspose.Cells prend en charge l'exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions) pour offrir la flexibilité de contrôler plusieurs aspects de la sortie HTML.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier HTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Configuration des Préférences d'Image pour le HTML**

À partir de la version 8.0.2, Aspose.Cells a exposé [**ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) pour la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions), permettant aux développeurs de spécifier les préférences d'image lors de l'enregistrement de feuilles de calcul au format HTML.

Ci-dessous sont détaillés certains des réglages d'image qui peuvent être appliqués,

- [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype): Spécifie le type d'image. Veuillez noter que toutes les formes, y compris les graphiques, sont rendues sous forme d'images dans le HTML de sortie.
- [**SmoothingMode**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode): Spécifie l'anti-crénelage pour les lignes, les courbes et les bords des zones remplies.
- [**TextRenderingHint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint): Spécifie la qualité du rendu du texte.
- [**Quality**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality): Spécifie la qualité de l'image entre 0 et 100, lorsque [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) est spécifié comme Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution): Obtient ou définit la résolution verticale de l'image en points par pouce.
- [**HorizontalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution): Obtient ou définit la résolution horizontale de l'image en points par pouce.
- [**TiffCompression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression): Obtient ou définit le type de compression pour les images lorsque [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) est spécifié comme Tiff.
- [**Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent): Indique si l'arrière-plan d'une image doit être transparent lorsque ImageFormat est spécifié comme Png.

Le code ci-dessous montre comment utiliser [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) pour spécifier différentes préférences.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Convertir un classeur Excel en Markdown**

L'API Aspose.Cells prend en charge l'exportation de feuilles de calcul au format Markdown. Pour exporter la feuille de calcul active au format Markdown, passez [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) comme deuxième paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Vous pouvez également utiliser la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions) pour spécifier des paramètres supplémentaires pour exporter la feuille de calcul au format Markdown.

L'exemple de code suivant montre comment exporter la feuille de calcul active au format Markdown en utilisant l'élément d'énumération [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Veuillez consulter le [fichier Markdown de sortie](md_sample.txt) généré par le code pour référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Convertir un classeur Excel en JSON**

Aspose.Cells prend en charge la conversion d'un classeur en fichier Json (JavaScript Object Notation).

L'exemple de code suivant démontre l'exportation de la feuille de calcul active en Json en utilisant [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) membre d'énumération. Veuillez consulter le code pour convertir [source file](Book1.xlsx) to the [output Json file](Book1.Json) généré par le code pour référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Convertir Excel en XML**
Aspose.Cells prend en charge la conversion d'un classeur en XML de feuille de calcul Excel 2003 et en données XML brutes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Convertir un classeur Excel en TIFF**
Aspose.Cells prend en charge la conversion d'un classeur en fichier TIFF.

Le code ci-dessous montre comment convertir Excel en TIFF :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Convertir un classeur Excel en DOCX**

L'API Aspose.Cells prend en charge la conversion de feuilles de calcul au format DOCX. Pour exporter le classeur au format DOCX, passez [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) en tant que deuxième paramètre de [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) méthode. Vous pouvez également utiliser [**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) classe pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul au format DOCX.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active au format DOCX en utilisant [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) membre d'énumération. Veuillez consulter le [output DOCX file](Book1.docx) généré par le code pour référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Convertir un classeur Excel en PPTX**

L'API Aspose.Cells prend en charge la conversion de feuilles de calcul au format PPTX. Pour exporter le classeur au format PPTX, passez [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) en tant que deuxième paramètre de [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) méthode. Vous pouvez également utiliser [**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) classe pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul au format PPTX.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active au format PPTX en utilisant [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) membre d'énumération. Veuillez consulter le [output PPTX file](Book1.pptx) généré par le code pour référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Sujets avancés**
- [Convertir la révision de XLSB en XLSM](/cells/fr/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/fr/net/convert-excel-to-html/)
- [Image](/cells/fr/net/convert-excel-to-image/)
- [Json](/cells/fr/net/convert-workbook-to-json/)
- [Convertir un classeur Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice calc).](/cells/fr/net/convert-excel-to-ods/)
- [Pdf](/cells/fr/net/convert-excel-workbook-to-pdf/)
- [Convertir Excel en CSV, TSV et Txt](/cells/fr/net/convert-excel-to-csv-tsv-and-txt/)
- [Suivre la progression de la conversion des documents](/cells/fr/net/track-document-conversion-progress/)
- [Convertir CSV, TSV et TXT en Excel](/cells/fr/net/convert-csv-tsv-and-txt-to-excel/)
