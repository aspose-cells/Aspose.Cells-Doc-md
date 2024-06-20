---
title: Pdf
type: docs
weight: 220
url: /fr/python-net/convert-excel-to-pdf/
description: Apprenez à convertir Excel en PDF avec l API Aspose.Cells pour Python via .NET.
keywords: Python convertit Excel en PDF, convertit Excel en PDF en utilisant Python, enregistre Excel en PDF avec Python, Excel en PDF en Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET prend en charge la conversion du classeur Excel en PDF. Dans cet exemple, nous verrons la conversion complète d'un classeur Excel en PDF.

{{% /alert %}}

## **Conversion du classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Microsoft Excel en documents PDF.

Aspose.Cells for Python via .NET prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document au format PDF, Aspose.Cells for Python via .NET remplit le champ **Producteur PDF** avec la valeur, par exemple 'Aspose.Cells for Python via .NET v23.2'.

Veuillez noter que vous pouvez modifier ces informations dans les documents de sortie par la propriété [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **Conversion directe**

Aspose.Cells pour Python via .NET prend en charge la conversion des feuilles de calcul en PDF indépendamment d'autres logiciels. Enregistrez simplement un fichier Excel au format PDF en utilisant la méthode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). La méthode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) fournit le membre d'énumération [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) qui convertit les fichiers Excel natifs au format PDF.

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1. Instanciez un objet de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier de modèle existant ou sauter cette étape si vous créez le classeur à partir de zéro.
1. Effectuez un travail (saisie de données, application de formatage, définition de formules, insertion d'images ou autres objets graphiques, etc.) sur la feuille de calcul en utilisant les API Aspose.Cells for Python via .NET.
1. Lorsque le code de la feuille de calcul est complet, appelez la méthode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) pour enregistrer la feuille de calcul.

Le format de fichier doit être PDF, choisissez *PDF* (une valeur prédéfinie) dans l'énumération [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) pour générer le document PDF final.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Conversion avancée**

Vous pouvez également choisir d'utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) pour définir différentes propriétés pour la conversion. Le fait de définir différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) vous donne le contrôle sur les paramètres d’impression, de police, de sécurité et de compression pour le fichier PDF de sortie. La propriété la plus importante est [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) qui vous permet d'enregistrer les fichiers Excel au format PDF/A conforme.

#### **Enregistrement du classeur en fichiers conformes PDF/A**

L'exemple de code ci-dessous démontre comment utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) pour enregistrer des fichiers Excel au format PDF/A conforme.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Veuillez noter que la propriété [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) a été ajoutée avec la sortie d'Aspose.Cells pour Python via .NET pour .NET 5.3.0.

{{% /alert %}}

#### **Définir l'heure de création du PDF**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), vous pouvez obtenir ou définir l'heure de création du PDF. Le code suivant démontre l'utilisation de la propriété [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) pour définir l'heure de création du fichier PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **Définir l'option ContentCopyForAccessibility**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), vous pouvez obtenir ou définir l'option de PDF [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) pour contrôler l'accès au contenu dans le PDF converti.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Exporter les propriétés personnalisées vers un PDF**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), vous pouvez exporter les propriétés personnalisées du classeur source vers le PDF. L'énumérateur [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) est fourni pour spécifier la manière dont les propriétés sont exportées. Ces propriétés peuvent être observées dans Adobe Acrobat Reader en cliquant sur Fichier, puis sur l'option propriétés comme indiqué dans l'image suivante. Le fichier modèle "sourceWithCustProps.xlsx" peut être téléchargé [ici](sourceWithCustProps.xlsx) pour les tests et le fichier PDF de sortie "outSourceWithCustProps" est disponible [ici](outSourceWithCustProps.pdf) pour l'analyse.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Attributs de conversion**

Nous travaillons à améliorer les fonctionnalités de conversion avec chaque nouvelle version. La conversion d'Excel en PDF d'Aspose.Cell a encore quelques limitations. MapChart n'est pas pris en charge lors de la conversion au format PDF. De plus, certains objets de dessin ne sont pas bien pris en charge.

Le tableau suivant répertorie toutes les fonctionnalités entièrement ou partiellement prises en charge lors de l'exportation au format PDF à l'aide d'Aspose.Cells pour Python via .NET. Ce tableau n'est pas final et ne couvre pas toutes les attributs de la feuille de calcul, mais identifie les fonctionnalités qui ne sont pas entièrement prises en charge ou partiellement prises en charge pour la conversion en PDF.

|**Élément du document**|**Attribut**|**Pris en charge**|**Notes**|
| :- | :- | :- | :- |
|Alignement| |Oui| |
|Paramètres de fond| |Oui| |
|Bordure|Couleur|Oui| |
|Bordure|Style de ligne|Oui| |
|Bordure|Largeur de ligne|Oui| |
|Données de cellule| |Oui| |
|Commentaires| |Oui| |
|Mise en forme conditionnelle| |Oui| |
|Propriétés du document| |Oui| |
|Objets de dessin| |Partiellement|Les effets d'ombre et 3D pour les objets graphiques ne sont pas bien pris en charge ; WordArt et SmartArt sont partiellement pris en charge.|
|Police|Taille|Oui| |
|Police|Couleur|Oui| |
|Police|Style|Oui| |
|Police|Souligner|Oui| |
|Police|Effets|Oui| |
|Images| |Oui| |
|Hyperlien| |Oui| |
|Graphiques| |Partiellement|Le MapChart n'est pas pris en charge.|
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
|Langue RTL (de droite à gauche)| |Oui| |

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de générer la feuille de calcul au format PDF. De cette façon, les valeurs dépendant des formules seront recalculées et les valeurs correctes seront rendues dans le PDF.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter des signets PDF](/cells/fr/python-net/add-pdf-bookmarks/)
- [Ajouter des signets PDF avec des destinations nommées](/cells/fr/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Éviter la page blanche dans le PDF final lorsqu'il n'y a rien à imprimer](/cells/fr/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Convertir un fichier XLSX au format PDF](/cells/fr/python-net/convert-xlsx-file-to-pdf-format/)
- [Convertir un fichier Excel au format PDF compatible avec PDFA-1a](/cells/fr/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir un fichier XLS avec des images ou des graphiques au format PDF](/cells/fr/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Créer une entrée PdfBookmark pour une feuille de graphique](/cells/fr/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF](/cells/fr/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorer les erreurs lors du rendu Excel vers PDF](/cells/fr/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limiter le nombre de pages généré - Conversion Excel vers PDF](/cells/fr/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimer les commentaires lors de l'enregistrement au format PDF](/cells/fr/python-net/print-comments-while-saving-to-pdf/)
- [Rendre les compléments Office lors de la conversion Excel en PDF](/cells/fr/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendre une page PDF par feuille de calcul Excel - Conversion Excel en PDF](/cells/fr/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendre les caractères supplémentaires Unicode dans le PDF final par Aspose.Cells](/cells/fr/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Redimensionner les images ajoutées - Conversion Excel en PDF](/cells/fr/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Sauvegarder chaque feuille de calcul dans un fichier PDF différent](/cells/fr/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Enregistrer Excel en PDF avec une taille standard ou minimale](/cells/fr/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Enregistrer des feuilles de calcul spécifiées au format PDF](/cells/fr/python-net/save-specified-worksheets-to-pdf/)
- [Sécuriser les documents PDF](/cells/fr/python-net/secure-pdf-documents/)
- [Spécifiez comment croiser la chaîne dans le PDF de sortie et l'image](/cells/fr/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
