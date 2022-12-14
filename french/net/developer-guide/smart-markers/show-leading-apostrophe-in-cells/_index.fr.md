---
title: Afficher l'apostrophe de tête dans les cellules
type: docs
weight: 70
url: /fr/net/show-leading-apostrophe-in-cells/
---
 Dans Microsoft Excel, l'apostrophe principale de la valeur de la cellule est masquée. Aspose.Cells fournit la fonctionnalité pour afficher l'apostrophe par défaut. Pour cela, le API fournit[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) propriété. Cette propriété indique s'il faut définir le[QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)propriété lors de la saisie d'une valeur de chaîne commençant par un guillemet simple dans la cellule. Réglage de la[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) propriété à**faux**affichera l'apostrophe principale dans le fichier Excel de sortie.

La capture d'écran suivante montre le fichier Excel de sortie avec l'apostrophe visible.

![tâche : image_autre_texte](show-leading-apostrophe-in-cells_1.jpg)

L'extrait de code suivant illustre cela en ajoutant des données avec des marqueurs intelligents dans le fichier Excel source. Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier source](98107425.xlsx)

[Fichier de sortie](98107426.xlsx)
## **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

L'implémentation de*DataObject*la classe est donnée ci-dessous

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
