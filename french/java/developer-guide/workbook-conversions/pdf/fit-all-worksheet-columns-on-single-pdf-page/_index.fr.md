---
title: Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 70
url: /fr/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez générer un fichier PDF qui intègre toutes les colonnes d'une feuille de calcul sur une seule page. La[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) propriété fournit cette fonctionnalité d'une manière très facile à utiliser. Les calculs complexes tels que la hauteur et la largeur de la page PDF de sortie sont gérés en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

## **Ajuster les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)garantit que toutes les colonnes d'une feuille de calcul sont rendues sur une seule page PDF, bien que les lignes puissent s'étendre sur plusieurs pages en fonction des données de la feuille de calcul.

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF rendu peut afficher le contenu dans une très petite taille. Il est toujours lisible lorsqu'il est mis à l'échelle dans une application de visualisation telle qu'Acrobat Reader.

{{% /alert %}}

 L'exemple de code ci-dessous montre comment utiliser le[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)propriété pour afficher une grande feuille de calcul de 100 colonnes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[**Workbook.calculateFormulaWorkbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
