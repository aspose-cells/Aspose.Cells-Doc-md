---
title: Conversion d un classeur dans différents formats
type: docs
weight: 20
url: /fr/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion entre de nombreux formats. Techniquement, la conversion consiste à charger un classeur dans un format de fichier et à le sauvegarder dans un autre.

{{% /alert %}}

## **Conversion d'Excel en XPS**

Le format de document XPS se compose de balisage XML structuré qui définit la mise en page d'un document et l'apparence visuelle de chaque page, avec des règles de rendu pour la distribution, l'archivage, le rendu, le traitement et l'impression de documents.

Le langage de balisage pour XPS est un sous-ensemble de XAML qui lui permet d'incorporer des éléments graphiques vectoriels dans les documents, en utilisant XAML pour baliser les primitives de la Windows Presentation Foundation (WPF). Les éléments utilisés sont décrits en termes de chemins et d'autres primitives géométriques.

Un fichier XPS est en fait une archive ZIP en Unicode utilisant les Conventions d'emballage ouvert, contenant les fichiers qui composent le document. Cela comprend un fichier de balisage XML pour chaque page, du texte, des polices intégrées, des images matricielles, des graphiques vectoriels 2D, ainsi que des informations de gestion des droits numériques. Le contenu d'un fichier XPS peut être examiné simplement en l'ouvrant dans une application qui prend en charge les fichiers ZIP.

À partir de Aspose.Cells 6.0.0, la conversion de Microsoft Excel en XPS est prise en charge.

### **Conversion d'une seule feuille de calcul en XPS**

L'exemple suivant montre comment convertir une seule feuille de calcul dans un fichier Excel en XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Exporter l'intégralité du classeur au format XPS**

L'exemple suivant montre comment convertir l'intégralité du classeur en format XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Conversion rapide d'Excel en XPS**

L'exemple suivant montre une façon simple de convertir directement le fichier Excel au format XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Conversion d'Excel en fichiers MHTML**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML) combine HTML normal avec des ressources externes; c'est-à-dire du contenu qui est généralement lié, comme des images, animations, audio, etc., en un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.

{{% alert color="primary" %}}

Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.

{{% /alert %}}

Convertir un tableur en MHTML est une opération rapide, comme le montre l'exemple ci-dessous.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Conversion de fichiers Excel en HTML**

Les API Aspose.Cells offrent une prise en charge de l'exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) qui permet aux développeurs de contrôler plusieurs aspects de la sortie HTML.

Le code ci-dessous démontre comment utiliser la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) pour exporter des fichiers Microsoft Excel au format HTML sans spécifier de paramètres supplémentaires.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

Vous pouvez obtenir les mêmes résultats en passant le [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) à la méthode [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)).

{{% /alert %}}

### **Configuration des préférences d'image pour HTML**

À partir de la version 8.0.2, Aspose.Cells a exposé [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) pour la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions), ce qui permet aux développeurs de spécifier les préférences d'image lors de l'enregistrement des feuilles de calcul au format HTML.

Les paramètres d'image qui peuvent être appliqués sont :

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType) : Obtient ou définit le type d'image. Veuillez noter que toutes les formes, y compris les graphiques, sont rendues sous forme d'images dans le fichier HTML de sortie.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality) : Obtient ou définit la qualité des images entre 0 et 100, lorsque ImageFormat est spécifié comme Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution) : Obtient ou définit la résolution verticale de l'image en points par pouce.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution) : Obtient ou définit la résolution horizontale de l'image en points par pouce.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression) : Obtient ou définit le type de compression pour les images lorsque ImageFormat est spécifié comme Tiff.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) : Indique si l'arrière-plan d'une image doit être transparent lorsque ImageFormat est spécifié comme Png.

Le code ci-dessous démontre comment utiliser [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) pour spécifier différentes préférences.

|**Vue du tableur avant l'exportation**|**Vue HTML après l'exportation**|
| :- | :- |
|![Vue du tableur avant l'exportation](converting-workbook-to-different-formats_1.png)|![Vue HTML après l'exportation](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Conversion d'Excel en fichiers PDF**

Les documents PDF sont largement utilisés comme format standard d'échange de documents entre organisations, secteurs gouvernementaux et individus. Les développeurs de logiciels sont souvent invités à trouver un moyen de convertir facilement des fichiers Microsoft Excel en documents PDF. Aspose.Cells prend en charge ces fonctionnalités. Cet article montre comment faire.

### **Conversion d'Excel en PDF**

La conversion de Microsoft Excel en PDF a été introduite avec Aspose.Cells for Java 2.3.0. À partir de cette version, Aspose.Cells peut [convertir des feuilles de calcul en PDF directement](#direct-conversion) (y compris [PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), sans avoir besoin d'un autre produit. Pour convertir des feuilles de calcul avec des versions plus anciennes d'Aspose.Cells, [utilisez Aspose.PDF pour la conversion](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cell convertit les feuilles de calcul en PDF avec un degré élevé de précision et de fidélité. Cependant, il existe quelques [limitations](/cells/fr/java/converting-workbook-to-different-formats/#conversion-attributes), répertoriées à la fin de cet article.

{{% alert color="primary" %}}

Aspose.Cells for Java écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du Document au format PDF, Aspose.Cells for Java remplit le champ **Application** avec la valeur 'Aspose.Cells' et le champ **Producteur PDF** avec une valeur, par exemple 'Aspose.Cells for Java v17.9'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells for Java de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

#### **Conversion directe**

Enregistrez un fichier Excel directement au format PDF à l'aide de la méthode [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)), et fournissez le membre d'interface [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF). La conversion directe de cette manière est la méthode de conversion la plus efficace. Elle ne perd pas de données ni de mise en forme, mais conserve le fichier PDF de sortie tel que le fichier Excel d'entrée.

Pour spécifier les options de sécurité lors de l'enregistrement au format PDF, utilisez [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Conversion avancée**

Vous pouvez également utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) pour définir différentes propriétés de la conversion. Définir différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) vous donnera le contrôle sur les paramètres d'impression, de police, de sécurité et de compression du fichier PDF résultant. La propriété la plus notable est [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) qui vous permet de sauvegarder les fichiers Excel au format PDF/A conforme.

##### **Enregistrement de feuilles de calcul Excel au format de fichiers conformes PDF/A**

Le code ci-dessous fournit un extrait de code qui démontre l'utilisation de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) pour sauvegarder les fichiers Excel au format PDF/A conforme.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Conversion avec Aspose.Pdf: Aspose.Cells avant 2.3.0**

Pour les versions d'Aspose.Cells antérieures à la version 2.3.0, vous devez utiliser un composant comme [Aspose.PDF pour Java](/pdf/java/) pour convertir les feuilles de calcul en fichiers PDF. Aspose.Cells et Aspose.PDF travaillent ensemble pour convertir une feuille de calcul en PDF via une étape intermédiaire.

Pour convertir des feuilles de calcul en PDF avec Aspose.Cells et Aspose.PDF :

1. Instanciez un objet de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) en appelant son constructeur vide.
2. Faites votre travail souhaité sur la feuille de calcul en utilisant l'API Aspose.Cells.
1. Appeler la méthode [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) pour enregistrer la feuille de calcul :
   4. Définissez le format de fichier en tant que XML.
   5. Sélectionnez Aspose_Pdf (une valeur prédéfinie) à partir de l'interface FileFormatType. Cela indique à la méthode d'enregistrement de générer une feuille de calcul au format XML compatible avec le schéma Aspose.PDF afin que Aspose.PDF pour Java puisse ensuite générer un document PDF.
6. Lorsque le fichier XML a été créé, créez un objet de la classe Pdf dans le package aspose.pdf.
7. Appelez la méthode bindXML de la classe Pdf et passez le nom du fichier XML de sortie.
8. Appelez la méthode save de la classe Pdf pour générer le document PDF.

Les étapes ci-dessus sont mises en œuvre ci-dessous dans un exemple.

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

#### **Attributs de conversion**

Nous travaillons dur pour améliorer la conversion et d'autres aspects d'Aspose.Cells à chaque sortie. La conversion d'Excel en PDF a quelques limitations. Certains paramètres de format spécifiés dans une feuille de calcul pourraient être perdus, et tous les objets de dessin ne sont pas pris en charge.

Le tableau ci-dessous répertorie toutes les fonctionnalités entièrement ou partiellement prises en charge lors de l'exportation au format PDF à l'aide d'Aspose.Cells. Ce tableau n'est pas final et ne couvre pas toutes les attributs de la feuille de calcul. Il peut également identifier les fonctionnalités qui pourraient ne pas être prises en charge ou partiellement prises en charge pour la conversion.

{{% alert color="primary" %}}

|**Elément du Document**|**Attribut**|**Pris en charge**|**Remarques**|
| :- | :- | :- | :- |
|Alignement| |Oui| |
|Rotation| |Partiellement|Prend en charge uniquement 90 et -90.|
|Paramètres de fond| |Oui| |
|Bordure|Couleur|Oui| |
|Bordure|Style de ligne|Oui| |
|Bordure|Largeur de ligne|Oui| |
|Données de cellule| |Oui| |
|Commentaires| |Non| |
|Mise en forme conditionnelle| |Oui| |
|Propriétés du document| |Oui| |
|Objets de Dessin| |Oui| |
|Police|Taille|Oui| |
|Police|Couleur|Oui| |
|Police|Style|Oui| |
|Police|Souligner|Oui| |
|Police|Effets|Partiellement|Seul l'effet de texte barré est pris en charge|
|Images| |Oui| |
|Hyperlien| |Oui| |
|Graphiques| |Oui| |
|Cellules Fusionnées| |Oui| |
|Saut de page| |Oui| |
|Configuration de la page|En-tête/Pied de page|Oui| |
|Configuration de la page|Marges|Oui| |
|Configuration de la page|Orientation de la page|Oui| |
|Configuration de la page|Taille de la page|Oui| |
|Configuration de la page|Zone d'impression|Oui| |
|Configuration de la page|Titres à imprimer|Oui| |
|Configuration de la page|Mise à l'échelle|Oui| |
|Hauteur de ligne/Largeur de colonne| |Oui| |
{{% /alert %}}
