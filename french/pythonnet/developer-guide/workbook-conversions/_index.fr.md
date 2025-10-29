---
title: Convertir Excel en PDF, en image et dans d autres formats
linktitle: Conversions de classeur
type: docs
weight: 65
url: /fr/python-net/convert-workbook-to-different-formats/
description: Convertir des fichiers Excel en Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML et plus encore en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Convertir le classeur Excel en PDF en Python, Convertir le classeur Excel en JPG en Python, Convertir le classeur Excel en image en Python, Convertir le classeur Excel en XPS en utilisant Python, Convertir Excel en Ods, Sxc et Fods via Python, Convertir le classeur Excel en HTML en Python, Convertir le classeur Excel en JSON en Python, Convertir le classeur Excel en DOCX en Python, Convertir le classeur Excel en TIFF ou en MARKDOWN avec Ptyhon.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET prend en charge la conversion entre de nombreux formats. Techniquement, la conversion signifie charger un classeur dans un format de fichier et le sauvegarder dans un autre.

{{% /alert %}}

## **Convertir un classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Microsoft Excel en documents PDF.

Aspose.Cells for Python via .NET prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

## **Convertir un classeur Excel en JPG**
Aspose.Cells pour Python via .NET prend en charge la conversion de fichiers Excel en JPG.
L'exemple de code ci-dessous montre comment sauvegarder un classeur en JPG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

## **Convertir un classeur Excel en image**
Aspose.Cells for Python via .NET prend en charge la conversion de fichiers Excel en images.
L'exemple de code ci-dessous montre comment sauvegarder un classeur en images.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

## **Convertir un classeur Excel en XPS**

Le format de document XPS se compose de balises XML structurées qui définissent la mise en page d'un document et l'apparence visuelle de chaque page, ainsi que des règles de rendu pour la distribution, l'archivage, le rendu, le traitement et l'impression de documents.

Le langage de balisage pour XPS est un sous-ensemble de XAML qui lui permet d'incorporer des éléments graphiques vectoriels dans des documents, en utilisant XAML pour baliser les primitives de la Fondation Windows Presentation (WPF). Les éléments utilisés sont décrits en termes de chemins et d'autres primitives géométriques.

Un fichier XPS est en fait une archive ZIP Unicode utilisant les Conventions d'Emballage Ouvert, contenant les fichiers constituant le document. Il comprend un fichier de balisage XML pour chaque page, du texte, des polices intégrées, des images raster, des graphiques vectoriels 2D, ainsi que des informations de gestion des droits numériques. Le contenu d'un fichier XPS peut être examiné simplement en l'ouvrant avec une application prenant en charge les fichiers ZIP.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

## **Convertir Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Python via .NET prend en charge la conversion de fichiers Excel en fichiers Ods, Sxc et Fods. L'exemple de code ci-dessous montre comment convertir le [modèle](book1.xlsx) en fichiers Ods, Sxc et Fods.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}


## **Conversion de Classeur Excel en Fichiers MHTML**

Le format MHTML combine du HTML normal avec des ressources externes (c'est-à-dire du contenu généralement lié tel que des images, des animations, de l'audio, etc.) dans un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.

Aspose.Cells for Python via .NET prend en charge la lecture et l'écriture de fichiers MHTML.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier MHTML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

## **Conversion de Classeur Excel en HTML**

L'API Aspose.Cells pour Python via .NET prend en charge l'exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells pour Python via .NET utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/) pour offrir la flexibilité de contrôler plusieurs aspects du HTML de sortie.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier HTML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

## **Configuration des Préférences d'Image pour le HTML**

Aspose.Cells pour Python via .NET a exposé [**image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) pour la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions), permettant aux développeurs de spécifier les préférences d'image lors de l'enregistrement de feuilles de calcul au format HTML.

Ci-dessous sont détaillés certains des réglages d'image qui peuvent être appliqués,

- [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/): Spécifie le type d'image. Veuillez noter que toutes les formes, y compris les graphiques, sont rendues sous forme d'images dans le HTML de sortie.
- [**smoothing_mode**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/): Spécifie l'anti-crénelage pour les lignes, les courbes et les bords des zones remplies.
- [**text_rendering_hint**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/): Spécifie la qualité du rendu du texte.
- [**quality**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/): Spécifie la qualité de l'image entre 0 et 100, lorsque [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) est spécifié comme Jpeg.
- [**vertical_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/): Obtient ou définit la résolution verticale de l'image en points par pouce.
- [**horizontal_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/): Obtient ou définit la résolution horizontale de l'image en points par pouce.
- [**tiff_compression**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/): Obtient ou définit le type de compression pour les images lorsque [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) est spécifié comme Tiff.
- [**transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/): Indique si l'arrière-plan d'une image doit être transparent lorsque ImageFormat est spécifié comme Png.

Le code ci-dessous montre comment utiliser [**HtmlSaveOptions.image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) pour spécifier différentes préférences.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

## **Convertir un classeur Excel en Markdown**

L'API Aspose.Cells pour Python via .NET prend en charge l'exportation de feuilles de calcul au format Markdown. Pour exporter la feuille de calcul active en Markdown, passez [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) comme deuxième paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.saveformat). Vous pouvez également utiliser [**MarkdownSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/markdownsaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul en Markdown.

L'exemple de code suivant montre comment exporter la feuille de calcul active au format Markdown en utilisant l'élément d'énumération [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/). Veuillez consulter le [fichier Markdown de sortie](md_sample.txt) généré par le code pour référence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

## **Convertir un classeur Excel en JSON**

Aspose.Cells pour Python via .NET prend en charge la conversion d'un classeur en fichier Json (JavaScript Object Notation).

L'exemple de code suivant démontre l'exportation de la feuille de calcul active en Json en utilisant [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) membre d'énumération. Veuillez consulter le code pour convertir [source file](Book1.xlsx) to the [output Json file](Book1.Json) généré par le code pour référence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **Convertir Excel en XML**
Aspose.Cells pour Python via .NET prend en charge la conversion d'un classeur en données XML de feuille de calcul XML 2003 Excel et plain XML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

## **Convertir un classeur Excel en TIFF**
Aspose.Cells pour Python via .NET prend en charge la conversion d'un classeur en fichier TIFF.

Le code ci-dessous montre comment convertir Excel en TIFF :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

## **Convertir un classeur Excel en DOCX**

L'API Aspose.Cells pour Python via .NET offre une prise en charge de la conversion de feuilles de calcul au format DOCX. Pour exporter le classeur au format DOCX, passez [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) en tant que deuxième paramètre de [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions) méthode. Vous pouvez également utiliser [**DocxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/) classe pour spécifier des paramètres supplémentaires pour exporter la feuille de calcul au format DOCX.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active au format DOCX en utilisant [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) membre d'énumération. Veuillez consulter le [output DOCX file](Book1.docx) généré par le code pour référence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

## **Convertir un classeur Excel en PPTX**

L'API Aspose.Cells pour Python via .NET offre une prise en charge de la conversion de feuilles de calcul au format PPTX. Pour exporter le classeur au format PPTX, passez [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) en tant que deuxième paramètre de [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions) méthode. Vous pouvez également utiliser [**PptxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions) pour spécifier des paramètres supplémentaires pour exporter la feuille de calcul au format PPTX.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active au format PPTX en utilisant [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) membre d'énumération. Veuillez consulter le [output PPTX file](Book1.pptx) généré par le code pour référence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

## **Sujets avancés**
- [Json](/cells/fr/python-net/convert-workbook-to-json/)
- [Pdf](/cells/fr/python-net/convert-excel-to-pdf/)
- [Convertir CSV, TSV et TXT en Excel](/cells/fr/python-net/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="python-net" >}}
