---
title: Afficher l apostrophe initial dans les cellules
type: docs
weight: 70
url: /fr/net/show-leading-apostrophe-in-cells/
---

Dans Microsoft Excel, l'apostrophe initiale de la valeur de la cellule est masquée. Aspose.Cells offre la possibilité d'afficher l'apostrophe par défaut. Pour cela, l'API fournit la propriété [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle). Cette propriété indique s'il faut définir la propriété [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) lors de la saisie d'une valeur de chaîne commençant par un seul guillemet dans la cellule. Le fait de définir la propriété [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) sur **false** affichera l'apostrophe initiale dans le fichier Excel de sortie.

La capture d'écran suivante montre le fichier Excel de sortie avec l'apostrophe visible.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Le code suivant illustre ceci en ajoutant des données avec des marqueurs intelligents dans le fichier Excel source. Les fichiers Excel source et de sortie sont joints à titre de référence.

[Fichier source](98107425.xlsx)

[Fichier de sortie](98107426.xlsx)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

La mise en œuvre de la classe *DataObject* est donnée ci-dessous

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
