---
title: Développer le texte de droite à gauche lors de l'exportation du fichier Excel au format HTML
type: docs
weight: 60
url: /fr/net/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---
{{% alert color="primary" %}} 

Aspose.Cells prend désormais en charge l'expansion du texte de droite à gauche lors de l'exportation du fichier Excel au format HTML. Cette fonctionnalité a été implémentée depuis la v8.9.0.0. Maintenant, si votre fichier Excel source contient du texte qui s'étend de droite à gauche, Aspose.Cells l'exportera correctement au format HTML.

{{% /alert %}} 
## **Développer le texte de droite à gauche lors de l'exportation du fichier Excel au format HTML**
 L'exemple de code suivant convertit le[exemple de fichier excel](5115502.xlsx) en HTML. Cette capture d'écran montre à quoi ressemble l'exemple Excel dans Microsoft Excel 2013.

![tâche : image_autre_texte](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

 Cette capture d'écran montre le[HTML de sortie généré avec une version plus ancienne](5115509).

![tâche : image_autre_texte](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

 Cette capture d'écran montre le[HTML de sortie généré avec une version plus récente](5115508).

![tâche : image_autre_texte](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Comme vous pouvez le voir sur les captures d'écran, la nouvelle version développe correctement le texte aligné à droite vers la gauche, tout comme Microsoft Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExpandTextFromRightToLeft-1.cs" >}}
