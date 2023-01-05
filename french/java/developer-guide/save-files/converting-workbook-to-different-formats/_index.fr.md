---
title: Conversion du classeur en différents formats
type: docs
weight: 20
url: /fr/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion entre de nombreux formats. Techniquement, la conversion signifie charger un classeur dans un format de fichier et l'enregistrer dans un autre.

{{% /alert %}}

## **Conversion d'Excel en XPS**

Le format de document XPS consiste en un balisage XML structuré qui définit la mise en page d'un document et l'apparence visuelle de chaque page, ainsi que des règles de rendu pour la distribution, l'archivage, le rendu, le traitement et l'impression des documents.

Le langage de balisage pour XPS est un sous-ensemble de XAML qui lui permet d'incorporer des éléments graphiques vectoriels dans des documents, en utilisant XAML pour baliser les primitives Windows Presentation Foundation (WPF). Les éléments utilisés sont décrits en termes de chemins et autres primitives géométriques.

Un fichier XPS est en fait une archive ZIP Unicode utilisant les Open Packaging Conventions, contenant les fichiers qui composent le document. Ceux-ci incluent un fichier de balisage XML pour chaque page, du texte, des polices intégrées, des images raster, des graphiques vectoriels 2D, ainsi que les informations de gestion des droits numériques. Le contenu d'un fichier XPS peut être examiné simplement en l'ouvrant dans une application prenant en charge les fichiers ZIP.

À partir de Aspose.Cells 6.0.0, la conversion Microsoft Excel tp XPS est prise en charge.

### **Conversion d'une seule feuille de calcul en XPS**

L'exemple suivant montre comment convertir une seule feuille de calcul dans un fichier Excel en XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Exporter le classeur entier vers XPS**

L'exemple suivant montre comment convertir l'intégralité du classeur au format XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Conversion rapide d'Excel en XPS**

L'exemple suivant montre un moyen simple de convertir directement le fichier Excel au format XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Conversion d'Excel en fichiers MHTML**

[MHTML](https://en.wikipedia.org/wiki/MHTML) combine le HTML normal avec des ressources externes ; c'est-à-dire du contenu généralement lié à des images, des animations, de l'audio, etc. dans un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.

{{% alert color="primary" %}}

Aspose.Cells prend en charge la lecture et l'écriture de fichiers MHTML.

{{% /alert %}}

La conversion d'une feuille de calcul en MHTML est une opération rapide, comme indiqué ci-dessous.

L'exemple de code ci-dessous montre comment enregistrer un classeur en tant que fichier MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Conversion de fichiers Excel en HTML**

 Les API Aspose.Cells prennent en charge l'exportation de feuilles de calcul au format HTML. A cet effet, Aspose.Cells utilise le**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**classe qui permet aux développeurs de contrôler plusieurs aspects de la sortie HTML.

Le code ci-dessous montre comment utiliser le**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class pour exporter des fichiers Excel Microsoft au format HTML sans spécifier de paramètres supplémentaires.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 Vous pouvez obtenir les mêmes résultats en passant le**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** au**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** méthode.

{{% /alert %}}

### **Définition des préférences d'image pour HTML**

 À partir de 8.0.2, Aspose.Cells a exposé**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**pour le**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class, qui permet aux développeurs de spécifier les préférences d'image lors de l'enregistrement des feuilles de calcul au format HTML.

Les paramètres d'image pouvant être appliqués sont :

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: Obtient ou définit le type d'image. Veuillez noter que toutes les formes, y compris les graphiques, sont rendues sous forme d'images dans la sortie HTML.
- **[Qualité](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: Obtient ou définit la qualité des images entre 0 et 100, lorsque ImageFormat est spécifié comme Jpeg.
- **[Résolution verticale] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: Obtient ou définit la résolution verticale de l'image en points par pouce.
- **[HorizontalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: Obtient ou définit la résolution horizontale de l'image en points par pouce.
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**obtient ou définit le type de compression des images lorsque ImageFormat est spécifié sur Tiff.
- **[Transparent](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**: Indique si l'arrière-plan d'une image doit être transparent lorsque ImageFormat est spécifié comme Png.

 Le code ci-dessous montre comment utiliser**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** pour spécifier différentes préférences.

|**Affichage de la feuille de calcul avant l'exportation**|**HTML vue après exportation**|
|:- |:- |
|![Affichage de la feuille de calcul avant l'exportation](converting-workbook-to-different-formats_1.png)|![HTML vue après exportation](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Conversion d'Excel en fichiers PDF**

Les documents PDF sont largement utilisés comme format standard d'échange de documents entre les organisations, les secteurs gouvernementaux et les particuliers. Les développeurs de logiciels sont souvent invités à trouver un moyen de convertir facilement des fichiers Excel Microsoft en documents PDF. Aspose.Cells prend en charge ces fonctionnalités. Cet article montre comment.

### **Conversion d'Excel en PDF**

Microsoft La conversion d'Excel en PDF a été introduite avec Aspose.Cells for Java 2.3.0. À partir de cette version, Aspose.Cells peut[convertir des feuilles de calcul en PDF directement](#direct-conversion) (y compris[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files) ), sans autre produit. Pour convertir des feuilles de calcul avec des versions plus anciennes de Aspose.Cells,[utilisez Aspose.PDF pour la conversion](#conversion-with-asposepdf-asposecells-prior-to-230).

 Aspose.Cell convertit les feuilles de calcul en PDF avec un degré élevé de précision et de fidélité. Cependant, il y a quelques[limites](/cells/fr/java/converting-workbook-to-different-formats/#conversion-attributes), répertoriés à la fin de cet article.

{{% alert color="primary" %}}

 Aspose.Cells for Java écrit directement les informations sur API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document à PDF, Aspose.Cells for Java remplit**Application** champ avec la valeur 'Aspose.Cells' et**PDF Producteur** champ avec une valeur, par exemple 'Aspose.Cells for Java v17.9'.

Veuillez noter que vous ne pouvez pas demander au Aspose.Cells for Java de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

#### **Conversion directe**

Enregistrez un fichier Excel directement au PDF en utilisant le**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** méthode, et fournir la**[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**membre de l'interface. La conversion directe comme celle-ci est la méthode de conversion la plus efficace. Il ne perd pas de données ni de formatage, mais conserve la sortie PDF ressemblant au fichier Excel d'entrée.

 Pour spécifier les options de sécurité lors de l'enregistrement dans PDF, utilisez**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Conversion avancée**

Vous pouvez également choisir d'utiliser le**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class pour définir différents attributs pour la conversion. Définition de différentes propriétés de**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class vous donnera le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le fichier PDF résultant. La propriété la plus remarquable est la**[Conformité](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**qui vous permet d'enregistrer les fichiers Excel dans des fichiers PDF/A conformes à la norme PDF.

##### **Enregistrement de feuilles de calcul Excel dans des fichiers conformes PDF/A**

L'extrait de code fourni ci-dessous illustre l'utilisation de**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** classe pour enregistrer les fichiers Excel au format PDF/A conforme PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Conversion avec Aspose.Pdf : Aspose.Cells avant 2.3.0**

 Pour les versions Aspose.Cells antérieures à la version 2.3.0, vous devez utiliser un composant tel que[Aspose.PDF for Java](/pdf/java/)pour convertir des feuilles de calcul en fichiers PDF. Aspose.Cells et Aspose.PDF fonctionnent ensemble pour convertir une feuille de calcul en PDF via une étape intermédiaire.

Pour convertir des feuilles de calcul en PDF avec Aspose.Cells et Aspose.PDF :

1.  Instancier un objet de la**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**classe en appelant son constructeur vide.
1. Effectuez le travail souhaité sur la feuille de calcul en utilisant le Aspose.Cells API.
1. Appeler le**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**méthode pour enregistrer la feuille de calcul :
 1. Définissez le format de fichier sur XML.
 1. Sélectionnez Aspose_Pdf (une valeur prédéfinie) dans l'interface FileFormatType. Cela ordonne à la méthode de sauvegarde de générer une feuille de calcul au format XML compatible avec le schéma Aspose.PDF afin que Aspose.PDF for Java puisse ensuite générer un document PDF.
1. Une fois le fichier XML créé, créez un objet de la classe Pdf dans le package aspose.pdf.
1. Appelez la méthode bindXML de la classe Pdf et transmettez le nom du fichier XML de sortie.
1. Appelez la méthode save de la classe Pdf pour générer le document PDF.

Les étapes ci-dessus sont mises en œuvre ci-dessous dans un exemple.

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler**[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** méthode juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le fichier PDF.

{{% /alert %}}

#### **Attributs de conversion**

Nous travaillons dur pour améliorer la conversion et d'autres aspects de Aspose.Cells à chaque version. La conversion d'Excel en PDF a quelques limitations. Certains paramètres de format spécifiés dans une feuille de calcul peuvent être perdus et tous les objets de dessin ne sont pas pris en charge.

Le tableau ci-dessous répertorie toutes les fonctionnalités entièrement ou partiellement prises en charge lors de l'exportation vers PDF à l'aide de Aspose.Cells. Ce tableau n'est pas définitif et ne couvre pas tous les attributs de la feuille de calcul. Il peut également identifier les fonctionnalités qui peuvent ne pas être prises en charge ou qui sont partiellement prises en charge pour la conversion.

{{% alert color="primary" %}}

|**Élément de document**|**Attribut**|**Réseau pris en charge**|**Remarques**|
|:- |:- |:- |:- |
|Alignement||Oui||
|Rotation||Partiellement|Prend uniquement en charge 90 et -90.|
|Paramètres d'arrière-plan||Oui||
|Frontière|Couleur|Oui||
|Frontière|Style de ligne|Oui||
|Frontière|Largeur de ligne|Oui||
|Cell Données||Oui||
|commentaires||Non||
|Mise en forme conditionnelle||Oui||
|Propriétés du document||Oui||
|Objets de dessin||Oui||
|Police de caractère|Taille|Oui||
|Police de caractère|Couleur|Oui||
|Police de caractère|Style|Oui||
|Police de caractère|Souligner|Oui||
|Police de caractère|Effets|Partiellement|Seul l'effet barré est pris en charge|
|Images||Oui||
|Lien hypertexte||Oui||
|Graphiques||Oui||
|Fusionné Cells||Oui||
|Saut de page||Oui||
|Mise en page|En-tête/Pied de page|Oui||
|Mise en page|Marges|Oui||
|Mise en page|Orientation des pages|Oui||
|Mise en page|Taille de la page|Oui||
|Mise en page|Zone d'impression|Oui||
|Mise en page|Titres imprimés|Oui||
|Mise en page|Mise à l'échelle|Oui||
|Hauteur de ligne/Largeur de colonne||Oui||
{{% /alert %}}
