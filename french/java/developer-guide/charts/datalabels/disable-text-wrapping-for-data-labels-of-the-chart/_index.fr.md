---
title: Désactiver le retour à la ligne pour les étiquettes de données du graphique
type: docs
weight: 60
url: /fr/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 permet aux utilisateurs de faire un retour à la ligne ou non du texte à l'intérieur des libellés de données d'un graphique. Par défaut, le texte des libellés de données est en retour à la ligne.

{{% /alert %}}

Aspose.Cells fournit la méthode [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Définissez **True** ou **False** pour activer ou désactiver le retour à la ligne du texte sur les libellés de données respectivement.

De même, utilisez la méthode [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) pour savoir si un libellé de données est déjà en retour à la ligne.

Cette capture d'écran montre un fichier Excel d'exemple contenant un graphique dans lequel le texte des libellés de données est en retour à la ligne. Comme vous pouvez le voir, vous pouvez vérifier ou effacer l'option **Encadrer le texte dans la forme** dans la section ALIGNEMENT du panneau Format des libellés de données dans Microsoft Excel 2013.

**Retour à la ligne des libellés de données**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

Le code d'exemple suivant charge le fichier Excel d'exemple en utilisant Aspose.Cells et désactive le retour à la ligne du texte des libellés de données à l'aide de la méthode [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Lorsque le code est exécuté, le graphique ressemble à ceci. Le texte précédemment en retour à la ligne est maintenant déroulé.

**Affichage des libellés de données sur une seule ligne uniquement**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
{{< app/cells/assistant language="java" >}}
