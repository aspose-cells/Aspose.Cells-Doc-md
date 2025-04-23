---
title: Afficher l apostrophe initial dans les cellules
type: docs
weight: 20
url: /fr/java/show-leading-apostrophe-in-cells/
---

## **Afficher une apostrophe de tête dans les cellules**

Dans Microsoft Excel, l'apostrophe initiale dans la valeur de la cellule est masquée. Aspose.Cells offre la fonctionnalité d'afficher par défaut l'apostrophe. Pour cela, l'API fournit la propriété [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle). Cette propriété indique s'il faut définir la propriété [**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix) lors de la saisie d'une valeur de chaîne commençant par un seul guillemet dans la cellule. Le réglage de la propriété [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle) sur **false** affichera l'apostrophe initiale dans le fichier Excel de sortie.

La capture d'écran suivante montre le fichier Excel de sortie avec l'apostrophe visible.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Le code suivant illustre ceci en ajoutant des données avec des marqueurs intelligents dans le fichier Excel source. Les fichiers Excel source et de sortie sont joints à titre de référence.

[Fichier source](AllowLeadingApostropheSample.xlsx)

[Fichier de sortie](AllowLeadingApostropheSample_out.xlsx)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

La mise en œuvre de la classe *DataObject* est donnée ci-dessous

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
{{< app/cells/assistant language="java" >}}
