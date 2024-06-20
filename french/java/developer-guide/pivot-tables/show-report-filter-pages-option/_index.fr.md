---
title: Option Afficher les pages de filtre de rapport
type: docs
weight: 140
url: /fr/java/show-report-filter-pages-option/
---

## **Afficher l'option de pages de filtre de rapport**

Excel prend en charge la création de tableaux croisés dynamiques, l'ajout de filtres de rapport et l'activation de l'option "Afficher les pages de filtre de rapport". Aspose.Cells prend également en charge cette fonctionnalité pour activer l'option "Afficher les pages de filtre de rapport" sur le tableau croisé dynamique créé. Ce qui suit est l'écran montrant l'option dans Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

En conséquence de cette option, le classeur créé contient davantage de feuilles de calcul. Elle divise chaque valeur possible du filtre du rapport dans une feuille de calcul séparée. Dans cet exemple, il y a un filtre sur "Position" et les données ont trois positions distinctes (A, B, C). Cette fonctionnalité ajoute 3 feuilles de calcul supplémentaires nommées A, B, C qui sont la même table pivot mais avec l'option préselectionnée A, B et C.

Le fichier d'exemple et le fichier de sortie peuvent être téléchargés à partir des liens suivants :

[samplePivotTable.xlsx](81920917.xlsx)

[outputSamplePivotTable.xls](81920918.xlsx)

## Code source

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-ShowReportFilterPagesOption-1.java" >}}
