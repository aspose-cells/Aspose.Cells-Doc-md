---
title: Afficher l'apostrophe de tête dans les cellules
type: docs
weight: 20
url: /fr/java/show-leading-apostrophe-in-cells/
---
## **Afficher l'apostrophe de tête dans les cellules**

Dans Microsoft Excel, l'apostrophe principale de la valeur de la cellule est masquée. Aspose.Cells fournit la fonctionnalité pour afficher l'apostrophe par défaut. Pour cela, le API fournit[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)propriété. Cette propriété indique s'il faut définir le[**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)propriété lors de la saisie d'une valeur de chaîne commençant par un guillemet simple dans la cellule. Réglage de la[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)propriété à**faux**affichera l'apostrophe principale dans le fichier Excel de sortie.

La capture d'écran suivante montre le fichier Excel de sortie avec l'apostrophe visible.

![tâche : image_autre_texte](show-leading-apostrophe-in-cells_1.jpg)

L'extrait de code suivant illustre cela en ajoutant des données avec des marqueurs intelligents dans le fichier Excel source. Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier source](AllowLeadingApostropheSample.xlsx)

[Fichier de sortie](AllowLeadingApostropheSample_out.xlsx)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

L'implémentation de*DataObject*la classe est donnée ci-dessous

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
