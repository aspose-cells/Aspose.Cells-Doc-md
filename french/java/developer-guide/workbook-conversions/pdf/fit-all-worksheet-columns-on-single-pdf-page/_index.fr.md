---
title: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 70
url: /fr/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Il arrive parfois que vous souhaitiez générer un fichier PDF qui s'adapte à toutes les colonnes d'une feuille de calcul sur une seule page. La propriété [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) fournit cette fonctionnalité d'une manière très facile à utiliser. Les calculs complexes tels que la hauteur et la largeur de la page PDF de sortie sont gérés en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

## **Adapter les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) garantit que toutes les colonnes d'une feuille de calcul sont rendues sur une seule page PDF, bien que les lignes puissent s'étendre sur plusieurs pages en fonction des données dans la feuille de calcul.

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée contient de nombreuses colonnes, le fichier PDF rendu peut afficher le contenu à une taille très réduite. Il reste lisible lorsqu'il est agrandi dans une application de visualisation telle que Acrobat Reader.

{{% /alert %}}

Le code d'exemple ci-dessous montre comment utiliser la propriété [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) pour rendre une grande feuille de calcul de 100 colonnes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
