---
title: Expansion du texte de droite à gauche lors de l exportation d un fichier Excel vers HTML
type: docs
weight: 60
url: /fr/python-net/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}} 

Aspose.Cells pour Python via .NET supporte désormais l’expansion du texte de droite à gauche lors de l’exportation d’un fichier Excel en HTML. Cette fonctionnalité est implémentée depuis la version v8.9.0.0. Si votre fichier Excel source contient du texte qui s’étend de droite à gauche, Aspose.Cells l’exportera correctement en HTML.

{{% /alert %}} 

## **Expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML**
Le code d'exemple suivant convertit le [fichier excel d'exemple](5115502.xlsx) en HTML. Cette capture d'écran montre à quoi ressemble le fichier excel d'exemple dans Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Cette capture d'écran montre la [sortie HTML générée avec une ancienne version](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Cette capture d'écran montre la [sortie HTML générée avec une nouvelle version](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Comme vous pouvez le voir dans les captures d'écran, la nouvelle version expand le texte aligné à droite vers la gauche correctement, tout comme Microsoft Excel.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExpandTextFromRightToLeft-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
