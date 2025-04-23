---
title: Expansion du texte de droite à gauche lors de l exportation d un fichier Excel vers HTML
type: docs
weight: 820
url: /fr/java/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}} 

Aspose.Cells prend désormais en charge l'expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML. Cette fonctionnalité a été implémentée depuis la version 8.9.0.0. Désormais, si votre fichier excel source contient un texte qui s'étend de droite à gauche, Aspose.Cells l'exportera correctement vers HTML.

{{% /alert %}} 
## **Expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML**
Le code d'exemple suivant convertit le [fichier Excel d'exemple](5472562.xlsx) en HTML. Cette capture d'écran montre à quoi ressemble le fichier Excel d'exemple dans Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Cette capture d'écran montre la [sortie en HTML générée avec une version plus ancienne](5472570).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Cette capture d'écran montre la [sortie en HTML générée avec une version plus récente](5472563).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Comme vous pouvez le voir dans les captures d'écran, la nouvelle version expand le texte aligné à droite vers la gauche correctement, tout comme Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-ExpandTextFromRightToLeftWhileExportingExcelFileToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
