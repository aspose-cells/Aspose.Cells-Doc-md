---
title: PDF
type: docs
weight: 220
url: /fr/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion du classeur Excel en PDF. Dans cet exemple, nous verrons la conversion complète d'un classeur Excel en PDF.

{{% /alert %}}

## **Conversion du classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Excel Microsoft en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle lors de la conversion.

{{% alert color="primary" %}}

 Aspose.Cells for .NET écrit directement les informations sur API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document à PDF, Aspose.Cells for .NET remplit**Application** champ avec la valeur 'Aspose.Cells' et**PDF Producteur**champ avec valeur, par exemple 'Aspose.Cells v17.9'.

Veuillez noter que vous ne pouvez pas demander au Aspose.Cells for .NET de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

### **Conversion directe**

 Aspose.Cells for .NET prend en charge la conversion de feuilles de calcul en PDF indépendamment des autres logiciels. Enregistrez simplement un fichier Excel au PDF en utilisant le**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classe'**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** méthode. Le**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** méthode fournit la**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**membre d'énumération qui convertit les fichiers Excel natifs au format PDF.

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1.  Instancier un objet de la**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)**classe en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier de modèle existant ou ignorer cette étape si vous créez le classeur à partir de rien.
1. Effectuez n'importe quel travail (saisir des données, appliquer une mise en forme, définir des formules, insérer des images ou d'autres objets de dessin, etc.) sur la feuille de calcul à l'aide des API Aspose.Cells.
1.  Lorsque le code de la feuille de calcul est terminé, appelez le**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classe'**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**méthode pour enregistrer la feuille de calcul.

 Le format de fichier doit être PDF donc sélectionnez*PDF* (une valeur prédéfinie) à partir du**[Enregistrer le format] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**énumération pour générer le document final PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Conversion avancée**

 Vous pouvez également choisir d'utiliser le**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class pour définir différents attributs pour la conversion. Définition de différentes propriétés du**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** La classe vous permet de contrôler les paramètres d'impression, de police, de sécurité et de compression pour la sortie PDF. La propriété la plus importante est**[Conformité](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**qui vous permet d'enregistrer les fichiers Excel dans des fichiers PDF/A conformes à la norme PDF.

#### **Enregistrement du classeur dans des fichiers conformes PDF/A**

 L'extrait de code fourni ci-dessous montre comment utiliser le**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**classe pour enregistrer les fichiers Excel au format PDF/A conforme PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 Veuillez noter que le**[Conformité](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**La propriété a été ajoutée avec la sortie de Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Définir l'heure de création PDF**

 Avec le**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**classe, vous pouvez obtenir ou définir l'heure de création PDF. Le code suivant illustre l'utilisation de**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** propriété pour définir l'heure de création du fichier PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Définir l'option ContentCopyForAccessibility**

Avec le**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** classe, vous pouvez obtenir ou définir le PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** option pour contrôler l'accès au contenu dans le PDF converti.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Exporter les propriétés personnalisées vers PDF**

Avec le**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** classe, vous pouvez exporter les propriétés personnalisées du classeur source vers la classe PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**L'énumérateur est fourni pour spécifier la manière dont les propriétés sont exportées. Ces propriétés peuvent être observées dans Adobe Acrobat Reader en cliquant sur Fichier, puis sur l'option Propriétés, comme indiqué dans l'image suivante. Le fichier modèle "sourceWithCustProps.xlsx" peut être téléchargé[ici](sourceWithCustProps.xlsx) pour tester et produire le fichier PDF "outSourceWithCustProps" est disponible[ici](outSourceWithCustProps.pdf) pour analyse.

![tâche : image_autre_texte](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Attributs de conversion**

Nous nous efforçons d'améliorer les fonctionnalités de conversion à chaque nouvelle version. La conversion Excel vers PDF de Aspose.Cell a encore quelques limitations. Certaines mises en forme de feuille de calcul peuvent être perdues lors de la conversion au format PDF. De plus, certains objets de dessin ne sont pas encore pris en charge.

Le tableau qui suit répertorie toutes les fonctionnalités entièrement ou partiellement prises en charge lors de l'exportation vers PDF à l'aide de Aspose.Cells. Ce tableau n'est pas définitif et ne couvre pas tous les attributs de la feuille de calcul, mais il identifie les fonctionnalités qui ne sont pas prises en charge ou partiellement prises en charge pour la conversion vers PDF. .

|**Élément de document**|**Attribut**|**Prise en charge**|**Remarques**|
|:- |:- |:- |:- |
|Alignement||Oui||
|Paramètres d'arrière-plan||Oui||
|Frontière|Couleur|Oui||
|Frontière|Style de ligne|Oui||
|Frontière|Largeur de ligne|Oui||
|Cell Données||Oui||
|commentaires||Oui||
|Mise en forme conditionnelle||Oui||
|Propriétés du document||Oui||
|Objets de dessin||Partiellement|Objets pris en charge : TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Police de caractère|Taille|Oui||
|Police de caractère|Couleur|Oui||
|Police de caractère|Style|Oui||
|Police de caractère|Souligner|Oui||
|Police de caractère|Effets|Partiellement|Seul l'effet barré est pris en charge|
|Images||Oui||
|Lien hypertexte||Oui||
|Graphiques||Partiellement||
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
|Langue RTL (de droite à gauche)||Oui||

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le fichier PDF.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter PDF Signets](/cells/fr/net/add-pdf-bookmarks/)
- [Ajouter des signets PDF avec des destinations nommées](/cells/fr/net/add-pdf-bookmarks-with-named-destinations/)
- [Évitez les pages vierges dans la sortie PDF lorsqu'il n'y a rien à imprimer](/cells/fr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Modifiez la police uniquement sur les caractères Unicode spécifiques lors de l'enregistrement au format PDF](/cells/fr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Contrôler le chargement des ressources externes dans le classeur MS Excel lors du rendu vers PDF](/cells/fr/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Convertir un fichier XLS au format PDF](/cells/fr/net/convert-an-xls-file-to-pdf-format/)
- [Convertir le fichier Excel au format PDF compatible avec PDFA-1a](/cells/fr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir le fichier XLS avec des images ou des graphiques en PDF](/cells/fr/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Créer PdfBookmarkEntry pour la feuille de graphique](/cells/fr/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF](/cells/fr/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Obtenez DrawObject et Bound lors du rendu à PDF à l'aide de la classe DrawObjectEventHandler](/cells/fr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Obtenir des avertissements pour la substitution de polices lors du rendu du fichier Excel](/cells/fr/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorer les erreurs lors du rendu d'Excel en PDF](/cells/fr/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limiter le nombre de pages générées - Conversion Excel à PDF](/cells/fr/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimer les commentaires tout en enregistrant au PDF](/cells/fr/net/print-comments-while-saving-to-pdf/)
- [Rendu des compléments Office lors de la conversion d'Excel en PDF](/cells/fr/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendre une page PDF par feuille de calcul Excel - Conversion d'Excel en PDF](/cells/fr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendre les caractères supplémentaires Unicode dans la sortie PDF par Aspose.Cells](/cells/fr/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Rééchantillonnage des images ajoutées - Conversion d'Excel en PDF](/cells/fr/net/resampling-added-images-excel-to-pdf-conversion/)
- [Enregistrer chaque feuille de calcul dans un fichier PDF différent](/cells/fr/net/save-each-worksheet-to-a-different-pdf-file/)
- [Enregistrez Excel dans PDF avec une taille standard ou minimale](/cells/fr/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Documents sécurisés PDF](/cells/fr/net/secure-pdf-documents/)
- [Spécifiez comment traverser la chaîne dans la sortie PDF et l'image](/cells/fr/net/specify-how-to-cross-string-in-output-pdf-and-image/)
