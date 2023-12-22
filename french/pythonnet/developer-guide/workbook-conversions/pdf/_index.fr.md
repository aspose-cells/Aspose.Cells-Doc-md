---
title: Pdf
type: docs
weight: 220
url: /fr/python-net/convert-excel-to-pdf/
description: Apprenez à convertir Excel en PDF avec Aspose.Cells for Python via .NET API.
keywords: Python converT Excel to PDF, ConverT Excel to PDF using Python, Python save Excel to PDF, Excel to PDF in Python
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET prend en charge la conversion du classeur Excel en PDF. Dans cet exemple, nous verrons la conversion complète d'un classeur Excel en PDF.

{{% /alert %}}

##  **Conversion du classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre des organisations, des secteurs gouvernementaux et des particuliers. Il s'agit d'un format de document standard et il est souvent demandé aux développeurs de logiciels de trouver un moyen de convertir des fichiers Excel Microsoft en documents PDF.

Aspose.Cells for Python via .NET prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET écrit directement les informations sur API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document vers PDF, Aspose.Cells for Python via .NET remplit**PDF Producteur** champ avec une valeur, par exemple 'Aspose.Cells for Python via .NET v23.2'.

 Veuillez noter que vous pouvez modifier ces informations dans les documents de sortie en**[PdfSaveOptions.producer](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/)** propriété.

{{% /alert %}}

###  **Conversion directe**

 Aspose.Cells for Python via .NET prend en charge la conversion des feuilles de calcul vers PDF indépendamment des autres logiciels. Enregistrez simplement un fichier Excel au PDF en utilisant le**[Cahier d'exercices](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**classe'**[enregistrer](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** méthode. Le**[enregistrer](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** la méthode fournit le**[SaveFormat.PDF](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**membre d'énumération qui convertit les fichiers Excel natifs au format PDF.

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1.  Instancier un objet du**[Cahier d'exercices](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**classe en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier modèle existant ou ignorer cette étape si vous créez le classeur à partir de zéro.
1. Effectuez tout travail (saisie de données, application d'un formatage, définition de formules, insertion d'images ou d'autres objets de dessin, etc.) sur la feuille de calcul à l'aide des API Aspose.Cells for Python via .NET'.
1.  Lorsque le code de la feuille de calcul est terminé, appelez le**[Cahier d'exercices](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**classe'**[enregistrer](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**méthode pour enregistrer la feuille de calcul.

 Le format de fichier doit être PDF, alors sélectionnez*PDF* (une valeur prédéfinie) de la**[SaveFormat](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**énumération pour générer le document final PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

###  **Conversion avancée**

 Vous pouvez également choisir d'utiliser le**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** classe pour définir différents attributs pour la conversion. Définition de différentes propriétés du**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** La classe vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour la sortie PDF. La propriété la plus importante est**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**qui vous permet d'enregistrer les fichiers Excel dans des fichiers PDF/A conformes à la norme PDF.

####  **Enregistrement du classeur dans les fichiers conformes PDF/A**

 L'extrait de code fourni ci-dessous montre comment utiliser le**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**classe pour enregistrer les fichiers Excel au format PDF/A conforme à PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Attention, le**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**la propriété a été ajoutée avec la sortie de Aspose.Cells for Python via .NET for .NET 5.3.0.

{{% /alert %}}

####  **Définir l'heure de création PDF**

 Avec le**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**classe, vous pouvez obtenir ou définir l’heure de création PDF. Le code suivant montre l'utilisation de**[PdfSaveOptions.created_time](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/)** propriété pour définir l’heure de création du fichier PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

####  **Définir l’option ContentCopyForAccessibility**

Avec le**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** classe, vous pouvez obtenir ou définir le PDF**[PdfSecurityOptions.accessibility_extract_content](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)** option pour contrôler l'accès au contenu dans le PDF converti.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

####  **Exporter les propriétés personnalisées vers PDF**

Avec le**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** classe, vous pouvez exporter les propriétés personnalisées du classeur source vers le fichier PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)**L'énumérateur est fourni pour spécifier la manière dont les propriétés sont exportées. Ces propriétés peuvent être observées dans Adobe Acrobat Reader en cliquant sur l'option Fichier puis sur Propriétés, comme indiqué dans l'image suivante. Le fichier modèle "sourceWithCustProps.xlsx" peut être téléchargé[ici](sourceWithCustProps.xlsx) pour les tests et la sortie, le fichier PDF "outSourceWithCustProps" est disponible[ici](outSourceWithCustProps.pdf) pour analyse.

![tâche : image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

###  **Attributs de conversion**

Nous travaillons pour améliorer les fonctionnalités de conversion à chaque nouvelle version. La conversion Excel de Aspose.Cell en PDF présente encore quelques limitations. MapChart n'est pas pris en charge lors de la conversion au format PDF. De plus, certains objets de dessin ne sont pas bien pris en charge.

Le tableau qui suit répertorie toutes les fonctionnalités entièrement ou partiellement prises en charge lors de l'exportation vers PDF en utilisant Aspose.Cells for Python via .NET. Ce tableau n'est pas définitif et ne couvre pas tous les attributs de la feuille de calcul, mais il identifie les fonctionnalités qui ne sont pas prises en charge ou partiellement prises en charge pour la conversion. au PDF.

|**Élément de document**|**Attribut**|**Prise en charge**|**Remarques**|
| :- | :- | :- | :- |
|Alignement| |Oui| |
|Paramètres d'arrière-plan| |Oui| |
|Frontière|Couleur|Oui| |
|Frontière|Style de ligne|Oui| |
|Frontière|Largeur de ligne|Oui| |
|Cell Données| |Oui| |
|commentaires| |Oui| |
|Mise en forme conditionnelle| |Oui| |
|Propriétés du document| |Oui| |
|Dessiner des objets| |Partiellement|Les effets d'ombre et 3D pour les objets dessinés ne sont pas bien pris en charge ; WordArt et SmartArt sont partiellement pris en charge.|
|Police de caractère|Taille|Oui| |
|Police de caractère|Couleur|Oui| |
|Police de caractère|Style|Oui| |
|Police de caractère|Souligner|Oui| |
|Police de caractère|Effets|Oui||
|Images| |Oui| |
|Lien hypertexte| |Oui| |
|Graphiques| |Partiellement|MapChart n'est pas pris en charge.|
|Fusionné Cells| |Oui| |
|Saut de page| |Oui| |
|Mise en page|En-tête/pied de page|Oui| |
|Mise en page|Marges|Oui| |
|Mise en page|Orientation des pages|Oui| |
|Mise en page|Taille de la page|Oui| |
|Mise en page|Zone d'impression|Oui| |
|Mise en page|Imprimer les titres|Oui| |
|Mise en page|Mise à l'échelle|Oui| |
|Hauteur de ligne/largeur de colonne| |Oui| |
|Langue RTL (de droite à gauche)| |Oui| |

{{% alert color="primary" %}}

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

##  **Sujets avancés**
- [Ajouter PDF Favoris](/cells/fr/python-net/add-pdf-bookmarks/)
- [Ajouter des signets PDF avec des destinations nommées](/cells/fr/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Évitez les pages vierges dans la sortie PDF lorsqu'il n'y a rien à imprimer](/cells/fr/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Convertir le fichier XLSX au format PDF](/cells/fr/python-net/convert-xlsx-file-to-pdf-format/)
- [Convertir le fichier Excel au format PDF compatible avec PDFA-1a](/cells/fr/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir un fichier XLS avec des images ou des graphiques en PDF](/cells/fr/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Créer PdfBookmarkEntry pour la feuille de graphique](/cells/fr/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF](/cells/fr/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorer les erreurs lors du rendu d'Excel vers PDF](/cells/fr/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limiter le nombre de pages générées - Conversion Excel à PDF](/cells/fr/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimer les commentaires lors de l'enregistrement au PDF](/cells/fr/python-net/print-comments-while-saving-to-pdf/)
- [Rendre les compléments Office lors de la conversion d'Excel en PDF](/cells/fr/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendu d'une page PDF par feuille de calcul Excel - Conversion d'Excel en PDF](/cells/fr/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Afficher les caractères supplémentaires Unicode dans la sortie PDF par Aspose.Cells](/cells/fr/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Rééchantillonnage des images ajoutées - Conversion Excel vers PDF](/cells/fr/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Enregistrez chaque feuille de calcul dans un fichier PDF différent](/cells/fr/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Enregistrez Excel dans PDF avec une taille standard ou minimale](/cells/fr/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Enregistrer les feuilles de calcul spécifiées au PDF](/cells/fr/python-net/save-specified-worksheets-to-pdf/)
- [Documents sécurisés PDF](/cells/fr/python-net/secure-pdf-documents/)
- [Spécifiez comment croiser la chaîne dans la sortie PDF et l'image](/cells/fr/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
